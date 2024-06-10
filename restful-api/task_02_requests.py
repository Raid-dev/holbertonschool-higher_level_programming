#!/bin/python3
def fetch_and_print_posts():
    import requests

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        for post in data:
            title = post['title']
            print(title)
    else:
        print('Failed to fetch data:', response.status_code)


def fetch_and_save_posts():
    import csv
    import requests

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        csv_file = "posts.csv"
        with open(csv_file, "w", newline="") as file:
            fieldnames = ['id', 'title', 'body']

            with open(csv_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for post in data:
                    id = post['id']
                    title = post['title']
                    body = post['body']
                    writer.writerow({'id': id, 'title': title, 'body': body})

            print("CSV file created successfully.")
    else:
        print('Failed to fetch data:', response.status_code)
