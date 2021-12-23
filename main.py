#Existing Student list
Student_list = [["1721862", "Kazi Jawad", "paid"], ["1721876", "Bushra Saba", "unpaid"], ["1722021", "Joya Moni", "unpaid"], ["1431298", "Isra Islam", "unpaid"], ["1411012", "Zulker Nien", "paid"],
                ["1922097", "Juaria Iqbal", "unpaid"], ["1921662", "Asha Moni", "paid"], ["1921740", "Maruf Hasan", "unpaid"], ["1610481", "Samsul Islam", "unpaid"], ["1730653", "Riya Afrin", "unpaid"]]


#Define function for displaying total fees collected
def total_fees_collected():
    sum = 0
    x=2000
    for i in range(0, len(Student_list)):
        if Student_list[i][2] == "paid":
            sum = sum + x
    print("***_Total fees collected {}TK_***".format(sum))

#Define function for fees collection, update and print receipt
def payment():
    x = 10 # Arbitrary value for enter the loop
    found = 1
    while x != "0":
        student_id = input("Enter your ID: ")  # Enter Student ID
        for i in range(0, len(Student_list)):
            if student_id == Student_list[i][0]:
                if Student_list[i][2] == "paid":  # If paid then workout below
                    print("\n")  # For new line
                    print("*** You have already paid ***")
                    found = 0
                    x="0"
                if Student_list[i][2] == "unpaid":  # Simple condition to enter the next step
                    option = 1
                    while option != "0":
                        amount = int(input("Enter required amount: "))  # Enter exact amount
                        if amount == 2000:  # If amount correct then
                            Student_list[i][2] = "paid"
                            print("\n")  # For new line
                            print("*** Payment Receipt ***")
                            print("-----------------------")
                            print("ID: {0}\nName: {1}\nYour payment was successful!\n".format(Student_list[i][0], Student_list[i][1], Student_list[i][2]))
                            option = "0"
                            found = 0
                            x="0"
                        else:  # If amount is not correct
                            print("\n") # For new line
                            print("--- Please! enter required fees ---")
                            found = 0

        if found == 1: # If ID was wrong
            print("User ID doesn't exist. Please check....")


#Define function for displaying unpaid persons list
def unpaid_list():
    found = 1
    print("****** Unpaid persons list ******")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("Student_ID  Student Name  Payment Condition")
    for i in range(0, len(Student_list)):
        if Student_list[i][2] == "unpaid":
            print("{0:10}  {1:17}  {2:17}".format(Student_list[i][0], Student_list[i][1], Student_list[i][2]))
            found = 0
    if found == 1:  # After checking the all student and everyone is paid
            print("\n")
            print("*** There is no unpaid person! ***")
option = 11 #Arbitrary value for entering while loop

#Loop to repeatedly display the menu
while option != "0":
    print("What do you wish to do?")
    print("1 -> Check total fees collected")
    print("2 -> Make your Payment")
    print("3 -> List of persons whose fees is not paid")
    print("0 -> Exit menu")
    print("\n")  # printing new line
    option = input("Select an option: ") # Enter option

    #check chosen option and called the appropriate function
    if option == "1":
        total_fees_collected() # Call total_fees_collected() function
        print("\n") # For new line
    elif option == "2":
        payment() # Call payment() function
        print("\n") # For new line
    elif option == "3":
        unpaid_list() # Call unpaid_list() function
        print("\n") # For new line
    elif option == "0":
        print("*** Thank you for using the system! ***")
    else:
        print("\n") # For new line
        print("***Non-existing option***")
        print("\n") # For new line





