import random
user_choice=int(input("Enter Your Choice:Type 0 for Rock,1 for Paper,2 for sessior:"))
if user_choice<=2:
    if user_choice>=0:
        computer_choice=random.randint(0,2)
        print("computer choicce: ",computer_choice)
        if(computer_choice==user_choice):
            print("it's Draw")
        elif(computer_choice==0 and user_choice==2):
            print("You Lose")
        elif(user_choice==0 and computer_choice==2):
            print("You Win")
        elif(computer_choice>user_choice):
            print("You Lose")
        elif(user_choice>computer_choice):
            print("You Win")
else:
    print("Inavalid..")
        
        
    
    

 
