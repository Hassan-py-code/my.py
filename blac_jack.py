# import random
# from turtle import Screen,Turtle
# window=Screen()
# window.bgcolor("green")
# sam=Turtle()
# window.title("Octucode :in python")
# list_of_shape=("مربع","مثلت","دائرة","squar","circle","triangle")
# list_shape=["turtle","squar","triangle","arrow"]
# def draw_sguar():
#     for _ in range(4):
#         sam.pensize(10)
#         sam.color("red")
#         sam.shape("turtle")
#         sam.forward(100)
#         sam.left(90)
# def draw_triagle():
#     for _ in range(3):
#         sam.pensize(5)
#         sam.color("purple")
#         sam.shape("triangle")
#         sam.forward(200)
#         sam.left(120)

# def draw_circle():
#     for _ in range(2):
#        sam.color("yellow")
#        sam.pensize(11)
#        sam.shape('arrow')
#        sam.circle(100)

# while True:
#     user_choice=window.textinput("لحظة من قضلك","مالذي تريد رسمه مثلت مربع دائرة")
#     if user_choice in list_of_shape:
#         if user_choice=="مربع"or user_choice=="square":
#             draw_sguar()
#         elif user_choice=="مثلت"or user_choice=="triangle":
#             draw_triagle()
#         elif user_choice=="دائرة"or user_choice=="circle":
#             draw_circle()
#     elif user_choice=="خروج"or "exit":
#         False
#         window.clear()
#         sam.color('black')
#         sam.hideturtle()
#         window.bgcolor("lightCyan1")
#         sam.write("press any key to exit",align="center",font=("arial",35,"normal"))
# window.exitonclick()



import random
from turtle import Screen,Turtle
sam=Turtle()
window=Screen()
window.bgcolor('green')
list_of_shape=["squar","triangle","circle","مربع","دائرة","مثلت"]
def draw_sguar():
  for _ in range(4): 
    sam.shape('square')
    sam.color('red')
    sam.pensize(10)
    sam.forward(200)
    sam.left(90)

def draw_triangle():
  for _ in range(3):
    sam.shape("triangle")
    sam.color('cyan')
    sam.pensize(6)
    sam.forward(150)
    sam.left(120)

def draw_circle():
   for _ in range(1):
     sam.shape("circle")
     sam.color("yellow")
     sam.pensize(9)
     sam.circle(100)

while True:
  user_name=window.textinput("welcom to choice in turtle","squar,triangle,circle,مثلت مربع دائرة")
  if user_name in list_of_shape:
     if user_name=="مربع" or user_name=="squar":
       draw_sguar()
     elif user_name=="مثلت" or user_name=="triangle":
         draw_triangle()
     elif user_name=="دائرة" or user_name=="circle":
        draw_circle()
  elif user_name=="Exit" or user_name=="خروج":
      sam.clear()
      sam.hideturtle()
      window.bgcolor("black")
      break
window.exitonclick()





