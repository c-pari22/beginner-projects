import tkinter
import eight_ball
import random 
import time
from tkinter import messagebox



root = tkinter.Tk()

def displayAnswer():	

	rand_choice = random.randint(0, 20)
	text = tkinter.Text(root)
	text.insert(tkinter.INSERT, "Searching the Depths of the Universe for the Answer......")
	text.pack()
	time.sleep(0.5)	
	if question.get() is not "":
		text.pack_forget()			
		tkinter.messagebox.showinfo("The Answer You Seek", eight_ball.responses[rand_choice])	
	question.delete(0, tkinter.END)

root.minsize(width = 1300, height = 700)
play_button = tkinter.Button(root, width = 13, height = 3, fg = "red", text = "Find the Answer", font = 108, bg = '#00ffff',  command = displayAnswer)
play_button.pack()
question = tkinter.Entry(root, width = 40, textvariable = "", bd = 5)
question.pack()
label = tkinter.Label(text = "Ask Your Question Here!")
label.pack()

root.mainloop()


