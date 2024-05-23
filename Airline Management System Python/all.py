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

def display_routes(routes):
    if not routes:
        print("No routes found within the specified number of layovers.")
    for i, (path, distance) in enumerate(routes):
        layovers = len(path) - 2  # -2 because the start and end are not considered layovers
        print(f"Route {i + 1}: {' -> '.join(path)}, Layovers: {layovers}, Total Distance: {distance} km")

class MinHeap:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i != 0 and self.key(self.heap[self.parent(i)]) > self.key(self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.key(self.heap[left]) < self.key(self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.key(self.heap[right]) < self.key(self.heap[smallest]):
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def heap_sort(self):
        sorted_array = []
        while len(self.heap) > 0:
            sorted_array.append(self.extract_min())
        return sorted_array

def sort_routes(routes, key):
    heap = MinHeap(key)
    for route in routes:
        heap.insert(route)
    return heap.heap_sort()

def key_by_distance(route):
    return route[1]

def key_by_layovers(route):
    return len(route[0]) - 2  # -2 because start and end are not considered layovers

def interactive_menu():
    graph = Graph()

    while True:
        print("\nInteractive Menu:")
        print("1. Add airport")
        print("2. Add flight")
        print("3. Find routes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            airport = input("Enter airport code: ")
            graph.add_airport(airport)
            print(f"Airport {airport} added.")
        elif choice == '2':
            origin = input("Enter origin airport code: ")
            destination = input("Enter destination airport code: ")
            distance = int(input("Enter distance: "))
            graph.add_flight(origin, destination, distance)
            print(f"Flight from {origin} to {destination} with distance {distance} added.")
        elif choice == '3':
            start = input("Enter start airport code: ")
            end = input("Enter destination airport code: ")
            max_layovers = int(input("Enter maximum number of layovers: "))
            routes = bfs_route_discovery(graph, start, end, max_layovers)

            if not routes:
                print("No routes found within the specified number of layovers.")
                continue

            print("\nSelect sorting preference:")
            print("1. Sort by total travel distance")
            print("2. Sort by number of layovers")

            sort_choice = input("Enter your choice: ")

            if sort_choice == '1':
                sorted_routes = sort_routes(routes, key_by_distance)
            elif sort_choice == '2':
                sorted_routes = sort_routes(routes, key_by_layovers)
            else:
                print("Invalid choice, displaying unsorted routes.")
                sorted_routes = routes

            display_routes(sorted_routes)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    interactive_menu()
