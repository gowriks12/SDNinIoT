#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    controller=net.addController(name='controller',
                      controller=OVSController,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    door_li = net.addHost('door_li', cls=Host, ip='10.0.2.5', defaultRoute=None)
    dining_li = net.addHost('dining_li', cls=Host, ip='10.0.1.3', defaultRoute=None)
    garage_sen = net.addHost('garage_sen', cls=Host, ip='10.0.4.11', defaultRoute=None)
    door_sen = net.addHost('door_sen', cls=Host, ip='10.0.5.12', defaultRoute=None)
    kit_li = net.addHost('kit_li', cls=Host, ip='10.0.1.1', defaultRoute=None)
    AC = net.addHost('AC', cls=Host, ip='10.0.3.9', defaultRoute=None)
    living_li = net.addHost('living_li', cls=Host, ip='10.0.1.2', defaultRoute=None)
    phone = net.addHost('phone', cls=Host, ip='10.0.3.8', defaultRoute=None)
    TV = net.addHost('TV', cls=Host, ip='10.0.3.7', defaultRoute=None)
    bath_li = net.addHost('bath_li', cls=Host, ip='10.0.2.4', defaultRoute=None)
    garage_li = net.addHost('garage_li', cls=Host, ip='10.0.2.6', defaultRoute=None)
    bed_sen = net.addHost('bed_sen', cls=Host, ip='10.0.5.13', defaultRoute=None)
    kit_sen = net.addHost('kit_sen', cls=Host, ip='10.0.4.10', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s1, kit_li)
    net.addLink(s1, living_li)
    net.addLink(s1, dining_li)
    net.addLink(s2, bath_li)
    net.addLink(s2, door_li)
    net.addLink(s2, garage_li)
    net.addLink(s3, TV)
    net.addLink(s3, phone)
    net.addLink(s3, AC)
    net.addLink(s4, kit_sen)
    net.addLink(s4, garage_sen)
    net.addLink(s5, door_sen)
    net.addLink(s5, bed_sen)
    net.addLink(s8, s5)
    net.addLink(s1, s6)
    net.addLink(s2, s6)
    net.addLink(s3, s7)
    net.addLink(s4, s8)
    net.addLink(s6, s7)
    net.addLink(s7, s8)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s5').start([controller])
    net.get('s1').start([controller])
    net.get('s6').start([controller])
    net.get('s3').start([controller])
    net.get('s8').start([controller])
    net.get('s2').start([controller])
    net.get('s4').start([controller])
    net.get('s7').start([controller])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

