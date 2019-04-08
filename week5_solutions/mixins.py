import json
import xml.etree.ElementTree as ET
class Xmlable:
    def to_xml(self):
        root_name = self.__class__.__name__
        name = self.__class__.__name__
        # print(name)
        root_el = ET.Element(name)
        print("root elenme", root_el)
        for key, value in self.__dict__.items():
            el =  ET.SubElement(root_el, key)
            el.text = value
        return ET.dump(root_el)

class Jsonable:
    def to_json(self, indent=4):
        new_dict = {}
        new_dict['dict'] = self.__dict__
        new_dict['type'] = self.__class__.__name__
        data = json.dumps(new_dict, indent=indent)
        return data

        #print(json.loads(data))
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        # TODO pass key values positional arguments
        vals = list(data['dict'].values())
        ls = data['dict'].values()
        print(*ls)
        obj = cls(*ls)
        return obj

class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

maria = Panda("Maria")
print(maria.to_xml())


my_hash = { 'songs': [] }
for song in self.songs_list:
    my_hash['songs'].append(song.__dict__)

