import numpy as np
import pywt
import math
from scipy import signal
import pdb


def proc_signal(sig, fs=1/60, wavename='db5'):
    """
    Process a given signal given a user specified frequency
    and mother wavelet
    
    :param sig: The signal to process
    :param fs: The frequency of the analysis, defaults to 1/60
    :param wavename: The mother wavelet, defaults to 'db5'
    :return: The reconstructed signal and the mean value
    """
    sig = sig[~np.isnan(sig)]

    b,a = signal.butter(10,fs/3,'lowpass', fs=fs)
    sig = signal.filtfilt(b,a,sig)
    lvl = int(math.log(24*60*60*fs/2, 2)-2)
    print("wavelet: {}, decomposition level: {}, fs: {}".format(wavename, lvl, fs))
    wl = pywt.Wavelet(wavename)
    coeff_all = pywt.wavedec(sig, wl, level=lvl)

    for idx, coeff in enumerate(coeff_all):
        if 0 == idx or idx >= 2 :
            coeff_all[idx] = coeff*0
    t = np.linspace(0, sig.size-1, sig.size)/fs/60/60
    recon = pywt.waverec(coeff_all, wavelet=wl)
    return recon, np.mean(sig), lvl

