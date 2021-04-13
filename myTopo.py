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
        kitchen_li = self.addHost( 'kitchen_li' )
	living_li = self.addHost( 'living_li' )
        dining_li = self.addHost( 'dining_li' )
        bath_li = self.addHost( 'bath_li' )
        door_li = self.addHost( 'door_li' )
        garage_li = self.addHost( 'garage_li' )
        TV = self.addHost( 'TV' )
        phone = self.addHost( 'phone' )
        refri = self.addHost( 'refri' )
        AC = self.addHost( 'AC' )
	kit_sen = self.addHost( 'kit_sen' )
	garage_sen = self.addHost( 'garage_sen' )
	door_sen = self.addHost( 'door_sen' )
	bed_sen = self.addHost( 'bed_sen' )
	lights = self.addSwitch('s1')
        appli = self.addSwitch('s2')
        sensors = self.addSwitch('s3')
        

        # Add links
        self.addLink( kitchen_li, lights)
	self.addLink( living_li, lights)
        self.addLink( dining_li, lights )
        self.addLink( bath_li, lights )
        self.addLink( door_li, lights )
        self.addLink( garage_li, lights )
        self.addLink( TV, appli )
        self.addLink( phone, appli )
        self.addLink( refri, appli )
        self.addLink( AC, appli )
        self.addLink( kit_sen, sensors )
        self.addLink( garage_sen, sensors )
        self.addLink( door_sen, sensors )
        self.addLink( bed_sen, sensors )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
