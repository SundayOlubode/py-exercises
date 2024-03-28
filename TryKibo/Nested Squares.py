# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 04:20:44 2021

@author: user
"""

import turtle
pen = turtle.Turtle()

pen.color("blue")

def draw_square(n):
  pen.penup()
  pen.goto( - n * 10, n * 10)
  pen.pendown()
  for i in range(0,4):
    pen.fd(n * 20)
    pen.rt(90)
  

for i in range(1,20):
  draw_square(i)