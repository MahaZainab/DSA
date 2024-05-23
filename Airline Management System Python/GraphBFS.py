class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_airport(self, airport):
        if airport not in self.adjacency_list:
            self.adjacency_list[airport] = []

    def add_flight(self, origin, destination, distance):
        if origin not in self.adjacency_list:
            self.add_airport(origin)
        if destination not in self.adjacency_list:
            self.add_airport(destination)
        self.adjacency_list[origin].append((destination, distance))

    def get_neighbors(self, airport):
        return self.adjacency_list.get(airport, [])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

def bfs_route_discovery(graph, start, end, max_layovers):
    queue = Queue()
    queue.enqueue((start, [start], 0))  # (current_airport, path_taken, cumulative_distance)
    routes = []

    while not queue.is_empty():
        current_airport, path, distance = queue.dequeue()

        # If we have reached the destination within the layover limit, record the route
        if current_airport == end:
            if len(path) - 2 <= max_layovers:  # -2 because the start and end are not considered layovers
                routes.append((path, distance))
            continue

        # If we have reached the layover limit, do not explore further
        if len(path) - 1 > max_layovers + 1:  # +1 because the start is not considered a layover
            continue

        for neighbor, flight_distance in graph.get_neighbors(current_airport):
            if neighbor not in path:  # Avoid cycles
                new_path = path + [neighbor]
                new_distance = distance + flight_distance
                queue.enqueue((neighbor, new_path, new_distance))

    return routes
