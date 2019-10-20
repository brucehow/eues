import numpy as np
import pywt
import pycwt as wavelet
import matplotlib.pyplot as plt
import pdb


def plot_features(origin_sig, proc_sig, base, features, casename, t1, t2, fs=1/60):
    """
    Plot the features of the signal given the original and processed signals
    
    :param origin_sig: The original signal
    :param proc_sig: The processed signal
    :param base: The baseline for the signal
    :param features: An array containing the signal features
    :param casename: The name of the analysed column
    :param t1: The starting timeframe
    :param t2: The ending timeframe
    :param fs: The frequency, defaults to 1/60
    :return: Plots the graph saving the results to a file
    """
    t = np.linspace(0, proc_sig.size-1, proc_sig.size)/fs/60/60
    onsets, peaks, rturns, baseline = features
    proc_sig = proc_sig + base
    plot_spectrum(origin_sig, 'cgau8', casename, t1, t2, fs=fs)
    plt.figure(2)
    plt.plot(t, origin_sig, color='black', label='original signal')
    plt.plot(t, proc_sig, color='red', label='reconstruct signal')

    S = 20
    plt.scatter(onsets/fs/60/60, proc_sig[onsets], s= S, color='green', marker='o', label='onset')
    plt.scatter(peaks/fs/60/60,  proc_sig[peaks], s= S, color='blue', marker='*', label='peak')
    plt.scatter(rturns/fs/60/60,  proc_sig[rturns], s=S, color='black', marker='s', label='return to baseline')
    plt.legend()
    plt.xlabel('Time(hours)')
    plt.xlim((t1/fs/60/60, t2/fs/60/60))
    plt.ylabel('Temperature')
    plt.savefig('./output/{}_1.png'.format(casename), dpi=300)
    plt.close('all')


def plot_spectrum(sig, wavename, casename, t1, t2, fs=1/60):
    """
    Plot the spectrogram from a given signal, timeframes and frequency
    
    :param sig: The processed signal to plot
    :param wavename: The name of the wavelet
    :param casename: The name of the analysed column
    :param t1: The starting timeframe
    :param t2: The ending timeframe
    :param fs: The frequency, defaults to 1/60
    :return: Plots the spectrogram saving the results to a file
    """
    T = np.array(range(t1,t2))
    dat = sig[T]
    dt = 1/fs
    t = T/fs/60/60
    dat_norm = dat / dat.std()  # Normalized dataset
    mother = wavelet.Morlet(6)
    s0 = 2 * dt  
    dj = 1 / 12  
    J = 7 / dj
    wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(dat_norm, dt, dj, s0, J, mother)
    power = (np.abs(wave)) ** 2
    period = 1 / freqs/60/60

    plt.figure(1, figsize=(6.4, 4.8))
    bx = plt.axes([0.1, 0.37, 0.65, 0.28])
    levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]
    bx.contourf(t, period, power, np.log2(levels), extend='both', cmap=plt.cm.prism)
    bx.set_ylabel('Period (hours)')
    bx.set_xlabel('Time (hours)')
    plt.savefig('./output/{}_2.png'.format(casename), dpi = 300)
    plt.close('all')
