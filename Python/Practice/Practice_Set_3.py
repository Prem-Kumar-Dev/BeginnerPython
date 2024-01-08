def PS3No1():
    a=int(input("Number:_"))
    if a%2==0:
        print("Even")
    else:
        print("Odd")

def PS3No2():
    a=int(input("Number:_"))
    if a%5==0:
        print("{} is divisible by 5".format(a))
    else:

        print("{} is not divisible by 5".format(a))

def PS3No3():
    a=input("A Character:_")
    if a.upper()==a:
        print(a.lower())
    else:
        print(a.upper())

def PS3No4():
    a=input("An Alphabet:_")
    if a.upper()=='A' or a.upper()=='E' or a.upper()=='I' or a.upper()=='O' or a.upper()=='U':
        print(a,"is a vowel")
    else:
        print(a,"is a consonant")

def PS3No5():
    a=input("The name of the plant:_")
    if a=="Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
    elif a=="spathiphyllum":
        print("No, I want a big Spathiphyllum!")
    else:
        print("Spathiphyllum! Not", a)

def PS3No6():
    a=int(input("Year:_"))
    if a<1582:
        print("Not within the Gregorian calender period")
    elif a%400==0 and a%100==0:
        print("{} is Leap Year".format(a))
    elif a%4==0 and a%100!=0:
        print("{} is Leap Year".format(a))
    else:
        print("{} is Not a Leap Year".format(a))

def PS3No7():
    a=int(input("An Integer:_"))
    if a%2!=0:
        print("Not Win")
    elif a%2==0 and a in range(2,6):
        print("Win")
    elif a%2==0 and a in range (6,21):
        print("Not Win")
    elif a%2==0 and a>20:
        print("Win")

def PS3No8():
    av_amount=10000
    print("Your Balance:",av_amount)
    with_amount= float(input("Withdrawl Amount:_"))
    if with_amount%5==0 and with_amount<av_amount:
        print("Transaction is successful!")
    elif with_amount>av_amount:
        print("Balance is low")
    else:
        print("Transaction is failed!")
    av_amount=av_amount-with_amount

    print("New Balance:",av_amount)

PS3No8()

