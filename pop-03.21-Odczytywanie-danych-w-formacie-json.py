import json

# text ="""[
#     {
#         "title": "Nauka Pythona w godzinę",
#         "author": "Kamil Brzeziński",
#         "tags": [
#             "python",
#             "programming",
#             "automation"
#         ],
#         "likes": 7
#     },
#     {
#         "title": "Java czy Python",
#         "author": "Mariusz",
#         "tags": [
#             "python",
#             "programming",
#             "java"
#         ],
#         "likes": 9,
#         "visible": true,
#         "second_author": null
#     }
# ]"""
#
# entries = json.loads(text)
# print(entries[1]['title'])
# print(entries[1]['tags'])
# print(entries[1]['tags'][2])
# print(entries[0]['likes'])

with open('entries.json') as json_file:
    entries = json.load(json_file)

    print(entries[1]['title'])
    print(entries[1]['tags'])
    print(entries[1]['tags'][2])
    print(entries[0]['likes'])
