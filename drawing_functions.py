import turtle


def draw_rectangle(side1, side2, color, fill):
    ''' draws a rectangle with side1 as horizontal and side2 as vertical'''
    turtle.setheading(0)
    turtle.color(color)
    turtle.pendown()
    if fill is True:
        turtle.begin_fill()
    for i in range(0,4):
        if i%2 == 0:
            turtle.forward(side1)
        else:
            turtle.forward(side2)
        turtle.right(90)
    if fill is True:
        turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)


def draw_road(length, width, horizontal):
    ''' Draws an individual road'''
    draw_rectangle(length, width, 'black', True)
    turtle.setheading(270)
    turtle.forward(width/2 - 3)
    turtle.left(90)

    # #Orienting horizontal roads
    # turtle_distance_horz = length/10
    # while(horizontal and turtle_distance_horz < length):
    #     turtle.forward(length/10)
    #     draw_rectangle(length/45, width/5, 'yellow', True)
    #     turtle_distance_horz += (length/10)

    # # Orienting vertical roads
    # turtle_distance_vert = width/10
    # turtle.forward(length/2 - 3)
    # turtle.right(90)
    # turtle.forward(450)
    # while(horizontal is False and turtle_distance_vert < width):
    #     turtle.setheading(90)
    #     turtle.forward(width/10)
    #     draw_rectangle(length/5, width/45, 'yellow', True)
    #     turtle_distance_vert += (width/10)
    

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


def draw_person(x_pos, y_pos):
    '''draws a person at a specific x and y coordinate'''
    turtle.setpos(x_pos, y_pos + 20)
    turtle.setheading(0)
    turtle.color('brown')
    turtle.pendown()
    # head
    turtle.circle(15)
    # torso
    turtle.setheading(270)
    turtle.forward(65)
    # legs
    turtle.setheading(235)
    turtle.forward(45)
    turtle.right(180)
    turtle.penup()
    turtle.forward(45)
    turtle.setheading(305)
    turtle.pendown()
    turtle.forward(45)
    turtle.right(180)
    turtle.penup()
    turtle.forward(45)
    # arms
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(45)
    turtle.pendown()
    turtle.forward(35)
    turtle.right(180)
    turtle.penup()
    turtle.forward(35)
    turtle.setheading(135)
    turtle.pendown()
    turtle.forward(35)
    turtle.right(180)
    turtle.penup()
    turtle.forward(35)


def draw_people(num_people,x_pos_left, y_pos_middle):
    '''draw how may people are required
    x_pos_left is bottom left most x_coord in grid section
    y_pos_middle is middle y_coord in grid section'''
    coord_iteration = 225 / (num_people + 1)
    for i in range(1, num_people + 1):
        draw_person(x_pos_left + (i*coord_iteration), y_pos_middle)


def draw_windows(num_windows, x_pos_left, y_pos_middle):
    '''draw the amount of windows required on the house
    x_pos_left is bottom left most x_coord in grid section
    y_pos_middle is middle y_coord in grid section'''
    coord_iteration = 225 / (num_windows + 1)
    turtle.setpos(x_pos_left + 20/num_windows + coord_iteration/2 ,y_pos_middle - 15)
    turtle.setheading(0)
    turtle.color('black')
    for i in range(1, num_windows + 1):
        draw_rectangle(26, 26, 'black', False)
        turtle.forward(13)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(26)
        turtle.penup()
        turtle.left(90)
        turtle.forward(13)
        turtle.left(90)
        turtle.forward(13)
        turtle.left(90)
        turtle.pendown()
        turtle.forward(26)
        turtle.penup()
        turtle.right(90)
        turtle.forward(13)
        turtle.right(90)
        turtle.forward(coord_iteration)



def draw_house(num_windows, x_pos_left, y_pos_middle):
    '''draw a house with as many windows required
    x_pos_left is bottom left most x_coord in grid section
    y_pos_middle is middle y_coord in grid section'''
    turtle.setpos(x_pos_left + 20, y_pos_middle)
    # house
    draw_rectangle(175, 100, 'pink', True)
    # roof
    turtle.color('grey')
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(35)
    turtle.forward(106.82)
    turtle.right(70)
    turtle.forward(106.82)
    turtle.right(145)
    turtle.forward(175)
    turtle.end_fill()
    turtle.penup()
    # door
    turtle.setpos(x_pos_left + 95.5, y_pos_middle - 55)
    turtle.setheading(90)
    draw_rectangle(30, 45, 'brown', True)
    turtle.setpos(x_pos_left+107.5, y_pos_middle - 80)
    turtle.color('yellow')
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
    # windows
    draw_windows(num_windows, x_pos_left, y_pos_middle)



    







if __name__ == "__main__":
    # Setting up the screen and turtle settings
    screen = turtle.Screen()
    screen.setup(900, 900)
    turtle.speed(speed='fastest')
    turtle.penup()
    # Drawing the roads
    draw_road_system()
    
    draw_house(3, -450, 345)

    

    turtle.done()
    