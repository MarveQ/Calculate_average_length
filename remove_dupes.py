def remove_dupes(string):
    new_string = ''
    for char in string:    
        if char not in new_string and char != " ":
            new_string += char
    return new_string

def main():
    string = input("Enter any string: ")
    new_string = remove_dupes(string)
    print("Your new string is: ", new_string)

main()
