import tkinter as tk
import numpy as np
import shutil
import tkinter.font as tkFont
import os
import analyse
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter.messagebox import showerror

def gui():
	window = tk.Tk()
	window.title('EUES')
	ft1 = tkFont.Font(family='Fixdsys', size=22, weight=tkFont.BOLD)
	W = window.winfo_screenwidth()/1.1
	H = window.winfo_screenheight()/1.1
	W, H = int(W), int(H)
	window.geometry('{}x{}'.format(W, H))
	path = tk.StringVar()
	s1,s2,s3,s4 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s5,s6,s7,s8 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s9,s10,s11,s12 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s13,s14  = tk.StringVar(),tk.StringVar()

if __name__ == '__main__':
	main()
