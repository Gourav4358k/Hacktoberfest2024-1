import os

def kbc_questions():
    os.system("cls")    #for clearing screen output
    questions=["Que : 1\n Which animal is known as the 'Ship of the Desert ? \n", #questions in list format
               "Que : 2\n How many days are there in a week ? \n",
               "Que : 3\n How many hours are there in a day ? \n",
               "Que : 4\n How many letters are there in the English alphabet ? \n",
               "Que : 5\n Rainbow consist of how many colours ? \n",
               "Oue : 6\n How many days are there in a leap year ? \n",
               "Que : 7\n How many minutes are there in an hour ? \n",
               "Que : 8\n How many seconds are there in a minute ? \n",
               "Que : 9\n How many seconds make one hour ? \n",
               "Que : 10\n Baby frog is known as....... \n",
               ]
    answer=["Camel",       #answers in list format
            "7 Days",
            "24 Hours",
            "26 letters",
            "7 colours",
            "366 days",
            "60 minutes",
            "60 seconds",
            "3600 seconds",
            "Tadpole",
            ]
    optional_Answer_1=["Tiger","Dog","Camel","Zebra"]                               #list of options
    optional_Answer_2=["4 Days","7 Days","6 Days","10 Days"]
    optional_Answer_3=["24 Hours","20 Hours","12 Hours","10 Hours"]
    optional_Answer_4=["10 letters","20 letters","26 letters","28 letters"]
    optional_Answer_5=["5 colours","10 colours","12 colours","7 colours"]
    optional_Answer_6=["300 days","355 days","366 days","365 days"]
    optional_Answer_7=["60 minutes","30 minutes","100 minutes","50 minutes"]
    optional_Answer_8=["30 seconds","60 seconds","100 seconds","50 seconds"]
    optional_Answer_9=["3000 seconds","6000 seconds","3600 seconds","5000 seconds"]
    optional_Answer_10=["Tadpole","Squid","Turtel","Mangur"]

    winnings=["1000",
              "2000",
              "4000",
              "8000",
              "16000",
              "32000",
              "64000",
              "128000",
              "256000",
              "512000"]
    
    current_Winning=0

    for i in range(0,10):
        print("Current Winning is : ",current_Winning)
       
        print(questions[i])      #prints the questions from the list quenstions
        
        if(i==0):
            for j in range(0,4):
                print(j+1,")",optional_Answer_1[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_1[ans]==answer[0]):
              print("correct answer : ",answer[0])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
        if(i==1):
            for j in range(0,4):
                print(j+1,")",optional_Answer_2[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_2[ans]==answer[1]):
              print("correct answer : ",answer[1])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break 
            else:
              print("Wrong answer...\n Try again ")
              break

        if(i==2):
            for j in range(0,4):
                print(j+1,")",optional_Answer_3[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_3[ans]==answer[2]):
              print("correct answer : ",answer[2])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==3):
            for j in range(0,4):
                print(j+1,")",optional_Answer_4[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_4[ans]==answer[3]):
              print("correct answer : ",answer[3])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==4):
            for j in range(0,4):
                print(j+1,")",optional_Answer_5[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_5[ans]==answer[4]):
              print("correct answer : ",answer[4])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==5):
            for j in range(0,4):
                print(j+1,")",optional_Answer_6[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_6[ans]==answer[5]):
              print("correct answer : ",answer[5])
              current_Winning=current_Winning+int(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==6):
            for j in range(0,4):
                print(j+1,")",optional_Answer_7[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_7[ans]==answer[6]):
              print("correct answer : ",answer[6])
              current_Winning=current_Winning+float(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==7):
            for j in range(0,4):
                print(j+1,")",optional_Answer_8[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_8[ans]==answer[7]):
              print("correct answer : ",answer[7])
              current_Winning=current_Winning+float(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break  
            else:
              print("Wrong answer...\n Try again ")
              break
       
        if(i==8):
            for j in range(0,4):
                print(j+1,")",optional_Answer_9[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_9[ans]==answer[8]):
              print("correct answer : ",answer[8])
              current_Winning=current_Winning+float(winnings[i])
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break
        
        if(i==9):
            for j in range(0,4):
                print(j+1,")",optional_Answer_10[j],end="      ")
            ans=int(input("\n \n Choose the correct answer : "))
            ans=ans-1
          # print(type(ans))
            if(optional_Answer_10[ans]==answer[9]):
              print("correct answer : ",answer[9])
              current_Winning=current_Winning+float(winnings[i])
              khatam=1
              print("khatam")
              if(khatam==1):
               os.system("cls")
               print(" Congratulations ",name.capitalize(), "You Won The Game ...")
               print(" You Won Rs. ",current_Winning,"/-")
            elif(ans==-1):
              os.system("cls")
              print(" Congratulations ",name.capitalize(), "\n")
              print(" You Won Rs. ",current_Winning,"/- \n")
              print(" 'Thankyou for playing KBC...'")
              break
            else:
              print("Wrong answer...\n Try again ")
              break

        print("\n")
        # print(answer[i])


os.system("cls")
print("Welcome to KBC show ")
name = input("Register your name : ")
print("hi",name,"ji to start the KBC Enter : 0  & 1 to exit the show")
start=input(" : ")
khatam=0
if(start=="0"):

    kbc_questions()
   
    # if(khatam==1):                #it's not working, no idea why ?
    #    os.system("cls")
    #    print(" Congratulations You Won The Game ...")
    #    print(" You Won Rs. 1111111111 ")



elif(start=="1"):
    print(name," bye have a nice day")

else:
    print("Invalid Option")
