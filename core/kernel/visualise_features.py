import numpy as np
import pdb
import matplotlib.pyplot as plt
import pywt as wavelet

def plot_features(origin_sig, proc_sig, base, features, casename, fs=1/60):
    t = np.linspace(0, proc_sig.size-1, proc_sig.size)/fs/60/60
    onsets, peaks, rturns, baseline = features
    proc_sig = proc_sig + base

    plt.figure(1)
    plt.plot(t, origin_sig, color='red', label='Original Signal')
    plt.plot(t, proc_sig, color='green', label='Reconstructed Signal')
    plt.legend()
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (degrees)')
    plt.savefig('./output{}_1.png'.format(casename), dpi=100)

    plt.figure(2)
    plt.plot(t, proc_sig, color='red', label='Reconstructed Signal')
    S = 100
    plt.scatter(onsets/fs/60/60, proc_sig[onsets], s=S, color='green', marker='o', label='Onset')
    plt.scatter(peaks/fs/60/60,  proc_sig[peaks], s=S, color='blue', marker='*', label='Peak')
    plt.scatter(rturns/fs/60/60,  proc_sig[rturns], s=S, color='black', marker='s', label='Return to Baseline')
    plt.legend()
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (degrees)')
    plt.savefig('./output/{}_2.png'.format(casename), dpi=100)

    plt.figure(3)
    plt.plot(t, proc_sig, color='red', label='Reconstructed Signal')
    plt.scatter(onsets/fs/60/60, proc_sig[onsets], color='green', marker='o', label='Onset')
    plt.scatter(peaks/fs/60/60,  proc_sig[peaks], color='blue', marker='*', label='Peak')
    plt.legend()
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (degrees)')
    plt.xlim((t[1000], t[1000+2*24*60]))
    plt.savefig('./output/{}_3.png'.format(casename), dpi=100)
    plt.close('all')
	
def plot_spectrum(sig, wavename, casename, fs=1/60):
	dat = sig
	dt = 1/fs
	t = np.linspace(0, sig.size-1, sig.size)/fs/60/60

	dat_norm = dat / dat.std()  # Normalized dataset
	mother = wavelet.Morlet(6)
	s0 = 2 * dt  
	dj = 1 / 12  
	J = 7 / dj
	wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(dat_norm, dt, dj, s0, J, mother)
	power = (np.abs(wave)) ** 2
	period = 1 / freqs/60/60
	figprops = dict(figsize=(11, 8), dpi=72)
	fig = plt.figure(**figprops)
	ax = plt.axes([0.1, 0.75, 0.65, 0.2])
	plt.plot(t, sig)
	bx = plt.axes([0.1, 0.37, 0.65, 0.28], sharex=ax)
	levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]
	bx.contourf(t, period, power, np.log2(levels),
			extend='both', cmap=plt.cm.prism)
	bx.set_ylabel('Period (hours)')
	bx.set_xlabel('Time (hours)')
	plt.savefig('./output/{}_4.png'.format(casename), dpi = 100)
	plt.close('all')
