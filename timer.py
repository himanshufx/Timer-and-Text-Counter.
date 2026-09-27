import time

def timer():
    user = int(input("Enter seconds for timer: "))
    while True:
        time.sleep(1)
        user -= 1
        print(user)
        if user == 1:
            print("Timer completed")
            break
        else:
            continue

def tryagain():
    timer()

    while True:
        try_again = str(input("Want to set another timer: (Yes/No): ")).lower()

        if try_again == "yes":
            timer()
        elif try_again == "no":
            print("Thanks for coming!")
            break
        else:
            print("Wrong option, Choose correct option!")

tryagain()