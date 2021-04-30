# SDNinIoT
1. Open terminal, type sudo ~/mininet/examples/miniedit.py
2. open topology designed.
3. Start wireshark packet capture.
4. Run topology and check for packets in wireshark
5. Open terminals of Door sensor, door lights, kitchen lights, living room lights and AC.
6. tcpdump command in AC, lights terminals and run the shell script in door sensor to ping other nodes.
7. Check wireshark packet capture.
8. Second scenario where the phone pings the lights and AC to switch off.
9. Similar to scenario 1 open the terminals and demonstrate. 
10. Adding match priorities for packets from kitchen sensor
	sudo mn --custom myTopo.py --topo mytopo
	mininet> sh ovs-ofctl add-flow s3 in_port=1,dl_type=0x0800,nw_src=10.0.4.1,priority=40000,actions=normal
	mininet> sh ovs-ofctl dump-flows s3
Show the flow table entries in s3.
11. Dropping packets depiction
	mininet> sh ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.5.1,actions=drop
	mininet> sh ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.5.2,actions=drop
	mininet> sh ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.4.2,actions=drop
	mininet> sh ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.4.1,actions=drop
	mininet> sh ovs-ofctl dump-flows s6
	mininet> door_sen ping -c 3 door_li
	mininet> door_sen ping -c 3 AC
open xterm and demonstrate ping and dropping of packets.
