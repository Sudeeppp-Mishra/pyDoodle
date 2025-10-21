reminders = []

def add(reminder):
    reminders.append({"text":reminder, "completed":False})
    
    print(f"\n{'*'*len('Reminder added: '+reminder)}")
    print(f"Reminder added: {reminder}")
    print(f"{'*'*len('Reminder added: '+reminder)}")

def delete():
    if len(reminders) == 0:
        print("\n***********************")
        print("No reminders to delete!")
        print("***********************")
        return
    
    display()
        
    idx = int(input("Enter the no. of reminder to delete: "))
    
    if idx not in [i for i in range(len(reminders)+1)]:
        print(f"\n{'*'*len('Please enter the index that is in your list!')}")
        print("The index is not in your reminder's list!"
              "\nPlease enter the index that is in your list!")
        print(f"{'*'*len('Please enter the index that is in your list!')}")
        
    if idx in [i for i in range(len(reminders)+1)]:
        removed = reminders.pop(idx-1)
        print(f"{'*'*len('Deleted reminder: '+removed['text'])}")
        print(f"Deleted reminder: {removed['text']}")
        print(f"{'*'*len('Deleted reminder: '+removed['text'])}")

def modify():
    if len(reminders)==0:
        print("\n**************************************")
        print("Nothing to modify! Add reminder first!")
        print("**************************************")
        return
    
    display()
        
    idx = int(input("Enter index of reminder to modify: "))
    
    if idx not in [i for i in range(len(reminders)+1)]:
        print("\n***************************************************************")
        print("Please only enter the index listed in your reminders to modify!")
        print("***************************************************************")
        return
    
    modified = input("\nEnter the modified reminder: ")
    previous = reminders[idx-1]['text']
    
    reminders[idx-1]['text'] = modified
    
    print(f"\n{'*'*len(previous+' modified to '+modified+' successfully!')}")
    print(f"\"{previous}\" modified to \"{reminders[idx-1]['text']}\" successfully!")
    print(f"{'*'*len(previous+' modified to '+modified+' successfully!')}")

def is_completed():
    if len(reminders) == 0:
        print("\n********************************************")
        print("There is no reminder to set to be completed!")
        print("********************************************")
        return
    
    display()
    
    idx = int(input("Enter the index of reminder which is completed: "))
    
    if idx not in [i for i in range(len(reminders)+1)]:
        print("\n***********************************************")
        print("There is no reminder of this index in the list!")
        print("***********************************************")
    
    if reminders[idx-1]['completed']==False:
        reminders[idx-1]['completed'] = True    
        reminders[idx-1]['text']+=' ✔'
    else:
        print("\n*******************")
        print("ALREADY COMPLETED ✔")
        print("*******************")
        return

def display():
    if len(reminders)==0:
        print("\n**********************************")
        print("You haven't set any reminders yet!")
        print("**********************************")
        return
    
    print("\n<<----YOUR REMINDERS---->>\n")
    for i in range(len(reminders)):
        print(f"{i+1}. {reminders[i]['text']}")

def main():
    print(f"\033[1m  \n<<---WELCOME TO REMINDERS--->> \033[0m") # \033[1m ... \033][0m is for bold text
    
    while True:
        print("\n**************************************")
        choice = input("Enter \n1 for adding a reminder\n2 for deleting a reminder\n3 for modifying a reminder\n4 for selecting a reminder as complete\n5 for displaying reminders (q for exit):\n")
        print("**************************************\n")
        
        match choice:
            case '1':
                reminder = input("Enter your reminder to be set: ")
                add(reminder)
            
            case '2':
                delete()
                
            case '3':
                modify()
                
            case '4':
                is_completed()
                
            case '5':
                display()
            
            case 'q':
                break
            
            case _:
                print("Invalid Choice! Please enter valid choice!")
                
if __name__ == '__main__':
    main()