import graphics as g
from graphics import *

def welcomeMessage():
    print( "Welcome to the area computation tool!")
    print()
    print( "******Menu******" )
    print()
    return welcomeMessage
    
def Menu():
    print( "Tri    Compute the area of a triangle" )
    print( "Trap   Compute the area of a trapezoid")
    print( "Rec    Compute the area of a rectangle")
    print( "Quit   Quit the tool")
    return Menu 

def shapeChoice():
    print()
    choice=input( "Please enter your choice:  ")
    while not(choice == 'tri', 'trap', 'rec'):
        print(" '' is an invalid choice")
        choice=input( "Please enter your choice:  ")
        if choice == tri:
            print( "You chose: tri")
        if choice == trap:
            print("You chose: trap")
        if choice ==rec:
            print("You chose: rec")
            return shapeChoice

def main():
    welcomeMessage()
    Menu()
    shapeChoice()
    
main()
    
    