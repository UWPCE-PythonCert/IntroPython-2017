# Send emails thanking donors or generate a report.
# Python 3.6


import actions


donors = {'brian': [99], 'larry': [100], 'tyler': [101], 'mary': [102],
          'david': [103]}


# Get email template
with open('email.txt', 'r') as f:
    e_template = f.read()

while True:
    print('1. Send a thank you\n'
          '2. Create a report\n'
          '3. Send letters to all\n'
          '4. Quit\n')

    response = input('Please enter desired selection: ')

    if not response.isdigit():
        print('    Invalid entry, re-enter selection')
        continue

    # Send a thank you
    if response == '1':
        while True:
            user_input = input('Please enter full name: ')
            
            if user_input.isalpha():
                break
            else:
                print('    Invalid entry, please re-enter name')
        
        # Print list of donors
        if user_input.lower() == 'list':
            print()
            actions.list_database(donors)
            print()
        else:
            # Check or append new donor, get donation amount, and print email
            while True:
                money = input('Please enter donation amount: ')
                
                try:
                    donors.setdefault(user_input, []).append(float(money))
                except ValueError:
                    print('    Please enter a valid dollar amount')
                    continue
                else:
                    print()
                    actions.send_thankyou(user_input,
                                          donors[user_input][-1],
                                          e_template)
                    break

    # Create a report
    elif response == '2':
        actions.create_report(donors)
        print()

    # Bulk send all thank you's
    elif response == '3':
        for donor, donation in donors.items():
            print()
            actions.send_thankyou(donor,
                                  sum(donation),
                                  e_template)

    # Exit
    elif response == '4':
        raise SystemExit
