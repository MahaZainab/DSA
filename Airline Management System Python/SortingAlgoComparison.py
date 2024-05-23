def quicksort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[len(arr) // 2])
    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]
    return quicksort(left, key) + middle + quicksort(right, key)
def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = mergesort(arr[:mid], key)
    right = mergesort(arr[mid:], key)
    return merge(left, right)

import time
from all import Graph, bfs_route_discovery, sort_routes, key_by_distance, key_by_layovers

def generate_routes(num_routes):
    import random
    routes = []
    for _ in range(num_routes):
        path_length = random.randint(2, 10)
        path = [chr(random.randint(65, 90)) for _ in range(path_length)]
        distance = random.randint(100, 1000)
        routes.append((path, distance))
    return routes

def measure_time(sort_function, routes, key):
    start_time = time.time()
    sorted_routes = sort_function(routes, key)
    end_time = time.time()
    return end_time - start_time

def main():
    num_routes_list = [10, 100, 1000, 5000, 10000]
    key = key_by_distance

    for num_routes in num_routes_list:
        routes = generate_routes(num_routes)
        print(f"\nNumber of routes: {num_routes}")

        # Measure time for heapsort
        heap_time = measure_time(sort_routes, routes, key)
        print(f"Heapsort time: {heap_time:.6f} seconds")

        # Measure time for quicksort
        quicksort_time = measure_time(quicksort, routes, key)
        print(f"Quicksort time: {quicksort_time:.6f} seconds")

        # Measure time for mergesort
        mergesort_time = measure_time(mergesort, routes, key)
        print(f"Mergesort time: {mergesort_time:.6f} seconds")

if __name__ == "__main__":
    main()
