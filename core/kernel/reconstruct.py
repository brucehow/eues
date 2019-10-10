import numpy as np
import pywt
import math
from scipy import signal

def proc_signal(sig, fs=1/60, wavename='db5'):
	sig = sig[~np.isnan(sig)]

	b,a = signal.butter(10,fs/8,'lowpass', fs=fs)
	sig = signal.filtfilt(b,a,sig)
	lvl = int(math.log(24*60*60*fs/2, 2) - 2)
	print("wavelet: {}, decomposition level: {}, fs: {}".format(wavename, lvl, fs))
	wl = pywt.Wavelet(wavename)
	coeff_all = pywt.wavedec(sig, wl, level=lvl)

	coeff_all[0] = coeff_all[0]*0
	coeff_all[-5] = coeff_all[-5]*2
	coeff_all[-4] = coeff_all[-4]*2
	coeff_all[-3] = coeff_all[-3]*2
	coeff_all[-2] = coeff_all[-2]*2
	coeff_all[-1] = coeff_all[-1]*2
	t = np.linspace(0, sig.size-1, sig.size)/fs/60/60
	recon = pywt.waverec(coeff_all, wavelet= wl)

	return recon, np.mean(sig)

