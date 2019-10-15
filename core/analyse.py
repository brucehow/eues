import kernel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(input_file, th_begin, th_end, wavelet, sample_interval, testcase_name):
	try:
		data = pd.read_excel(input_file)
	except Exception:
		return 'fail to open {}'.format(input_file), []
	else:
		return True,data
  
def check_input(data, th_begin, th_end, sample_interval, testcase_name, thd):
  pass

def start_analysis(infile, th_begin, th_end, wavelet, sample_interval, testcase_name, thd):
  pass
