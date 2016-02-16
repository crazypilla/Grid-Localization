#!/usr/bin/env python
import rosbag
from tf.transformations import *
import numpy as np
import rospy
import math
import roslib
import os
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
translationvals=np.zeros((1,89))
rotation1vals=np.zeros((1,89))
rotation2vals=np.zeros((1,89))
#rangevals=np.zeros((1,89))
#bearingvals=np.zeros((1,89))
angles=[0]*3
angles1=[0]*3
os.environ["HOME"]
#tagNumvals=np.zeros((1,89))
observationsval=np.zeros((89,3))
def getbagvals():
	global pub
	global translationvals	
	global rotation1vals
	global rotation2vals
	global rangevals
	global bearingvals
	global observationsval
	i=0
	j=0
	bag = rosbag.Bag('/home/robotics/catkin_ws/src/lab3/grid.bag')
	for topic,msg,t in bag.read_messages(topics=['Movements']):   
		
		theta_x= msg.rotation1.x
		theta_y= msg.rotation1.y
		theta_z= msg.rotation1.z
		theta_w= msg.rotation1.w
		angles=euler_from_quaternion([theta_x,theta_y,theta_z,theta_w])
		rotation1vals[:,i]=angles[2]
		
		translationvals[:,i]=msg.translation*100

		theta_x= msg.rotation2.x
		theta_y= msg.rotation2.y
		theta_z= msg.rotation2.z
		theta_w= msg.rotation2.w
		angles1=euler_from_quaternion([theta_x,theta_y,theta_z,theta_w])
		rotation2vals[:,i]=angles1[2]
		i=i+1
	
	#print rotation2vals
	
	for topic,msg,t in bag.read_messages(topics=['Observations']):   
		
		theta_x= msg.bearing.x
		theta_y= msg.bearing.y
		theta_z= msg.bearing.z
		theta_w= msg.bearing.w
		angles=euler_from_quaternion([theta_x,theta_y,theta_z,theta_w])
		#bearingvals[:,j]=angles[2]
		#rangevals[:,j]=msg.range
		
		#tagNumvals[:,j]=msg.tagNum
		observationsval[j,0]=msg.tagNum
		observationsval[j,1]=msg.range*100
		observationsval[j,2]=angles[2]
		j=j+1
	#print observationsval
	#print bearingvals
	bag.close()

def calprob(x,mean,variance):
	prob=(1/(variance*math.sqrt(2*math.pi)))*math.exp((-1)*((x-mean)**2)/(2*(variance)**2))
	return prob

def calcprobs():
    global pub
    global translationvals
    global rotation1vals
    global rotation2vals
    global observationsval
    prob=[[[0 for k in range(4)]for j in range(35)]for i in range(35)]
    temp_prob=[[[0 for k in range(4)]for j in range(35)]for i in range(35)]
    temp_prob1=[[[0 for k in range(4)]for j in range(35)]for i in range(35)]
    prob[11][27][2]=1
    #print prob[0][1][1]
    #print np.sum(prob)
    marker = Marker()
    marker.header.frame_id = "/base_link"
    marker.type = marker.LINE_STRIP
    marker.action = marker.ADD
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.a = 1.0
    marker.pose.orientation.w = 1.0
    marker.id = 0
    marker.type = Marker.LINE_STRIP
    marker.scale.x = 0.1
    marker.color.r = 1.0
    marker.color.a = 1.0
    
    m1 = Marker()
    m1.header.frame_id = "/base_link"
    m1.type = m1.CUBE
    m1.action = m1.ADD
    m1.scale.x = 1.2
    m1.scale.y = 1.2
    m1.scale.z = 1
    m1.color.b = 1.0
    m1.color.a=1.0
    m1.pose.orientation.w = 1.0
    m1.id = 1
    m1.pose.position.x=2
    m1.pose.position.y=26
    #pub.publish(m1)
    
    
    
 
    m2 = Marker()
    m2.header.frame_id = "/base_link"
    m2.type = m2.CUBE
    m2.action = m2.ADD
    m2.scale.x = 1.2
    m2.scale.y = 1.2
    m2.scale.z = 1
    m2.color.b = 1.0
    m2.color.a=1.0
    m2.pose.orientation.w = 1.0
    m2.id = 2
    m2.pose.position.x=2
    m2.pose.position.y=16
    #pub.publish(m2)
    
    
    m3 = Marker()
    m3.header.frame_id = "/base_link"
    m3.type = m3.CUBE
    m3.action = m3.ADD
    m3.scale.x = 1.2
    m3.scale.y = 1.2
    m3.scale.z = 1
    m3.color.b = 1.0
    m3.color.a=1.0
    m3.pose.orientation.w = 1.0
    m3.id = 3
    m3.pose.position.x=2
    m3.pose.position.y=6
    #pub.publish(m3)
    
    m4 = Marker()
    m4.header.frame_id = "/base_link"
    m4.type = m4.CUBE
    m4.action = m4.ADD
    m4.scale.x = 1.2
    m4.scale.y = 1.2
    m4.scale.z = 1
    m4.color.b = 1.0
    m4.color.a=1.0
    m4.pose.orientation.w = 1.0
    m4.id = 4
    m4.pose.position.x=21
    m4.pose.position.y=6
    #pub.publish(m4)
    
    m5 = Marker()
    m5.header.frame_id = "/base_link"
    m5.type = m5.CUBE
    m5.action = m5.ADD
    m5.scale.x = 1.2
    m5.scale.y = 1.2
    m5.scale.z = 1
    m5.color.b = 1.0
    m5.color.a=1.0
    m5.pose.orientation.w = 1.0
    m5.id = 5
    m5.pose.position.x=21
    m5.pose.position.y=16
    #pub.publish(m5)
    
    m6 = Marker()
    m6.header.frame_id = "/base_link"
    m6.type = m6.CUBE
    m6.action = m6.ADD
    m6.scale.x = 1.2
    m6.scale.y = 1.2
    m6.scale.z = 1
    m6.color.b = 1.0
    m6.color.a=1.0
    m6.pose.orientation.w = 1.0
    m6.id = 6
    m6.pose.position.x=21
    m6.pose.position.y=26
    #pub.publish(m6)
    
       
    
    
    
    
    
    
    
    for num in range(89):
	trans_orig=translationvals[:,num]
	#print trans_orig
	rot1_orig=rotation1vals[:,num]
	#print rot1_orig
        rot2_orig=rotation2vals[:,num]	
	#print rot2_orig
	count=0	
	check = 0
	c=0
	temp_prob=prob
	for i in range(35):
		for j in range(35):
			for k in range(4):
				if(prob[i][j][k]>0.4):
					center1=[((2*i)+1)*10,((2*j)+1)*10,(( (math.pi/2)*k) +(math.pi/4) )]
					#print center1
					for i1 in range(35):
						for j1 in range(35):
							for k1 in range(4):
								c=c+1
								center2=[((2*i1)+1)*10,((2*j1)+1)*10,(( (math.pi/2)*k1) +(math.pi/4) )]
								#print center2
								transval=math.sqrt( (center1[0]-center2[0]) **2+(center1[1]-center2[1])**2)
								#print transval
								angleval=math.atan2((center2[1]-center1[1]),(center2[0]-center1[0]))+math.pi
								#print angleval
								
								rot1val=angleval-center1[2]
								#print rot1val
								if rot1val>math.pi:
									rot1val=rot1val-2*math.pi
								#print rot1val

								rot2val=center2[2]-angleval
								if rot2val>math.pi:
									rot2val=rot2val-2*math.pi
								Noise_translation=transval-trans_orig
								#print Noise_translation
								Noise_rot1=rot1val-rot1_orig
								"""if Noise_rot1>math.pi:
									Noise_rot1=Noise_rot1-2*math.pi"""
								#print Noise_rot1
								Noise_rot2=rot2val-rot2_orig
								"""if Noise_rot2>math.pi:
									Noise_rot2=Noise_rot2-2*math.pi"""
								temp_prob[i1][j1][k1]=calprob(Noise_translation,0,10)*calprob(Noise_rot1,0,(math.pi/4))*calprob(Noise_rot2,0,math.pi/4)*prob[i][j][k]
	prob=temp_prob
	print c
	
	"""print np.sum(prob)
	for a in range(35):
	    for b in range(35):
		for c in range(4):
		   if (prob[a][b][c]>0.01):
	              #print prob
		      count=count+1
		      print count"""

	for l in range(35):
		for m in range(35):
			for n in range(4):
				#if(prob[l][m][n]>0.1):
					centerval=[((2*l)+1)*10,((2*m)+1)*10,(( (math.pi/2)*n) +(math.pi/4) )]
					#print centerval
					if observationsval[num][0]==0:
						x_landmark=125
						y_landmark=525
					
					elif observationsval[num][0]==1:
						x_landmark=125
						y_landmark=325
					elif observationsval[num][0]==2:
						x_landmark=125
						y_landmark=125
					elif observationsval[num][0]==3:
						x_landmark=425
						y_landmark=125
					elif observationsval[num][0]==4:
						x_landmark=425
						y_landmark=325
					elif observationsval[num][0]==5:
						x_landmark=425
						y_landmark=525
					

					rangeval_req=math.sqrt( (centerval[0]-x_landmark) **2+(centerval[1]-y_landmark)**2)
					bearingval_req=math.atan2((centerval[1]-y_landmark),(centerval[0]-x_landmark))+math.pi
					Noise_range=rangeval_req-observationsval[num][1]
					Noise_bearing=bearingval_req-observationsval[num][2]
					#print Noise_range
					#print Noise_bearing
					if Noise_bearing>math.pi:
								#print Noise_bearing
								Noise_bearing=Noise_bearing-2*math.pi
								#Noise_rot2=rot2val-rot2_orig
					temp_prob1[l][m][n]=calprob(Noise_bearing,0,math.pi/4)*calprob(Noise_range,0,10)*prob[l][m][n]
					#if l==5 and m==20 and n==1:
						#print prob[l][m][n]
			
					
	prob=temp_prob1
	#print np.sum(prob)
	prob=prob/np.sum(prob)
	#print np.sum(prob)
	arr=np.array(prob)
	xval,yval,zval=np.unravel_index(arr.argmax(),arr.shape)
	print [xval,yval,zval]
	p = Point()
	p.x = (xval)
	p.y = (yval)
	p.z = 0
	marker.points.append(p)	
	#pub.publish(marker)		
    #print marker
    while not rospy.is_shutdown():
    		pub.publish(m1)
    		pub.publish(m2)
    		pub.publish(m3)
    		pub.publish(m4)
    		pub.publish(m5)
    		pub.publish(m6)
		pub.publish(marker)
		
	


if __name__ == '__main__':
     try:
           global pub
           rospy.init_node('rviz_display')
	   topic = 'visualization_marker'
	   pub = rospy.Publisher(topic, Marker,queue_size=10)
           getbagvals()
	   calcprobs()
	   #print rangevals
     except rospy.ROSInterruptException:
           pass
