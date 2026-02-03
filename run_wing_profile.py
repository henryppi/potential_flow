import numpy as np
import matplotlib.pyplot as plt

n = 30

alpha = 1*np.pi/8
U = 2 
R = 1
gamma = -10
a = 0*0.52
c = 1.0

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
# transform = 1/(1-R**2/(z**2))
circle = circle-0.2*1j

transform = z + c**2/z
w_wing = w_cyl*transform

wing = circle + c**2/circle


fig1, [ax0,ax1] = plt.subplots(2,1,figsize=(6,12))

# w_cyl = np.nan_to_num(w_cyl)
# levels = np.linspace(np.min(np.abs(-w_cyl)),np.max(np.abs(-w_cyl)),100)
# print(levels)
# print(np.min(np.abs(w_cyl)),np.max(np.abs(w_cyl)))
# print(w_cyl)

# ax1.plot(circ_x,circ_y,'-k',lw=3)
# ax1.plot(unit_circ_x,unit_circ_y,'--k',lw=1)
ax0.contourf(xx,yy,np.reshape(-w_cyl,[n,n]),20,cmap='jet')
ax0.quiver(xx.flatten(),yy.flatten(),w_cyl.real,-w_cyl.imag,color='k')
ax0.plot(circle.real,circle.imag,'-k',lw=3)

ax0.axis('equal')

ax1.quiver(xx.flatten(),yy.flatten(),w_wing.real,-w_wing.imag,color='k')
ax1.plot(wing.real,wing.imag,'-k',lw=3)
ax1.axis('equal')

plt.savefig("./images/magnus_effect.png",dpi=200)
plt.show()


# %% potential flow
# % transformation cylinder to plate 
# clear all; close all

# x = -2.5:0.1913:2.5;
# y = x;
# alpha =1*pi/8;  U = 2;  R = 1;
# Gamma = -10;
# a=0*0.52;

# [X,Y] = meshgrid(x,y);
# Z = X + 1i*Y;
# kreisInd = abs(Z)<(R*1.03)^2;
# Z(kreisInd) = NaN;
# kreis = 1.1*R*exp(1i*(0:0.01:2*pi))+0.2*1i-0.03;
# wZyl = U*(exp(-1i*alpha)-R^2./(Z.^2*exp(-1i*alpha)-1i*a))-1i.*(Gamma./(2.*pi.*Z));
# transform = 1./(1-R^2./(Z.^2));
# wPlatte = wZyl.*transform;

# figure()
# hold on
# quiver(X(:),Y(:),real(wZyl(:)),-imag(wZyl(:)));
# plot(kreis-0.2*1i,'r','LineWidth',4)
# axis equal
# axis off
# print('pot_flow_cylinder','-dpng','-r200')
# close(gcf)

# %% Joukowsky transform
# Z=flipud(Z);
# fz = Z(:)+R^2./Z(:);
# fx = real(fz);
# fy = imag(fz);
# platte = kreis+R^2./kreis;
# platte = platte -0.2*1i;

# figure()
# hold on
# quiver(fx,fy,real(wPlatte(:)),-imag(wPlatte(:)))
# plot(platte,'r','LineWidth',4)
# axis equal
# axis off
# print('pot_flow_plate','-dpng','-r200')
# close(gcf)