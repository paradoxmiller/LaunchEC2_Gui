#!/usr/bin/env python3

from tkinter import Tk, Label, Button
import os

class AWSEC2GUI:
	def __init__(self, master):
		self.master = master
		master.title("AWS EC2 GUI")

		self.label = Label(master, text="Would you like to create an EC2 instance?", font = "Courier 20 bold")
		self.label.pack()

		self.greet_button = Button(master, text="Launch T2 Micro Instance", bg="#909090",fg='red', font = "Courier 16 bold", highlightbackground='#555555',activeforeground='red',activebackground='orange', bd="5", padx="15", pady="12", relief="raised", width="28", command=self.greet)
		self.greet_button.pack()
		
		self.greet_button = Button(master, text="Launch M3 Medium Instance",bg="#909090", fg='red', font = "Courier 16 bold",highlightbackground='#555555',activeforeground='#757575',activebackground='#8e8e9e', bd="5", padx="15", pady="12", relief="raised", width="28", command=self.greetm3)
		self.greet_button.pack()
		
		self.greet_button = Button(master, text="Launch M4 Large Instance",bg="#909090", fg='red', font = "Courier 16 bold",highlightbackground='#555555',activeforeground='#757575',activebackground='#8e8e9e', bd="5", padx="15", pady="12", relief="raised", width="28", command=self.greetm4)
		self.greet_button.pack()
		
		self.greet_button = Button(master, text="Launch M5 24xlarge Instance",bg="#909090", fg='red', font = "Courier 16 bold",highlightbackground='#555555',activeforeground='#757575',activebackground='#8e8e9e',bd="5", padx="15", pady="12", relief="raised", width="28", command=self.greetm5)
		self.greet_button.pack()

		self.close_button = Button(master, text="Exit", bg="#959595", fg='green', font = "Courier 16 bold", bd="5", padx=15, pady=12,highlightbackground='#555555',activeforeground='green',activebackground='orange', width="28", command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Launching EC2 T2 Micro instance now, this may take several minutes...")
		#os.system('aws ec2 run-instances --image-id ami-55ef662f --count 1 --instance-type t2.micro --key-name mykey --security-groups default')
		os.system('aws ec2 describe-instances')
		
	def greetm3(self):
		print("Launching EC2 M3 instance now, this may take several minutes...")
		#os.system('aws ec2 run-instances --image-id ami-55ef662f --count 1 --instance-type t2.micro --key-name mykey --security-groups default')
		os.system('aws ec2 describe-instances')
	
	def greetm4(self):
		print("Launching EC2 M4 instance now, this may take several minutes...")
		#os.system('aws ec2 run-instances --image-id ami-55ef662f --count 1 --instance-type t2.micro --key-name mykey --security-groups default')
		os.system('aws ec2 describe-instances')
	
	def greetm5(self):
		print("Launching EC2 M5 instance now, this may take several minutes...")
		#os.system('aws ec2 run-instances --image-id ami-55ef662f --count 1 --instance-type t2.micro --key-name mykey --security-groups default')
		os.system('aws ec2 describe-instances')
	
	

root = Tk()
root.title("AWS EC2 GUI")
root.geometry("675x400+350+125")
my_gui = AWSEC2GUI(root)
root.mainloop()
