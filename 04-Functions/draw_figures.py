import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = figures.draw_square('enter length')

# Draw a square
for i in range(4):
    pen.forward(side_length)
    pen.right(90)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()