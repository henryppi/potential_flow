import numpy as np
import matplotlib.pyplot as plt

n = 30

alpha = 1*np.pi/8
U = 2 
R = 1
gamma = -10
a = 0*0.52

x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
ang = np.linspace(0,2*np.pi,100)

xx,yy = np.meshgrid(x,y)

z = xx.flatten() + yy.flatten()*1j

mask = np.where(np.abs(z)<(R*1.03)**2)
z[mask] = np.nan

# xx[mask] = np.nan
# yy[mask] = np.nan

circle = 1.1*R*np.exp(ang*1j)+0.2*1j-0.03

w_cyl = U * (np.exp(alpha*1j) - R**2/(z**2*np.exp(alpha*1j)-a*1j))-1j*(gamma/(2*np.pi*z))
transform = 1/(1-R**2/(z**2))

circle = circle-0.2*1j

fig1, ax1 = plt.subplots(1,1,figsize=(6,6))

# ux,uy = np.gradient(phi_pol,axis=(0,1))
# ax4[1].streamplot(rr,aa,ux,uy,density=0.5, color='b',linewidth=0.5)




# w_cyl = np.nan_to_num(w_cyl)
# levels = np.linspace(np.min(np.abs(-w_cyl)),np.max(np.abs(-w_cyl)),100)
# print(levels)
# print(np.min(np.abs(w_cyl)),np.max(np.abs(w_cyl)))
# print(w_cyl)

# ax1.plot(circ_x,circ_y,'-k',lw=3)
# ax1.plot(unit_circ_x,unit_circ_y,'--k',lw=1)
ax1.contourf(xx,yy,np.reshape(-w_cyl,[n,n]),20,cmap='jet')
ax1.quiver(xx.flatten(),yy.flatten(),w_cyl.real,-w_cyl.imag,color='k')
ax1.plot(circle.real,circle.imag,'-k',lw=3)

ax1.axis('equal')

plt.savefig("./images/magnus_effect.png",dpi=200)
plt.show()
