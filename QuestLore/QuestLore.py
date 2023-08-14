''' EverQuest - Text-based Adventure Game
By: Dallin Hull
V 0.1
'''

from DunIntro import dungeonIntro
from endCredits import *
# Main Story Quest

# Inventory

inventory = []
guard =["far","awake"]

# Locations

    #Game Intro

def gameIntro():
    print("Welcome to EverQuest, Adventurer! Would you like to play?")
    print()
    answer = input("y/n ")

    if answer == "y":
        print()
        print("Your courage is admirable! Let us begin...")
        print()
    else:
        print()
        print("Are you sure? Let me repeat...")
        print()
        gameIntro()

    #Dungeon
        #Dungeon 1



  
def dungeonCommand():
    dungeonOne = input("What do you do adventurer? ")
# Commands ---------------------------------------
    if dungeonOne == "commands":
        print()
        print("look at, take, use, touch, inventory, surroundings")
        print("i.e. look at wall")
        print()
        dungeonCommand()
# Surroundings -----------------------------------
    elif dungeonOne == "surroundings":
        dungeonIntro()
        dungeonCommand()
# Inventory --------------------------------------
    elif dungeonOne == "inventory":
        print()
        print(inventory)
        print()
        dungeonCommand()
# Skeleton and Bone ------------------------------
    elif dungeonOne == "look at skeleton":
        print()
        print("You creep hesitantly toward what must have been a tortured prisoner long ago. Upon inspection of the remains, you see that a bone in the leg of the skeleton seems close to dislodging itself from the rest. ")
        print()
        dungeonCommand()
    elif dungeonOne == "touch skeleton":
        print()
        print("Every bone in the skeleton has been petrified and seems to be hard as stone. Perhaps a bone could be useful...")
        print()
        dungeonCommand()
    elif dungeonOne == "take bone":
        if "bone" in inventory:
            print()
            print("The bone is already in your inventory.")
            print()
            dungeonCommand()
        else:
            inventory.append("bone")
            print()
            print("You grab hold of the loose femer bone and, with some effort, wrench it free from it's now inanimate master. You place it in your inventory. ")
            print()
            dungeonCommand()
    elif dungeonOne == "use bone":
        if "bone" not in inventory:
            print()
            print("There is no bone in your inventory.")
            print()
            dungeonCommand()
        else:
            if "far" in guard:
                print()
                print("You look around, but cannot think of a use for the bone right now.")
                print()
                dungeonCommand()
            else:
                inventory.remove("bone")
                guard[1] = "faint"
                print()
                print("With the guard so close, you get an idea. You retrieve the bone from your inventory and hold it outside the bars just above the guard's head.")
                print("You bring down the bone with as much force as you can muster. With a loud THAWK, the guard slumps to the ground.")
                print("You're time is limited.")
                print()
                dungeonCommand()
# Bed and Needle ----------------------------------------
    elif dungeonOne == "look at bed":
        print()
        print("In spite of the skeleton's presence, the bed seems to be the most horrific part of this dungeon.")
        print("It is an unkempt pile of hay that is turning black in some places with mold. A putrid smell permeates from the bed and has been assaulting your nostrils since you awoke.")
        print("You spy cockroaches emerging from and withdrawing into the hay like groundhogs. You also see a glint of silver peaking out from the hay.")
        print()
        dungeonCommand()
    elif dungeonOne == "touch bed":
        print()
        print("Reluctantly, you begin to russle through the hay in the slim chance you find anything useful.")
        print("To your surprise, a somewhat robust silver needle rises to the top of the sickening bed.")
        print()
        dungeonCommand()
    elif dungeonOne == "take needle":
        if "needle" in inventory:
            print()
            print("The needle is already in your inventory.")
            print()
            dungeonCommand()
        else:
            inventory.append("needle")
            print()
            print("You take the needle from the stack of hay and quickly retreat back to the middle of the prison.")
            print()
            dungeonCommand()
    elif dungeonOne == "use needle":
        if "needle" not in inventory:
            print()
            print("There is no needle in your inventory.")
            print()
            dungeonCommand()
        else:
            if "far" in guard:
                print()
                print("The guard glances toward you. Better not use this now.")
                print()
                dungeonCommand()
            else:
                if "awake" in guard:
                    print()
                    print("The guard could wake at any minute! Better incapacitate him first.")
                    print()
                    dungeonCommand()
                else:
                    inventory.remove("needle")
                    print()
                    print("Now is the time to escape. You grabe the lock on your door and shove the needle inside.")
                    print("Eventually, you are able to pick the lock and the door swings open.")
                    endCredits()
# Rocks ---------------------------------------------------------
    elif dungeonOne == "look at rocks":
        print()
        print("The rocks are black and small enough to fit a couple in your hands.")
        print()
        dungeonCommand()
    elif dungeonOne == "take rocks":
        if "rocks" in inventory:
            print()
            print("The rocks are already in your inventory.")
            print()
            dungeonCommand()
        else:
            if "near" in guard:
                print()
                print("Umm...you threw those down the hall, remember?")
                print()
                dungeonCommand()
            else:
                inventory.append("rocks")
                print()
                print("You stash the rocks away in your inventory.")
                print()
                dungeonCommand()
    elif dungeonOne == "use rocks":
            if "near" in guard:
                print()
                print("Umm...you threw those down the hall, remember?")
                print()
                dungeonCommand()
            else:
                if "rocks" in inventory:
                    guard[0] = "near"
                    inventory.remove("rocks")
                    print()
                    print("When the guard is not paying attention, you stick your arm out through the bars of the door and throw the rocks down the corridor.")
                    print("The rocks make a clacking noise as they land on the stone floor.")
                    print("The guard snaps his head towards the sound. Then, with a grin, slowly changes his gaze to you.")
                    print("'So you think me to be stupid, do yuh? Well we will see who laughs now!' The guard picks up his chair and moves it within 1 foot of your cell door.")
                    print()
                    print("After about 30 minutes, you hear soft snoring by your cell door. The guard is fast asleep in his chair.")
                    print()
                    dungeonCommand()
                else:
                    print()
                    print("There are no rocks in your inventory")
                    print()
                    dungeonCommand()
#Guard (NOT INCLUDING rocks and bone and lock interactions) --------
    elif dungeonOne == "look at guard":
        print()
        print("The guard wears a red uniform and his face is adorned with a permanent scowl. He sits about 5 feet from the door to your cell.")
        print()
        dungeonCommand()
    elif dungeonOne == "touch guard":
        if "far" in guard:
            print()
            print("He is too far away.")
            print()
            dungeonCommand()
        else:
            print()
            print("You rethink your actions, since waking him would ruin your chances.")
            print()
            dungeonCommand()
# Walls and Floor ------------------------------------------
    elif dungeonOne == "look at wall":
        print()
        print("The wall is made of tightly packed stone blocks. There are finger nail marks left from previous prisoners.")
        print()
        dungeonCommand()
    elif dungeonOne == "touch wall":
        print()
        print("All warmth is sucked from your hand immediately. The wall is ice-cold and damp.")
        print()
        dungeonCommand()
    elif dungeonOne == "look at floor":
        print()
        print("The floor is made exactly the same as the walls. Some spots are stained red.")
        print()
        dungeonCommand()
    elif dungeonOne == "touch floor":
        print()
        print("All warmth is sucked from your hand immediately. The floor is ice-cold and damp.")
        print()
        dungeonCommand()
    elif dungeonOne == "look at lock":
        print()
        print("The lock is seems rather hefty. It may be pickable...")
        print()
        dungeonCommand()
    elif dungeonOne == "look at moon":
        print()
        print("As you stare at the beauty of the moon, you are both comforted and pained by this reminder of freedom.")
        print()
        dungeonCommand()
    elif dungeonOne == "touch lock":
        if "awake" in guard:
            print()
            print("The guard glares at you. 'Hey! Back off from that lock if you know what's good for yuh.")
            print("Better not right now.")
            print()
            dungeonCommand()            
        else:
            print()
            print("You grab the lock and pull with all your might...but to no avail.")
            print("There has got to be some way of getting this thing off.")
            print()
            dungeonCommand()
    # Else --------------------------------------------------------
    else:
        print()
        print("That does nothing.")
        print()
        dungeonCommand()


#LET THE GAME BEGIN!

gameIntro()
    
print()
print("You awake in confusion. Your clothes are sodden and cold. Your body aches, stiff with soreness, as you sit up on what feels like stone. The only light source is the pale gleeming of the moon through a barred window. ")
print()

dungeonIntro()

dungeonCommand()

endCredits()


'''
print("As your eyes adjust, you see that you are in a dungeon. The walls and floor are built of gray stone blocks.")
print("On the wall across from you, there is a lifeless skeleton hanging by shackles on the wall.")
print("On your right, you see a door amde of bars with a thick lock securing it to the wall. On your left, you see a bed made of rotting straw.")
print("On the floor, you see some sharp rocks and a rusty spoon.")
print()
input = print("What do you do adventurer?")
'''



