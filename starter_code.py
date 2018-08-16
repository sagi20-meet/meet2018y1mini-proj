# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:sagi meromi
Date:
"""
import turtle
import random
import time         #We'll need this later in the lab
print('green, blue, yellow, pink, red, purple, black, white, brown orange') 
bg_color = input("type yur chosen your backround color here ======> ")

score = 0
scorecount = turtle.clone()
scorecount.hideturtle()
gameover = turtle.clone()
gameover.penup()
gameover.goto(0,-400)
gameover.color('black')
gameover.hideturtle()
            
turtle.bgcolor(bg_color)
turtle.penup()
turtle.goto(0,300)
turtle.write("SNAKE GAME", align="center", font=('Arial', 50, "normal"))
turtle.penup()
turtle.goto(-400,-250)
turtle.pensize(5)
turtle.pendown()
turtle.goto(-400,250)
turtle.goto(400,250)
turtle.goto(400,-250)
turtle.goto(-400,-250)
turtle.penup()
turtle.goto(0,0)
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
TIME_STEP = 100
turtle.setup(SIZE_X, SIZE_Y)#Curious? It's the turtle window  
                             #size.
turtle.penup()


SQUARE_SIZE = 20
START_LENGTH = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)



###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = None

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
##    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
def down():
    global direction
    direction = DOWN
##    move_snake()
    print("you pressed the down key!")

def left():
    global direction
    direction = LEFT
##    move_snake()
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
##    move_snake()
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(775/2/SQUARE_SIZE)+1
    max_x=int(775/2/SQUARE_SIZE)-1
    min_y=-int(475/2/SQUARE_SIZE)-1
    max_y=int(475/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the
        #food turtle go to the randomly-generated
    food.goto(food_x, food_y)
    food_id = food.stamp()
    food_stamps.append(food_id)
    food_pos.append((food_x, food_y))##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]


    
    
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")

    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down")

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    global food_stamps, food_pos,score
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind])#Remove eaten food#stamp
        print(score)
        score += 1
        scorecount.clear()
        scorecount.color('black')
        scorecount.hideturtle()
        scorecount.penup()
        scorecount.goto(0,-350)
        scorecount.write(score ,align = "center", font=('Arial', 50))
        turtle.bgcolor(bg_color)
        turtle.penup()
        turtle.goto(0,300)
        turtle.write("SNAKE GAME", align="center", font=('Arial', 50, "normal"))
        turtle.penup()
        turtle.goto(-400,-250)
        turtle.pensize(5)
        turtle.pendown()
        turtle.goto(-400,250)
        turtle.goto(400,250)
        turtle.goto(400,-250)
        turtle.goto(-400,-250)
        turtle.penup()
        turtle.goto(0,0)

        if score == 5:
            snake.fillcolor("yellow")
        elif score == 10:
            snake.fillcolor("blue")
        elif score == 15:
            snake.fillcolor("red")
        elif score == 20:
            snake.fillcolor("white")
        elif score == 25:
            snake.fillcolor("purple")
        elif score == 30:
            snake.fillcolor("green")
        elif score == 35:
            snake.shape("trash.gif")
        elif score == 40:
            snake.shape("diamond.gif")
        elif score == 45:
            snake.shape("glove.gif")
        
        
        

        
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        while len(food_stamps) < 4:
            make_food()

    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
        
    if pos_list[-1] in pos_list[:-1]:
        print('you ate yourself!')
        scorecount.clear()
        gameover.write('GAME OVER', font=('Arial', 95), align="center")
        time.sleep(3)
        quit()
    
    #HINT: This if statement may be useful for Part 8

    
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()

    

    UP_EDGE = 250
    DOWN_EDGE = -250
    RIGHT_EDGE = 400
    LEFT_EDGE = -400

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("you tuched the edge GAME OVER")
        scorecount.clear()
        gameover.write('GAME OVER' , font=('Arial', 95), align="center")
        time.sleep(3)
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you tuched the edge GAME OVER")
        scorecout.clear()
        gameover.write('GAME OVER', font=('Arial', 95), align="center")
        time.sleep(3)
        quit()
    if new_y_pos >= UP_EDGE:
        print("you tuched the edge GAME OVER")
        scorecount.clear()
        gameover.write('GAME OVER', font=('Arial', 95), align="center")
        time.sleep(3)
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you tuched the edge GAME OVER")
        scorecount.clear()
        gameover.write('GAME OVER', font=('Arial', 95), align="center")
        time.sleep(3)
        quit()

    
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()
turtle.register_shape('diamond.gif')
turtle.register_shape('glove.gif')
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.hideturtle()
    food.goto(this_food_pos)
    food_id = food.stamp()
    food_stamps.append(food_id)
    
    ####WRITE YOUR CODE HERE!!

    


