try:
    import RPi.GPIO as GPIO
    from tkinter import *
    import time
    import picamera
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)  #ena 1
    GPIO.setup(13,GPIO.OUT)  #ena 2
    GPIO.setup(15, GPIO.OUT) #ena 3
    GPIO.setup(16, GPIO.OUT) #ena 4

    GPIO.setup(29,GPIO.OUT)  #inp 1  (inp's are used to control motor direction)
    GPIO.setup(31,GPIO.OUT)  #inp 2  (Ex: inp 1.high with inp 2.low spins motor A in one direction)
    GPIO.setup(33, GPIO.OUT) #inp 3
    GPIO.setup(37, GPIO.OUT) #inp 4

    GPIO.output(11,  1) #ena 1 enabled
    GPIO.output(13, 1)#ena 2 enabled
    GPIO.output(15, 1)#ena 3 enabled
    GPIO.output(16, 1)#ena 4 enabled

    inp1PWM= GPIO.PWM(29, 30)#pin7  @ 30 Hz (60 changes per sec, 30 cycles per sec)
    inp2PWM= GPIO.PWM(31, 30)#pin11 @ 30 Hz (60 changes per sec, 30 cycles per sec)
    inp3PWM= GPIO.PWM(33, 30)#pin31 @ 30 Hz (60 changes per sec, 30 cycles per sec)
    inp4PWM= GPIO.PWM(37, 30)#pin33 @ 30 Hz (60 changes per sec, 30 cycles per sec)

    inp1PWM.start(0)#This is the duty cycle (how long pin is hot/100)
    inp2PWM.start(0)#Pretty much means what percent of the time there is voltage flowing per cycle
    inp3PWM.start(0)#I have these four pins instanciated at 0 b/c the for loop will
    inp4PWM.start(0)#be setting the duty cycle here


    speed = 70#Instanciate the PWM of the motors.
    wDown= False
    aDown= False
    sDown= False
    dDown= False

    '''Start the GUI & Logic Below'''

    root = Tk()

    def key(event, key):#parameter "event" is necessary b/c of the lambda I'm using. Parameter "key" contains the string info for
        global wDown                                       #which button is doing what (Released (WR, AR, SR, DR), or Pressed (WP, AP, SP, DP))
        global aDown
        global sDown
        global dDown
        print(key)

    #See what keys are pressed, and assign that value to a boolean.
        if key == "WP":
            wDown=True
        elif key == "WR":
            wDown=False

        elif key == "AP":
            aDown=True
        elif key == "AR":
            aDown=False

        elif key == "SP":
            sDown=True
        elif key == "SR":
            sDown=False

        elif key == "DP":
            dDown=True
        elif key == "DR":
            dDown=False


        if wDown==True and aDown==False and sDown==False and dDown==False:#North
             inp1PWM.ChangeDutyCycle(70)
             inp3PWM.ChangeDutyCycle(70)
            # print "North"

        elif wDown==True and aDown==False and sDown==False and dDown==True:#NorthEast
             inp1PWM.ChangeDutyCycle(100)
             inp3PWM.ChangeDutyCycle(50)
            # print "North_East"

        elif wDown==False and aDown==False and sDown==False and dDown==True:#East
             inp1PWM.ChangeDutyCycle(70)
             inp4PWM.ChangeDutyCycle(70)
            # print "East"

        elif wDown==False and aDown==False and sDown==True and dDown==True:#SouthEast
             inp2PWM.ChangeDutyCycle(100)
             inp4PWM.ChangeDutyCycle(50)
            # print "South_East"

        elif wDown==False and aDown==False and sDown==True and dDown==False:#South
             inp2PWM.ChangeDutyCycle(70)
             inp4PWM.ChangeDutyCycle(70)
            # print "South"

        elif wDown==False and aDown==True and sDown==True and dDown==False:#SouthWest
             inp2PWM.ChangeDutyCycle(50)
             inp4PWM.ChangeDutyCycle(100)
            # print "South_West"

        elif wDown==False and aDown==True and sDown==False and dDown==False:#West
             inp2PWM.ChangeDutyCycle(70)
             inp3PWM.ChangeDutyCycle(70)
            # print "West"

        elif wDown==True and aDown==True and sDown==False and dDown==False:#Kim Kardashian's child
             inp1PWM.ChangeDutyCycle(50)
             inp3PWM.ChangeDutyCycle(100)
            # print "North_West"

        else:
             inp1PWM.ChangeDutyCycle(0)
             inp2PWM.ChangeDutyCycle(0)
             inp3PWM.ChangeDutyCycle(0)
             inp4PWM.ChangeDutyCycle(0)
            # print "Stopped"



    def callback():#GOT IT!
        frame.focus_set()
        print ("The program is a runnin'.")



    frame = Frame(root, width=100, height=100)

    #keyPRESS
    frame.bind("w", lambda event: key(event, "WP"))
    frame.bind("a", lambda event: key(event, "AP"))
    frame.bind("s", lambda event: key(event, "SP"))
    frame.bind("d", lambda event: key(event, "DP"))

    #keyRELEASE
    frame.bind("<KeyRelease-w>", lambda event: key(event, "WR"))
    frame.bind("<KeyRelease-a>", lambda event: key(event, "AR"))
    frame.bind("<KeyRelease-s>", lambda event: key(event, "SR"))
    frame.bind("<KeyRelease-d>", lambda event: key(event, "DR"))

    #frame.bind("<Double-space>", SuperBoost)#super Boost
    #frame.bind("<space>",Boost)#plain Ole Boost
    frame.pack()
    callback()#This keeps me from having to click every time
    root.mainloop()

except KeyboardInterrupt:
    print("Cleaning up GPIO Pins.")
    GPIO.cleanup()
