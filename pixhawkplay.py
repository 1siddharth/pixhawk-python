import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

from dronekit import connect
          mavproxy.py --master=/dev/ttyUSB0


#vehicle = connect("COM14",baud =57600,wait_ready=True)
vehicle = connect(connection_string ,wait_ready=True)


aa=vehicle.gps_0

print("this is it",aa)

lat =155.586846
long =52.59587454

# initial values dist camdist=7.619(ft) resL=1920 ,resB=1080
surfL=17.9 
surfB=11.6
camdist =231.95
#suppose xx
TL=17.9/231.96=0.07716
TB=11.6/231.96 =0.050008
newL=TL*xx*100
newB=TB*xx*100
pixelL=newL*1920(cm)
pixelB=newB*1080(cm)
xlat=(newL*(0.0362/1.0247)*x)
ylong=(newB*(0.0362/1.0247)*y)




# get xlat,ylong moments final
if(x<960 and y>=540)
  xlat=lat-xlat
  ylong=ylong-long
elif(x<540 and y<540)
  xlat=lat-xlat
  ylong=long-ylong
elif(x>540 and y<540)
  xlat=xlat-lat
  ylong=long-ylong
elif(x>=540 and y>540)
  xlat=xlat-lat
  ylong=ylong-long
return x y



# get x,y moments
if(x<960 and y>=540)
  x=960-x
  y=y-540
elif(x<540 and y<540)
  x=940-x
  y=540-y
elif(x>540 and y<540)
  x=x-940
  y=540-y
elif(x>=540 and y>540)
  x=x-940
  y=y-540
return x y


vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")
