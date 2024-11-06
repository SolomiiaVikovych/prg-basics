###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

## Draw figures
side_length_square = figures.draw_square('enter length')
side_length_triangle = figures.draw_triangle('enter length')
side_length_a = figures.draw_rectangle_a('enter side a length ')
side_length_b = figures.draw_rectangle_b(' enter side b ')


for i in range(4):
      pen.forward(side_length_square)
      pen.right(90)
pen.penup()
pen.goto(-100, 100)
pen.pendown()      


for i in range(2):
      pen.forward(side_length_a)
      pen.right(90)
      pen.forward(side_length_b)
      pen.right(90)
pen.penup()
pen.goto(-300, 350)
pen.pendown()      

for i in range(3):
      pen.right(60)
      pen.forward(side_length_triangle)
      pen.right(60)
pen.penup()
pen.goto(-400, 150)
pen.pendown()    

for i in range(4):
      pen.forward(side_length_square)
      pen.right(90)
pen.penup()
pen.goto(-230, 100)
pen.pendown()      


for i in range(2):
      pen.forward(side_length_a)
      pen.right(90)
      pen.forward(side_length_b)
      pen.right(90)
pen.penup()
pen.goto(-280, 130)
pen.pendown()      

for i in range(3):
      pen.right(60)
      pen.forward(side_length_triangle)
      pen.right(60)
pen.penup()
pen.goto(-4500, 170)
pen.pendown()    
            
         
        
   




...
...

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()