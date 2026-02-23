import numpy as np
import matplotlib.pyplot as plt

n=100

U = 10 
R = 1
gamma = -4

C = 1.15
cx = -0.12
cy = 0.18

r = np.linspace(C,5,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)

xx = rr * np.cos(aa)
yy = rr * np.sin(aa)

z = xx.flatten() + yy.flatten()*1j

circle = C*np.exp(ang*1j) # for plotting
circle += cx + 1j*cy 
circle = circle + 1**2/circle

w_cyl = U * (1 - R**2/(np.copy(z)**2))-1j*(gamma/(2*np.pi*np.copy(z))) # complex potential

z += cx + 1j * cy
z = np.copy(z) + 1**2/np.copy(z)

xx = np.reshape(z.real,[n,n])
yy = np.reshape(z.imag,[n,n])

fig1, ax1 = plt.subplots(1,1,figsize=(6,6),facecolor='w',frameon=False)

#plot grid
for i in range(n)[::4]:
    plt.plot(xx[i,:],yy[i,:],'-k',lw=1)
for i in range(n)[::8]:    
    plt.plot(xx[:,i],yy[:,i],'--k',lw=1)

# ax1.axis('equal')
ax1.set_xlim(-4, 4)
ax1.set_ylim(-4, 4)
ax1.plot(circle.real,circle.imag,'-k',lw=3)
# ax1.set_title('Joukowsky Wing')

ax1.axis('off')

plt.savefig("./images/joukowsky_wing_grid.png",dpi=200,bbox_inches='tight')
plt.show()
