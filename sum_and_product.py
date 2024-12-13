# SumAndProduct.py

# Function to calculate the sum of all whole numbers up to and including n
def sums(n):
    """
    Computes the sum of all whole numbers from 1 to n.
    :param n: A positive integer
    :return: Sum of all whole numbers from 1 to n
    """
    return sum(range(1, n + 1))

# Function to calculate the product of all whole numbers up to and including n
def products(n):
    """
    Computes the product of all whole numbers from 1 to n.
    :param n: A positive integer
    :return: Product of all whole numbers from 1 to n
    """
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def main():
    # Prompt the user for input
    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)
    
    while number != 0:
        # Call sums() function
        total_sum = sums(number)
        # Call products() function
        total_product = products(number)
        
        # Display the results
        print(f"The sum of numbers from 1 to {number} is: {total_sum}")
        print(f"The product of numbers from 1 to {number} is: {total_product}")
        
        # Prompt for the next input
        numberString = input("Enter a positive integer or 0 to quit: ")
        number = int(numberString)

# Run the program
main()
