#moretests.py

roster = [['Dan', 100, 200, 300, 400], ['Abbey', 100, 200, 300], ["Megan", 100, 200, 300, 100, 100], ['Spencer', 100, 200, 300], ['Marylee', 100, 200, 300]]    

while True:
    print("Whome would you like to thank?")
    for i in range(0, len(roster)):
        print(roster[i][0])
    print()
    selection = input("Please type the name of the donor you would like to thank: ")
    for i in range(0, len(roster)):
        if selection in roster[i]:
            nameloc = roster[i].index(selection)
            print(nameloc)
            break