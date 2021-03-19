import turtle as tr


class Circle:
    def __init__(self, startX, startY, radius, color):
        self.__startX = startX
        self.__startY = startY
        self.__radius = radius
        self.__color = color

    def draw(self):
        tr.up()
        tr.goto(self.__startX, self.__startY - self.__radius)
        tr.down()
        tr.begin_fill()
        tr.color(self.__color)
        tr.circle(self.__radius)
        tr.end_fill()
