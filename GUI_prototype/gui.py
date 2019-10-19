import tkinter as  tk
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

def resize( w_box, h_box, pil_image): 
	w, h = pil_image.size  
	f1 = 1.0*w_box/w 
	f2 = 1.0*h_box/h    
	factor = min([f1, f2])   
	width = int(w*factor)    
	height = int(h*factor)    
	return pil_image.resize((width, height), Image.ANTIALIAS) 

def gui():


	window = tk.Tk()
	window.title('EUES')
	W = window.winfo_screenwidth()
	H = window.winfo_screenheight()
	window.geometry('{}x{}'.format(W, H))
	path = tk.StringVar()
	s1,s2,s3,s4 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s5,s6,s7,s8 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s9,s10,s11,s12 = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
	s13,s14  = tk.StringVar(),tk.StringVar()
	def selectPath():
		path.set(askopenfilename())

	def button1_func(infile, th_begin, th_end, wavelet, sample_interval, testcase_name):
		print("input file name: {} {}\n".format(infile, wavelet))
		showerror(title="Error", message= "input file {} not exit".format(infile))

	def button2_func():
		print("button2_func test\n")
		s1.set('default')
		s2.set('default')
		s3.set('default')
		s4.set('default')
		s5.set('default')
		s6.set('default')
		s7.set('default')
		s8.set('default')
		s9.set('default')
		s10.set('default')
		s11.set('default')
		s12.set('default')
		s13.set('default')
		s14.set('default')
		pil_image11 = Image.open(r'./output/cheetah 1 calib_3.png') 
		pil_image_resized11 = resize(int(2*W/3.5) , int(H/2.5), pil_image11)
		tk_image11 = ImageTk.PhotoImage(pil_image_resized11)
		img_lable1.configure(image=tk_image11)    
		img_lable1.photo=tk_image11

		pil_image21 = Image.open(r'./output/cheetah 1 calib_3.png') 
		pil_image_resized21 = resize(int(2*W/3.5) , int(H/2.5), pil_image21)
		tk_image21 = ImageTk.PhotoImage(pil_image_resized21)
		img_lable2.configure(image=tk_image21)    
		img_lable2.photo=tk_image21

	frame = tk.Frame(window, bd=1)
	frame.pack(side='left')
	frame1 = tk.Frame(frame, bd=1, height=int(H), width=int(W/3.5))
	frame2 = tk.Frame(frame, bd=1, bg='green',height=int(H/2.5), width=int(2*W/3.5))
	frame3 = tk.Frame(frame, bd=1, bg='blue',height=int(H/2.5), width=int(2*W/3.5))

	frame11 = tk.Frame(frame1, bg='blue', bd=1, height=int(H/4), width=int(W/3.5))
	frame12 = tk.Frame(frame1, bg='green', bd=1, height=int(H/4), width=int(W/3.5))
	frame13 = tk.Frame(frame1, bg='yellow', bd=1, height=int(H/4), width=int(W/3.5))

	tk.Label(frame12, text="input file").grid(row=0, sticky=tk.W)
	tk.Label(frame12, text="time start(hour)").grid(row=1,sticky=tk.W)
	tk.Label(frame12, text="time end(hour)").grid(row=2,sticky=tk.W)
	tk.Label(frame12, text="wavelet").grid(row=3,sticky=tk.W)
	tk.Label(frame12, text="sample interval(s)").grid(row=4, sticky=tk.W)
	tk.Label(frame12, text="test case name").grid(row=5, sticky=tk.W)
	tk.Button(frame12, text = "select path", command = selectPath).grid(row = 0, column = 2)
	e1 = tk.Entry(frame12,textvariable = path)
	e2 = tk.Entry(frame12)
	e3 = tk.Entry(frame12)
	e4 = ttk.Combobox(frame12, values=['haar','db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7',\
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
	e5 = tk.Entry(frame12)
	e6 = tk.Entry(frame12)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e4.current(0)
	e5.grid(row=4, column=1)
	e6.grid(row=5, column=1)
	button1 = tk.Button(frame11, text='start', command=lambda: button1_func(e1.get(), \
			e2.get(), e3.get(), e4.get(), e5.get(), e6.get())).place(x=0, y=0)
	button2 = tk.Button(frame11, text='dump result', command=button2_func).place(x=0, y=100)


	tk.Label(frame13, text="EUEs number").grid(row=0, sticky=tk.W)
	tk.Label(frame13, text="wavelets number").grid(row=1,sticky=tk.W)
	tk.Label(frame13, text="features").grid(row=2,sticky=tk.W)
	tk.Label(frame13, text="MEAN").grid(row=2, column=1,sticky=tk.W)
	tk.Label(frame13, text="SD").grid(row=2, column=2, sticky=tk.W)
	tk.Label(frame13, text="SEM").grid(row=2, column=3, sticky=tk.W)

	tk.Label(frame13, text="amplitude").grid(row=3, sticky=tk.W)
	tk.Label(frame13, text="duration").grid(row=4, sticky=tk.W)
	tk.Label(frame13, text="area").grid(row=5, sticky=tk.W)
	tk.Label(frame13, text="inter time").grid(row=6, sticky=tk.W)
	

	e1r = tk.Entry(frame13,textvariable = s1)
	e2r = tk.Entry(frame13,textvariable = s2)
	e3r = tk.Entry(frame13,textvariable = s3)
	e4r = tk.Entry(frame13,textvariable = s4)

	e5r = tk.Entry(frame13,textvariable = s5)
	e6r = tk.Entry(frame13,textvariable = s6)
	e7r = tk.Entry(frame13,textvariable = s7)
	e8r = tk.Entry(frame13,textvariable = s8)

	e9r = tk.Entry(frame13,textvariable = s9)
	e10r = tk.Entry(frame13,textvariable = s10)
	e11r = tk.Entry(frame13,textvariable = s11)
	e12r = tk.Entry(frame13,textvariable = s12)

	e13r = tk.Entry(frame13,textvariable = s13)
	e14r = tk.Entry(frame13,textvariable = s14)


	e1r.grid(row=0, column=1)
	e2r.grid(row=1, column=1)

	e3r.grid(row=3, column=1)
	e4r.grid(row=3, column=2)
	e5r.grid(row=3, column=3)

	e6r.grid(row=4, column=1)
	e7r.grid(row=4, column=2)
	e8r.grid(row=4, column=3)

	e9r.grid(row=5, column=1)
	e10r.grid(row=5, column=2)
	e11r.grid(row=5, column=3)

	e12r.grid(row=6, column=1)
	e13r.grid(row=6, column=2)
	e14r.grid(row=6, column=3)

	pil_image1 = Image.open(r'./init.png') 
	pil_image_resized1 = resize(int(2*W/3.5) , int(H/2.5), pil_image1)
	tk_image1 = ImageTk.PhotoImage(pil_image_resized1)
	img_lable1 = tk.Label(frame2, image=tk_image1, width=int(2*W/3.5), height=int(H/2.5))
	
	pil_image2 = Image.open(r'./init.png') 
	pil_image_resized2 = resize(int(2*W/3.5) , int(H/2.5), pil_image2)
	tk_image2 = ImageTk.PhotoImage(pil_image_resized2)
	img_lable2 = tk.Label(frame3, image=tk_image2, width=int(2*W/3.5), height=int(H/2.5))

	img_lable1.pack()    
	img_lable2.pack()
	frame1.pack(side='left')
	frame2.pack(side='top')
	frame3.pack(side='bottom')
	frame11.pack(side='top', anchor = 'w', padx=50, pady=10)
	frame12.pack(side='top', anchor = 'w', padx=50, pady=50)
	frame13.pack(side='top', anchor = 'w', padx=50, pady=10)
	#pdb.set_trace()
	window.mainloop()
if __name__ == "__main__":
	gui()