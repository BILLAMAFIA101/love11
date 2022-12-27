#  TOOLS CREATED BY SUHAIB

import os

import sys

import marshal

import time

import requests

import platform

import base64

ua = []

cp = []

ok = []

loop = +1

#### LOGO ####

logo2 = """"

██░░░██░░░░▄███▄░░██░░░██░████░░░██░░██

██░░░██░░░██▀░▀██░██▄░▄██░██▄░░░░██░░██

██░░░██░░░██▄░▄██░░██▄██░░██▀░░░░██░░██

██░░░████░░▀███▀░░░░███░░░████░░░▀████▀"""

#### LOGO ####

logo = """"

┏━━┓┏━━┳┓╋╋┏┓╋╋┏━━━┓

┃┏┓┃┗┫┣┫┃╋╋┃┃╋╋┃┏━┓┃

┃┗┛┗┓┃┃┃┃╋╋┃┃╋╋┃┃╋┃┃

┃┏━┓┃┃┃┃┃╋┏┫┃╋┏┫┗━┛┃

┃┗━┛┣┫┣┫┗━┛┃┗━┛┃┏━┓┃

┗━━━┻━━┻━━━┻━━━┻┛╋┗"""

#----  MAIN  ----#

def menu():

	os.system("clear")	print(logo)

	print(" ")

	print(" [1] BILLA YOUTUBE CHANNEL LINK ")

	print(" [2] BILLA LOVE ")

	print(" [0] EXIT TOOL ")

	love = input(" CHOOSE : ")

	if love in ["1","01"]:

		    sohaib()

	elif love in ["2","02"]:

             mylove()

	elif love in ["0","00"]:

		    exit()

def sohaib():

	print(logo)

	print(57*'-')

	print (" ")

	os.system("xdg-open https://youtube.com/channel/UC5U6VqYYW4-RS3mc_GYmY1A")

  

  

def mylove():

	                os.system("clear")

	                print (logo2)

	                print(57*'-')

	                print("I LOVE YOU VERY MUCH")

main()

menu()
