"""
Created on Wed May 29 13:32:14 2024

@author: Simanto
"""

import itertools
import gzip
import math

def brute_force_on_numbers():
    digits = '0123456789'

    # Function to print the progress
    def print_progress(current, total):
        progress = (current / total) * 100
        print(f"\rProcessing: {progress:.2f}%", end='')

    # Calculate the total number of combinations
    total_combinations = sum(10 ** length for length in range(8, 11))
    
    current_count = 0
    
    # Open a gzip file in write mode
    with gzip.open('number_combinations.txt.gz', 'wt') as file:
        for length in range(8, 11):
            combinations = itertools.product(digits, repeat=length)
            
            for combination in combinations:
                file.write(''.join(combination) + '\n')
                current_count += 1
                print_progress(current_count, total_combinations)
    
    print("\nTask complete.")
    

def real_time_brute_force():
    # Define the set of digits
    digits = '0123456789'
    
    # Specify the phone number to search for
    phone_number = '01601217735'  # Replace this with the actual phone number
    
    # Flag to check if the phone number is found
    found = False
    
    def print_progress(current, total):
        progress = (current / total) * 100
        print(f"\rProcessing: {progress:.2f}%", end='')
    
    total_combinations = sum(10 ** length for length in range(8, 11))
    current_count = 0
    
    # Iterate over lengths from 8 to 10
    for length in range(11, 12):
        # Generate all combinations of the current length
        combinations = itertools.product(digits, repeat=length)
        # Check each combination for the phone number
        for combination in combinations:
            comb_str = ''.join(combination)
            
            current_count += 1
            #print_progress(current_count, total_combinations)
            print(comb_str)
            if comb_str == phone_number:
                found = True
                print(f'Phone number {phone_number} found in combinations.')
                break
        if found:
            break

    if not found:
        print(f'Phone number {phone_number} not found in combinations.')

# Call the function to execute the task
real_time_brute_force()