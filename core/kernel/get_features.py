import numpy as np

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
