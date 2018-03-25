"""
Contains the view logic for stockscreener app
"""
import datetime
import iexfinance
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from requests import ConnectionError
from iexfinance import Stock
from .models import Screen

# Create your views here.
def index(request):
    """ Main page """
    message ="Pleast enter a stock symbol (e.g., GOOG)"
    response = None

    if request.method == "POST":

        try:
            ticker = request.POST.get("ticker", "")
            symbol = ticker.upper()
            company = get_stock_info(symbol)

            if company is not None:
                history = get_price_history(symbol)
                response = run_screens(history)
                message = "Here are your results for {}".format(symbol)
            else:
                message = "Invalid stock symbol '{}'".format(symbol)

        except ConnectionError as cxn:
            message = ("Currently experiencing connection problems.\n"
                       "Please try again later.")

    return render(request, 'index.html', {"message": message,
                                          "response": response})


def get_stock_info(ticker):
    """ Checks if the ticker is valid

    :param ticker String: the stock ticker

    :return: company name or None if invalid
    :rtype: String

    """
    # Let connection errors percolate to the calling function
    try:
        stock = Stock(ticker.upper())
        return stock.get_company().get("companyName")

    except iexfinance.utils.exceptions.IEXSymbolError as exc:
        return None

    except ValueError as ve:
        # If empty
        return None


def get_price_history(ticker):
    """ Loads the price history of a stock for the last 252 days.  Note, 252
    days is a limit of iexfinance function.

    :param ticker: the stock ticker symbol
    :type: String

    :return: list of price objects
    :rtype: list

    """
    today = datetime.date.today()
    start = today - datetime.timedelta(days=365)
    data = iexfinance.get_historical_data(ticker, start=start, end=today,
                                          output_format="json")
    quotes = data.get(ticker)

    history = []
    for date in quotes.keys():
        quote = quotes.get(date)
        history.append({"date": date,
                        "open": quote.get("open"),
                        "close": quote.get("close"),
                        "high": quote.get("high"),
                        "low": quote.get("low")})

    return history


def run_screens(history):
    """ Given a stocks's price history, run screens to find any matches

    :param history list: list of price objects

    :return: screen results
    :rtype: String

    """
    screen_results = []
    screens = Screen.objects.all()

    for screen in screens:
        scr_res = {
            "name": screen.name,
            "desc": screen.description,
            "pass": True,
            "rules": []
        }

        for rule in screen.rules.all():
            res = evaluate_formula(rule.formula, history)

            scr_res["rules"].append({
                "criteria": rule.criteria,
                "pass": res
            })

            if not res:
                scr_res["pass"] = False

        screen_results.append(scr_res)

    return screen_results


def evaluate_formula(formula, history):
    """ Evaluate rule formula

    :param formula String: var1 operator var2 format

    :return: if formula is true or not
    :rtype: boolean

    """
    # Rule formula syntax var1 operator var2
    (var1, operator, var2) = formula.split(" ")
    (value1, value2) = get_variable_values(operator, var1, var2, history)

    # For XOVER and XUNDER rules, assume var1 < var2
    if operator == "XOVER":
        return cross_over(history, value1, value2)
    elif operator == "XUNDER":
        return cross_under(history, value1, value2)
    elif operator == "GT":
        return value1 > value2
    elif operator == "GTE":
        return value1 >= value2
    elif operator == "LT":
        return value1 < value2
    elif operator == "LTE":
        return value1 <= value2
    else:
        raise Exception("Unrecognized rule operator {}".format(operator))


def get_variable_values(operator, var1, var2, history):
    """ Depending on the operator, set var1 and var2 accordingly

    :param operator String: the operator
    :param var1 String: first variable
    :param var2 String: second variable

    :return: tuple of var1 and var2 value
    :rtype: tuple

    """
    if operator in ["XOVER", "XUNDER"]:
        return (int(var1.replace("MA", "")), int(var2.replace("MA", "")))
    else:
        return(convert_variable_value(var1, history),
               convert_variable_value(var2, history))


def convert_variable_value(var, history):
    """ Converts variable depending on type

    :param var String: the variable

    :return: the int or float value of the result
    :rtype: int or float

    """
    if "MA" in var:
        return last_moving_average(history, int(var.replace("MA", "")))
    elif var == "CP":
        return last_closing_price(history)
    else:
        raise Exception("Unrecognized rule operator {}".format(var))


def last_closing_price(history):
    """ Gets the last closing price from stock's history

    :param history list: list of price objects

    :return: last closing price
    :rtype: float

    """
    return history[-1].get("close")


def last_moving_average(history, days):
    """ Returns the simple moving average of a stock over n days

    :param history list: list of price objects
    :param days int: number of days

    :return: moving average
    :rtype: float

    """
    return sum([p["close"] for p in history[(-1 * days):]])/days


def prev_moving_average(history, days):
    """ Returns the simple moving average of stock over n days for previous day

    :param history list: list of price objects
    :param days int: number of days

    :return: moving average
    :rtype: float

    """
    return sum([p["close"] for p in history[(-1 * days) -1:-1]])/days


def cross_over(history, fast_moving_average, slow_moving_average):
    """ Does faster moving average move from being less than slower moving
    average yesterday to greater than today

    :param fast_moving_average int: fast moving average days modifier
    :param slow_moving_average int: slow moving average days modifier

    :return: if there is a cross over
    :rtype: boolean

    """
    last_fast = last_moving_average(history, fast_moving_average)
    last_slow = last_moving_average(history, slow_moving_average)
    prev_fast = prev_moving_average(history, fast_moving_average)
    prev_slow = prev_moving_average(history, slow_moving_average)

    return prev_fast < prev_slow and last_fast > last_slow


def cross_under(history, fast_moving_average, slow_moving_average):
    """ Does faster moving average move from being greather than slower moving
    average yesterday to less than today

    :param fast_moving_average int: fast moving average days modifier
    :param slow_moving_average int: slow moving average days modifier

    :return: if there is a cross under
    :rtype: boolean

    """
    last_fast = last_moving_average(history, fast_moving_average)
    last_slow = last_moving_average(history, slow_moving_average)
    prev_fast = prev_moving_average(history, fast_moving_average)
    prev_slow = prev_moving_average(history, slow_moving_average)

    return prev_fast > prev_slow and last_fast < last_slow
