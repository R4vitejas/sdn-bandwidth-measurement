from mininet.topo import Topo
from mininet.link import TCLink

class OrangeTopo(Topo):
    def build(self):
        # Adding 3 switches as per the Orange Problem requirement 
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Adding 3 hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Link Implementation with Performance Metrics 
        # We use 100Mbps bandwidth and 5ms delay to enable performance analysis
        self.addLink(h1, s1, bw=100, delay='5ms', cls=TCLink)
        self.addLink(h2, s2, bw=100, delay='5ms', cls=TCLink)
        self.addLink(h3, s3, bw=100, delay='5ms', cls=TCLink)
        
        # Inter-switch links (Linear Topology)
        self.addLink(s1, s2, bw=100, delay='5ms', cls=TCLink)
        self.addLink(s2, s3, bw=100, delay='5ms', cls=TCLink)

topos = {'orangetopo': (lambda: OrangeTopo())}
