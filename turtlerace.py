import turtle
import random


t = turtle.Turtle()


t.up()
t.goto(-100, 100)
t.down()
t.speed(0)


#Racetrack

for i in range(15):
    t.write(i)
    t.rt(90)
    t.fd(200)
    t.lt(180)
    t.fd(200)
    t.rt(90)
    t.fd(20)


#Player1

Red = turtle.Turtle()

Red.shape("turtle")
Red.color("red")
Red.up()
Red.goto(-120, 70)
Red.down()
#Player2
Blue = turtle.Turtle()

Blue.shape("turtle")
Blue.color("blue")
Blue.up()
Blue.goto(-120, 40)
Blue.down()
#Player3
Green = turtle.Turtle()

Green.shape("turtle")
Green.color("green")
Green.up()
Green.goto(-120, 10)
Green.down()
# Move
x_Blue = 0
x_Green = 0
x_Red =  0
Winner = input("Which turtle will win?")
text = turtle.Turtle()
text.up()
text.goto(120, 120)
text.goto(-120, 120)
text.write("You think the winner will be this turtle"+ Winner)
text.down()



while True:

    if x_turkiye > 305:
        break
    ilk_asama = random.randint(1, 5)
    x_turkiye = x_turkiye + ilk_asama
    turkiye.forward(ilk_asama)

    ikinci_asama = random.randint(1,5)
    x_yunanistan =  x_yunanistan + ikinci_asama
    yunanistan.forward(ikinci_asama)

    ucuncu_asama = random.randint(1, 5)
    x_brezilya = x_brezilya + ucuncu_asama
    brezilya.forward(ucuncu_asama)















turtle.done()


