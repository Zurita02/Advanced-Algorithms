from math import sqrt
from turtle import done, rt, fd, lt
import turtle


PHI = 2 / (sqrt(5) -1)

def square(size):
    for _ in range(4):
        fd(size)
        lt(90)

   

#square()
#print(PHI)


def golden_spiral(n):
    size = 5
    for _ in range (n):
        turtle.pencolor("black")
        square(size)
        turtle.pencolor("yellow")
        turtle.circle(size,90)
        size *= PHI


def print_fibonacci(n):
    a = 1
    b = 1
    for _ in range(n):
        r = b / a 
        print(f'{a:15}{b:15}{r:20.16f}')
        a,b = b, a+b


turtle.pensize(3)
#golden_spiral(11)
#done()

print_fibonacci(40)