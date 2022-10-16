import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile


fs, data = wavfile.read("./schwa_sample_sox.wav")

x = data.copy()
x = x / 32767


u = lfilter([1, -0.99], [1], x)
cepstL = 30


def local_maxium(x):
    """
    求序列的极大值
    :param x:
    :return:
    """
    d = np.diff(x)
    l_d = len(d)
    maxium = []
    loc = []
    for i in range(l_d - 1):
        if d[i] > 0 and d[i + 1] <= 0:
            maxium.append(x[i + 1])
            loc.append(i + 1)
    return maxium, loc



def Formant_Cepst(u, cepstL):
    """
    :param u:
    :param cepstL:
    :return:
    """
    # this will return the half of the samples of the speech
    wlen2 = len(u) // 2
 
    U = np.log(np.abs(np.fft.fft(u)[:wlen2]))
    Cepst = np.fft.ifft(U)
    cepst = np.zeros(wlen2, dtype=np.complex)
    cepst[:cepstL] = Cepst[:cepstL]
    cepst[-cepstL + 1:] = Cepst[-cepstL + 1:]
    spec = np.real(np.fft.fft(cepst))
    val, loc = local_maxium(spec)
    return val, loc, spec

# length = data.shape[0] / samplerate
# time = np.linspace(0., length, data.shape[0]) 
# plt.plot(time, data[:, 0])
#length = x.shape[0] / fs
#t = np.linspace(0., length, x.shape[0])
#plt.plot(t, x, label="waveform")
#plt.legend()
#plt.xlabel("Time [s]")
#plt.ylabel("Amplitude")
#plt.savefig('foo.png', bbox_inches='tight')


wlen = len(u)
wlen2 = wlen // 2
print(wlen)
print(wlen2)
# 预处理-加窗
u2 = np.multiply(u, np.hamming(wlen))

U_abs = np.log(np.abs(np.fft.fft(u2))[:wlen2])

freq = [i * fs / wlen for i in range(wlen2)]

val, loc, spec = Formant_Cepst(u, cepstL)





#plt.plot(freq, U_abs, 'k', color="green")
#plt.title('Spectrum')
#plt.savefig('spectrum.png', bbox_inches='tight')



# This is to plot the whole formants
#plt.title('Ceptrum Formants')
#for i in range(len(loc)):
#    plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
#    plt.text(freq[loc[i]], spec[loc[i]], 'Freq={}'.format(int(freq[loc[i]])))
#plt.savefig('Ceptrum Formants.png', bbox_inches='tight')





#plt.plot(freq, spec, 'k', color="blue")
plt.title('Ceptrum Formants')
for i in range(len(loc)):
    plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
    plt.text(freq[loc[i]], spec[loc[i]], 'F{}={}'.format(i+1, int(freq[loc[i]])))
plt.savefig('Ceptrum Formants.png', bbox_inches='tight')


# This is to plot the first four formants.








for i in range(len(loc)):
   print(freq[loc[i]])


#for i in range(len(loc)):
#    plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
#    plt.text(freq[loc[i]], spec[loc[i]], 'Freq={}'.format(int(freq[loc[i]])))



#plt.subplot(4, 1, 1)
#plt.plot(freq, U_abs, 'k')
#plt.title('频谱')
#plt.subplot(4, 1, 2)
#plt.plot(freq, spec, 'k')
#plt.title('倒谱法共振峰估计')
#for i in range(len(loc)):
   # plt.subplot(4, 1, 2)
  #  plt.plot([freq[loc[i]], freq[loc[i]]], [np.min(spec), spec[loc[i]]], '-.k')
 #   plt.text(freq[loc[i]], spec[loc[i]], 'Freq={}'.format(int(freq[loc[i]])))
#p = 12


















