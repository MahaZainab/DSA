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

from all import Graph, bfs_route_discovery, display_routes, sort_routes, key_by_distance, key_by_layovers
def interactive_menu():
    graph = Graph()
    graph.add_flight("A", "B", 100)
    graph.add_flight("A", "C", 200)
    graph.add_flight("B", "C", 150)
    graph.add_flight("B", "D", 250)
    graph.add_flight("C", "D", 300)
    graph.add_flight("C", "E", 350)
    graph.add_flight("D", "E", 400)

    max_layovers = 2
    routes = bfs_route_discovery(graph, "A", "E", max_layovers)

    while True:
        print("\nInteractive Menu:")
        print("1. Display all routes")
        print("2. Sort routes by total travel distance")
        print("3. Sort routes by number of layovers")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_routes(routes)
        elif choice == '2':
            sorted_routes = sort_routes(routes, key_by_distance)
            display_routes(sorted_routes)
        elif choice == '3':
            sorted_routes = sort_routes(routes, key_by_layovers)
            display_routes(sorted_routes)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def display_routes(routes):
    if not routes:
        print("No routes found within the specified number of layovers.")
    for i, (path, distance) in enumerate(routes):
        layovers = len(path) - 2  # -2 because the start and end are not considered layovers
        print(f"Route {i + 1}: {' -> '.join(path)}, Layovers: {layovers}, Total Distance: {distance} km")

# Sample Usage
if __name__ == "__main__":
    interactive_menu()

