# BERTHA-v1
B.E.R.T.H.A. in action:  https://youtu.be/HXsstZKxdW8


Description:
  Version 1.0 of my personal robo-project, B.E.R.T.H.A. (Acronym doesn't represent anything yet.) She's a simple 3-wheeled surveillance     cart that streams video over WiFi (LAN). Her "brain" is a Raspberry Pi 3 running the Raspbian Pixel OS. She streams video from the         Raspberry Pi camera module to the controlling computer (running Windows OS).  

Software Used:
  VNC Server (On Raspberry Pi)
  VNC Viewer (On Windows Computer)
  Netcat 
  Mplayer
  
Hardware:
  Raspberry Pi 3 Model B
  Raspberry Pi Camera Module 
  L298N Motor Driver
  4xAA battery pack
  5 volt phone charger (2400 mAh)
  Micro USB cable (Powering Raspberry Pi)
  3-6 volt motors w/gearbox
  Small Caster Wheel 
  Homemade Frame
  
  
  
========   ListenForStream.cmd   ========

This file is ran on the Windows Computer you want to stream the video to. Execute this file before you execute BeginStream.sh. 




========   BeginStream.sh   ========

This bash file is ran on the Raspberry Pi after ListenForStream.cmd is ran. This file will have to be edited to account for your paths to mplayer and netcat.




========   Controller.py   ========

Start VNC server on the pi, connect to the pi on the Windows computer, and execute this script. Upon execution, this script will create a 100x100 window on the pi. The robot will only move when that 100x100 frame is the active window (click it to make it active).

