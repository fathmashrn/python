import numpy as np
import matplotlib.pyplot as plt

#user input

A=int(input("enter amplitude: "))
f=int(input("enter frequency: "))
phi=int(input("enter phase: "))
duration=int(input("enter duration: "))
sampling_rate=int(input("enter sampling rate: "))

#derived eq

omega=2*np.pi*f

#time range

t=np.linspace(0,duration,int(sampling_rate*duration),endpoint=False)

#SHM equation

x=A*np.sin(omega*t+phi)
v=A*omega*np.cos(omega*t+phi)
a=-A*(omega**2)*np.sin(omega*t+phi)

#plotting

plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(t,x,label="displacement x(t)",color="green")
plt.ylabel("x(t)")
plt.legend()

plt.subplot(3,1,2)
plt.plot(t,v,label="velocity v(t)",color="red")
plt.ylabel("v(t)")
plt.legend()

plt.subplot(3,1,3)
plt.plot(t,a,label="acceleration a(t)",color="blue")
plt.xlabel("time(s)")
plt.ylabel("a(t)")
plt.legend()

plt.tight_layout()
plt.show()
