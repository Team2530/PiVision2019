#! /usr/bin/python
import pixy
import time
from ctypes import *
from pixy import *

import math as math
import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

import threading
from networktables import NetworkTables

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.25.30.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")
NetworkTables.getTable("datatable").putNumber('test', 1);

# pixy2 Python SWIG get line features example #

print ("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")

class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

#class IntersectionLine (Structure):
#  _fields_ = [
#    ("m_index", c_uint),
#    ("m_reserved", c_uint),
#    ("m_angle", c_uint) ]

vectors = VectorArray(100)
#intersections = IntersectionLineArray(100)
frame = 0

while 1:
  line_get_all_features ()
#  i_count = line_get_intersections (100, intersections)
  v_count = line_get_vectors (100, vectors)

  if v_count > 0: #i_count > 0 or
    print 'frame %3d:' % (frame)
    frame = frame + 1
#    for index in range (0, i_count):
#      print '[INTERSECTION: INDEX=%d ANGLE=%d]' % (intersections[index].m_index, intersections[index].m_angle)
    for index in range (0, 1): #v_count
      print '[VECTOR: INDEX=%d X0=%3d Y0=%3d X1=%3d Y1=%3d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1)
      x3 = vectors[index].m_x1 - vectors[index].m_x0
      y3 = vectors[index].m_y1 - vectors[index].m_y0
      r1, t1 = cart2pol(x3, y3)
      print r1
      print math.degrees(t1)
      NetworkTables.getTable("datatable").putNumber('r1', r1);
      NetworkTables.getTable("datatable").putNumber('t1', math.degrees(t1));
    time.sleep(1)

