# Name: Kobe Alexander
# Date: 3/29/2026
# Assignment: Module 1.3 Assignment

#The purpose of this code is to take a number from the user and then countdown backwords until theres no more numbers

def countdown_song(bottles):
    """
    Counts backward from the number of bottles entered by the user.
    Displays the song lyrics, changing from 'bottles' to 'bottle'
    when the count reaches 1.
    """
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        
        if bottles - 1 == 1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")


def main():
    print("Welcome to the Bottles of Beer countdown song!\n")

    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown_song(bottles)

    print("The wall is empty. Time to buy more beer!")


main()