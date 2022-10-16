"""
Vowel	[i]	[ɪ]	[e]	[ɛ]	[æ]	[ɑ]	[ɔ]	[o]	[ʊ]	[u]	[ʌ]
F2      2620    2220    2060    1480    1760    1180    760     760     940     920     1320
F1	280	360	600	560	800	740	480	480	380	320	760
"""

from __future__ import unicode_literals
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import numpy


fig = plt.figure()
ax = fig.gca()
ax.plot(105, 200)
ax.yaxis.tick_right()
ax.xaxis.tick_top()
secax = ax.secondary_xaxis('top')
secax.set_xlabel(r'F2')
secax_y2 = ax.secondary_yaxis('right')
secax_y2.set_ylabel(r'F1')
plt.grid()


plt.rcParams['text.usetex'] = True




plt.title(r'$F_{1}/F_{2} \ formant \ chart$')
plt.plot(2620,280, "ro", color="red")
plt.plot(2220,360, "ro", )
plt.plot(2060,600, "ro")
plt.plot(1480,560, "ro")
plt.plot(1760,600, "ro")
plt.plot(2060,600, "ro")
plt.plot(2060,600, "ro")






plt.text(2620, 280, '${[i]}$', color="black",horizontalalignment='center', verticalalignment='center', fontsize=16)


plt.savefig('typo.png', bbox_inches='tight', dpi = 600)
