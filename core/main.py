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

	def button2_func(testcase_name):
		outdir = askdirectory()
		for file in os.listdir('./output'):
			shutil.copy('./output/' + file, outdir)

	frame12 = tk.Frame(window, bg='green', bd=1)
	frame13 = tk.Frame(window, bg='yellow', bd=1)
	tk.Label(frame12, text="Input File:", font=ft1).grid(row=0, sticky=tk.W)
	tk.Label(frame12, text="Column Analysed:", font=ft1).grid(row=1, sticky=tk.W)
	tk.Label(frame12, text="Sample-Rate Used(s):", font=ft1).grid(row=2, sticky=tk.W)

	tk.Label(frame12, text="Start Time (hours):", font=ft1).grid(row=3,sticky=tk.W)
	tk.Label(frame12, text="End Time (hours):", font=ft1).grid(row=4,sticky=tk.W)
	tk.Label(frame12, text="Wavelet Type:", font=ft1).grid(row=5,sticky=tk.W)
	tk.Label(frame12, text="EUEs Threshold (xSD):", font=ft1).grid(row=6,sticky=tk.W)
	
	tk.Button(frame12, text = "[Choose File]", font=ft1, command = selectPath).grid(row = 0, column = 2, sticky=tk.W)
	e1 = tk.Entry(frame12,textvariable = path,font=ft1)
	e2 = tk.Entry(frame12, font=ft1)
	e3 = tk.Entry(frame12, font=ft1)
	e4 = tk.Entry(frame12, font=ft1)
	e5 = tk.Entry(frame12, font=ft1)
	e6 = ttk.Combobox(frame12, font=ft1, values=['haar','db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7',\
		'db8', 'db9', 'db10', 'db11', 'db12', 'db13', 'db14', 'db15', 'db16', 'db17', 'db18', \
		'db19', 'db20', 'db21', 'db22', 'db23', 'db24', 'db25', 'db26', 'db27', 'db28', 'db29', \
		'db30', 'db31', 'db32', 'db33', 'db34', 'db35', 'db36', 'db37', 'db38','sym2', 'sym3', \
		'sym4', 'sym5', 'sym6', 'sym7', 'sym8', 'sym9', 'sym10', 'sym11', 'sym12', 'sym13', 'sym14',\
		'sym15', 'sym16', 'sym17', 'sym18', 'sym19', 'sym20','coif1', 'coif2', 'coif3', 'coif4', \
		'coif5', 'coif6', 'coif7', 'coif8', 'coif9', 'coif10', 'coif11', 'coif12', 'coif13', \
		'coif14', 'coif15', 'coif16', 'coif17','bior1.1', 'bior1.3', 'bior1.5', 'bior2.2', 'bior2.4',\
		'bior2.6', 'bior2.8', 'bior3.1', 'bior3.3', 'bior3.5', 'bior3.7', 'bior3.9', 'bior4.4', \
		'bior5.5', 'bior6.8','rbio1.1', 'rbio1.3', 'rbio1.5', 'rbio2.2', 'rbio2.4', 'rbio2.6', \
		'rbio2.8', 'rbio3.1', 'rbio3.3', 'rbio3.5', 'rbio3.7', 'rbio3.9', 'rbio4.4', 'rbio5.5', 'rbio6.8',\
		'dmey', 'gaus1', 'gaus2', 'gaus3', 'gaus4', 'gaus5', 'gaus6', 'gaus7', 'gaus8', 'mexh', 'morl',\
		'cgau1', 'cgau2', 'cgau3', 'cgau4', 'cgau5', 'cgau6', 'cgau7', 'cgau8', 'shan', 'fbsp', 'cmor'])
	e7 = tk.Entry(frame12, font=ft1)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1)
	e6.grid(row=5, column=1)
	e7.grid(row=6, column=1)
	e6.current(0)
	button1 = tk.Button(frame12, text='[Generate Results]', font=ft1, command=lambda: button1_func(e1.get(), \
			e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get())).grid(row=7, column=0, sticky=tk.W)
	
	tk.Label(frame13, font=ft1, text="Result").grid(row=1, sticky=tk.W)
	tk.Label(frame13, font=ft1, text="Number of EUEs:").grid(row=2, sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Number of Wavelets:").grid(row=3,sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Feature").grid(row=4,sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Mean").grid(row=4, column=1,sticky=tk.W)
	tk.Label(frame13, font=ft1,text="SD").grid(row=4, column=2, sticky=tk.W)
	tk.Label(frame13, font=ft1,text="SEM").grid(row=4, column=3, sticky=tk.W)

	tk.Label(frame13, font=ft1,text="Amplitude:").grid(row=5, sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Duration:").grid(row=6, sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Area:").grid(row=7, sticky=tk.W)
	tk.Label(frame13, font=ft1,text="Inter Time:").grid(row=8, sticky=tk.W)
	button2 = tk.Button(frame13, font=ft1,text='[Export Results]', command=lambda: button2_func(e2.get())).grid(row=9, column=0, sticky=tk.W)


	e1r = tk.Entry(frame13,font=ft1,textvariable = s1)
	e2r = tk.Entry(frame13,font=ft1,textvariable = s2)
	e3r = tk.Entry(frame13,font=ft1,textvariable = s3)
	e4r = tk.Entry(frame13,font=ft1,textvariable = s4)

	e5r = tk.Entry(frame13,font=ft1,textvariable = s5)
	e6r = tk.Entry(frame13,font=ft1,textvariable = s6)
	e7r = tk.Entry(frame13,font=ft1,textvariable = s7)
	e8r = tk.Entry(frame13,font=ft1,textvariable = s8)

	e9r = tk.Entry(frame13,font=ft1,textvariable = s9)
	e10r = tk.Entry(frame13,font=ft1,textvariable = s10)
	e11r = tk.Entry(frame13,font=ft1,textvariable = s11)
	e12r = tk.Entry(frame13,font=ft1,textvariable = s12)

	e13r = tk.Entry(frame13,font=ft1,textvariable = s13)
	e14r = tk.Entry(frame13,font=ft1,textvariable = s14)


	e1r.grid(row=2, column=1)
	e2r.grid(row=3, column=1)

	e3r.grid(row=5, column=1)
	e4r.grid(row=5, column=2)
	e5r.grid(row=5, column=3)

	e6r.grid(row=6, column=1)
	e7r.grid(row=6, column=2)
	e8r.grid(row=6, column=3)

	e9r.grid(row=7, column=1)
	e10r.grid(row=7, column=2)
	e11r.grid(row=7, column=3)

	e12r.grid(row=8, column=1)
	e13r.grid(row=8, column=2)
	e14r.grid(row=8, column=3)

	frame12.pack(side='top', anchor = 'n', padx=10, pady=10)
	frame13.pack(side='top', anchor = 'n', padx=10, pady=10)

	window.mainloop()

if __name__ == "__main__":
	gui()
