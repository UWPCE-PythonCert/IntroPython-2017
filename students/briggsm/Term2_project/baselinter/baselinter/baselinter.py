'''BaseLinter'''

import json
import datetime
import os

LOCATION = "D:\\UW\\Intro-to-Python\\IntroPython-2017\\students\\briggsm\\Term2_project\\baselinter\\baselinter\\" # os.path.dirname(os.path.realpath('__file__'))
THISDATE = str(datetime.date.today()) # e:\MB\Better-Butter\Projects\BaseLinter
LIST_of_SETS = []
LINTER_NAME = ""


def open_set_json(filename):
    '''Opens a JSON file and returns the a list of sets.'''
    with open(filename) as f:
        read_data = f.read()
    in_data = json.loads(read_data)
    list_of_sets = []
    for key, value in in_data.items():
        list_of_sets.append(set(value))
    return list_of_sets


def text_to_list(filename):
    '''Take a text and return a list of words in order.'''
    try:
        with open(filename) as f:
            in_text = f.read()
            text_list = in_text.split()
            return text_list
    except FileNotFoundError:
        print("Error trying to find your file.")
        text_list = []
        return text_list


def wordlist_to_text(wordlist):
    '''Take a list of words and return a single string.'''
    text_out = ""
    for w in wordlist:
        text_out = text_out + w + " "
    text_out = text_out.strip()
    return text_out


def return_members(list_of_sets, item):
    '''Returns the set of an item is a member of the set, otherwise returns None.'''
    for i in list_of_sets:
        if item in i:
            return i
            break
    return None


def select_update(choices, wordlist, wordloc):
    '''With choices, the wordlist, a location, select a choice and 
    return updated wordlist.'''
    these_choices = list(choices)
    preview_list = wordlist[:]
    if (wordloc - 10) < 10:
        preview_start = 0
    else:
        preview_start = wordloc-10
    if wordloc + 10 > len(wordlist):
        preview_end = len(wordlist)
    else:
        preview_end = wordloc + 10
    preview_token = "[[" + wordlist[wordloc].strip() + "]]"
    preview_list[wordloc] = preview_token
    preview_list = preview_list[preview_start:preview_end]
    display_string = ""
    for w in preview_list:
        display_string = display_string + w + " "
        display_string.strip()
    display_choices = ""
    for ind, choice in enumerate(these_choices):
        display_choices = display_choices + "{} ) {} ".format(ind+1, choice)
    print("""
Select ----------------------------\n
{}\n
-----------------------------------\n
{}
-----------------------------------
""".format(display_string, display_choices))
    choiceindex = input("Select an option. > ")
    wordupdate = these_choices[int(choiceindex)-1]
    wordlist[wordloc] = wordupdate
    return wordlist


def load_linter():
    '''Load linters'''
    global LIST_of_SETS
    global LINTER_NAME
    global LOCATION

    linters = { "American Homophone" : "\\data\\guide-amhomo.json",
                "MS Docs Voice Guide" : "\\data\\guide-msdocs.json",
                "Business Jargon" : "\\data\\guide-businessjargon.json"}
    print("Choose a new linter.\n")
    lint_list = list(linters.keys())
    display_choices = ""
    for ind, choice in enumerate(lint_list):
        display_choices = display_choices + "{} ) {} ".format(ind+1, choice)
    print(display_choices)
    lint_choice = input("Select an option. > ")
    lint_choice = int(lint_choice) - 1
    LINTER_NAME = lint_list[lint_choice]
    LIST_of_SETS = open_set_json(LOCATION + "\\" + linters[LINTER_NAME])
    
    return True


def exit_app():
    '''Save the data; close the app.'''
    print("Goodbye.")
    return False

def check_file():
    ''' '''
    try:
        filename = input("File to check. > ")
    except FileNotFoundError:
        print("Please try a valid file name.")
        return True
    wordlist = text_to_list(filename)
    for wordloc, word in enumerate(wordlist):
        choices = return_members(LIST_of_SETS, word)
        if choices:
            wordlist = select_update(choices, wordlist, wordloc)
    outtext = wordlist_to_text(wordlist)
    filename_out = filename.split(".")[0] + "-" + THISDATE + "." + filename.split(".")[1]
    print("Done checking. Saving file as {}".format(filename_out))
    with open(filename_out, 'w') as f:
        f.write(outtext)
    return True




chooser = {
    "1": ("Check file.", check_file),
    "2": ("Load new linter.", load_linter),
    "3": ("Quit.", exit_app)
    }


def main():
    '''The main logic of the Linter application interface.'''
    global LINTER_NAME
    global LIST_of_SETS

    LINTER_NAME = "American Homophone"
    LIST_of_SETS = open_set_json(LOCATION + "\\data\\guide-amhomo.json")

    run = True
    while run == True:
        print("\nBase Linter | {} | {}\n".format(LINTER_NAME, THISDATE))
        try:
            for k in chooser.keys():
                print("{} | {}".format(k, chooser[k][0]))
            sel = input("Type a choice. > ")
            run = chooser[sel][1]()
        except KeyError:
            print("Please type a valid choice.")
        except IndexError:
            print("Please type a valid choice.")


if __name__ == "__main__":
    main()