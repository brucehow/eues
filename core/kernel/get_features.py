import numpy as np
from scipy import signal
from scipy import stats
import pdb
'''
    api: erode, dilate, get_baseline, get_onsets, get_peaks
    description: a series api to detect onsets and peaks using
    1-D morphological filter
    '''
def erode(sig, struct_len):
    ret = np.zeros_like(sig)
    for i in range(0, len(ret) - struct_len, 1):
        ret[i] = np.min(sig[i:i+struct_len])
    ret[i:] = ret[i-1]
    return ret

def dilate(sig, struct_len):
    ret = np.zeros_like(sig)
    for i in range(struct_len-1, len(ret) , 1):
        ret[i] = np.max(sig[i - struct_len + 1:i+1])
    ret[0:struct_len-2] = ret[struct_len-1]
    return ret

def get_onsetsline(sig, struct_len):
    ret1 = erode(sig, struct_len)
    ret2 = dilate(ret1, struct_len)
    return ret2

def get_onsets(baseline, mask_len):
    delta = baseline[1:] - baseline[0:-1]
    start, end, pre_start, pre_end, onsets = -1, -1, -1, -1, []
    for i in range(len(delta)):
        if -1 == start and 0 != delta[i]:
            start = i
        #print("start:{}, value{}; ".format(start, delta[i]), )
        if -1 != start and -1 == end and 0 == delta[i]:
            end = i
        #print("end:{}, value{}; ".format(end, delta[i]), )
        if -1 != start and -1 != end:
            if(end - start < mask_len):
                #pre_start = start
                end = -1
                continue
            
            if (start - pre_end < mask_len):
                #print("debug0",)
                #print(pre_end, start, end, start - pre_end, end - start, mask_len)
                start = pre_start
                onsets[-1] = start + np.argmin(baseline[start:end])
            #start, end = -1, -1
            else:
                onsets.append(start + np.argmin(baseline[start:end]))
            #print("debug1",)
            #print(pre_end, start, end, start - pre_end, end - start, mask_len)
            
            pre_start, pre_end = start,end
            start,end = -1,-1
    #pdb.set_trace()
    return np.array(onsets)

def get_peaks(sig, onsets):
    peaks, areas = [], []
    for i in range(len(onsets)-1):
        peak = onsets[i] + np.argmax(sig[onsets[i]:onsets[i+1]])
        peaks.append(peak)
        areas.append(np.sum(sig[onsets[i]:onsets[i+1]]))
    return np.array(peaks), np.array(areas)

def get_returns(sig, onsets, peaks):
    rturns = np.zeros_like(peaks)
    for i in range(len(peaks)):
        sample = np.abs(sig[peaks[i]:onsets[i+1]])
        rturns[i] = peaks[i] + np.argmin(sample)
    return rturns
def get_baseline(sig, struct_len):
    '''
        half_filter_len = int((24*60*60*fs)/16)
        baseline = sig.copy()
        #pdb.set_trace()
        for i in range(len(sig)):
        if i >= half_filter_len and i < len(sig) - half_filter_len:
        sample = sig[(i-half_filter_len):(i + 1 + half_filter_len)]
        baseline[i] = np.mean(sample)
        '''
    #b,a = signal.butter(50,fs/200,'lowpass', fs=fs)
    #baseline = signal.filtfilt(b,a,sig)
    
    return get_onsetsline(sig, struct_len)

def remove_fakeonsets(sig, onsets, thd):
    true_onsets = []
    for i in range(len(onsets)-1):
        sample = sig[onsets[i]:onsets[i+1]]
        height = np.max(sample) - np.min(sample)
        if height >= thd:
            true_onsets.append(onsets[i])
    return np.array(true_onsets)

'''
    api: get_features(sig, fs = 1/60)
    description: extract features from processed signal
    '''
def get_statistics(feature):
    mnv = np.mean(feature)
    stdv = feature.std()
    semv = stats.sem(feature)
    return mnv, stdv, semv
