from __future__ import unicode_literals
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile
import os


#file_name =  "./schwa_sample_sox.wav"

"""
Read the Audio File
"""
def read_file(file_name):
    fs, data = wavfile.read(file_name)
    x = data.copy()
    x = x / 32767
    u = lfilter ([1, -0.99], [1], x)
    wlen2 = len(u)//2
    return u, wlen2

"""

Get the audio spec

"""
def get_spec(file_name):
    u, wlen2 = read_file(file_name)

    fft_val = np.fft . fft (u) # get the fft value the sample number is 31614, which include the REL and IMAGE part of the signal

    abs_fft = np.abs(fft_val) # get the absolute value of the fft_val, which they are: sqrt(x**2 + y**2), x is the REL, y is the IMG

    nyquist_fft = np.abs(fft_val)[: wlen2]   # this let we get the half of the sample data

    log_fft = np.log(np.abs(np.fft . fft (u) [: wlen2]))   # this will add the log function since our auditory system is unlinear and close to the log

    Cepst = np. fft . ifft(log_fft)

    cepst = np.zeros(wlen2, dtype=np.complex)    # generate wlen2's 0j

    # define the cepstL like 30
    cepstL = 30

    cepst [: cepstL] = Cepst[:cepstL]
    cepst[-cepstL + 1:] = Cepst[-cepstL + 1:]

    spec = np.real(np. fft . fft (cepst) )    # we will get the fft spectrum to us
    return spec


def local_maxium(x):
    d = np.diff(x)
    l_d = len(d)
    maxium = []
    loc = []
    for i in range(l_d - 1):
        if d[i] > 0 and d[i + 1] <= 0:
            maxium.append(x[i + 1])
            loc.append(i + 1)
    return maxium, loc


def get_formant(file_name):
    val, loc = local_maxium(get_spec(file_name))
    u, wlen2 = read_file(file_name)
    fs, data = wavfile.read(file_name)
    freq = [i * fs / len(u) for i in range(wlen2)]
    formant_list = []
    for i in range(2):
        formant_list.append(freq[loc[i]])
    return formant_list




if __name__ == "__main__":
   path_dir = "./splitaudio"
   for file_name in os.listdir(path_dir):
       if file_name[-4:] == ".wav":
        print(get_formant(path_dir + "/" + file_name))



#import mpl_toolkits.axisartist as AA
#import numpy


#fig = plt.figure()
#ax = fig.gca()
#ax.plot(105, 200)
#ax.yaxis.tick_right()
#ax.xaxis.tick_top()
#secax = ax.secondary_xaxis('top')
#secax.set_xlabel(r'F2')
#secax_y2 = ax.secondary_yaxis('right')
#secax_y2.set_ylabel(r'F1')
#plt.grid()





#plt.title(r'$F_{1}/F_{2} \ formant \ chart$')
#plt.plot(formant_list[0], formant_list[1], "ro", color="red")



#path_name = []
#path_dir = "./splitaudio"
#for file_name in os.listdir(path_dir):
#    if file_name[-4:] == ".wav":
#        path_name.append(file_name)

#print(path_name[-1][:-4])

#plt.text(formant_list[0], formant_list[1], path_name[-1][:-4], color="black",horizontalalignment='center', verticalalignment='center', fontsize=16)

#plt.savefig('formant_visulization.png', bbox_inches='tight', dpi = 600)
