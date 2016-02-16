#Grid Localization Based on Real Data in ROS

The objective of this assignment is to make you familiar with Grid Localization which
a variant of discrete Bayes Localization. In addition you will learn how to create your
own messages in ROS and how to use them. Also you will get your hands on working
with rosbag.
What is Grid Localization
Grid Localization is a variant of discrete Bayes Localization. In this method, the map
converted to a Grid. At each time step, the algorithm nds out the probabilities of
the robot presence at every grid cell. The grid cells with maximum probabilities at each
step, characterize the robot's trajectory.
Grid Localization runs in two iterative steps. Movement and Observation.
After each movement, you should compute if that certain movement can move the robot
etween grid cells. For each observation, you should nd the most probable cells which
the given observation may have occured in them.
Rosbag :
Rosbags are used for dumping the messages published to certain topics to les. For
this assignment, we have provided a bag le for you which includes the movements ans
observations information. So you need to write a code and read the bag le. For this
purpose, rst have a look at Rosbag Tutorial. After that go through the following steps.
 Create a package named lab3 and then create these two messages in your package.
Motion.msg which includes in order
int32 timeTag
geometry
msgs/Quaternion rotation1
 translation
geometry msgs/Quaternion rotation2
and the Observation.msg which includes
int32 timeTag
int32 tagNum
float range
geometry msgs/Quaternion bearing
After creating these messages, apply the required changed to package.xml and
CMakelist.txt.
 Use rosbag info command to nd the required information of the given bag le.
This tutorial may be useful.
 Using the tutorials and acquired information, write a code which reads the infor-
mation in the bag le.
Motion Model, Observation Model and Map
For the purpose of localization, you should have access to map. There are six landmarks
in you map as follows:
Tag number 0 : x = 1.25m, y = 5.25m
Tag number 1 : x = 1.25m, y = 3.25m
Tag number 2 : x = 1.25m, y = 1.25m
Tag number 3 : x = 4.25m, y = 1.25m
Tag number 4 : x = 4.25m, y = 3.25m
Tag number 5 : x = 4.25m, y = 5.25m
The robot moves in the area within these landmarks. You should make a grid for 7m*7m
coverage. Your cell size should be 20com*20cm. You also should assume a dimension
for the robot's heading. So your grid is 3 dimensional. The third dimension covers the
robot's heading. You can discretize that with your desired value (10 degree, 20 degree
or more). The rst pose of your robot within the grid is (12, 28) and the rst heading
is 200.52 degree. The robot's rst pose in the 3rd dimension depends on your selected
descritization size, you should nd it out yourself. For example if your discretization size
is 90 degress, the cell number in 3rd dimension will be 200.52/90+1 = 3. So the robot's
rst pose is (12 , 28, 3). (Notice that I have assumed there is no cell with index zero).
As you may have noticed, the motion model of this robot is (rotation, translation, rotation)
and the observation model is (range, bearing). In Grid Localization, for the purpose
of moving robot between cells, the motion and observation noises should be adjusted.
You need a translation and rotation noise for movement and range and bearing noise for
your observation. A good selection for this purpose is half the cell size (Why???). So for
the example of 20*20 cells and 90 degree discritization, range and translation noises are
10cm, and bearing and rotation noises are 45 degrees.
