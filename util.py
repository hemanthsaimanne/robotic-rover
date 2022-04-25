

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import os, time

m1_1 = 11
m1_2 = 12
m2_1 = 15 
m2_2 = 13 


def init_gpio():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(m1_1,GPIO.OUT)
	GPIO.setup(m1_2,GPIO.OUT)
	GPIO.setup(m2_1,GPIO.OUT)
	GPIO.setup(m2_2,GPIO.OUT)

	

def back():
    GPIO.output(m1_1, False)
    GPIO.output(m1_2, True)
    GPIO.output(m2_1, True)
    GPIO.output(m2_2, False)
    
def right():
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, True)
	GPIO.output(m2_2, False)

def left():
	GPIO.output(m1_1, False)
	GPIO.output(m1_2, True)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, True)
	
def forward():
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, True)
	
def stop():
	GPIO.output(m1_1, False)
	GPIO.output(m1_2, False)
	GPIO.output(m2_1, False)
	GPIO.output(m2_2, False)

def right1():
	GPIO.output(m2_1, True)

def left1():
	GPIO.output(m1_2, True)
def right2():
	GPIO.output(m1_1, True)

def left2():
	GPIO.output(m2_2, True)
	
def rr():
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, True)
	GPIO.output(m2_1, True)
	GPIO.output(m2_2, True)

def ll():
	GPIO.output(m1_1, True)
	GPIO.output(m1_2, True)
	GPIO.output(m2_1, True)
	GPIO.output(m2_2, True)


