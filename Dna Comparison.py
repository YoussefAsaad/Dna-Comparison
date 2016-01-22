def InputsOfDna(): #Obtains the two strings of Dna
    Dna1=""
    Dna2=""
    Dna1=input('Enter first Dna(A,T,C,G): ')
    Dna2=input('Enter second Dna(A,T,C,G): ')
    Dna1=Dna1.lower()
    Dna2=Dna2.lower()
    return(Dna1,Dna2);

def CheckingDna(Dna1,Dna2):

    for i in range(0,len(Dna1)): #checks that only certain letters were entered for dna #1
        if not((Dna1[i]=="a") or (Dna1[i]=="t") or (Dna1[i]=="c") or (Dna1[i]=="g")):
            Dna1=input("Enter Dna1 again:")
            Dna1, Dna2 = CheckingDna(Dna1,Dna2)
            break;

    for i in range(0,len(Dna2)): #checks that only certain letters were entered for dna #2
        if not((Dna2[i]=="a") or (Dna2[i]=="t") or (Dna2[i]=="c") or (Dna2[i]=="g")):
            Dna2=input("Enter Dna2 again:")
            Dna1, Dna2 = CheckingDna(Dna1,Dna2)
            break;
    
    return(Dna1,Dna2);

def CheckWhichCommand(Dna1,Dna2): # Checks that a legal command was entered
    Command=input("type a to add an indel, d to delete an indel, s for score, q for quit: ")
    if(Command=="a"): CommandA(Dna1,Dna2)
    elif(Command=="d"): CommandD(Dna1,Dna2)
    elif(Command=="s"): CommandS(Dna1,Dna2)
    elif(Command=="q"):print("you quit the program")
    else:
        print()
        print("invaild entry please try again")
        CheckWhichCommand(Dna1,Dna2)
    return;

def CommandA(Dna1,Dna2): #Adds indel for either Dna#1 or Dna#2
    WhichDna=input("Which dna would you like to add an idel to (1 or 2): ")
    
    if (WhichDna == "1"):
        NumIndex=input("which index do you want to add an indel (between 0, "+ str(len(Dna1))+ "):")

        if(int(NumIndex)<0) or (int(NumIndex)>(len(Dna1))):
            print("Error not in index")
            CommandA(Dna1,Dna2)
        else:
            Dna1= Dna1[:int(NumIndex)] + "-" + Dna1[int(NumIndex):]
            print()
            print("new Dna1: ",Dna1)
            print()
            CheckWhichCommand(Dna1,Dna2)
        
    
    elif(WhichDna == "2"):
        NumIndex=input("which index do you want to add an indel (between 0, "+ str(len(Dna2))+ "):")

        if(int(NumIndex)<0) or (int(NumIndex)>(len(Dna2))):
            print("Error not in index")
            CommandA(Dna1,Dna2)
        else:
                Dna2= Dna2[:int(NumIndex)] + "-" + Dna2[int(NumIndex):]
                print()
                print("New Dna2: ",Dna2)
                print()
                CheckWhichCommand(Dna1,Dna2)
    else:
        print()
        print("invalid entry please try again")
        CommandA(Dna1,Dna2)
    return;

def CommandD(Dna1,Dna2): #deletes and indel from either Dna string
    WhichDna=input("Which dna would you like to delete an idel to (1 or 2): ")

    if (WhichDna == "1"):
        NumIndex=input("Enter index of indel you would like to delete(between 1, "+ str(len(Dna1))+ "):")

        if(Dna1[int(NumIndex)-1]=="-"):
            Dna1=Dna1[:int(NumIndex)-1] +Dna1[(int(NumIndex)):]
            print()
            print("new Dna1:",Dna1)
            print()
            CheckWhichCommand(Dna1,Dna2)

        else:
            print ("There is no indel at this index")
            CheckWhichCommand(Dna1,Dna2)

    elif (WhichDna == "2"):
        NumIndex=input("Enter index of indel you would like to delete(between 1, "+ str(len(Dna2))+ "):")

        if(Dna2[int(NumIndex)-1]=="-"):
            Dna2=Dna2[:int(NumIndex)-1] +Dna2[(int(NumIndex)):]
            print()
            print("new Dna2:",Dna2)
            print()
            CheckWhichCommand(Dna1,Dna2)

        else:
            print ("There is no indel at this index")
            CheckWhichCommand(Dna1,Dna2)

    else:
        print()
        print("invalid entry please try again")
        CommandA(Dna1,Dna2)

    return;

def CommandS(Dna1,Dna2): #Compares the two Dna strings together to come up with a score
    Len1=len(Dna1)
    Len2=len(Dna2)
    matches=0
    misMatches=0
    
    if(Len1<Len2):
        for i in range(0,(Len2-Len1)):
            Dna1=Dna1+("-")
            
    elif(Len1>Len2):
        for i in range(0,(Len1-Len2)):
            Dna2=Dna2+("-")
            
    else:
        print

    for i in range(0,len(Dna1)):
        if(Dna1[i]==Dna2[i]) and (Dna1[i]!= "-"):
            matches+=1
            Dna1=Dna1[:(i)] +Dna1[i].lower() + Dna1[(i+1):]
            Dna2=Dna2[:(i)] +Dna2[i].lower() + Dna2[(i+1):]
        else:
            misMatches+=1
            Dna1=Dna1[:(i)] +Dna1[i].upper() + Dna1[(i+1):]
            Dna2=Dna2[:(i)] +Dna2[i].upper() + Dna2[(i+1):]

    print("Matches: ",matches)
    print("Mismatches: ",misMatches)
    print("Dna1: ",Dna1)
    print("Dna2: ",Dna2)
    CheckWhichCommand(Dna1,Dna2)
    return

def main(): #main function
    Dna=InputsOfDna()
    Check=CheckingDna(Dna[0],Dna[1])
    CheckWhichCommand(Check[0],Check[1])
    return;

main() #runs the main fucntion
    
