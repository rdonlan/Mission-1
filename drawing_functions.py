import turtle


def draw_rectangle(side1, side2, color, fill):
    ''' draws a rectangle with side1 as horizontal and side2 as vertical
    @side1 {int}: the horizontal length of the rectangle
    @side2 {int}: the vertical length of the rectangle
    @color {str}: the color of the rectangle
    @fill {bool}: true if the rectangle will be filled, false if it will be empty
    return: None
    '''
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
    ''' Draws an individual road
    @length {int}: the horizontal length of the road
    @width {int}: the vertical length of the road
    @horizontal {bool}: True if the road is horizontal, False if road is vertical
    return: None
    '''
    draw_rectangle(length, width, 'black', True)
    turtle.setheading(270)
    turtle.forward(width/2 - 3)
    turtle.left(90)

    #Orienting horizontal roads
    turtle_distance_horz = length/10
    while(horizontal and turtle_distance_horz < length):
        turtle.forward(length/10)
        draw_rectangle(length/45, width/5, 'yellow', True)
        turtle_distance_horz += (length/10)

    # Orienting vertical roads
    turtle_distance_vert = width/10
    turtle.forward(length/2 - 3)
    turtle.right(90)
    turtle.forward(450)
    while(horizontal is False and turtle_distance_vert < width):
        turtle.setheading(90)
        turtle.forward(width/10)
        draw_rectangle(length/5, width/45, 'yellow', True)
        turtle_distance_vert += (width/10)
    

def draw_road_system():
    '''Calls funcitons to draw road grid
    return: None
    '''
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
    '''draws a person at a specific x and y coordinate
    @x_pos {float}: x-coordinate to draw person
    @y_pos {float}: y-coordinate to draw person
    return: None
    '''
    turtle.setpos(x_pos, y_pos + 20)
    turtle.setheading(0)
    turtle.color('brown')
    turtle.pendown()
    # head
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
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
    @num_people {int}: number of people to draw
    @x_pos_left {float}: the bottom left most x-coordinate in the grid section
    @y_pos_middle {float}: the middle y-coordinate in the grid section
    return: None
    '''
    coord_iteration = 225 / (num_people + 1)
    for i in range(1, num_people + 1):
        draw_person(x_pos_left + (i*coord_iteration), y_pos_middle)


def draw_windows(num_windows, x_pos_left, y_pos_middle):
    '''draw the amount of windows required on the house
    @num_windows {int}: number of windows to draw
    @x_pos_left {float}: the bottom left most x-coordinate in the grid section
    @y_pos_middle {float}: the middle y-coordinate in the grid section
    return: None
    '''
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
    @num_windows {int}: number of windows to draw
    @x_pos_left {float}: the bottom left most x-coordinate in the grid section
    @y_pos_middle {float}: the middle y-coordinate in the grid section
    return: None
    '''
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


def draw_tree(x_pos, y_pos, height_multiplier):
    '''draw a tree given an x and y coordinate
    @x_pos {float}: x-coordinate to draw tree
    @y_pos {float}: y-coordinate to draw tree
    @height_multiplier {float}: a value to multiply the height of 
        the tree, less trees = higher multiplier
    return: None
    '''
    turtle.setpos(x_pos, y_pos + 40*height_multiplier)
    # leaves
    turtle.color('green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(315)
    turtle.forward(40*height_multiplier)
    turtle.right(135)
    turtle.forward(20*height_multiplier)
    turtle.left(135)
    turtle.forward(40*height_multiplier)
    turtle.right(135)
    turtle.forward(20*height_multiplier)
    turtle.left(135)
    turtle.forward(40*height_multiplier)
    turtle.right(135)
    turtle.forward(88.284271247*height_multiplier)
    turtle.right(135)
    turtle.forward(40*height_multiplier)
    turtle.left(135)
    turtle.forward(20*height_multiplier)
    turtle.right(135)
    turtle.forward(40*height_multiplier)
    turtle.left(135)
    turtle.forward(20*height_multiplier)
    turtle.right(135)
    turtle.forward(40*height_multiplier)
    turtle.penup()
    turtle.end_fill()
    
    # stump
    turtle.setheading(270)
    turtle.color('brown')
    turtle.forward(85*height_multiplier)
    turtle.right(90)
    turtle.forward(8)
    draw_rectangle(10*height_multiplier, 20*height_multiplier, 'brown', True)
    turtle.penup()


def draw_forest(num_trees, x_pos_left, y_pos_middle):
    '''draw a forest with as many trees as required
    @num_trees {int}: number of trees to draw
    @x_pos_left {float}: the bottom left most x-coordinate in the grid section
    @y_pos_middle {float}: the middle y-coordinate in the grid section
    return: None
    '''
    turtle.setpos(x_pos_left + 20, y_pos_middle)
    coord_iteration = 225 / (num_trees + 1)
    for i in range(1, num_trees + 1):
        draw_tree(x_pos_left + (i*coord_iteration), y_pos_middle, (0.5/num_trees) + 1)



if __name__ == "__main__":
    # Setting up the screen and turtle settings
    screen = turtle.Screen()
    screen.setup(900, 900)
    turtle.speed(speed='fastest')
    turtle.penup()

    turtle.done()
    