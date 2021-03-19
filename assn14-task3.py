from circle import Circle
from rectangle import Rectangle
import turtle as tr


def main():
    done = False
    list1 = []
    while not done:
        print(" 1) Enter Circle: \n 2) Enter Rectangle: \n 3) Remove Shapes: \n 4) Draw Shapes: \n 5) Exit: ")
        userInput = eval(input("Enter a number: "))
        if userInput == 1:
            startX, startY = eval(input("Enter (x,y) coordinate for your circle position: "))
            radius = eval(input("Enter circle radius: "))
            color = input("Enter a color (green, red, blue, and yellow only): ")
            if color == "green" or color == "red" or color == "blue" or color == "yellow":
                list1.append(Circle(startX, startY, radius, color))
            else:
                input("Please pick a proper color: ")
        elif userInput == 2:
            startX, startY = eval(input("Enter (x,y) coordinate for your rectangle position: "))
            width = eval(input("Enter width: "))
            height = eval(input("Enter height: "))
            color = input("Enter a color: ")
            if color == "green" or color == "red" or color == "blue" or color == "yellow":
                list1.append(Rectangle(startX, startY, width, height, color))
            else:
                print("please pick a proper color: ")
        elif userInput == 3:
            if len(list1) == 0:
                print("There are no items to remove: ")
            else:
                print("There are ", len(list1), " items in your list")
                del list1[eval(input("Which would you like to remove? (enter an integer): ")) - 1]

        elif userInput == 4:
            tr.clear()
            for item in list1:
                item.draw()

        else:
            done = True
            print("Thanks for playing! ")
            tr.done()


main()
