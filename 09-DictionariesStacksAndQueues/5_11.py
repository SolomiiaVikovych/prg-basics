import json


json_file = 'voting.json'

    # Read the contents of the JSON file
try:
     with open(json_file, 'r') as file:
            voting_data = json.load(file)
except FileNotFoundError:
        # If the file does not exist, start with an empty dictionary
        voting_data = {}

    # Prompt user for a vote
person_name = input('Name of the person you are voting for: ').strip()

if person_name:
        # Increase the vote count for the person or add them with a vote count of 1
        if person_name in voting_data:
            voting_data[person_name] += 1
        else:
            voting_data[person_name] = 1

        # Save voting data back to the JSON file
        with open(json_file, 'w') as file:
            json.dump(voting_data, file, indent=4)

        print(f"Vote recorded for {person_name}.")
else:
        print("No name entered. Please try again.")

