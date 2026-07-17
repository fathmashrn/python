import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

#user input

f1=int(input("enter first frequency: "))
f2=int(input("enter second frequency: "))

sampling_rate=44100
duration=10
t=np.linspace(0,duration,int(sampling_rate*duration),endpoint=False)

#generate two sine waves

wave1=np.sin(2*np.pi*f1*t)
wave2=np.sin(2*np.pi*f2*t)

#generate beats
beats=0.5*(wave1+wave2)

#plotting

plt.figure(figsize=(10,5))

t_zoom=t[:int(1*sampling_rate)]
beats_zoom=beats[:int(1*sampling_rate)]
plt.plot(t_zoom,beats_zoom,color="purple")
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("beats")
plt.grid(True)
plt.show()
