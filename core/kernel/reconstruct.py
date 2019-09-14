import numpy as np
import pywt
import math
from scipy import signal

def proc_signal(sig, fs = 1/60, wavename = 'db5'):
	sig = sig[~np.isnan(sig)]

	b,a = signal.butter(10,fs/8,'lowpass', fs=fs)
	sig = signal.filtfilt(b,a,sig)
	lvl = int(math.log(24*60*60*fs/2, 2) - 2)
	print("wavelet: {}, decomposition level: {}, fs: {}".format(wavename, lvl, fs))
	wl = pywt.Wavelet(wavename)
	coeff_all = pywt.wavedec(sig, wl, level=lvl)
	#pdb.set_trace()
	#cA6, cD6,cD5, cD4, cD3, cD2, cD1= coeff_all
	coeff_all[0] = coeff_all[0]*0
	coeff_all[-5] = coeff_all[-5]*0
	coeff_all[-4] = coeff_all[-4]*0
	coeff_all[-3] = coeff_all[-3]*0
	coeff_all[-2] = coeff_all[-2]*0
	coeff_all[-1] = coeff_all[-1]*0
	t = np.linspace(0, sig.size-1, sig.size)/fs/60/60
	#cA6 = cA6*0
	#pdb.set_trace()
	recon = pywt.waverec(coeff_all, wavelet= wl)

	#plt.show()
	return recon, np.mean(sig)

