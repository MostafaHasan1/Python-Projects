x=2
while 1 != x:
    num = int(input("What number are you thinking: "))
    if num % 2 == 0:
        print("That's an even number! Have another?")
    else:
        print("That's an odd number! Have another?")
