def remove_repeated_numbers(numbers):
    unique_numbers = []
    for num in numbers:    
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def main():
    numbers = []
    for i in range(10):
        try: 
            num = int(input(f"Enter numbeer {i + 1}: "))
            numbers.append(num)
        except ValueError:
                print("Invalid input. Please enter a valid number.")
    unique_numbers = remove_repeated_numbers(numbers)
    print("\nOrigin Numbers List: ", numbers)
    print("Unique List:", unique_numbers)

main()
