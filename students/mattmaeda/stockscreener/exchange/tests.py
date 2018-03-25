"""
Test for exchange
"""
import datetime
import json
import mock
import os
import iexfinance
from django.urls import reverse
from django.test import TestCase, RequestFactory
from requests import ConnectionError
from exchange.views import *
from exchange.models import Rule, Screen

MY_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA = os.path.join(MY_PATH, "testdata", "test_historical_data.json")

BOGUS_SYMBOL = "BOGUSCOMPANY"
NON_EXISTENT = "IDONOTEXIST"
CONN_ERROR = "CONNERROR"

XOVER_TEST = [
    {
        'name': 'Screen1',
        'desc': 'Screen 1',
        'pass': True,
        'rules': [
            {
                'criteria': '50MA crossover 200MA',
                'pass': True
            }
        ]
    },
    {
        'name': 'Screen2',
        'desc': 'Screen 2',
        'pass': False,
        'rules': [
            {
                'criteria': '50MA crossunder 200MA',
                'pass': False
            }
        ]
    }
]


# Create your tests here.
class IEXFinanceStock(object):
    """ Mock object for iexfinance.Stock """
    def __init__(self, ticker):
        self.ticker = ticker

        if ticker == CONN_ERROR:
            raise ConnectionError("Test bad connection")


    def get_company(self):
        if self.ticker == BOGUS_SYMBOL:
            return {"companyName": "Bogus Company"}
        elif self.ticker == NON_EXISTENT:
            raise iexfinance.utils.exceptions.IEXSymbolError("INVALID")
        else:
            raise ValueError("Ticker empty")


class IEXFinanceMock(object):
    """ Mock object for iexfinance.get_historical_data """
    def __init__(self):
        self.return_value = json.load(open(TEST_DATA))
        self.start = None
        self.end = None
        self.format = None


    def get_historical_data(self, ticker, start=None, end=None,
                            output_format=None):
        """ Returns the canned response data """
        self.start = start
        self.end = end
        self.format = output_format
        return self.return_value


class ExchangeViewsTests(TestCase):
    """ Validates exchange view functions """


    def setUp(self):
        """ Setup variables for test """
        self.factory = RequestFactory()
        self.crossunder = []
        self.crossover = []

        for i in range(199):
            self.crossunder.append({"close": 25.00})
            self.crossover.append({"close": 25.00})

        self.crossunder.append({"close": 27.00})
        self.crossunder.append({"close": 10.00})
        self.crossover.append({"close": 23.00})
        self.crossover.append({"close": 40.00})

        r1 = Rule(formula="MA50 XOVER MA200", criteria="50MA crossover 200MA")
        r1.save()

        r2 = Rule(formula="MA50 XUNDER MA200", criteria="50MA crossunder 200MA")
        r2.save()

        s1 = Screen(name="Screen1", description="Screen 1")
        s1.save()
        s1.rules.add(r1)

        s2 = Screen(name="Screen2", description="Screen 2")
        s2.save()
        s2.rules.add(r2)


    def test_cross_under_valid(self):
        """ Validate cross under check """
        self.assertIs(cross_under(self.crossunder, 50, 200), True)


    def test_cross_under_invvalid(self):
        """ Validate cross under check """
        self.assertIs(cross_under(self.crossover, 50, 200), False)


    def test_cross_over_valid(self):
        """ Validate cross over check """
        self.assertIs(cross_over(self.crossover, 50, 200), True)


    def test_cross_over_invalid(self):
        """ Validate cross over check """
        self.assertIs(cross_over(self.crossunder, 50, 200), False)


    def test_prev_moving_average(self):
        """ Validate previous moving average """
        self.assertEqual(prev_moving_average(self.crossover, 50), 24.96)


    def test_last_moving_average(self):
        """ Validate last moving average """
        self.assertEqual(last_moving_average(self.crossover, 50), 25.26)


    def test_last_closing_price(self):
        """ Validate last closing price """
        self.assertEqual(last_closing_price(self.crossover), 40.00)


    def test_convert_variable_value_moving_average(self):
        """ Validate conversion of variable value for moving average"""
        self.assertEqual(convert_variable_value("MA50", self.crossover), 25.26)


    def test_convert_variable_value_closing_price(self):
        """ Validate conversion of variable value for closing price"""
        self.assertEqual(convert_variable_value("CP", self.crossover), 40.00)


    def test_convert_variable_value_unknown(self):
        """ Validate conversion of variable value for invalid var"""
        with self.assertRaises(Exception):
            convert_variable_value("BAD50", self.crossover)


    def test_get_variable_values_crossover(self):
        """ Validate get_variable_values with crossover """
        (val1, val2) = get_variable_values("XOVER", "MA50", "MA200",
                                           self.crossover)
        self.assertEqual(val1, 50)
        self.assertEqual(val2, 200)


    def test_get_variable_values_crossunder(self):
        """ Validate get_variable_values with crossunder """
        (val1, val2) = get_variable_values("XUNDER", "MA50", "MA200",
                                           self.crossover)
        self.assertEqual(val1, 50)
        self.assertEqual(val2, 200)


    def test_get_variable_values_non_crossing(self):
        """ Validate get_variable_values for non crossing operators """
        (val1, val2) = get_variable_values("GT", "CP", "MA50", self.crossover)
        self.assertEqual(val1, 40.00)
        self.assertEqual(val2, 25.26)


    def test_evaluate_formula_xover_valid(self):
        """ Validate evaluate_formula with valid xover """
        self.assertIs(evaluate_formula("MA50 XOVER MA200", self.crossover),
                      True)


    def test_evaluate_formula_xover_invalid(self):
        """ Validate evaluate_formula with invalid xover """
        self.assertIs(evaluate_formula("MA50 XOVER MA200", self.crossunder),
                      False)


    def test_evaluate_formula_xunder_valid(self):
        """ Validate evaluate_formula with valid xunder """
        self.assertIs(evaluate_formula("MA50 XUNDER MA200", self.crossunder),
                      True)


    def test_evaluate_formula_xunder_invalid(self):
        """ Validate evaluate_formula with invalid xunder """
        self.assertIs(evaluate_formula("MA50 XUNDER MA200", self.crossover),
                      False)


    def test_evaluate_formala_gt_valid(self):
        """ Validate evaluate_formula with valid GT """
        self.assertIs(evaluate_formula("MA50 GT MA200", self.crossover), True)


    def test_evaluate_formala_gt_invalid(self):
        """ Validate evaluate_formula with invalid GT """
        self.assertIs(evaluate_formula("MA50 GT MA200", self.crossunder), False)


    def test_evaluate_formala_gte_valid(self):
        """ Validate evaluate_formula with valid GTE """
        self.assertIs(evaluate_formula("MA50 GTE MA200", self.crossover), True)


    def test_evaluate_formala_gte_invalid(self):
        """ Validate evaluate_formula with invalid GTE """
        self.assertIs(evaluate_formula("MA50 GTE MA200", self.crossunder),
                      False)


    def test_evaluate_formala_gte_equal(self):
        """ Validate evaluate_formula for GTE equality"""
        self.assertIs(evaluate_formula("MA50 GTE MA50", self.crossunder), True)


    def test_evaluate_formala_lt_valid(self):
        """ Validate evaluate_formula with valid LT """
        self.assertIs(evaluate_formula("MA200 LT MA50", self.crossover), True)


    def test_evaluate_formala_lt_invalid(self):
        """ Validate evaluate_formula with invalid LT """
        self.assertIs(evaluate_formula("MA50 LT MA200", self.crossover), False)


    def test_evaluate_formala_lte_valid(self):
        """ Validate evaluate_formula with valid LTE """
        self.assertIs(evaluate_formula("MA200 LTE MA50", self.crossover), True)


    def test_evaluate_formala_lte_invalid(self):
        """ Validate evaluate_formula with invalid LTE """
        self.assertIs(evaluate_formula("MA200 LTE MA50", self.crossunder),
                      False)


    def test_evaluate_formala_lte_equal(self):
        """ Validate evaluate_formula for LTE equality"""
        self.assertIs(evaluate_formula("MA50 LTE MA50", self.crossunder), True)


    def test_get_stock_info_valid(self):
        """ Validates that valid stock return value returns correct info """
        with mock.patch('exchange.views.Stock', IEXFinanceStock) as m:
            response = get_stock_info(BOGUS_SYMBOL)
            self.assertEqual("Bogus Company", response)


    def test_get_stock_info_nonexistent(self):
        """ Validates that valid stock return value returns correct info """
        with mock.patch('exchange.views.Stock', IEXFinanceStock) as m:
            response = get_stock_info(NON_EXISTENT)
            self.assertEqual(None, response)


    def test_get_stock_info_empty(self):
        """ Validates that valid stock return value returns correct info """
        with mock.patch('exchange.views.Stock', IEXFinanceStock) as m:
            response = get_stock_info("")
            self.assertEqual(None, response)


    def test_get_price_history(self):
        """ Validate the get_price_history function """
        with mock.patch('exchange.views.iexfinance', IEXFinanceMock()) as m:
            history = get_price_history("GOOG")
            self.assertEqual(len(history), 252)
            today = datetime.date.today()
            start = today - datetime.timedelta(days=365)
            self.assertEqual(m.start, start)
            self.assertEqual(m.end, today)
            self.assertEqual(m.format, "json")


    def test_index_connection_error(self):
        """ Validates that index view handles connection error """
        with mock.patch('exchange.views.Stock', IEXFinanceStock) as m:
            request = self.factory.post('exchange', {"ticker": CONN_ERROR})
            output = index(request)
            self.assertContains(output,
                                "Currently experiencing connection problems")


    def test_run_screens(self):
        """ Validate run screens """
        res = run_screens(self.crossover)
        self.assertEqual(res, XOVER_TEST)


    @mock.patch('exchange.views.get_price_history')
    def test_the_whole_enchilada(self, mock_history):
        """ Test the whole thing """
        mock_history.return_value = self.crossover
        with mock.patch('exchange.views.Stock', IEXFinanceStock) as m:
            request = self.factory.post('exchange', {"ticker": BOGUS_SYMBOL})
            output = index(request)
            self.assertContains(output,
                                "Here are your results for BOGUSCOMPANY")
