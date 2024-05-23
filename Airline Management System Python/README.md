# Airline Management System

This project implements an airline route management system using a graph data structure. It includes functionality for adding airports and flights, discovering all possible routes between two airports using Breadth-First Search (BFS), and sorting the routes based on total travel distance or the number of layovers.

This Python project implements an airline management system with a focus on three main functionalities:

1. **Route Discovery using BFS**: Finds all possible flight routes between two airports considering a maximum number of layovers.
2. **Efficient Airport Lookup using Hashing**: Utilizes a custom hash table for fast retrieval of airport information based on airport codes.
3. **Optimal Route Selection using Heap Sort**: Allows sorting of discovered routes based on either total travel distance or the number of layovers, with comparisons to other sorting algorithms (Quick Sort and Merge Sort) for performance analysis.

## Requirements

- Python 3.x.
- An IDE like Visual Studio Code to run and manage the project.

## Features

- **Add Airports**: Add airports by their codes.
- **Add Flights**: Add flights between airports with distances.
- **Find Routes**: Discover all possible routes from a start airport to a destination airport with a specified maximum number of layovers.
- **Sort Routes**: Sort routes by total travel distance or the number of layovers.

## Compile the Python Files:

Navigate to the src directory containing the Python files and compile them using the following commands:
- Python GraphBFS.py
- Python Hashing.py
- Python Heapsort.py
- MenuGraph.py

BFS.ipynb can be run cell by cell by pressing shift+enter keys

## Using the Application

Each component of the application serves a distinct purpose. Here are the instructions on how to use each part:

- **AirlineRouteFinder**: 
  - **Purpose**: Finds all possible flight routes between two specified airports considering a maximum number of layovers.
  - **Usage**: Input the origin and destination airports along with the maximum allowed layovers to find possible routes.
  
- **AirportHashTable**:
  - **Purpose**: Manages airport data efficiently using a custom hash table, allowing for fast retrieval, insertion, and deletion of airport information based on airport codes.
  - **Usage**: 
    - **Add**: Add airport entries by their codes.
    - **Search**: Search for airport entries by their codes.
    - **Delete**: Delete airport entries by their codes.

- **RouteSorter**:
  - **Purpose**: Sorts discovered routes based on user preferences regarding travel distance or number of layovers.
  - **Usage**: Choose your preferred sorting criterion (distance or layovers) to sort and view the routes.

- **SortingPerformanceTest**:
  - **Purpose**: Tests and compares the performance of different sorting algorithms (heap sort, quick sort, and merge sort) especially as the number of routes increases.
  - **Usage**: Automatically runs on execution and prints out performance metrics for the different sorting algorithms. It is ideal for analyzing which sorting method is the most efficient under varying conditions.
