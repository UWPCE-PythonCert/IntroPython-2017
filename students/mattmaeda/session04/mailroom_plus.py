#!/usr/bin/env python3

DONORS = {
    "George Washington": [1],
    "John Adams": [3],
    "Thomas Jefferson": [3],
    "John Quincy Adams": [2],
    "James Madison": [1]
}


def invalid_choice(response):
    print("Invalid choice '{}'".format(response))


def thanks():
    donor = input("Enter full name: ")
    if donor not in DONORS:
        DONORS[donor] = []

    donation = input("Enter a donation amount: ")
    DONORS[donor].append(int(donation))

    print("Dear {},\nThank you for your " \
          "donation of {}.\n\n".format(donor,donation))


def report():
    print("\n\n")
    print("{msg1: <50}| {msg2: <12}| " \
          "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",
                                           msg2="Total Given",
                                           msg3="Num Gifts",
                                           msg4="Average Gift"))
    print("-" * 90)
    for donor in _get_sorted_donors():
        money = DONORS[donor]
        total = sum(money)
        num = len(money)
        avg = total/num
        print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=donor,
                                                              t=total,
                                                              n=num,
                                                              a=avg))
    print("\n\n")


def _get_sorted_donors():
    totals = {}
    sorted_donors = []
    for d in DONORS.keys():
        total = sum(DONORS[d])
        if total in totals:
            totals[total].append(d)
        else:
            totals[total] = [d]

    for total in reversed(sorted(totals.keys())):
        sorted_donors += totals[total]

    return sorted_donors


if __name__ == "__main__":
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
                invalid_choice(choice)

            elif choice == 1:
                thanks()
            elif choice == 2:
                report()
            else:
                quit = True

        except ValueError:
            invalid_choice(response)
