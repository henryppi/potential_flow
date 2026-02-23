import numpy as np
import matplotlib.pyplot as plt

n=100

U = 2 
R = 1
gamma = -10

C = 1.15
cx = -0.12
cy = 0.08

r = np.linspace(C,3,n)
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

cs1 = ax1.contour(xx,yy,np.reshape(np.abs(w_cyl),[n,n]),levels=12,colors='k',linestyles='dashed',linewidths=1.5)
# cs1 = ax1.contour(xx,yy,np.reshape(w_cyl.real,[n,n]),levels=12,colors='k',linestyles='dashed',linewidths=1.5)

cs2 = ax1.contour(xx,yy,np.reshape(w_cyl.imag,[n,n]),levels=12,colors='k',linestyles='solid',linewidths=1.5)
# ax4[0].set_xlim([xmin,xmax])
# ax4[0].set_ylim([ymin,ymax])
ax1.axis('equal')
ax1.set_title('Joukowsky Wing')

h1,tmp = cs1.legend_elements()
# h2,tmp = cs2.legend_elements()
# ax1.legend([h1[0], h2[0]], ['$\phi$ velocity potential', '$\psi$ streamline'],loc=1)



# ax1.contourf(xx,yy,np.reshape(-w_cyl,[n,n]),20,cmap='jet')
# ax1.contour(xx,yy,np.reshape(-w_cyl,[n,n]),20,'k')
# ax1.quiver(xx.flatten(),yy.flatten(),w_cyl.real,-w_cyl.imag,color='k')
# ax1.streamplot(xx,yy,np.reshape(w_cyl.real,[n,n]),np.reshape(-w_cyl.imag,[n,n]))

ax1.plot(circle.real,circle.imag,'-k',lw=3)
# ax1.axis('equal')

plt.savefig("joukowsky_wing.png",dpi=200)
plt.show()
