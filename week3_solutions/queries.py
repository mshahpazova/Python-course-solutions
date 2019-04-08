# queries.py

def filter(file_path, **kwargs):
    all_entries = []
    f = open(file_path, "r")
    lines = f.readlines()


    csv_keys = lines[0].split(',')

    filter_functions = { 'order_by': lambda entry, value : True }
    for key in csv_keys:
        filter_functions[key] = lambda entry, value : entry[key] == value
        filter_functions[key + '__contains'] = lambda entry, value : value in entry[key]
        filter_functions[key + '__starts_with'] = lambda entry, value : entry[key][0:len(value)] == value
        filter_functions[key + '__gt'] = lambda entry, value : entry[key] > value
        filter_functions[key + '__lt'] = lambda entry, value : entry[key] < value


    for line in lines:
        entry = {}
        for i, value in enumerate(line.split(',')):
            entry[csv_keys[i-1]] = value
        all_entries.append(entry)

    filtered_entries = filter(lambda entry : all(filter_functions[key](entry, value) for key, value in kwargs), all_entries)

    if 'order_by' in kwargs:
        ordered_entries = sorted(filtered_entries, key=lambda entry : entry[kwargs['order_by']])
        return ordered_entries
    else:
        return filtered_entries
    
def count(file_path, **kwargs):
    return len(list(filter(file_path, kwargs)))

def first(file_path, **kwargs):
    return list(filter(file_path, kwargs))[0]

def last(file_path, **kwargs):
    return list(filter(file_path, kwargs))[-1]
    

print(filter('example_data.csv', full_name="Diana Harris"))
