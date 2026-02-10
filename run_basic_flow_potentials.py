import numpy as np
import matplotlib.pyplot as plt

U_infty = 1.0
theta = 20.0*np.pi/180
p = 1.0

n = 20
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
xx,yy = np.meshgrid(x,y)



# w = U_infty*z**p
# print(type(w))

phi = U_infty * (xx*np.cos(theta)+yy*np.sin(theta))
psi = U_infty * (yy*np.cos(theta)-xx*np.sin(theta))



# plt.quiver(z.real,z.imag,w.real,w.imag)
plt.contour(xx,yy,phi,levels=10,colors='k',linestyles='dashed')
plt.contour(xx,yy,psi,levels=10,colors='k',linestyles='solid')
plt.axis('equal')
# plt.show()
plt.close()

z = xx + yy*1j
phi_complex = U_infty*np.exp(-1j*theta)*z
psi_complex = phi_complex.imag - 1j * phi_complex.real
plt.contour(xx,yy,phi_complex,levels=10,colors='k',linestyles='dashed')
plt.contour(xx,yy,psi_complex,levels=10,colors='k',linestyles='solid')
plt.axis('equal')
# plt.show()
plt.close()


uy,ux = np.gradient(phi, axis=(0, 1))
# plt.contour(xx,yy,phi,levels=10,colors='k',linestyles='dashed')
# plt.contour(xx,yy,psi,levels=10,colors='k',linestyles='solid')
# plt.streamplot(xx, yy, ux, uy, density=0.5, color='b', linewidth=0.5)
plt.quiver(xx,yy,ux,uy,color='r')
plt.axis('equal')
# plt.show()
plt.close()

# wedge flow
p = 2
phi_wedge = z**p
psi_wedge = phi_wedge.imag - 1j * phi_wedge.real

plt.contour(xx,yy,phi_wedge,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_wedge,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.plot([0,0,3],[3,0,0],'-r',lw=5)
plt.axis('equal')
# plt.show()
plt.close()

# flow around plate
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,4*n)
xx,yy = np.meshgrid(x,y)
z = xx + yy*1j
p = 0.5
phi_wedge = z**p
psi_wedge = phi_wedge.imag - 1j * phi_wedge.real
plt.contour(xx,yy,phi_wedge,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_wedge,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.plot([0,3],[0,0],'-r',lw=5)
plt.axis('equal')
# plt.show()
plt.close()

# source 
z0 = 0 + 1j * 0
m = 1.0

x_u = np.linspace(-3,3,n)
y_u = np.linspace(0.01,3,n)
xx_u,yy_u = np.meshgrid(x_u,y_u)
z_u = xx_u + yy_u*1j

x_l = np.linspace(-3,3,n)
y_l = np.linspace(-3,-0.01,n)
xx_l,yy_l = np.meshgrid(x_l,y_l)
z_l = xx_l + yy_l*1j

phi_u_source = (m/2/np.pi) *np.log(z_u-z0)
psi_u_source = phi_u_source*1j
phi_l_source = (m/2/np.pi) *np.log(z_l-z0)
psi_l_source = phi_l_source*1j

plt.contour(xx_u,yy_u,phi_u_source,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx_u,yy_u,psi_u_source,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.contour(xx_l,yy_l,phi_l_source,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx_l,yy_l,psi_l_source,levels=12,colors='k',linestyles='solid',linewidths=1)

plt.axis('equal')
# plt.show()
plt.close()

# circulation
z0 = 0 + 1j * 0
omega = 1.0

x_u = np.linspace(-3,3,n)
y_u = np.linspace(0.01,3,n)
xx_u,yy_u = np.meshgrid(x_u,y_u)
z_u = xx_u + yy_u*1j

x_l = np.linspace(-3,3,n)
y_l = np.linspace(-3,-0.01,n)
xx_l,yy_l = np.meshgrid(x_l,y_l)
z_l = xx_l + yy_l*1j

phi_u_source = -1j*(omega/2/np.pi) *np.log(z_u-z0)
psi_u_source = phi_u_source*1j
phi_l_source = -1j*(omega/2/np.pi) *np.log(z_l-z0)
psi_l_source = phi_l_source*1j

plt.contour(xx_u,yy_u,phi_u_source,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx_u,yy_u,psi_u_source,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.contour(xx_l,yy_l,phi_l_source,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx_l,yy_l,psi_l_source,levels=12,colors='k',linestyles='solid',linewidths=1)

plt.axis('equal')
# plt.show()
plt.close()

# polar plot wedge
c=1.0
n=100
r = np.linspace(0,3,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*rr*np.cos(2*aa)
psi_pol = c*rr*np.sin(2*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
plt.contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.plot([0,0,3],[3,0,0],'-r',lw=5)
plt.axis('equal')
plt.show()
# plt.close()

# polar plot plate
c=1.0
n=100
r = np.linspace(0,3,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = c*np.sqrt(rr)*np.cos(0.5*aa)
psi_pol = c*np.sqrt(rr)*np.sin(0.5*aa)
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
plt.contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1)
plt.plot([0,3],[0,0],'-r',lw=5)
plt.axis('equal')
plt.show()
plt.close()


# polar plot source

m = 1.0
n=100
r = np.linspace(0,3,n)
ang = np.linspace(0,2*np.pi,n)
rr,aa = np.meshgrid(r,ang)
phi_pol = m/2/np.pi*np.log(rr)
psi_pol = m/2/np.pi*aa
xx = rr * np.cos(aa)
yy = rr * np.sin(aa)
plt.contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1)
# plt.plot([0,0,3],[3,0,0],'-r',lw=5)
plt.axis('equal')
plt.show()
plt.close()

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
plt.contour(xx,yy,phi_pol,levels=12,colors='k',linestyles='dashed',linewidths=1)
plt.contour(xx,yy,psi_pol,levels=12,colors='k',linestyles='solid',linewidths=1)
# plt.plot([0,0,3],[3,0,0],'-r',lw=5)
plt.axis('equal')
plt.show()
# plt.close()