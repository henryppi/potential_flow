import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend_bases import MouseButton
from matplotlib.patches import PathPatch
from matplotlib.path import Path

def Circle(rad,n):
    circ = np.zeros([n,2],float)
    circ[:,0] = rad*np.cos(np.linspace(0,2*np.pi,n))
    circ[:,1] = rad*np.sin(np.linspace(0,2*np.pi,n))
    return circ

def rotz(points,ang):
    return np.asarray((np.matrix([[np.cos(ang),-np.sin(ang)],[np.sin(ang),np.cos(ang)]])*points.transpose()).transpose())

class JoukowskyTransform:
    def __init__(self):
        self.n = 100
        self.cx = 0.0
        self.cy = 0.0
        self.rad = 1.0
        self.ang = 0.0*np.pi/180
        self.redraw()
        self.unit_circle = Circle(1.0,self.n)
        self.transformed = self.transform(np.copy(self.circle))
    
    def get_circle(self):
        return self.circle
    
    def get_unit_circle(self):
        return self.unit_circle
    
    def get_transformed(self):
        return self.transformed 

    def set_para(self,cx,cy,rad,ang):
        self.cx = cx
        self.cy = cy
        self.rad = rad
        self.ang = ang

    def redraw(self):
        self.circle = Circle(self.rad,self.n)
        self.circle[:,0] += self.cx
        self.circle[:,1] += self.cy
        self.transformed = self.transform(np.copy(self.circle))
        self.transformed = rotz(self.transformed,self.ang)

    def transform(self,points):
        z = points[:,0] + 1j*points[:,1]
        z_trans = z+1.0**2/z
        # z_trans = 1/(1-self.rad**2/(z**2))
        points[:,0] = z_trans.real
        points[:,1] = z_trans.imag
        return points
        
def distance(points,x,y):
    return np.sqrt((points[:,0]-x)**2+(points[:,1]-y)**2)

class CircleInteractor:
    showverts = True
    epsilon = 5  # max pixel distance to count as a vertex hit

    
    def __init__(self,ax):
        self.ax = ax
        canvas = self.ax.figure.canvas

        self.cx = -0.12
        self.cy = 0.08
        n = 100
        self.rad = 1.15
        self.ang = 10.0*np.pi/180
        
        self.points = np.array([[self.cx,self.cy],\
                          [self.cx+self.rad*np.cos(self.ang),self.cy+self.rad*np.sin(self.ang)]])

        self._ind = None  # the active vertex

        x= self.points[:,0]
        y = self.points[:,1]
        self.line, = self.ax.plot(x, y, marker='o', markerfacecolor='r', animated=True)

        self.JT = JoukowskyTransform()
        unit = self.JT.get_unit_circle()
        self.JT.set_para(self.cx,self.cy,self.rad,self.ang)
        self.JT.redraw()
        circ = self.JT.get_circle()
        wing = self.JT.get_transformed()

        self.unit, = self.ax.plot(unit[:,0],unit[:,1],'--k',lw=0.5,animated=True)
        self.circ, = self.ax.plot(circ[:,0],circ[:,1],'-k',lw=1.5,animated=True)
        self.wing, = self.ax.plot(wing[:,0],wing[:,1],'-b',lw=3,animated=True)
        
        self.ax.axis('equal')

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """
        # print('get_ind_under_point')
        pixel_coords = (event.x,event.y)
        inv_trans = self.ax.transData.inverted()
        data_coords = inv_trans.transform(pixel_coords)
        d = distance(self.points,data_coords[0],data_coords[1])        

        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Callback for draws."""
        # print('on_draw')
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.unit)
        self.ax.draw_artist(self.circ)
        self.ax.draw_artist(self.wing)
        self.ax.draw_artist(self.line)

    def on_button_press(self, event):
        """Callback for mouse button presses."""
        # print('on_button_press')
        if (event.inaxes is None
                or event.button != MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)
        

    def on_button_release(self, event):
        """Callback for mouse button releases."""
        # print('on_button_release')
        if (event.button != MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback for key presses."""
        # print('on_key_press')
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """Callback for mouse movements."""
        # print('on_mouse_move')
        if (self._ind is None
                or event.inaxes is None
                or event.button != MouseButton.LEFT
                or not self.showverts):
            return

        if self._ind == 0:
            #center move
            self.cx = event.xdata
            self.cy = event.ydata
            
        elif self._ind == 1:
            # rad / ang move
            self.rad = np.sqrt((self.cx-event.xdata)**2+(self.cy-event.ydata)**2)
            self.ang = np.arctan2(-(self.cy-event.ydata),-(self.cx-event.xdata))
        else:
            pass

        self.points[0,:] = [self.cx, self.cy]
        self.points[1,:] = [self.cx+self.rad*np.cos(self.ang), self.cy+self.rad*np.sin(self.ang)]
        
        self.JT.set_para(self.cx,self.cy,self.rad,self.ang)
        self.JT.redraw()
        circ = self.JT.get_circle()
        wing = self.JT.get_transformed()

        self.circ.set_data(circ[:,0],circ[:,1])
        self.wing.set_data(wing[:,0],wing[:,1])
        self.line.set_data(self.points[:,0],self.points[:,1])

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.unit)
        self.ax.draw_artist(self.circ)
        self.ax.draw_artist(self.wing)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

fig, ax = plt.subplots(figsize=(8,8),facecolor='w',frameon=False)
fig.patch.set_facecolor('none') 
ax.patch.set_facecolor('none')

interactor = CircleInteractor(ax)
ax.set_title('Joukowsky Transformation (drag points to deform)')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')
plt.savefig('./images/joukowsky_transformation_interactive.png',bbox_inches='tight',dpi=200)
plt.show()