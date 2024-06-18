import json

person = {
    'name': 'Kamil',
    'age': 36,
    'male': True,
    'languages': ('Python', 'Java', 'C++'),
    'blog_post': [
        {'title': 'Programoanie jest super', 'views': 1378},
        {'title': 'Java czy Python', 'views': 4319}
    ],
    'warnings': None
}


json_string = json.dumps(person, indent=4)
print(json_string)


with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
