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
        

class CircleInteractor:
    showverts = True
    epsilon = 5  # max pixel distance to count as a vertex hit

    def __init__(self,ax_circ):
        self.ax = ax_circ
        canvas = self.ax.figure.canvas
        # self.pathpatch = pathpatch
        # self.pathpatch.set_animated(True)

        cx = -0.12
        cy = 0.08
        n = 100
        rad = 1.15
        ang = 20.0*np.pi/180
        
        p0 = np.array([cx,cy])
        p1 = np.array([cx+rad*np.cos(ang),cy+rad*np.sin(ang)])

        self.JT = JoukowskyTransform()
        unit = J.get_unit_circle()
        self.J.set_para(cx,cy,rad,ang)
        self.J.redraw()
        circ = J.get_circle()
        wing = J.get_transformed()

        self.unit = ax.plot(unit[:,0],unit[:,1],)

        self.ax_unit, = ax.plot(unit[:,0],unit[:,1],'--k',lw=0.5,animated=True)
        self.ax_circ, = ax.plot(circ[:,0],circ[:,1],'-k',lw=1.5,animated=True)
        self.ax_wing, = ax.plot(wing[:,0],wing[:,1],'-b',lw=3,animated=True)
        
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
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # to display coords
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Callback for draws."""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)

    def on_button_press(self, event):
        """Callback for mouse button presses."""
        if (event.inaxes is None
                or event.button != MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Callback for mouse button releases."""
        if (event.button != MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback for key presses."""
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
        if (self._ind is None
                or event.inaxes is None
                or event.button != MouseButton.LEFT
                or not self.showverts):
            return

        vertices = self.pathpatch.get_path().vertices

        vertices[self._ind] = event.xdata, event.ydata
        self.line.set_data(zip(*vertices))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)



fig, ax = plt.subplots()

cx = -0.12
cy = 0.08
n = 100
rad = 1.15
ang = 20.0*np.pi/180

J = JoukowskyTransform()
unit = J.get_unit_circle()
J.set_para(cx,cy,rad,ang)
J.redraw()
circ = J.get_circle()
wing = J.get_transformed()

ax_unit = ax.plot(unit[:,0],unit[:,1],'--k',lw=0.5)
ax_circ = ax.plot(circ[:,0],circ[:,1],'-k',lw=1.5)
ax_wing = ax.plot(wing[:,0],wing[:,1],'-b',lw=3)
ax.axis('equal')
plt.show()




# pathdata = [
#     (Path.MOVETO, (1.58, -2.57)),
#     (Path.CURVE4, (0.35, -1.1)),
#     (Path.CURVE4, (-1.75, 2.0)),
#     (Path.CURVE4, (0.375, 2.0)),
#     (Path.LINETO, (0.85, 1.15)),
#     (Path.CURVE4, (2.2, 3.2)),
#     (Path.CURVE4, (3, 0.05)),
#     (Path.CURVE4, (2.0, -0.5)),
#     (Path.CLOSEPOLY, (1.58, -2.57)),
# ]

# codes, verts = zip(*pathdata)
# path = Path(verts, codes)
# patch = PathPatch(
#     path, facecolor='green', edgecolor='yellow', alpha=0.5)
# ax.add_patch(patch)


# class PathInteractor:
#     """
#     A path editor.

#     Press 't' to toggle vertex markers on and off.  When vertex markers are on,
#     they can be dragged with the mouse.
#     """

#     showverts = True
#     epsilon = 5  # max pixel distance to count as a vertex hit

#     def __init__(self, pathpatch):

#         self.ax = pathpatch.axes
#         canvas = self.ax.figure.canvas
#         self.pathpatch = pathpatch
#         self.pathpatch.set_animated(True)

#         x, y = zip(*self.pathpatch.get_path().vertices)

#         self.line, = ax.plot(
#             x, y, marker='o', markerfacecolor='r', animated=True)

#         self._ind = None  # the active vertex

#         canvas.mpl_connect('draw_event', self.on_draw)
#         canvas.mpl_connect('button_press_event', self.on_button_press)
#         canvas.mpl_connect('key_press_event', self.on_key_press)
#         canvas.mpl_connect('button_release_event', self.on_button_release)
#         canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
#         self.canvas = canvas

#     def get_ind_under_point(self, event):
#         """
#         Return the index of the point closest to the event position or *None*
#         if no point is within ``self.epsilon`` to the event position.
#         """
#         xy = self.pathpatch.get_path().vertices
#         xyt = self.pathpatch.get_transform().transform(xy)  # to display coords
#         xt, yt = xyt[:, 0], xyt[:, 1]
#         d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
#         ind = d.argmin()
#         return ind if d[ind] < self.epsilon else None

#     def on_draw(self, event):
#         """Callback for draws."""
#         self.background = self.canvas.copy_from_bbox(self.ax.bbox)
#         self.ax.draw_artist(self.pathpatch)
#         self.ax.draw_artist(self.line)

#     def on_button_press(self, event):
#         """Callback for mouse button presses."""
#         if (event.inaxes is None
#                 or event.button != MouseButton.LEFT
#                 or not self.showverts):
#             return
#         self._ind = self.get_ind_under_point(event)

#     def on_button_release(self, event):
#         """Callback for mouse button releases."""
#         if (event.button != MouseButton.LEFT
#                 or not self.showverts):
#             return
#         self._ind = None

#     def on_key_press(self, event):
#         """Callback for key presses."""
#         if not event.inaxes:
#             return
#         if event.key == 't':
#             self.showverts = not self.showverts
#             self.line.set_visible(self.showverts)
#             if not self.showverts:
#                 self._ind = None
#         self.canvas.draw()

#     def on_mouse_move(self, event):
#         """Callback for mouse movements."""
#         if (self._ind is None
#                 or event.inaxes is None
#                 or event.button != MouseButton.LEFT
#                 or not self.showverts):
#             return

#         vertices = self.pathpatch.get_path().vertices

#         vertices[self._ind] = event.xdata, event.ydata
#         self.line.set_data(zip(*vertices))

#         self.canvas.restore_region(self.background)
#         self.ax.draw_artist(self.pathpatch)
#         self.ax.draw_artist(self.line)
#         self.canvas.blit(self.ax.bbox)


# interactor = PathInteractor(patch)
# ax.set_title('drag vertices to update path')
# ax.set_xlim(-3, 4)
# ax.set_ylim(-3, 4)

# plt.show()