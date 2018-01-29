#!/usr/bin/python

import serial

s = serial.Serial("/dev/ttyACM0")

while(True):
  l = s.readline()
  x = l.rstrip().split(",")
  if len(x)==3:#ensure x has all three rgb values
    rgb = [int(val) for val in x]
  else:
    rgb = (0,0,0)
  print rgb
