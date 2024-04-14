from algorithms.binary_search import binary_search_iterative
from time import time

def test_binary_search():
    n = 100000
    unique_numbers = set()
    
    # Add numbers from 1 to n to the set
    for num in range(1, n + 1):
        unique_numbers.add(num)
    
    # Convert the set to a sorted list
    sorted_unique_list = sorted(list(unique_numbers))

    start = time()
    index = binary_search_iterative(sorted_unique_list, 3) 
    assert index == 2
