"""
Description: This program will store an employee's SSN in a dictionary
along with their age, first name, and last name. This program also has
the capability to delete and change employees added to the dictionary.
"""
__author__="Daniel Aarness"
__date__="1/22/16"

def checkSSN(tmpssn):
    """
    Description: This function checks to see if a SSN is valid.
    Pre-Condition: tmpssn must be a string
    """
    if len(tmpssn) == 11:
        if tmpssn[0:3].isdigit() and tmpssn[4:6].isdigit() and tmpssn[7:].isdigit() and tmpssn[3] == '-' and tmpssn[6] == '-':
            return True
        else:
            return False
    else:
        return False

def createMenu(tmpMenuList):
    """
    Description: this function returns a menu
    Pre-Condition: tmpMenuList must have only 5 items
    """
    ct = 0
    choicect = 1
    finalMenu = choicect+")"+tmpMenuList[ct]
    ct += 1
    choicect += 1
    while ct < len(tmpMenuList):
        for el in tmpMenuList:
            finalMenu += choicect+")"+tmpMenuList[ct]+"\n"
            ct+=1
            choicect+=1
    return finalMenu

def deleteEmp(tmpSSN,empDict):
    """
    Description: this function deletes an employee
    Pre-Condition: tmpsss is a string empDict is a dictionary
    """
    if tmpSSN in empDict:
        del empDict[tmpSSN]
        return True
    else:
        return False

def addEmp(tmpSSN,tmpDict,tmpInfo):
    """
    Description: this function adds an employee to the dictionary.
    Pre-Condition: tmpSSN is a string, tmpDict is a dictionary, tmpInfo is a list
    """
    tmpDict[tmpSSN] = tmpInfo
    return True

def changeEmp(tmpDict,tmpSSN,tmpAge):
    """
    Description: this function edits the age of an employee
    Pre-Condition: tmpDict is a dictionary, tmpSSN is a string, tmpAge is a string
    """
    infoList = tmpDict[tmpSSN]
    infoList[-1] = tmpAge
    tmpDict[tmpSSN] = infoList

def printDict(tmpDict):
    """
    Description: this function prints a dictionary
    Pre-Condition: tmpDict is a dictionary
    """
    heading = "{0:11s} {1:15s} {2:15s} {3:3s}".format("SSN","First Name","Last Name","Age")
    print(heading)
    for k in tmpDict:
        ssn = k
        empList = tmpDict[k]
        fname = empList[0]
        lname = empList[1]
        age = empList[2]
        print("{0:11s} {1:15s} {2:15s} {3:3s}".format(ssn,fname,lname,age))
#main
#initialize the dictionary
empDict = {}
#choose which 5 variables to put into the menu
menuList = ["Add Employee","Delete Employee", "Change Employee", "Print Roster", "Quit"]
mainMenu = createMenu(menuList)
#print the menu
print(mainMenu)
#ask user what they want to do
userInp = input("Please input a number: ")
while userInp != 5:
    if userInp == 1:
        #ask the user to input an SSN
        empSSN = input("Please input the employee's SSN: ")
        if checkSSN(empSSN):
            #initialize the empInfo list
            empInfo = []
            #ask user for necessary info and put info into empInfo list 
            fname = input("Please input the Employee's first name: ")
            empInfo.append(fname)
            lname = input("Please input the Employee's last name: ")
            empInfo.append(lname)
            empAge = input("Please input the Employee's age: ")
            empInfo.append(empAge)
            if addEmp(empSSN,empDict,empInfo):
                #after user has been added to dictionary return to main menu
                print(fname, "has been succesfully added to the database.\n")
                print(mainMenu)
                userInp = input("Please input a number: ")
        else:
            #if SSN is invalid return to main menu
            print("ERROR -- invalid SSN -- Returning to main menu\n")
            print(mainMenu)
            userInp = input("Please input a number: ")        
    elif userInp == 2:
        #ask user for SSN of the employee they wish to delete
        empDel = input("Please input the SSN of the employee you wish to delete: ")
        if deleteEmp(empDel,empDict):
            #if SSN is in dictionary delete it and tell user it has been deleted
            print("Succesfully Deleted\n")
            print(mainMenu)
            userInp = input("Please input a number: ")           
        else:
            #if provided ssn is not in the dictionary return to main menu
            print("ERROR -- SSN not in database -- Returning to main menu\n")
            print(mainMenu)
            userInp = input("Please input a number: ")
    elif userInp == 3:
        #ask user which employee they want to edit
        empChange = input("Please input the SSN of the employee you wish to edit: ")
        if empChange in empDict:
            #ask user for updated age
            newAge = input("Please input the updated age of the employee: ")
            changeEmp(empDict,empChange,newAge)
            print("\n")
            print(mainMenu)
            userInp = input("Please input a number: ")
        else:
            #if ssn not in dictionary return to main menu
            print("ERROR -- SSN not in database -- Returning to main menu\n")
            print(mainMenu)
            userInp = input("Please input a number: ")
    elif userInp == 4:
        #call printDict function if user enters 4
        printDict(empDict)
        print("\n")
        #return to main menu after dictionary is printed
        print(mainMenu)
        userInp = input("Please input a number: ")
    else:
        #ask user to try again if they do not enter a valid number
        print("ERROR -- Please input a valid choice")
        print(mainMenu)
        userInp = input("Please input a number: ")
#thank user for using a program!!
print("Thanks for using this program")       
