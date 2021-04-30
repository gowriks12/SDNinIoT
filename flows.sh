#!/bin/bash

sudo ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.5.1,priority=40000,actions=drop
sudo ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.5.2,priority=40000,actions=drop
sudo ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.4.2,priority=40000,actions=drop
sudo ovs-ofctl add-flow s6 in_port=3,dl_type=0x0800,nw_src=10.0.4.1,priority=40000,actions=drop

sudo ovs-ofctl add-flow s6 in_port=1,priority=4000,actions=normal
sudo ovs-ofctl add-flow s6 in_port=2,priority=4000,actions=normal
