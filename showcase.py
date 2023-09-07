import json

# Function to read and print usernames from the JSON file
def read_usernames(file_name):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            usernames = data['usernames']
            print("Usernames:")
            for username in usernames:
                print(username)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_name}'.")

# Specify the JSON file to read
json_file_name = 'usernames.json'

# Call the function to read and print the usernames
read_usernames(json_file_name)
