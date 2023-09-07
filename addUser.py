import json

# Function to add a new username to the JSON database
def add_username(file_name, new_username):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        
        # Check if the 'usernames' key exists in the JSON data
        if 'usernames' in data:
            usernames = data['usernames']
            usernames.append(new_username)
        else:
            usernames = [new_username]

        data['usernames'] = usernames

        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print(f"Username '{new_username}' added successfully!")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_name}'.")

# Specify the JSON file to update
json_file_name = 'usernames.json'

# Prompt the user for a new username
new_username = input("Enter a new username: ")

# Call the function to add the new username to the JSON database
add_username(json_file_name, new_username)
