import numpy as np
import matplotlib.pyplot as plt

def plot_features(origin_sig, proc_sig, features, casename, fs=1/60):
    t = np.linspace(0, proc_sig.size-1, proc_sig.size)/fs/60/60
    onsets, peaks = features

    plt.figure(1)
    plt.plot(t, origin_sig, color='red', label='Original Signal')
    plt.plot(t, proc_sig, color='green', label='Reconstructed Signal')
    plt.legend()
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (degrees)')
    plt.savefig('./output{}_1.png'.format(casename), dpi=100)

    plt.figure(2)
    plt.plot(t, proc_sig, color='red', label='Reconstructed Signal')
    plt.scatter(onsets/fs/60/60, proc_sig[onsets], color='green', marker='o', label='Onset')
    plt.scatter(peaks/fs/60/60,  proc_sig[peaks], color='blue', marker='*', label='Peak')
    plt.legend()
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (degrees)')
    plt.savefig('./output/{}_2.png'.format(casename), dpi=100)