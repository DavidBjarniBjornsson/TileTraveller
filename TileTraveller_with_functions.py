#https://github.com/DavidBjarniBjornsson/TileTraveller

# 1: Implementation two was a little bit easier because of the time saved by making functions for the directions. But because I didn´t find a way to use functions for the if statements, it still took quite some time
# 2: Implementation two is more readable beacuse it´s cleaner writing and not as big of a mess as implementation one. Using functions to print out the directions makes the code more readble
# 3: Using functions I was able to save myself quite some time not having to write upp every single print message. But that was about it.  

# One big while loop to keep the player in the game
# Player starts in tyle 1,1
# Player enters the direction in which he wants to go
# Player's new tyle displayed
# Every tyle is its own variable with its own possible inputs
# When the player gets to the tile 3,1 the while loop stops and the player wins 

tile_1 = 1.1
tile_2 = 1.2
tile_3 = 1.3
tile_4 = 2.3
tile_5 = 2.2
tile_6 = 2.1
tile_7 = 3.3
tile_8 = 3.2
tile_9 = 3.1
position = tile_1
win = False

validation = 1 

def invalid():
    print("Not a valid direction!")
    val = 0
    return val
def N():
    print("You can travel: (N)orth.")
    return
def NS():
    print("You can travel: (N)orth or (S)outh.")
    return
def ES():
    print("You can travel: (E)ast or (S)outh.")
    return
def EW():
    print("You can travel: (E)ast or (W)est.")
    return
def SW():
    print("You can travel: (S)outh or (W)est.")
    return
def NES():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    return

while not win:
    if position == tile_1:
        if validation == 1:
            N()
        command = str(input("Direction: "))
        if command == 'n' or command == 'N': 
            position = tile_2   
            win = False
            validation = 1
        else:
            invalid()

    elif position == tile_2:
        
        if validation == 1:
            NES()
        command = str(input("Direction: "))        
        if command == 'N' or command == 'n':
            position = tile_3
            validation = 1
        elif command == 'E' or command == 'e':
            position = tile_5
            validation = 1
        elif command == 'S' or command == 's':
            position = tile_1
            validation = 1
        else:
            invalid()
    
    elif position == tile_3:
        if validation == 1:
            ES()
        command = str(input("Direction: "))
        if command == 'E' or command == 'e':
            position = tile_4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile_2
            validation = 1
        else:
            invalid()
    
    elif position == tile_4:
        if validation == 1:
            EW()
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile_3
            validation = 1
        elif command == 'E' or command == 'e':
            position = tile_7
            validation = 1
        else:
            invalid()
    elif position == tile_5:
        if validation == 1:
            SW()
        command = str(input("Direction: "))
        if command == 'S' or command == 's':
            position = tile_6
            validation = 1
        elif command == 'W' or command == 'w':
            position = tile_2
            validation = 1
        else:
            invalid()
    elif position == tile_6:
        if validation == 1:
            N()
        command = str(input("Direction: "))           
        if command == 'N' or command == 'n':
            position = tile_5
            validation = 1
        else:
            invalid()
    elif position == tile_7:
        if validation == 1:
            SW()
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile_4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile_8
            validation = 1
        else:
            invalid()
    
    elif position == tile_8:
        if validation == 1:
            NS()
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile_7
            validation = 1
        elif command == 'S' or command == 's':
            position = tile_9
            validation = 1
        else:
            invalid()
    
    elif position == tile_9:
        print("Victory!")
        win = True