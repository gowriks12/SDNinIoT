#!/bin/bash
ping -c 1 10.0.2.2 #ping door_lights
ping -c 1 10.0.3.3 #ping AC
ping -c 1 10.0.1.2 #ping living_lights
ping -c 1 10.0.1.1 #ping kitchen_lights
ping -c 1 10.0.1.3 #ping dining_lights
ping -c 1 10.0.2.1 #ping bathroom_lights
ping -c 1 10.0.2.3 #ping garage_lights
ping -c 1 10.0.3.1 #ping TV
	#ping -c 1 10.0.0.10 #ping kit_sen
	#ping -c 1 10.0.0.9 #ping garage_sen
	#ping -c 1 10.0.0.7 #ping door_sen
	#ping -c 1 10.0.0.4 #ping bed_sen
