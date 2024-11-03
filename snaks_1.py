
import turtle
import time
import random

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0) #Turns off the screen updates


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")  
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments= []



# Functions
def go_up():
    head.direction == "up"
    
def go_down():
    head.direction == "down"
    
def go_left():
    head.direction == "left"
    
def go_right():
    head.direction == "right"
    
  
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
        
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
        

while True:
    wn.update()
    #  check for a collision with the food
    if head.distance(food)<20:
        # move the food to a random spot 
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # Add a segment 
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


    # move the end segments  first in reverse order
    for index in range(len(segments) -1 , 0 , -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # move segments 0 to where the head is 
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)




    move()
    
    time.sleep(delay)

wn.mainloop()
