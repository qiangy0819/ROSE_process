import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
from collections import defaultdict
import seaborn as sns
from numpy.fft import fft, ifft, fftfreq
import scipy
from scipy import interpolate
import pandas as pd
def FWHM(data):
    half_max = (np.max(data)+ np.min(data)) / 2.0
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - data[])
    d = np.sign(half_max - np.array(data))
    #plot(data)
    #plot(d) #if you are interested
    #find the left and right most indexes
    left_idx = np.where(d > 0)[0][0]
    right_idx = np.where(d > 0)[0][-1]
    if not left_idx or not right_idx:
        return None
    return right_idx - left_idx