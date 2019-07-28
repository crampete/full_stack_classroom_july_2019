old_dictionary = {
    'course': 'full stack',
    'backend': 'python',
    'frontend': 'react',
    'database': 'mongo'
}

new_dictionary_interchanged = {}

for key, value in old_dictionary.items():
    new_dictionary_interchanged[value] = key

print(new_dictionary_interchanged)