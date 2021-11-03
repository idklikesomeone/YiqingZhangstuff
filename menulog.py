def mainmenufunction():

   import os
   os.system('cls')

   print(" ------------------------------------------------")
   print("|                                                |")
   print("|    07Menu                                      |")
   print("|    Name : Yiqing                               |")
   print("|    Version : 01                                |")
   print("|                                                |")
   print(" ------------------------------------------------")
   print()
   print("1. Hello World")
   print("2. Goodbye World")
   print("3. Goodbye Person")
   print("4. Good Teacher")
   print("5. forLoop")
   print("6. whileLoop")
   print("7. string Loop")
   print("8. Convert to ascii")
   print("9. Encode a string")
   print("x. To Exit")
   optionnumber = input("Enter an option ")
   if optionnumber == "1":
       helloworldfunction()
   elif optionnumber == "2":
       goodbyeworldfunction()
   elif optionnumber == "3":
       goodbyepersonfunction() 
   elif optionnumber == "4":
       goodteacherfunction()
   elif optionnumber == "5":
       forloopfunction()
   elif optionnumber == "6":
        whileloopfunction()
   elif optionnumber == "7":
      stringloopfunction()
   elif optionnumber =="8":
       stringloopfunction()
   elif optionnumber =="9":
      stringloopfunction()
   elif optionnumber == "x":
       exitfunction()
   else:
       print()
       print("---Start of Output ---------------------------")
       print()
       print("invalid option")
       print()
       print("----End of Output -----------------------------")
       print()
       print()
       print()
       input("Press Enter to continue")
       mainmenufunction()

def mainmenuotherfunction():
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Yiqing                               |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print()
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit") 
    

def helloworldfunction():

    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 1")
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def goodbyeworldfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 2")
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def goodbyepersonfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 3")
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    personname = input("What is your name ? ")
    print("Goodbye", personname)
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def goodteacherfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 4")
    print()
    print("----Start of Output ---------------------------")
    print()
    teachername = input("Teacher's name (try Mr Horan) ")
    if teachername =="Mr Horan":
        print("You are lucky, he is a great teacher.") 
    else:
        print(teachername, "is an ok teacher")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def forloopfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()  
    print("Enter an option 5")
    print()
    print("----Start of Output ---------------------------")
    print()
    for x in range (1,500):
      print(x) 
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def whileloopfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 6")
    print()
    print("----Start of Output ---------------------------")
    print()

    userguess = 0
    correctanswer = "IST"

    while correctanswer != userguess:
        userguess = input("What is the name of this subject ")
        if correctanswer != userguess:
           print("Not Correct - try again")

    print()
    print()
    print(" Congratulations!!")
    print()
    print()
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def stringloopfunction():
    import os
    os.system('cls')
    mainmenuotherfunction() 
    print("Enter an option 7")
    print()
    print("---Start of Output ---------------------------")
    print()
    print("invalid option")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def convertfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 8")
    print()
    print("---Start of Output ---------------------------")
    print()
    print("invalid option")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def encodestringfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option 9")
    print()
    print("---Start of Output ---------------------------")
    print()
    print("invalid option")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    mainmenufunction()

def exitfunction():
    import os
    os.system('cls')
    mainmenuotherfunction()
    print("Enter an option x")
    print()
    print("----Start of Output ---------------------------")
    print()
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    print()
    quit()
  
mainmenufunction()















