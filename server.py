import RPi.GPIO as GPIO
import sys
from flask import Flask, render_template, Response,request
import time
import threading
import util as ut
ut.init_gpio()

#from serialtest import get_dist
app = Flask(__name__)


@app.route('/f',methods=['POST','GET'])
def f():
    #GPIO.setmode(GPIO.BOARD)
    LPWM = 11
    RPWM = 13
    GPIO.setup(LPWM,GPIO.OUT)
    GPIO.setup(RPWM,GPIO.OUT)
    q=GPIO.PWM(RPWM,3600)
    p=GPIO.PWM(LPWM,3600)
    ut.forward()
    return Response(200)
    
@app.route('/r',methods=['POST','GET'])
def r():
    RPWM = 15
    GPIO.setup(RPWM,GPIO.OUT)
    LPWM = 11
    GPIO.setup(LPWM,GPIO.OUT)
    q=GPIO.PWM(LPWM,3600)
    p=GPIO.PWM(RPWM,3600)
    ut.right()
    return Response(200)
    
@app.route('/l',methods=['POST','GET'])
def l():
    RPWM = 12
    GPIO.setup(RPWM,GPIO.OUT)
    LPWM = 13
    GPIO.setup(LPWM,GPIO.OUT)
    q=GPIO.PWM(LPWM,3600)
    p=GPIO.PWM(RPWM,3600)
    ut.left()
    return Response(200)

@app.route('/rr',methods=['POST','GET'])
def rr():
    RPWM = 15
    GPIO.setup(RPWM,GPIO.OUT)
    LPWM = 11
    GPIO.setup(LPWM,GPIO.OUT)
    q=GPIO.PWM(LPWM,100)
    p=GPIO.PWM(RPWM,3600)
    ut.right()
    return Response(200)
    
@app.route('/ll',methods=['POST','GET'])
def ll():
    RPWM = 12
    GPIO.setup(RPWM,GPIO.OUT)
    LPWM = 13
    GPIO.setup(LPWM,GPIO.OUT)
    q=GPIO.PWM(LPWM,100)
    p=GPIO.PWM(RPWM,3600)
    ut.left()
    return Response(200)


@app.route('/ro',methods=['POST','GET'])
def ro():
    RPWM = 15
    GPIO.setup(RPWM,GPIO.OUT)
    p=GPIO.PWM(RPWM,3600)
    ut.right1()
    return Response(200)
    
@app.route('/lo',methods=['POST','GET'])
def lo():
    RPWM = 12
    GPIO.setup(RPWM,GPIO.OUT)
    p=GPIO.PWM(RPWM,3600)
    ut.left1()
    return Response(200)

@app.route('/or',methods=['POST','GET'])
def oor():
    RPWM = 11
    GPIO.setup(RPWM,GPIO.OUT)
    p=GPIO.PWM(RPWM,3600)
    ut.right2()
    return Response(200)
    
@app.route('/ol',methods=['POST','GET'])
def ol():
    RPWM = 13
    GPIO.setup(RPWM,GPIO.OUT)
    p=GPIO.PWM(RPWM,3600)
    ut.left2()
    return Response(200)

@app.route('/b',methods=['POST','GET'])
def b():
    #GPIO.setmode(GPIO.BOARD)
    RPWM = 12
    GPIO.setup(RPWM,GPIO.OUT)
    LPWM = 15
    GPIO.setup(LPWM,GPIO.OUT)
    q=GPIO.PWM(LPWM,3600)
    p=GPIO.PWM(RPWM,3600)
    ut.back()
    return Response(200)
            
@app.route('/s',methods=['POST','GET'])
def stop():
    print("Stop")
    ut.stop()
    return Response(200)

if __name__ == "__main__":
    app.run(host="192.168.43.1",port=5000,debug=True)
