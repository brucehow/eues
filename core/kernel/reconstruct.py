import numpy as np
import pywt
import math
from scipy import signal

def proc_signal(sig, fs = 1/60, wavename = 'db5'):
	sig = sig[~np.isnan(sig)]
	b,a = signal.butter(10,fs/8,'lowpass', fs = fs)
	sig = signal.filtfilt(b,a,sig)
	lvl = int(math.log(24*60*60*fs/2, 2) - 2)
	print("wavelet: {}, decomposition level: {}, fs: {}".format(wavename, lvl, fs))
	wl = pywt.Wavelet(wavename)
	coeff_all = pywt.wavedec(sig, wl, level=lvl)
	return (pywt.waverec(coeff_all, wavelet= wl).np.mean(sig))

