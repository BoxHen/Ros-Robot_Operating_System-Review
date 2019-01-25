ROS Service

	A ROS Service is a ROS Server and ROS child
	A service is not like a topic since a service is a one time communication 
		-ROS topics look like this: publisher -> topic message -> subscriber
		-ROS Services look like this:  server <- request message <- client
		-			       server -> response message -> client

	To create a client/server ros service app:
		-define the service message(service file)
		-create ros server node
		-create ros client node
		-execute the service
		-consume the service by the node
	
	We can check ros services with "rosservice list"
	get more info on ros services with "rosservice info 'service name'"
		this will give us info on the arguments needed for the service
	we can check the type of the service with "rossrv info 'type'"
		this shows the structure of the message
	we can call the service with "rosservice call 'service name' 'arguments'"
		ex - rosservice call /spawn 7 7 0 t2
