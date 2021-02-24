import turtle

def draw_rectangle(side1, side2, color):
    ''' draws a rectangle with side1 as horizontal and side2 as vertical'''
    turtle.setheading(0)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,4):
        if i%2 == 0:
            turtle.forward(side1)
        else:
            turtle.forward(side2)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)


def draw_road(length, width, horizontal):
    ''' Draws an individual road'''
    draw_rectangle(length, width, 'black')
    turtle.setheading(270)
    turtle.forward(width/2 - 3)
    turtle.left(90)

    #Orienting horizontal roads
    turtle_distance_horz = length/10
    while(horizontal and turtle_distance_horz < length):
        turtle.forward(length/10)
        draw_rectangle(length/45, width/5, 'yellow')
        turtle_distance_horz += (length/10)

    # Orienting vertical roads
    turtle_distance_vert = width/10
    turtle.forward(length/2 - 3)
    turtle.right(90)
    turtle.forward(450)
    while(horizontal is False and turtle_distance_vert < width):
        turtle.setheading(90)
        turtle.forward(width/10)
        draw_rectangle(length/5, width/45, 'yellow')
        turtle_distance_vert += (width/10)
    


def draw_road_system():
    '''Calls funcitons to draw road grid'''
    turtle.penup()
    # Horizontal roads
    for i in range(-1, 2):
        turtle.setpos(-450,i*(900/4))
        draw_road(900,30, True)
    # Vertical roads
    for i in range(-1, 2):
        turtle.setpos(i*(900/4),450)
        draw_road(30,900, False)





if __name__ == "__main__":
    # Setting up the screen and turtle settings
    screen = turtle.Screen()
    screen.setup(900, 900)
    turtle.speed(speed='fastest')

    # Drawing the roads
    draw_road_system()
    turtle.done()
    