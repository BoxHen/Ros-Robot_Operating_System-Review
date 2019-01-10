Initializing the roscpp Node
	
	The first thing to do before calling any roscpp functions in a node is ros::init(). Initializing the node 
	this way reads the command line arguments and environment to figure out the node name, namespace, and 
	remappings. It does not contact the master. You can use other ROS functions after calling ros::init() to 
	check on the status of the master. Generally:
	void ros::init(<command line or remapping arguments>, std::string node_name, uint32_t options);
		ros::init(argc, argv, "my_node_name");
		ros::init(argc, argv, "my_node_name", ros::init_options::AnonymousName);

	Arguments
		argc and argv
			ROS uses these to parse remapping arguments from the command line. It also modifies them 
			so that they no longer contain any remapping arguments, so that if you call ros::init() 
			before processing your command line you will not need to skip those arguments yourself.
 
		node_name
			This is the name that will be assigned to your node unless it's overridden by one of the 
			remapping arguments. Node names must be unique across the ROS system. If a second node 
			is started with the same name as the first, the first will be shutdown automatically. In 
			cases where you want multiple of the same node running without worrying about naming them 
			uniquely, you may use the init_options::AnonymousName option described below.

		options
			This is an optional argument that lets you specify certain options that change roscpp's 
			behavior. The field is a bitfield, so multiple options can be specified. The options are 
			described in the Initialization Options section.

Starting the roscpp Node
	
	To start a roscpp node, create a ros::NodeHandle:
		ros::NodeHandle nh;

	Calling and creating ros::NodeHandle will call ros::start(), and ros::shutdown() when the last 
	ros::NodeHandle is destroyed. You can manually manage the lifetime of the node by calling 
	ros::start() and ros::shutdown().

Shutting Down the Node

	You can call the ros::shutdown() to shutdown the node and kill all open subscriptions, publications, 
	service calls, and service servers. By default Ctrl-C will automatically shutdown the node.
	(SIGINT handler)

