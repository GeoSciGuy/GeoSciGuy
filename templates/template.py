# Created by : Matthew Herrinng
# Created on : 2025-10-07   
# Description: Template for Python files
#              (c) Copyright 2025 Matthew Herrinng
#              All rights reserved.


# Import Area
import os
import time
import sys
import datetime

# Variables Area

# Helper FUnctions

# Main Function
def main():
    start_time = time.perf_counter()
    try:
        print("Hello, World!")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        elapsed_time = time.perf_counter() - start_time
        print(f"Execution completed in {elapsed_time:.3f} seconds.")

main()
