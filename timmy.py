tim = "global"
tim=10

choice = "global"

#=========================================================
def mainmenu():
    print("1)add to tim")
    print("2)subtract from tim")
    
    choice = input("pick a number")
    
    if choice == "1":
        print("you chose one")
        tim = tim+5
        print(tim)
    if choice == "2":
        print("you chose two")
#=========================================================

    
mainmenu()

