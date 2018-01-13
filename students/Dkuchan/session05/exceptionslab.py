# exceptionslab.py



def safe_input():
    return None



while True:
    try:
        datas=input("Please input something cool: ")
    except:
        safe_input()
    if datas!='a':
        print("You didnt enter an 'a'")
        continue
        print("BLAAAAH")    #THIS IS GOOD TO KNOW IT DOES NOT CONTINUE THE LOOP AFTER THE CONTINUE!
    else:
        break
