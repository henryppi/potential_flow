import numpy as np
import matplotlib.pyplot as plt

n = 400

U = 2 
R = 1
gamma = -20

x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
ang = np.linspace(0,2*np.pi,100)

xx,yy = np.meshgrid(x,y)
z = xx.flatten() + yy.flatten()*1j
mask = np.where(np.abs(z)<(R*1.04)**2)
z[mask] = np.nan

circle = 1.1*R*np.exp(ang*1j) # for plotting

w_cyl = U * (1 - R**2/(z**2))-1j*(gamma/(2*np.pi*z)) # complex potential

fig1, ax1 = plt.subplots(1,1,figsize=(8,8),facecolor='w',frameon=False)
ax1.contourf(xx,yy,np.reshape(-w_cyl,[n,n]),20,cmap='jet')
# ax1.quiver(xx.flatten(),yy.flatten(),w_cyl.real,-w_cyl.imag,color='k')
ax1.streamplot(xx,yy,np.reshape(w_cyl.real,[n,n]),np.reshape(-w_cyl.imag,[n,n]))
ax1.plot(circle.real,circle.imag,'-k',lw=3)
ax1.axis('equal')
ax1.axis('off')

plt.savefig("./images/magnus_effect.png",dpi=200,bbox_inches='tight')
plt.show()
