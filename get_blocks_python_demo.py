import pixy 
import threading
from networktables import NetworkTables
import sys
import time
import logging
from ctypes import *
from pixy import *
import math

# Pixy2 Python SWIG get blocks example #

cond = threading.Condition()
notified = [false]

def connectionListener(connected, info):
	print(info, '; Connected=%s' % connected)
	with cond:
		notified[0] = True
		cond.notify()

NetworkTables.initialize(server='10.25.30.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
	print("Waiting for Connection")
	if not notified[0]:
		cond.wait()

print ("Pixy2 Python SWIG Get Blocks Program")

pixy.init ()
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0

while 1:
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print 'frame %3d:' % (frame)
    frame = frame + 1
    for index in range (0, count):
      print '[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height)


print



