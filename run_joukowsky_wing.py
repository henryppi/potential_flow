import numpy as np
import matplotlib.pyplot as plt

n = 500

U = 10 
R = 1
gamma = -8#32

C = 1.15
cx = -0.12
cy = 0.18

x = np.linspace(-5,5,n)
y = np.linspace(-5,5,n)
ang = np.linspace(0,2*np.pi,100)

xx,yy = np.meshgrid(x,y)
z = xx.flatten() + yy.flatten()*1j
mask = np.where(np.abs(z)<(1*1.07)**2)
z[mask] = np.nan

circle = C*np.exp(ang*1j) # for plotting
circle += cx + 1j*cy 
circle = circle + 1**2/circle

# w_cyl = U * (1 - C**2/(np.copy(z)**1))-1j*(gamma/(2*np.pi*np.copy(z))) # complex potential
w_cyl = U * (1 - C**2/(z**1))-1j*(gamma/(2*np.pi))/z # complex potential

z += cx + 1j * cy
z = np.copy(z) + 1**2/np.copy(z)

xx = np.reshape(z.real,[n,n])
yy = np.reshape(z.imag,[n,n])

fig1, ax1 = plt.subplots(1,1,figsize=(8,8),facecolor='w',frameon=False)
ax1.contourf(xx,yy,np.reshape(-w_cyl.real,[n,n]),20,cmap='jet')
# ax1.quiver(xx,yy,w_cyl.real,-w_cyl.imag,color='k')
# ax1.streamplot(xx,yy,np.reshape(w_cyl.real,[n,n]),np.reshape(-w_cyl.imag,[n,n]))
ax1.plot(circle.real,circle.imag,'-k',lw=3)

ax1.set_xlim([-4,4])
ax1.set_ylim([-4,4])
# ax1.axis('equal')
ax1.axis('off')


plt.savefig("./images/joukowsky_potential_contour.png",dpi=200,bbox_inches='tight')
plt.show()
