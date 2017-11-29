#!/usr/bin/env python3

"""
Mailroom3.py
Dict
Comprehension
Exception Handling
"""


donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
donations = [[200, 500], [2000, 3000], [4000, 5000], [100, 150]]
donor_dict = { donor_names:donations for (donor_names, donations) in zip(donor_names, donations)}


def print_list():
  print(donor_dict)

def make_donation():
  donor_name = str(input("Full Name: "))
  new_donation = int(input("How much do you want to donate?: "))

  if (donor_name not in donor_dict):
    donor_dict[donor_name] = []

  donor_dict[donor_name].append(new_donation)
  print("Thank you for donation, Mr./Ms. {}! Your donation amount is USD {}.".format(donor_name, new_donation))


def thank_you_loop():
  while True:

    try: 
      choice = int(input("Select from one of these options:\n"
                          "(1) Show a list\n"
                          "(2) Enter a donation\n"
                          "(3) Exit\n"
                          ))
      if choice == 3:
        break
      elif choice == 1:
        print_list()
      elif choice == 2:
        make_donation()
      else:
        print("please type 1, 2 or 3")

    except ValueError as e:
      print("Error happened. Error is ",type(e),"Please type the number (1 to 3)")


def create_report():
  print("{msg1: <50}| {msg2: <12}| " \

      "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                       msg2="Total Given",

                                       msg3="Num Gifts",

                                       msg4="Average Gift"))
  for d in donor_dict:
    t = sum(donor_dict[d])
    n = len(donor_dict[d]) #list.count() is to count inside of the list (i.e. # by blue)
    a = t/n

    print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))



def send_letters():
  try:
    for n, d in donor_dict.items():
      name = n.replace(" ", "_")
      f = open('{0}.txt'.format(name), 'wb')
      text = "Dear {},\n Thank you for your kind donation of {}.\n It will be put to very good use.\n Sincerely,\n -The Team".format(n, d).encode()
      f.write(text)
      f.close()

  except IOError as i:
      print("Error code is", e)
  print("letters are sent")


def mainloop():
  while True:
    answer = int(input("Select from one of these options:\n"
                           "(1) Send a Thank you\n"
                           "(2) Create a Report\n"
                           "(3) Send letters to everyone\n"
                           "(4) quit\n"
                           ))
    if answer == 4:
      break
    elif answer == 1:
      thank_you_loop()
    elif answer == 2:
      create_report()
    elif answer == 3:
      send_letters()
    else:
      print("please type 1, 2, 3 or 4")


if __name__ == "__main__":
  print('starting...')
  mainloop()
