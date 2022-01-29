import random

auto_try = True #set this to 'False' if you want to mannually play or to 'True' if you want to test automatically
switch = True #this is only relevant when 'auto_try' is on, determines whether or not to switch doors when asked to

num_of_tests = 100 #the respective number of tests to be run



wins = 0
for trial in range(0,num_of_tests):
    print(f"RUNNING TEST NUMBER {str(trial+1)}:")
    
    doors = {
        "1" : False,
        "2" : False,
        "3" : False
        }
    doors[random.choice(list(doors.keys()))] = True #sets a random door as 'True'

    #print(doors)

    if auto_try:
        chosen_door = random.choice(list(doors.keys()))
        print(f"Chosen door: {chosen_door}")
    else:
        print(f"Doors: {list(doors.keys())}")
        while True:
            chosen_door = input("Choose a door: ")
            if chosen_door in list(doors.keys()):
                break
            else:
                print("--unexpected value, try again--")
    #--------------------------------------------------------------------------- End of first stage
    while True:
        temp_key = random.choice(list(doors.keys() - chosen_door))
        if doors[temp_key]:
            continue #this check guarantees that the eliminated door will not be the chosen one nor the prized one
        else:
            doors.pop(temp_key)
            print(f"Opening Door {temp_key} ... Door {temp_key} did not contain the prize")
            print(f"Remaining doors are: {str(list(doors.keys()))}")
            break
        
    print("Would you like to switch doors?")
    
    #print(doors)

    if auto_try:
        if switch:
            chosen_door = random.choice(list(doors.keys() - chosen_door ))
            print(f"Switching doors... Your door is now Door {chosen_door}")
        else:
            print(f"Keeping Door... Your door remains Door {chosen_door}")
    else:
        
        while True:
            switch = input("yes/no: ").lower()
            if switch == "yes":
                chosen_door = random.choice(list(doors.keys() - chosen_door ))
                print(f"Swiching doors... Your door is now Door {chosen_door}")
                break
            elif switch == "no":
                print(f"Keeping Door... Your door remains Door {chosen_door}")
                break
            else:
                print("--Unexpected value, try again--")
    #--------------------------------------------------------------------------- End of second stage
    if doors[chosen_door]:
        print("     ...You won...")
        wins = wins + 1
    elif not doors[chosen_door]:
        print("     ...You lost...")
    print("\n")
    #--------------------------------------------------------------------------- End of third stage

print("\n\nEnd of tests")
print(f"You won {wins} out of {num_of_tests}")
print(f"Win percentage: {int((wins/num_of_tests)*100)}%")

input("press Enter to exit...") #pause for running on terminal

            
    

