from GraphBFS import Graph, bfs_route_discovery

class Menu:
    def __init__(self):
        self.graph = Graph()
    
    def display_menu(self):
        while True:
            print("\n1. Add Airport")
            print("\n2. Add Flight")
            print("\n3. Find Routes with BFS")
            print("\n4. Exit")
            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.add_airport()
            elif choice == '2':
                self.add_flight()
            elif choice == '3':
                self.find_routes()
            elif choice == '4':
                break
            else:
                print("\nInvalid choice. Please try again.")

    def add_airport(self):
        airport = input("\nEnter airport code: ")
        self.graph.add_airport(airport)
        print(f"\nAirport {airport} added.")

    def add_flight(self):
        origin = input("\nEnter origin airport code: ")
        destination = input("\nEnter destination airport code: ")
        distance = int(input("\nEnter distance between airports: "))
        self.graph.add_flight(origin, destination, distance)
        print(f"\nFlight from {origin} to {destination} with distance {distance} added.")

    def find_routes(self):
        start = input("\nEnter start airport code: ")
        end = input("\nEnter end airport code: ")
        max_layovers = int(input("\nEnter maximum number of layovers: "))
        routes = bfs_route_discovery(self.graph, start, end, max_layovers)
        
        if routes:
            print("\nRoutes found:")
            for route, distance in routes:
                print(f"Route: {' -> '.join(route)}, Distance: {distance}")
        else:
            print("\nNo routes found.")

# Instantiate and run the menu
menu = Menu()
menu.display_menu()
