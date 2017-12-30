from tkinter import Tk, Label, Button
import os

class AWSEC2GUI:
	def __init__(self, master):
		self.master = master
		master.title("AWS EC2 GUI")

		self.label = Label(master, text="Would you like to create an EC2 instance?", font = "Courier 20 bold")
		self.label.pack()

		self.greet_button = Button(master, text="Launch T2 Micro Instance", fg='red', font = "Courier 16 bold", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Exit", fg='green', font = "Courier 18 bold", command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Launching EC2 T2 Micro instance now, this may take several minutes...")
		os.system('aws ec2 run-instances --image-id ami-55ef662f --count 1 --instance-type t2.micro --key-name mykey --security-groups default')
		os.system('aws ec2 describe-instances')

root = Tk()
my_gui = AWSEC2GUI(root)
root.mainloop()


