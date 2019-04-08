# coding_skills.py
from functools import reduce
from operator import itemgetter
import json

def names_of_skills(skills):
    return list(map(lambda skill: skill['name'], skills))

def knows(language):
    return lambda person: language in names_of_skills(person['skills'])

def unite_arrays(arrays):
    return list(reduce(lambda arr1, arr2: arr1 + arr2, arrays))

def get_level_at(language):
    print()
    return lambda person: list(filter(lambda x: x['name'] == language, person['skills']))[0]['level']

def best_person_at(language, people):
    return max(
        list(filter(knows(language), people)),
        key=get_level_at(language)
    )

def read_file(file_path):
    read_file = open(file_path, "r")
    
    people = json.loads(read_file.read())['people']
    
    skills_of_all_people = list(map(lambda person : person['skills'], people))
    
    all_languages = list(set(names_of_skills(unite_arrays(skills_of_all_people))))
    
    result = list(map(
      lambda language: best_person_at(language, people),
      all_languages
    ))
    
    for i, person in enumerate(result):
        print(all_languages[i], end='')
        print(' - ', end='')
        print(person['first_name'], end='')
        print(' ', end='')
        print(person['last_name'])

read_file("coding_skills_data.json")

# [{'first_name': 'Ivo', 
# 'skills': [{'name': 'C++', 'level': 30}, {'name': 'PHP', 'level': 25}, {'name': 'Python', 'level': 80}, {'name': 'C#', 'level': 25}], 'last_name': 'Ivo'}, {'first_name': 'Rado', 'skills': [{'name': 'C++', 'level': 20}, {'name': 'PHP', 'level': 37}, {'name': 'Haskell', 'level': 70}, {'name': 'Java', 'level': 50}, {'name': 'C#', 'level': 10}, {'name': 'JavaScript', 'level': 60}], 'last_name': 'Rado'}, {'first_name': 'Rosi', 'skills': [{'name': 'JavaScript', 'level': 62}, {'name': 'Python', 'level': 66}, {'name': 'Ruby', 'level': 35}], 'last_name': 'Rosi'}, {'first_name': 'Pavli', 'skills': [{'name': 'Python', 'level': 77}, {'name': 'CSS', 'level': 99}, {'name': 'JavaScript', 'level': 33}, {'name': 'C#', 'level': 70}], 'last_name': 'Pavli'}, {'first_name': 'Cherna', 'skills': [{'name': 'C++', 'level': 99}, {'name': 'C', 'level': 99}], 'last_name': 'Ninja'}]
