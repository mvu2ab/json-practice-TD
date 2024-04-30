import json

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'a') as csv_file:

    for repo in data[:5]:
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']

        csv_line = f'{name},{html_url},{updated_at},{visibility}\n'

        csv_file.write(csv_line)
