from turtle import Turtle, Screen

# Set up turtle object
waller = Turtle() # Create an object
waller.color("coral") # Call a method and set a color
waller.shape("turtle")
waller.forward(100)

# Set up graphics
waller_screen = Screen()
waller_screen.exitonclick()
print(waller_screen.canvheight) # Access an attribute of an object

