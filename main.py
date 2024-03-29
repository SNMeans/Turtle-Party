
#Turtle Party Project
#Sumi Nia Means
# 09 26 2023
import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):  #forward helper function
  back(-1*len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
def spiral(len,angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75,45)
move(150)
turtle.color("blue")
spiral(100,90)
