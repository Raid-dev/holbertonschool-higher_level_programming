#!/usr/bin/python3
import os


def generate_invitations(template_content, attendees):
    """Function for generating invitations"""

    if not template_content:
        print("ERROR: template cannot be empty")
        return

    if not attendees:
        print("ERROR: attendees_list cannot be empty")
        return

    if not isinstance(template_content, str):
        print("ERROR: template must be a string")
        return

    if (not isinstance(attendees, list) or
            not all(isinstance(item, dict) for item in attendees)):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    for index, attendee in enumerate(attendees, start=1):
        template_schema = template_content
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = "{" + f"{key}" + "}"
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
        if not os.path.exists(f"output_{index}.txt"):
            with open(f"output_{index}.txt", "w") as file:
                file.write(template_schema)
        else:
            print("ERROR: file already exists")
            
            
if __name__ == "__name__":
    attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    with open('template.txt', 'r') as f:
        template_content = f.read()

    generate_invitations(template_content, attendees)
