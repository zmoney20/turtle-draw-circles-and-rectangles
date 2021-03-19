import turtle as tr


class Rectangle:
    def __init__(self, startX, startY, width, height, color):
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self):
        tr.up()
        tr.goto(self.__startX, self.__startY)
        tr.seth(0)
        tr.down()
        tr.begin_fill()
        tr.color(self.__color)
        tr.forward(self.__width)
        tr.left(90)
        tr.forward(self.__height)
        tr.left(90)
        tr.forward(self.__width)
        tr.left(90)
        tr.forward(self.__height)
        tr.end_fill()
