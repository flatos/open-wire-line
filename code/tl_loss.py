#%%------------------------------------------------

# Compute measured transmission line losses, plot some graphs


import numpy as np
import subprocess
import time
import re
import matplotlib.pyplot as plt
import functools
import io
import pandas as pd



#%%------------------------------------------------


# Voltage measurements at near, far ends of line (insulated 14AWG)

# freq (MHz), input to TL (mVrms), output from TL (mVrms)
data = np.array([   [7.195, 116.64, 116.49],
                    [14.3104, 118.47, 118.38],
                    [21.3609, 121.80, 121.32],
                    [28.4468, 124.49, 123.65],
                    [35.5209, 126.51, 125.00],
                    [42.8723, 131.46, 128.90],
                    [49.8874, 136.62, 133.80],
                    [57.0618, 146.86, 143.90]
])
loss_db = 20 * np.log10(data[:,2] / data[:,1])
TL_LEN = 65.58       # Physical line length (ft)
loss_db_100 = 100 / TL_LEN * loss_db


# Voltage measurements at near, far ends of line (bare 18AWG)

# freq (MHz), input to TL (mVrms), output from TL (mVrms)
data_bare = np.array([[7.343, 116.77, 116.17],
                    [14.686, 118.46, 117.88],
                    [22.029, 121.31, 120.47],
                    [29.372, 123.81, 123.20],
                    [36.715, 125.35, 124.27],
                    [44.058, 128.40, 127.36],
                    [51.401, 134.74, 133.04]
])
loss_db_bare = 20 * np.log10(data_bare[:,2] / data_bare[:,1])
TL_LEN_BARE = 65.75       # Line length (ft)
loss_db_100_bare = 100 / TL_LEN_BARE * loss_db_bare



# Display dB loss (0 - 60 MHz)

# (m, b), (SSE,), *_ = np.polyfit(data[:,0], loss_db_100, deg=1, full=True)
# Plot a best-fit line for some data
def _fit_line(x, y, style, freqs = np.array([0.0, 60.0])):
    (m, b), (SSE,), *_ = np.polyfit(x, y, deg=1, full=True)
    legend, = plt.plot(freqs, m*freqs + b, style)   
    return legend

# Plot properties
plt.rc('text', usetex=False)
plt.rc('font', family='serif')

plt.figure(figsize=(8, 6))
plt.title(f'Loss (dB/100ft)', fontsize=16)
plt.xlabel('Freq (MHz)', fontsize=16)
plt.ylabel('dB', fontsize=16)
plt.tight_layout()
plt.grid()
plt.grid(which='minor')

lines = []      # For legend

# Insulated TL (green)
lines0, = plt.plot(data[:,0], loss_db_100, 'go')         
line = _fit_line(data[:,0], loss_db_100, 'g')
lines.append(line)

# Bare TL (redn)
lines0, = plt.plot(data_bare[:,0], loss_db_100_bare, 'ro')         
line = _fit_line(data_bare[:,0], loss_db_100_bare, 'r')
lines.append(line)

# Others TLs for comparison

# Open-wire line (from ARRL Antenna Book, 1955 ed.)
x,y = [[3.5,7.0,14.0,21.0,28.0,50.0], [-0.03,-0.05,-0.07,-0.08,-0.1,-0.13]]     # Freq, loss
line = _fit_line(x, y, 'b--')
lines.append(line)

# "14-076 transmitting-type tubular twin lead" (from ARRL Antenna Book, 1955 ed.)
x,y = [[3.5,7.0,14.0,21.0,28.0,50.0], [-0.14,-0.22,-0.33,-0.41,-0.48,-0.68]]
line = _fit_line(x, y, 'k--')
lines.append(line)

# DXE-400MAX coaxial cable
x,y = [[5.0,10.0,30.0,50.0], [-0.3,-0.5,-0.8,-1.1]]
line = _fit_line(x, y, 'g--')
lines.append(line)


plt.legend(lines, ['Insulated 14AWG','Bare 18AWG','Open wire (ARRL)','14-076 twin lead','DXE-400MAX'], title='')
plt.show()




#%%------------------------------------------------
