def count_case_letters(string):
    upper_case_count = len([char for char in string if char.isupper()])
    lower_case_count = len([char for char in string if char.islower()])
    print(f"Number of upper-case letters: {upper_case_count}")
    print(f"Number of lower-case letters: {lower_case_count}")

def main():
    string = input("Enter any string: ")
    count_case_letters(string)

main()
