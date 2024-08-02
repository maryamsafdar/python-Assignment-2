def get_list():
    values = []

    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        values.append(value)
    
    # Print the list
    print("Here's the list:", values)

# Run the function
get_list()
