from math import pi,sin,cos
from turtle import *
def triangle(n,k,c,x,y,draw=True):
    points = [
        [k*cos(n/5+c)+x, k*sin(n/5+c)+y],
        [k*cos(2*pi/3+n/5+c)+x,k*sin(2*pi/3+n/5+c)+y],
        [k*cos(4*pi/3+n/5+c)+x,k*sin(4*pi/3+n/5+c)+y]
    ]
    if draw:
        penup()
        goto(*points[0])
        pendown()
        for a,b in points[1:] + [points[0]]:
            goto(a,b)
    return points

def midpoint(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((x1+x2)/2, (y1+y2)/2)

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def degree(rad):
    return rad*180/pi