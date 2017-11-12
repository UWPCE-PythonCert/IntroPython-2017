#!/usr/bin/env python3

REPORT_HEADER = "{donor: <50}| {total: <12}| {num: <10}| {avg: <12}"
REPORT_LINE = "{0: <50} ${1: 12.2f}{2: 12d}{3: 14.2f}"

class Mailroom(object):

    def __init__(self, donor_dict):
        self.donors = donor_dict


    def invalid_choice(self, response):
        print("Invalid choice '{}'".format(response))


    def thanks(self):
        donor = input("Enter full name: ")
        if donor not in self.donors:
            self.donors[donor] = []

        donation = input("Enter a donation amount: ")
        self.donors[donor].append(int(donation))

        print("Dear {},\nThank you for your " \
              "donation of {}.\n\n".format(donor,donation))


    def report(self):
        print("\n\n")
        print(REPORT_HEADER.format(donor="Donor Name",
                                   total="Total Given",
                                   num="Num Gifts",
                                   avg="Average Gift"))
        print("-" * 90)

        print("\n".join([REPORT_LINE.format(d,
                            sum(self.donors[d]),
                            len(self.donors[d]),
                            sum(self.donors[d])/len(self.donors[d]))
            for d in self._get_sorted_donors()]))

        print("\n\n")


    def _get_sorted_donors(self):
        totals = {}
        for d in self.donors.keys():
            totals.setdefault(sum(self.donors[d]),[]).append(d)

        sorted_donors = []
        for total in reversed(sorted(totals.keys())):
            sorted_donors += totals[total]

        return sorted_donors


if __name__ == "__main__":
    donors = {
        "George Washington": [1],
        "John Adams": [3],
        "Thomas Jefferson": [3],
        "John Quincy Adams": [2],
        "James Madison": [1]
    }

    mailroom = Mailroom(donors)

    quit = False

    while not quit:
        print("")
        print("1: Send a Thank You")
        print("2: Create a Report")
        print("3: Quit")
        print("")
        response = input("Enter your number choice: ")

        try:
            choice = int(response)
            if choice < 0 or choice > 3:
                mailroom.invalid_choice(choice)

            elif choice == 1:
                mailroom.thanks()
            elif choice == 2:
                mailroom.report()
            else:
                quit = True

        except ValueError:
            mailroom.invalid_choice(response)
