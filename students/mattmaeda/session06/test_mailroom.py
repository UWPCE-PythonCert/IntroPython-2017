import unittest
from mailroom import Mailroom

EXPECTED_REPORT = """

Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Monty Python                                       $       10.00           1         10.00
John Adams                                         $        3.00           1          3.00
Thomas Jefferson                                   $        3.00           1          3.00
John Quincy Adams                                  $        2.00           1          2.00
George Washington                                  $        1.00           1          1.00
James Madison                                      $        1.00           1          1.00

"""

class TestMailroom(unittest.TestCase):
    """ Unit tests for mailroom """
    def setUp(self):
        donors = {
            "George Washington": [1],
            "John Adams": [3],
            "Thomas Jefferson": [3],
            "John Quincy Adams": [2],
            "James Madison": [1]
        }

        self.mailroom = Mailroom(donors)


    def test_get_menu(self):
        """ test menu """
        self.assertEqual({1: "Send a Thank You",
                          2: "Create a Report",
                          3: "Quit"}, self.mailroom.get_menu())


    def test_thanks(self):
        """ test thank you letter """
        self.assertEqual("\n\nDear Monty Python,\nThank you for your " \
                         "donation of 10.\n\n",
                         self.mailroom.thanks("Monty Python", 10))


    def test_report(self):
        """ test report generation """
        self.mailroom.thanks("Monty Python", 10)
        self.assertEqual(EXPECTED_REPORT, self.mailroom.report())


    def test_get_sorted_donors(self):
        """ test sorting of donors """
        self.mailroom.thanks("Monty Python", 10)
        self.assertEqual(["Monty Python", "John Adams", "Thomas Jefferson",
                          "John Quincy Adams", "George Washington",
                          "James Madison"], self.mailroom._get_sorted_donors())


if __name__ == "__main__":
    unittest.main()
