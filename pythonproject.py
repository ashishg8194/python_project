#Project 1:ATM Simulator
balance=10000
attempts=3
correct_pin=1234
l=[]
b=True
while attempts>0:
    user_pin=int(input("Enter the pin:"))
    if user_pin==correct_pin:
        while True:
            print("1.Check Balance   2.Deposit")
            print("3.Withdraw        4.Exit")
            a=int(input("choose between the option given above:"))
            if a>4 or a<0:
                print("Invalid option!")
        
            elif a==4:
                print("Thank You")
                b=False
                for i in l:
                    print(i)
                break
            
            elif a==1:
                print(balance)
                    
            elif a==2:
                deposit=int(input("Enter the deposit amount:"))
                if deposit>=0:
                        balance+=deposit
                        l.append(("Deposit:"+str(deposit)))
                        print("New balance",balance)
                else:
                        print("Invalid amount!")
            elif a==3:
                    withdraw=int(input("Enter the withdraw amount:"))
                    if withdraw<=balance:
                        balance-=withdraw
                        l.append(("Withdraw:"+str(withdraw)))
                        print("New balance",balance)
                    else:
                        print("Invalid amount!")
              
    else:
        if attempts==0:
            print("Card blocked")
            break
        else:
            attempts-=1
            print("Wrong pin")
            print("left attempt:",attempts)
    if b== False:
         break


#Project 2:Student Marks Manager
students={"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
while True:
    print("1.Add student,  2.View all")
    print("3.Show topper,  4.Exit")
    a=int(input("choose any option given above:"))
    if a==4:
        print("Goodbye!")
        break
    elif a==1:
        c=input("Enter the student name:")
        if c in students.keys():
            print("Student already exists.")
        else:
            h=0
            j=[]
            while True:
                d=int(input("Enter  mark:"))
                
                if d<0 or d>100:
                    print("Invalid mark, try again.")
                elif h==2:
                    break
                else:
                    h+=1
                    j.append(d)
            students[c]=j
            print("Added succesfully!")
    elif a==2:
        for i,j in students.items():
            avg=sum(j)/3
            if avg>=85:
                print(f"{i} {avg:.2f} A")
            elif avg>=70:
                print(f"{i} {avg:.2f} B")
            elif avg>=50:
                print(f"{i} {avg:.2f} C")
            elif avg<=50:
                print(f"{i} {avg:.2f} F")
    elif a==3:
        a=0
        b=""
        for i,j in students.items():
            avg=sum(j)/3
            if avg>a:
                a=avg
                b=i
        print("Topper:",b)
    else:
        print("Invalid choice! Try again")
