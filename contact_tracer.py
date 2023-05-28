
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 10895647 # put your student number here as an integer
student_name   = 'Steven Mikoczi' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  CONTACT TRACER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "visualise".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client requirements" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 9 # squares (default is 9)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T TOUCH THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "visualise" function.  ALL of your solution code
#  must appear in this area.  Do NOT put any of your code in other
#  parts of the program and do NOT change any of the provided code
#  except as allowed in the main program below.
#


# Define global variables to use in functions

# Find the bottom left corner of entire grid to use as reference for mapping grid
left_edge = -(grid_width * cell_size) // 2 - 0.5 
bottom_edge = -(grid_height * cell_size) // 2 + 1

# Store the current selected variant
variant = 0

# Create Functions for 4 variants of one base image
def main_image(outside_color): # change colour to represent season
    # Draw Black border around 100 x 100 pixels
    penup()
    width(1)
    pendown()
    fillcolor('snow') # Set bg colour for icon
    begin_fill()
    seth(0)
    for wall in range(4):
        forward(100)
        left(90)
    end_fill()
    penup()

    # Get to starting point to draw window
    seth(0) 
    forward(10)
    seth(90)
    forward(15)

    # Begin drawing window pane
    color('darkgrey') # Choose colour of window pane
    fillcolor(outside_color) 
    width(3)
    begin_fill()
    seth(0)
    pendown()
    for window_pane in range(4):
        forward(80)
        left(90)
    end_fill()
    penup()

    # Get ready to draw inside frame of window
    seth(0)
    forward(40)
    seth(90)
    pendown()
    forward(80)
    backward(40)
    seth(180)
    forward(40)
    backward(80)
    forward(40)
    penup()

    # Draw plant pot
    seth(270)
    forward(55)
    seth(180)
    forward(10)
    seth(0)
    color('sienna') # Outline colour of plant pot
    width(1)
    begin_fill()
    fillcolor('chocolate') # Fill colour of plant pot
    pendown()
    forward(20)
    seth(75)
    forward(40)
    seth(180)
    forward(40)
    seth(285)
    forward(40)
    seth(0)
    forward(20)
    end_fill()
    
    # Draw the lip of the plant pot
    penup()
    seth(75)
    forward(30)
    seth(0)
    fillcolor('sienna') # Fill color of plant pot lip
    pendown()
    begin_fill()
    forward(5)
    seth(90)
    forward(10)
    seth(180)
    forward(45)
    seth(270)
    forward(10)
    seth(0)
    forward(45)
    end_fill()
    penup() # Penup to prepare for unique items to be added

def summer(outside_color): 
    # Add base image for icons
    main_image(outside_color)
    
    # Setup to draw the Sun
    seth(0)
    forward(16)
    seth(90)
    forward(64)
    seth(180)
    forward(25)
    seth(270)
    color('gold', 'yellow') # Sun color, outline and fill

    # Draw the sun
    pendown()
    begin_fill()
    circle(30,78)
    seth(90)
    forward(29)
    seth(180)
    forward(24)
    end_fill()
    penup()

    # Setup to start drawing plant
    forward(14)
    seth(270)
    forward(52)
    seth(90)
    width(3)
    color('green')
    seth(90)

    # Begin drawing plant
    pendown()
    circle(20,45)
    begin_fill() 
    color('green')
    circle(30,30) # Start of the stem from plant pot
    penup() # lift pen to avoid overlap of stem on flower
    forward(5)
    dot(10,'gold') # Draw first flower on left, choose colour and size of flower
    dot(5,'burlywood') # Draw pollen of flower, choose colour
    backward(5) # go back to stem to continue drawing
    seth(320)
    pendown() # Pendown to continue drawing stem
    circle(30,30)
    end_fill()
    angle = 85 # Degrees, set for curve for loop
    for right_curve in range(15):
        seth(angle)
        forward(2)
        angle = angle - 3
    dot(10,'gold') # Draw second flower on right, choose colour and size of flower
    dot(5,'burlywood') # Draw pollen of flower, choose colour
    penup()

def winter(outside_color):
    # Add base image of icon
    main_image('lightgrey')

    # Prepare to draw snow
    penup()
    color('white') # Choose colour of snow
    forward(13)
    dot(4)
    seth(110)
    forward(10)

    # Start drawing snow
    dot(4)
    seth(85)
    forward(20)
    dot(4)
    seth(120)
    forward(8)
    dot(4)
    for snow in range(5):
        seth(80)
        dot(4)
        forward(15)
        seth(120)
        dot(4)
        forward(12)
        seth(270)
        dot(4)
        forward(30)
        seth(180)
        forward(10)
        
    # Prepare to draw plant
    penup()
    seth(0)
    forward(42)
    seth(180)
    seth(90)

    # Draw Xmas Tree Trunk
    color('brown')
    width('3')
    pendown()
    begin_fill()
    forward(10)
    seth(180)
    forward(11)
    seth(270)
    forward(10)
    seth(0)
    forward(11)
    end_fill()
    penup()
    
    # Draw triangle base 
    length = 33 # Pixel length for base triangle
    seth(90) # go to staring point of tree
    forward(10)
    seth(180)
    forward(22)
    seth(0)
    color('green') # Colour of tree
    begin_fill()
    pendown()
    forward(length)
    left(135)
    forward(length / sqrt(2))
    left(90)
    forward(length / sqrt(2))
    left(135)
    end_fill()
    penup()

    # Draw middle of tree branches
    seth(90)
    forward(16)
    seth(0)
    forward(6)
    begin_fill()
    length = 22 # Pixel length of middle triangle
    pendown()
    forward(length)
    left(135)
    forward(length / sqrt(2))
    left(90)
    forward(length / sqrt(2))
    left(135)
    end_fill()
    penup()

    # Draw top of tree branches
    seth(90)
    forward(12)
    seth(0)
    forward(5)
    begin_fill()
    length = 11 # Pixel length of top triangle
    pendown()
    forward(length)
    left(135)
    forward(length / sqrt(2))
    left(90)
    forward(length / sqrt(2))
    left(135)
    end_fill()
    penup()

def spring(outside_color):
    # Add base image of icons
    main_image(outside_color)

    # Prepare to draw cloud
    seth(90)
    forward(45)
    seth(180)
    forward(45)
    seth(0)
    color('lightslategray','gainsboro') # Set outline colour and fill colour of cloud
    forward(20)
    seth(90)
    forward(15)
    seth(180)
    begin_fill()

    # Start drawing cloud
    pendown()
    circle(10,90)
    seth(180)
    circle(10,90)
    seth(0)
    forward(20)
    end_fill()
    penup()
    forward(3)
    begin_fill()
    pendown()
    forward(37)
    seth(120)
    circle(20,60)
    seth(90)
    circle(15,110)
    end_fill()
    penup()

    # Prepare to draw plant
    seth(270)
    forward(52)
    width(2)
    pencolor('green') # Choose plant colour
    seth(90)
    pendown()
    circle(20,45)
    fillcolor('green') # choose colour of leaf

    # Draw Leaf
    begin_fill()
    seth(150) 
    circle(30,30)
    seth(320)
    circle(30,30)
    
    # Draw Leaf 2
    seth(30)
    forward(10)
    seth(20)
    forward(10)
    seth(250)
    forward(5)
    seth(180)
    forward(15)
    end_fill()

    # Draw Stem
    seth(86)
    forward(7)
    seth(84)
    forward(7)
    seth(82)
    forward(7)

    # Draw flower
    dot(15,'crimson') # choose size and colour of flower
    dot(7, 'sandybrown') # choose size and colour of pollen
    penup()

def autumn(outside_color):
    # Add base image of icons
    main_image(outside_color)

    # Prepare to draw wind
    seth(0)
    forward(10)
    seth(90)
    forward(50)
    seth(0)
    color('ivory')  # Set colour of wind gusts
    pendown()

    # Draw wind gust
    angle = 35 # Degrees, Set variable for right_curve loop
    for right_curve in range(30):
        right(angle)
        forward(2)
        angle = angle - 3
    penup()
    seth(140)
    forward(18)
    # Draw second wind gust
    pendown()
    seth(0)
    angle = 35 # Degrees, set variable for right_curve loop
    for right_curve in range(30):
        right(angle)
        forward(2)
        angle = angle - 3
    penup()
    
    # Prepare to draw dandelions
    dandelion_stem = 'sandybrown'# Set colour of stems
    dandelion_colour = 'oldlace' # Set colour of dandelions
    seth(270)
    forward(42)
    seth(0)
    forward(30)
    seth(90)
    width(3)
    color(dandelion_stem) # Set colour of stems

    # Draw Dandelions
    pendown()
    angle = 8
    for left_curve in range(6):
        left(angle)
        forward(5)
        angle = angle + 3
    color(dandelion_colour)
    # dot(4,'cornsilk')
    seth(90)
    angle = 90
    for dandelion in range(36):
        width(1)
        seth(angle)
        forward(10)
        backward(10)
        angle = angle + 10
    penup()
    seth(270)
    forward(17)
    seth(0)
    forward(25)
    seth(90)
    color(dandelion_stem)
    pendown()
    width(3)
    angle = 8
    for right_curve in range(7):
        right(angle)
        forward(5)
        angle = angle + 7
    seth(90)
    color(dandelion_colour)
    angle = 90
    for dandelion in range(36):
        width(1)
        seth(angle)
        forward(10)
        backward(10)
        angle = angle + 10
    penup()


# Complete the visualisation using the provided data set
def visualise(instructions):
    
    #  Define a function to determine where to draw on the grid 
    def grid_placement(column=None, row=None):

        # Find x_coordinate
        if column == 'a':
            x_coord = left_edge # refers to global variable
        elif column == 'b':
            x_coord = left_edge + cell_size 
        elif column == 'c':
            x_coord = left_edge + cell_size * 2
        elif column == 'd':
            x_coord = left_edge + cell_size * 3        
        elif column == 'e':
            x_coord = left_edge + cell_size * 4  
        elif column == 'f':
            x_coord = left_edge + cell_size * 5  
        elif column == 'g':
            x_coord = left_edge + cell_size * 6  
        elif column == 'h':
            x_coord = left_edge + cell_size * 7  
        elif column == 'i':
            x_coord = left_edge + cell_size * 8 
    
        
        # Find y_coordinate
        if row == 1:
            y_coord = bottom_edge # refers to global variable
        elif row == 2:
            y_coord = bottom_edge + cell_size
        elif row == 3:
            y_coord = bottom_edge + cell_size * 2
        elif row == 4:
            y_coord = bottom_edge + cell_size * 3     
        elif row == 5:
            y_coord = bottom_edge + cell_size * 4 
        elif row == 6:
            y_coord = bottom_edge + cell_size * 5  
        elif row == 7: 
            y_coord = bottom_edge + cell_size * 6

        # Go to bottom left corner of selected grid square
        goto(x_coord,y_coord)

    # A function to draw selected variant
    def draw_variant():
        global variant # global variable stores currently selected icon variant

        # Draw the selected icon variant
        if variant == 'A':
            summer('deepskyblue')
        elif variant == 'B':
            winter('lightgrey')
        elif variant == 'C':
            spring('powderblue')
        elif variant == 'D': 
            autumn('navajowhite')
    
    # Begin to extract data provided by data_generator.py. 
    # Data generated is a list of instructions on how to move contact tracer
    for data in instructions:
    
        # Use global variable to store currently selected variant
        global variant

        # Extract Data from data set
        step_one = data[0] # Step one will always be the first instruction in the data set

        # What to do with a 'Start' command:
        if step_one == 'Start': # every set of instructions produced will begin with 'Start'
            variant = data[3]
            grid_placement(column = data[1], row = data[2])
            x_coord = xcor()
            y_coord = ycor()
            draw_variant()
            goto(x_coord, y_coord)
        
        # What to do with a 'Change' command:
        elif step_one == 'Change':
            x_coord = xcor() # store current x coordinate in order to return to corner of square
            y_coord = ycor() # store current y coordinate in order to return to corner of square
            variant = data[1] # changes variant selected using provided data set
            draw_variant()
            goto(x_coord, y_coord) # go back to bottom left corner of currently selected square

        # What to do with a 'North' command:
        elif step_one == 'North':
            x_coord = xcor()
            y_coord = ycor()
            how_many = data[1]
            for step in range(how_many):
                y_coord = y_coord + cell_size
                goto(x_coord, y_coord)
                draw_variant()
                goto(x_coord, y_coord)
        
        # What to do with a 'South' command:
        elif step_one == 'South':
            x_coord = xcor()
            y_coord = ycor()
            how_many = data[1]
            for step in range(how_many):
                y_coord = y_coord - cell_size
                goto(x_coord, y_coord)
                draw_variant()
                goto(x_coord, y_coord)
        
        # What to do with an 'East' command:
        elif step_one == 'East':
            x_coord = xcor()
            y_coord = ycor()
            how_many = data[1]
            for step in range(how_many):
                x_coord = x_coord + cell_size
                goto(x_coord, y_coord)
                draw_variant()
                goto(x_coord, y_coord)
        
        # What to do with a 'West' Command
        elif step_one == 'West':
            x_coord = xcor()
            y_coord = ycor()
            how_many = data[1]
            for step in range(how_many):
                x_coord = x_coord - cell_size
                goto(x_coord, y_coord)
                draw_variant()
                goto(x_coord, y_coord)
    
    # Draw the final variant in the left column of the window

    # Label the left column
    penup()
    goto(((grid_width + 1) * -cell_size) // 2, cell_size //2)
    pencolor('grey')
    write('Final Variant:',align='right', font= small_font)

    # Draw the final variant below title
    goto(((grid_width + 3) * -cell_size) // 2, (-cell_size // 1.7))
    draw_variant()  

#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data
    def data_set(new_seed = None):
        seed(new_seed)
        return raw_data(grid_width, grid_height)
else:
    print('\nNote: No data module available\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(bg_colour = 'linen',
                          line_colour = 'lightcoral',
                          draw_grid = True,
                          label_spaces = False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed()

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("House Plants through the Seasons")


# THE FOLLOWING LINES OF CODE ARE TO BUILD THE LEGEND FOR EACH ICON IN THE
# RIGHT PANEL OF THE SCREEN. TITLE WILL BE PLACED AT THE TOP AND 
# ICONS WILL BE PLACED AND LABELLED UNDERNEATH FROM A-D.

# Draw Title of Right Panel
penup()
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * 2.6))
pencolor('grey')
write('House Plants\nthrough\nthe Seasons',align = 'left', font = big_font)

# Draw Image A
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * 1.4))
summer('deepskyblue')
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * 1.1 ))
pencolor('grey')
write('A. Summer', align = 'left', font = small_font) # Label for image A

# Draw Image B
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -0.1))
winter('lightgrey')
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -0.4))
pencolor('grey')
write('B. Winter', align = 'left', font = small_font) # Labe for image B

# Draw Image C
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -1.6))
spring('powderblue')
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -1.9))
pencolor('grey')
write('C. Spring', align = 'left', font = small_font) # Label for image C

# Draw Image D
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -3.1))
autumn('navajowhite')
goto(((grid_width + 1.5) * cell_size) // 2, (cell_size * -3.4))
pencolor('grey')
write('D. Autumn', align = 'left', font = small_font)



### Call the student's function to process the data set
### ***** While developing your program you can call the
### ***** "data_set" function with a fixed seed for the
### ***** random number generator, but your final solution must
### ***** work with "data_set()" as the argument to "visualise",
### ***** i.e., for any data set that can be returned by
### ***** calling function "data_set" with no seed.
visualise(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)

#
#--------------------------------------------------------------------#
