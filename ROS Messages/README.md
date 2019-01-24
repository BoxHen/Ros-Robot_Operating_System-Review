ROS Messages

	Messages are defined by two things, the package name, where it belongs to and the message  		type
 
	There are standard ROS messages such as String, geomtry_msgs, Twist, and etc, but if we  		wanted to create our own messages, this is how:   
		-create a message folder in your package 
		-create the message file with file extension ".msg"
		-edit the message file by adding the elements (one per line)
		-update the dependencies 
			-in package.xml
			-in CMakeLists.txt
		-compile the package using catkin_make
		-make sure that your message is created using rosmsg show
