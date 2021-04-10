from turtle import Turtle , Screen
import random

# def moveForward():
#     t.forward(10)
# def moveBackward():
#     t.backward(10)
#
# def turnRight():
#     current_heading = t.heading()
#     t.setheading(current_heading - 10)


# def turnLeft():
#     current_heading = t.heading()
#     t.setheading(current_heading + 10)
#
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
# t = Turtle()
#
#
# s = Screen()
# s.listen()
# s.onkey(key= "w" , fun=moveForward)
# s.onkey(key = "s" , fun = moveBackward)
# s.onkey(key = "a" , fun = turnLeft)
# s.onkey(key = "d" , fun = turnRight)
# s.onkey(key = "c" , fun = clear)
# s.exitonclick()

s = Screen()
s.setup(width = 500 , height = 500)
user_bet = s.textinput(title = "Make your Bet" , prompt= "Which turtle will win the race ? Enter the color : ")
print(user_bet)

colors = ["red" , "orange" , "green", "yellow" , "blue" , "purple"]
y_pos = [-100, -70 , -40 , -10 , 30 , 70 ]
all_turtle = []

for i in range(len(colors)):
    t = Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(x = -240 , y= y_pos[i])
    t.speed("fast")
    all_turtle.append(t)

if user_bet :
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the game  The {winning_color} turtle is the winner")
            else:
                print(f"You've lost the game  The {winning_color} turtle is the winner")



        rand_dist = (random.randint(0 , 10))
        turtle.forward(rand_dist)




s.exitonclick()