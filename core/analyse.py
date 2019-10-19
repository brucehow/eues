import kernel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date
from scipy import signal
import pywt
import math

def load_data(input_file, th_begin, th_end, wavelet, sample_interval, testcase_name):
	try:
		data = pd.read_excel(input_file)
	except Exception:
		return 'fail to open {}'.format(input_file), []
	else:
		return True,data
  
def check_input(data, th_begin, th_end, sample_interval, testcase_name, thd):
	try:
		cols  = data.columns.values
		if testcase_name not in cols:
			return 'invalide test case: {}, which is not in {}'.format(testcase_name, cols), 0, 0, 0
		ts = int(sample_interval)
		fs = 1/ts
		t1 = int(float(th_begin)*60*60/ts)
		t2 = int(float(th_end)*60*60/ts)
		amp_thd = float(thd)
		if(t1 > data.shape[0] or t2 > data.shape[0]):
			return 't1: {} hours or t2: {} hours over the time duration: {} hours'.format(th_begin, th_end, data.shape[0]/fs/60/60),0,0,0,0
	except Exception:
		return 'invalid format for time start(hour): {} or time end(hour): {} or sample_interval(s): {} or thd: {}'.format(th_begin, th_end, sample_interval, thd), 0, 0, 0, 0
	else:
		return True, t1, t2, fs, amp_thd

def start_analysis(infile, th_begin, th_end, wavelet, sample_interval, testcase_name, thd):

	ret, data = load_data(infile, th_begin, th_end, wavelet, sample_interval, testcase_name)
	if(True != ret):
		return ret,[]

	ret, t1, t2, fs, amp_thd = check_input(data, th_begin, th_end, sample_interval, testcase_name, thd)
	if(True != ret):
		return ret, []

	orig_sig  = np.array(data[testcase_name])
	proc_sig, base  = kernel.proc_signal(orig_sig, fs = fs, wavename = wavelet)
	visal_f, sttis_f  = kernel.get_features(proc_sig + base, fs = fs, thd = amp_thd)
	pos = ((visal_f[0][:-1] >= t1) & (visal_f[0][:-1] <= t2))
	if([] == pos):
		return 'no EUEs found, please enlarge the time duration',[]

	kernel.plot_features(orig_sig, proc_sig, base, visal_f, testcase_name, t1, t2, fs=fs)
	results = kernel.dump_features(sttis_f, testcase_name, pos)
	return True, results
