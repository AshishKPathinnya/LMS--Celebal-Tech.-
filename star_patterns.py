
def lower_triangle(rows):        # Function to create a lower triangular star pattern
    
    print("Lower Triangle:")
    # Iterate through each row
    for i in range(rows):
                           
        print("*" * (i + 1))      # Print stars for the current row

# Function to create an upper triangular star pattern
def upper_triangle(rows):
    
    print("\nUpper Triangle:")
    
    for i in range(rows):
        
        print(" " * i + "*" * (rows - i))    # Print leading spaces and stars

# Function to create a pyramid star pattern
def pyramid(rows):
    
    print("\nPyramid:")
    
    for i in range(rows):
       
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))   # Print spaces and stars for centered pyramid


num_rows = 5 # number of rows for patterns


lower_triangle(num_rows)   # Generate the lower triangle pattern

upper_triangle(num_rows)   # Generate the upper triangle pattern

pyramid(num_rows)          # Generate the pyramid pattern