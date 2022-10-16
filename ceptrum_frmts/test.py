from __future__ import unicode_literals
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile

fs, data = wavfile.read("./schwa_sample_sox.wav")
x = data.copy()
x = x / 32767

u = lfilter ([1, -0.99], [1], x)


wlen2 = len(u)//2 # according to the half signal therom

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



    
val, loc = local_maxium(spec)

#print("################## This the val #################")
#for i in val:
#    print(i)
#print("################## This the location #################")
#for i in loc:
#   print(i)


wlen = len(u)
wlen2 = wlen // 2
freq = [i * fs / wlen for i in range(wlen2)]





color_spectrum = "#1f165b"
color_envlope = "#141414"
color_text_label = "#f82912"




plt.plot(freq, log_fft, 'k', color = color_spectrum)#color="#1f165b"
#plt.title('Spectrum')
#plt.savefig('spectrum.png', bbox_inches='tight', dpi = 300)


#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "serif"
#})

plt.rcParams['text.usetex'] = True


plt.plot(freq, spec, 'k', color=color_envlope)
plt.title('$Ceptrum_{Formants}$')
plt.legend(("wavform", "envelope"),
          shadow=True, loc=(1.05, 0.38), handlelength=1.5, fontsize=16)

plt.xlabel("$Frequency$", color="C0", fontsize=20)
plt.ylabel("$dB$", color="C0", fontsize=20)



# we only extract the first Four formants

formant_list = []
for i in range(4):
    plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
    plt.text(freq[loc[i]], spec[loc[i]], '$F_{}={}$'.format(i+1, int(freq[loc[i]])), color="green",horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(28000, i+1,'$F_{}={}$'.format(i+1, int(freq[loc[i]])), color=color_text_label,horizontalalignment='center', verticalalignment='center', fontsize=12)
    formant_list.append(freq[loc[i]])






#VTL = ((1 ∗ (35000/(4 ∗ f1))) + (3 ∗ (35000/(4 ∗ f2))) + (5 ∗(35000/(4 ∗ f3))) + (7 ∗ (35000/(4 ∗ f4))))/4

VTL = ((1 * (35000/(4 * formant_list[0]))) + (3 * (35000/(4 * formant_list[1]))) + (5 * (35000/(4 * formant_list[2]))) + (7 * (35000/(4 * formant_list[3]))))/4


plt.text(28000, -4,'$VTL={}cm$'.format(round(VTL)), color=color_text_label,horizontalalignment='center', verticalalignment='center', fontsize=12)


plt.savefig('Ceptrum Formants_demo.png', bbox_inches='tight', dpi = 600)






##################### Librosa ##############################



