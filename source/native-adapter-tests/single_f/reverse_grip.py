"""Bake a reverse grip into converted FK records without touching body curves.

Read immutable input on every build. Never apply this to a live/previously
modified record. The fitted grip has constant rotation, represented either by
constant channels or one-key curves; headers, counts and allocation stay exact.
"""
import math,struct
from scipy.spatial.transform import Rotation

def reverse_native_grip(data):
 raw=bytearray(data)
 u32=lambda at:struct.unpack_from('<I',raw,at)[0]
 assert u32(16)==293
 destinations={};values={};rotation_keys=set();other_keys=set()
 for i in range(u32(52)):
  at=u32(56)+i*8;bone,kind,value=struct.unpack_from('<HHf',raw,at)
  if bone==280 and kind in (4,5,6):
   assert kind not in values
   values[kind]=value;destinations[kind]=[at+4]
 for count_at,channels_at in [(24,28),(32,36)]:
  for i in range(u32(count_at)):
   at=u32(channels_at)+i*6;bone,kind,n,first=struct.unpack_from('<HBBH',raw,at);kind&=15
   keys=set(range(first,first+n))
   if count_at==24 and bone==280 and kind in (4,5,6):
    assert kind not in values and n==1
    key=u32(40)+first*16;value,vin,vout=struct.unpack_from('<3f',raw,key+4)
    assert vin==vout==0
    values[kind]=value;destinations[kind]=[key+4];rotation_keys|=keys
   else:other_keys|=keys
 assert set(values)=={4,5,6} and not rotation_keys&other_keys
 original=Rotation.from_euler('xyz',[values[k] for k in (4,5,6)])
 angles=(original*Rotation.from_rotvec([0,0,math.pi])).as_euler('xyz')
 allowed=set()
 for kind,angle in zip((4,5,6),angles):
  for at in destinations[kind]:struct.pack_into('<f',raw,at,float(angle));allowed.update(range(at,at+4))
 assert raw[:80]==data[:80] and len(raw)==len(data)
 assert all(a==b or i in allowed for i,(a,b) in enumerate(zip(data,raw)))
 return bytes(raw)
