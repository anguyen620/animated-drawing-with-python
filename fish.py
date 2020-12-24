#Name: Anh Nguyen
#Email: anh.nguyen@slu.edu
#Current Date: February 2, 2018
#Course Information: CSCI1300-02
#Instructor: Judy Etchison

#Sources Consulted:

#Honor Code Statement: In keeping with the honor code policies of St. Louis university, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.

from cs1graphics import *
from time import sleep

canvas = Canvas(500,500)

#Bowl shape
circle = Circle(180)
canvas.add(circle)
circle.moveTo(250,250)
circle.setFillColor("lightBlue")
circle.setBorderColor("lightBlue")

cover = Rectangle(250,73)
canvas.add(cover)
cover.moveTo(250,80)
cover.setFillColor("white")
cover.setBorderColor("white")

#Building the fish
fish = Layer()

body = Polygon(Point(200,250),Point(232,238),Point(265,245),Point(280,238),Point(280,262),Point(265,255),Point(232,262),Point(200,250))
body.setBorderColor('orange')
body.setFillColor("orange")
fish.add(body)

eye = Circle(3)
eye.setFillColor("black")
eye.moveTo(218,247)
fish.add(eye)

fin1 = Polygon(Point(223,244),Point(243,230),Point(243,244),Point(223,244))
fin1.setFillColor("orange")
fin1.setBorderColor('orange')
fish.add(fin1)

fin2 = fin1.clone()
fin2.flip()
fin2.rotate(180)
fin2.move(0,11)
fin2.setBorderColor('orange')
fish.add(fin2)

canvas.add(fish)

#Decorations
bubble = Circle(5)
bubble.moveTo(197,240)
bubble.setFillColor("white")
bubble.setBorderColor("white")
bubble2 = Circle(5)
bubble2.moveTo(203,230)
bubble2.setFillColor("white")
bubble2.setBorderColor("white")

seaweed1 = Path(Point(5,190),Point(14,176),Point(15,175),Point(2,158),Point(1,157),Point(14,137),Point(15,138),Point(2,118),Point(1,117),Point(14,97),Point(15,96),Point(2,76),Point(1,75),Point(14,55),Point(15,54))
canvas.add(seaweed1)
seaweed1.moveTo(330,353)
seaweed1.setBorderColor("darkGreen")
seaweed1.setBorderWidth(8)

seaweed2 = seaweed1.clone()
seaweed2.move(-170,20)
canvas.add(seaweed2)

seaweed3 = seaweed1.clone()
seaweed3.move(10,-10)
canvas.add(seaweed3)

seaweed4 = seaweed2.clone()
seaweed4.move(-15,-25)
canvas.add(seaweed4)

seaweed5 = seaweed1.clone()
seaweed1.move(35,-30)
canvas.add(seaweed5)

seaweed6 = seaweed2.clone()
seaweed6.move(-25,-30)
canvas.add(seaweed6)

#Animation
sleep(.1)
canvas.add(bubble)
sleep(0.10)
bubble.move(5,-5)
sleep(.10)
bubble.move(-5,-5)
sleep(.10)
bubble.move(-5,-5)
fish.move(0,-10)
sleep(.10)
bubble.move(5,-5)
sleep(.1)
bubble.move(5,-5)
canvas.add(bubble2)
fish.move(0,10)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(-5,-5)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(5,-5)
fish.move(0,-10)
sleep(.1)
bubble.move(5,-5)
bubble2.move(5,-5)
sleep(.1)
bubble.move(5,-5)
bubble2.move(-5,-5)
fish.move(0,10)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(-5,-5)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(5,-5)
sleep(.1)
bubble.move(5,-5)
bubble2.move(5,-5)
sleep(.1)
bubble.move(5,-5)
bubble2.move(-5,-5)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(-5,-5)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(5,-5)
sleep(.1)
bubble.move(5,-5)
bubble2.move(5,-5)
sleep(.1)
bubble.move(5,-5)
bubble2.move(-5,-5)
sleep(.1)
bubble.move(-5,-5)
bubble2.move(-5,-5)
sleep(.1)
canvas.remove(bubble)
bubble2.move(5,-5)
sleep(.1)
bubble2.move(5,-5)
sleep(.1)
canvas.remove(bubble2)
