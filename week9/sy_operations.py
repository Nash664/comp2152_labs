import os
import sys
import platform
import socket

print(platform.machine())
print(platform.architecture())

socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

print(os.name)
print(platform.system())

print(os.getpid())

f_name="fdpractice.txt"
#with open("fdpractice.txt","a+") as f:
 #   f.read()
  #  f.write("Hello,World")

f= os.open(f_name,os.O_RDWR | os.O_CREAT)
print(f)
f_obj= os.fdopen(f, "a+")
print(f_obj)