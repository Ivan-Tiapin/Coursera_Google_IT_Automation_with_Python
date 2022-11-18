"""Simulates server load, use load balancer to ensures that there are enough servers to serve those connections."""
import random

# Server load simulation.
class Server:
    def __init__(self):
        self.connections = {}

    def add_connection(self, connection_id):
        connection_load = random.random() * 10 + 1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        del self.connections[connection_id]

    def load(self):
        total = 0
        total = sum(self.connections.values())
        return total

    def __str__(self):
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")
print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


class LoadBalancing:
    # Initialize the load balancing system with one server.
    def __init__(self):
        self.connections = {}
        self.servers = [Server()]

    # Randomly selects a server and adds a connection to it.
    def add_connection(self, connection_id):
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server.
        self.connections[connection_id] = server
        # Add the connection to the server.
        server.add_connection(connection_id)
        self.ensure_availability()

    # Closes the connection on the server corresponding to connection_id.
    def close_connection(self, connection_id):
        # Find out the right server.
        server = self.connections[connection_id]
        # Close the connection on the server.
        server.close_connection(connection_id)
        # Remove the connection from the load balancer.
        del self.connections[connection_id]

    # Calculates the average load of all servers.
    def avg_load(self):
        # Sum the load of each server and divide by the amount of servers.
        total = 0
        for server in self.servers:
            total += server.load()
        return total / len(self.servers)

    def ensure_availability(self):
        # If the average load is higher than 50, spin up a new server.
        avg_load = self.avg_load()
        if avg_load > 50:
            self.servers.append(Server())

    def __str__(self):
        # Returns a string with the load for each server.
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())