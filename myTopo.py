"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        kitchen_li = self.addHost( 'kitchen_li', ip='10.0.1.1' )
	living_li = self.addHost( 'living_li', ip='10.0.1.2')
        dining_li = self.addHost( 'dining_li' , ip='10.0.1.3' )
        bath_li = self.addHost( 'bath_li' , ip='10.0.2.1' )
        door_li = self.addHost( 'door_li', ip='10.0.2.2'  )
        garage_li = self.addHost( 'garage_li', ip='10.0.2.3'  )
        TV = self.addHost( 'TV' , ip='10.0.3.1' )
        phone = self.addHost( 'phone', ip='10.0.3.2'  )
        # refri = self.addHost( 'refri' )
        AC = self.addHost( 'AC', ip='10.0.3.3'  )
	kit_sen = self.addHost( 'kit_sen', ip='10.0.4.1'  )
	garage_sen = self.addHost( 'garage_sen', ip='10.0.4.2'  )
	door_sen = self.addHost( 'door_sen', ip='10.0.5.1'  )
	bed_sen = self.addHost( 'bed_sen', ip='10.0.5.2'  )
	s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')
	s6 = self.addSwitch('s6')
	s7 = self.addSwitch('s7')
	s8 = self.addSwitch('s8')
        

        # Add links
        self.addLink( kitchen_li, s1)
	self.addLink( living_li, s1)
        self.addLink( dining_li, s1 )
        self.addLink( bath_li, s2 )
        self.addLink( door_li, s2 )
        self.addLink( garage_li, s2 )
        self.addLink( TV, s3 )
        self.addLink( phone, s3 )
        # self.addLink( refri, appli )
        self.addLink( AC, s3 )
        self.addLink( kit_sen, s4 )
        self.addLink( garage_sen, s4 )
        self.addLink( door_sen, s5 )
        self.addLink( bed_sen, s5 )
	self.addLink( s1, s6 )
	self.addLink( s2, s6 )
	self.addLink( s3, s7 )
	self.addLink( s4, s8 )
	self.addLink( s5, s8 )
	self.addLink( s6, s7 )
	self.addLink( s7, s8 )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
