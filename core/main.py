import tkinter as tk
import numpy as np
import shutil
import tkinter.font as tkFont
import os
import analyse
from PIL import Image, ImageTk 
from tkinter.filedialog import askopenfilename
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
	
	def selectPath():
		path.set(askopenfilename())

	def button1_func(infile, testcase_name, sample_interval,  th_begin, th_end, wavelet, thd):
		for file in os.listdir('./output'):
			os.remove('./output/' + file)
		err, ret = analyse.start_analysis(infile, th_begin, th_end, wavelet, sample_interval, testcase_name, thd)
		if True != err:
			showerror(title="Error", message= "{}".format(err))
			
		s1.set('{:.3g}'.format(ret[0]))
		s2.set('{:.3g}'.format(ret[1]))
		s3.set('{:.3g}'.format(ret[2]))
		s4.set('{:.3g}'.format(ret[3]))
		s5.set('{:.3g}'.format(ret[4]))
		s6.set('{:.3g}'.format(ret[5]))
		s7.set('{:.3g}'.format(ret[6]))
		s8.set('{:.3g}'.format(ret[7]))
		s9.set('{:.3g}'.format(ret[8]))
		s10.set('{:.3g}'.format(ret[9]))
		s11.set('{:.3g}'.format(ret[10]))
		s12.set('{:.3g}'.format(ret[11]))
		s13.set('{:.3g}'.format(ret[12]))
		s14.set('{:.3g}'.format(ret[13]))

if __name__ == '__main__':
	main()
