def update_list_in_file(new_list, file_path):
    # Read existing list from the file
    try:
        with open(file_path, 'r') as file:
            existing_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        existing_list = []

    # Find new strings and remove strings that are no longer in the list
    updated_list = list(set(existing_list + new_list))
    
    # Determine the strings that were added
    added_strings = list(set(updated_list) - set(existing_list))

    # Write the updated list back to the file
    with open(file_path, 'w') as file:
        for item in updated_list:
            file.write(f"{item}\n")

    print("List updated successfully.")
    
    return added_strings