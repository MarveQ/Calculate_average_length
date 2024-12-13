def calculate_average_length(strings):
    total_length = sum(len(one_string) for one_string in strings)
    return total_length / len(strings)

def main():
    user_input = input("Enter a list of strings separated by commas: ")
    raw_list = user_input.split(",")

    string_list = []
    for s in raw_list:
        string_list.append(s.strip())
        
    average_length = calculate_average_length(string_list)
    print(f"The average length of the strings is {average_length:.2f}")

main()
