import numpy as np
import matplotlib.pyplot as plt

U_infty = 1.0
theta = 20.0*np.pi/180
p = 1.0

n = 20
xmin = -3; xmax = 3
ymin = xmin; ymax = xmax

# =====================================================================
# uniform flow

x = np.linspace(xmin,xmax,n)
y = np.linspace(ymin,ymax,n)
xx,yy = np.meshgrid(x,y)

phi = U_infty * (xx*np.cos(theta)+yy*np.sin(theta))
psi = U_infty * (yy*np.cos(theta)-xx*np.sin(theta))

fig1, [ax11,ax12] = plt.subplots(1,2,figsize=(12,6),facecolor='w',frameon=False)

#  cartesian coordinates
cs111 = ax11.contour(xx,yy,phi,levels=10,colors='k',linestyles='dashed',linewidths=1.5)
cs112 = ax11.contour(xx,yy,psi,levels=10,colors='k',linestyles='solid',linewidths=1.5)
hx3 = ax11.quiver(0,0,U_infty *np.cos(theta),U_infty *np.sin(theta),color='b',zorder=10,scale=10)
ax11.set_xlim([xmin,xmax])
ax11.set_ylim([ymin,ymax])
ax11.set_title('uniform flow, cartesian coordinates')

h1,tmp = cs111.legend_elements()
h2,tmp = cs112.legend_elements()
ax11.legend([h1[0], h2[0],hx3], ['$\phi$ velocity potential', '$\psi$ streamline','velocity vector'])

# complex numbers
z = xx + yy*1j
phi_complex = U_infty*np.exp(-1j*theta)*z
psi_complex = phi_complex.imag - 1j * phi_complex.real
cs121 = ax12.contour(xx,yy,phi_complex,levels=10,colors='k',linestyles='dashed',linewidths=1.5)
cs122 = ax12.contour(xx,yy,psi_complex,levels=10,colors='k',linestyles='solid',linewidths=1.5)
h3 = ax12.quiver(0,0,U_infty *np.cos(theta),U_infty *np.sin(theta),color='b',zorder=10,scale=10)
ax12.set_xlim([xmin,xmax])
ax12.set_ylim([ymin,ymax])
ax12.set_title('uniform flow, complex numbers')

h1,tmp = cs121.legend_elements()
h2,tmp = cs122.legend_elements()
ax12.legend([h1[0], h2[0],h3], ['$\phi$ velocity potential', '$\psi$ streamline','velocity vector'])

fig1.savefig('./images/uniform_flow.png',bbox_inches='tight',dpi=200)

# =====================================================================
# wedge flow
c=1.0
n=100
fig2, ax2 = plt.subplots(2,2,figsize=(10,10),facecolor='w',frameon=False)

theta = 180*np.pi/180
p = np.pi/theta
r = np.linspace(0,3,n)
ang = np.linspace(0,1*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax2[0,0].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax2[0,0].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
h3=ax2[0,0].plot([-3,3],[0,0],'-r',lw=6,label='wall')

ax2[0,0].set_xlim([xmin,xmax])
ax2[0,0].set_ylim([-1,ymax])
ax2[0,0].axis('equal')
ax2[0,0].set_title('wedge angle $\Theta=180^\circ$')

h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax2[0,0].legend([h1[0], h2[0],h3[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall'],loc=1)


theta = 120*np.pi/180
p = np.pi/theta
r = np.linspace(0,3,n)
ang = np.linspace(0,theta,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax2[0,1].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax2[0,1].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
px = 3*np.cos(theta)
py = 3*np.sin(theta)
h3=ax2[0,1].plot([px,0,3],[py,0,0],'-r',lw=6,label='wall')


ax2[0,1].set_xlim([xmin,xmax])
ax2[0,1].set_ylim([-1,ymax])
ax2[0,1].axis('equal')
ax2[0,1].set_title('wedge angle $\Theta=120^\circ$')


h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax2[0,1].legend([h1[0], h2[0],h3[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall'],loc=1)

theta = 90*np.pi/180
p = np.pi/theta
r = np.linspace(0,3,n)
ang = np.linspace(0,theta,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax2[1,0].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax2[1,0].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
px = 3*np.cos(theta)
py = 3*np.sin(theta)
h3=ax2[1,0].plot([px,0,3],[py,0,0],'-r',lw=6,label='wall')

ax2[1,0].set_xlim([xmin,xmax])
ax2[1,0].set_ylim([-1,ymax])
ax2[1,0].axis('equal')
ax2[1,0].set_title('wedge angle $\Theta=90^\circ$')


h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax2[1,0].legend([h1[0], h2[0],h3[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall'],loc=1)

theta = 60*np.pi/180
p = np.pi/theta
r = np.linspace(0,3,n)
ang = np.linspace(0,theta,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax2[1,1].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax2[1,1].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
px = 3*np.cos(theta)
py = 3*np.sin(theta)
h3=ax2[1,1].plot([px,0,3],[py,0,0],'-r',lw=6,label='wall')

ax2[1,1].set_xlim([xmin,xmax])
ax2[1,1].set_ylim([-1,ymax])
ax2[1,1].axis('equal')
ax2[1,1].set_title('wedge angle $\Theta=60^\circ$')


h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax2[1,1].legend([h1[0], h2[0],h3[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall'],loc=1)
fig2.savefig('./images/wedge_flow.png',bbox_inches='tight',dpi=200)

# =====================================================================
# stagnation flow
fig3, ax3 = plt.subplots(1,2,figsize=(10,10),facecolor='w',frameon=False)

theta = 90*np.pi/180
p =2#0.5* np.pi/theta
r = np.linspace(0,3,n)
ang = np.linspace(0.5*np.pi,1.5*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax3[0].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax3[0].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
h3=ax3[0].plot([0,0],[-3,3],'-r',lw=6,label='wall')
h4=ax3[0].plot([xmin,0],[0,0],'-k',lw=4,label='stagnation streamline')
h5=ax3[0].plot([0],[0],'.k',lw=4,label='stagnation point',markersize=30)

ax3[0].set_xlim([xmin,xmax])
ax3[0].set_ylim([-1,ymax])
ax3[0].axis('equal')
ax3[0].set_title('wall $\Theta=180^\circ$')

h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax3[0].legend([h1[0], h2[0],h3[0],h4[0],h5[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall','stagnation streamline','stagnation point'],loc=2)

theta = 60*np.pi/180
p = np.pi/(theta*2)
r = np.linspace(0,3,n)
ang = np.linspace(theta,2*np.pi-theta,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr**p*np.cos(p*aa)
psi_pol = c*rr**p*np.sin(p*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax3[1].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax3[1].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
px1 = 3*np.cos(theta)
py1 = 3*np.sin(theta)
px3 = 3*np.cos(2*np.pi-theta)
py3 = 3*np.sin(2*np.pi-theta)
h3=ax3[1].plot([px1,0,px3],[py1,0,py3],'-r',lw=6,label='wall')
h4=ax3[1].plot([xmin,0],[0,0],'-k',lw=4,label='stagnation streamline')
h5=ax3[1].plot([0],[0],'.k',lw=4,label='stagnation point',markersize=30)

ax3[1].set_xlim([xmin,xmax])
ax3[1].set_ylim([-1,ymax])
ax3[1].axis('equal')
ax3[1].set_title('wedge angle $\Theta=120^\circ$')

h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax3[1].legend([h1[0], h2[0],h3[0],h4[0],h5[0]], ['$\phi$ velocity potential', '$\psi$ streamline','wall','stagnation streamline','stagnation point'],loc=1)
fig3.savefig('./images/stagnation_flow.png',bbox_inches='tight',dpi=200)

# =====================================================================
# # polar plot source
fig4, ax4 = plt.subplots(1,2,figsize=(12,6),facecolor='w',frameon=False)

m = 1.0
n=100
r = np.linspace(0,3,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = m/2/np.pi*np.log(rr)
psi_pol = m/2/np.pi*aa
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
cs1 = ax4[0].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax4[0].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
ax4[0].set_xlim([xmin,xmax])
ax4[0].set_ylim([ymin,ymax])
ax4[0].axis('equal')
ax4[0].set_title('point source / sink')

h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax4[0].legend([h1[0], h2[0]], ['$\phi$ velocity potential', '$\psi$ streamline'],loc=1)

# polar plot circulation
omega = 1.0
n=100
r = np.linspace(0,3,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = omega/2/np.pi*aa
psi_pol = -omega/2/np.pi*np.log(rr)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)

cs1 = ax4[1].contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1.5)
cs2 = ax4[1].contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1.5)
ax4[1].set_xlim([xmin,xmax])
ax4[1].set_ylim([ymin,ymax])
ax4[1].axis('equal')
ax4[1].set_title('circulation')

h1,tmp = cs1.legend_elements()
h2,tmp = cs2.legend_elements()
ax4[1].legend([h1[0], h2[0]], ['$\phi$ velocity potential', '$\psi$ streamline'],loc=1)
fig4.savefig('./images/source_circulation.png',bbox_inches='tight',dpi=200)

plt.show()