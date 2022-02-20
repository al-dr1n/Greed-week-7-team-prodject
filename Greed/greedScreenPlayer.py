import turtle

main_window = turtle.Screen()
main_window.title("Greed")
main_window.bgcolor("black")
main_window.setup(width = 800, height = 600)

player = turtle.Turtle()
player.color("white")
hashtag = "./public/images/hashtag.gif";
main_window.addshape(hashtag)
player.shape(hashtag)
player.penup()
player.speed(0)
player.setposition(0, -250)

playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 380:
        x = 380
    player.setx(x)

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")


main_window.mainloop()
