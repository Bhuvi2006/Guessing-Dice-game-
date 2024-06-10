import random
n=random.randint(1,6)
while True:
    a=int(input("Enter a number from 1 to 6: "))
    if n>a:
        print("ENTER BIG!")
    elif n==a:
        pass
    else:
        print(" ENTER SMALL!")
    if n== 1 and a==1:
        print(" _____")
        print("|     |")
        print("|  0  |")
        print("|_____|")
        print("You Guessed it right!!!")
        break
    elif n== 2 and a==2:
        print(" _____")
        print("| 0   |")
        print("|   0 |")
        print("|_____|")
        print("You Guessed it right!!!")
        break
    elif n== 3 and a==3:
        print(" _____ ")
        print("|     |")
        print("|0 0 0|")
        print("|_____|")
        print("You Guessed it right!!!")
        break
    elif n== 4 and a==4:
        print(" _____")
        print("|0   0|")
        print("|0   0|")
        print("|_____|")
        print("You Guessed it right!!!")
        break
    elif n== 5 and a==5:
        print(" _____")
        print("|0   0|")
        print("|  0  |")
        print("|_0__0|")
        print("You Guessed it right!!!")
        break
    elif n== 6 and a==6:
        print(" _____")
        print("|0 0 0|")
        print("|     |")
        print("|0 0 0|")
        print("|_____|")
        print("You Guessed it right!!!")
        break
        
    print("\n")
    
