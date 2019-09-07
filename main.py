import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt
import pdb

'''
api: load_data(input_file)
description: use pandas to load .xlsx file
'''
def load_data(input_file):
	data = pd.read_excel(input_file)
	return data
	#pdb.set_trace()
'''
    api: proc_signal(signal)
    description: wavelet decomposition signal at first, then extract interested frequency band
    finally reconstruct the signal.
    '''
def proc_signal(signal):
    signal = signal[~np.isnan(signal)]
    wl = pywt.Wavelet("db1")
    coeff_all = pywt.wavedec(signal, wl, level=5)
    #cA6, cD6,cD5, cD4, cD3, cD2, cD1= coeff_all
    coeff_all[0] = coeff_all[0]*0
    coeff_all[1] = coeff_all[1]*0
    coeff_all[2] = coeff_all[2]*0
    coeff_all[-1] = coeff_all[-1]*0
    t = np.linspace(0, signal.size-1, signal.size)/2
    #cA6 = cA6*0
    #pdb.set_trace()
    recon = pywt.waverec(coeff_all, wavelet= wl)
    plt.plot(t, signal, color = 'red', label='original signal')
    plt.plot(t, recon + np.mean(signal) , color = 'green', label = 'reconstruct signal')
    plt.legend()
    plt.xlabel('Time(hours)')
    plt.ylabel('Amplitude')
    plt.show()


def main():
	data = load_data('input_data.xlsx')
	proc_signal(np.array(data['07A-11']))


if __name__ == '__main__':
	main()
