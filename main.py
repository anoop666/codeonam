import turtle
import random

#######################################           Global Variables ###############################################################
#distinct_colors
colors  = ["red","green","blue","orange","purple","pink","yellow","dark green","dark red","lime","dark blue","medium violet red",
           "cyan","saddle brown","dark gray","dark orange","medium purple","magenta"]
#dark_colors
dark_colors = ["lime","red","green","blue","orange","purple","pink","yellow"]

#petal_tilt_angle
petal_angle = 90
#line_width
line_width_max = 2.7
line_width_mid = 2.1
line_width_min = 1.8
common_bg_color = 'white'
common_nbg_color = 'black'

degree360 = 360
degree180 = 180
degree30  = 30
degree40  = 40
degree45  = 45
degree60  = 60

##################################################################################################################################

if __name__ == "__main__":

    turtle.Turtle()
    turtle_screen = turtle.Screen()
    turtle_screen.bgcolor(common_nbg_color)
    turtle.speed(0)

    turtle.width(line_width_min)
    for k in range(0,int(degree360/degree30)):
      turtle.color(common_bg_color)
      for i in range(0,int(degree360/degree60)):
        turtle.fillcolor(random.choice(colors))
        turtle.begin_fill()
        turtle.circle(81,degree60,9)
        turtle.circle(81,degree60,9)
        turtle.left(degree180)
        turtle.end_fill()
      turtle.left(degree30)
    
    for k in range(0,int(degree360/degree30)):
      turtle.color(common_bg_color)
      for i in range(0,int(degree360/degree45)):
        turtle.fillcolor(random.choice(dark_colors))
        turtle.begin_fill()
        for j in range(0,int(degree360/degree40)):
          turtle.circle(30,15,3)
        turtle.left(degree180)
        turtle.end_fill()
      turtle.left(degree30)
    
    turtle.width(line_width_mid)
    turtle.color(common_nbg_color)
    for k in range(0,int(degree360/degree30)):
      for i in range(0,8):
        for j in range(0,9):
          turtle.circle(30,15,3)
        turtle.left(degree180)
      turtle.left(degree30)
    
    turtle.width(line_width_min)
    turtle.color(common_nbg_color)
    
    for k in range(0,int(360/30)):
      for i in range(0,6):
        turtle.circle(81,60,9)
        turtle.circle(81,60,9)
        turtle.left(degree180)
      turtle.left(degree30)

    turtle.width(line_width_min)
    turtle.home()
	
    #exit the turtle class on click()
    turtle.Screen().exitonclick()