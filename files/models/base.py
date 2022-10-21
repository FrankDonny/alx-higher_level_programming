#!/usr/bin/python3
"""The base module in the model package"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the instance variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts python strings to json strings"""
        if len(list_dictionaries) == 0:
            return "[]"
        for i in list_dictionaries:
            if isinstance(i, dict):
                return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """converts json strings to python strings"""
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saving json strings to a json file"""
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as theFile:
            if list_objs is None:
                theFile.write("[]")
            else:
                j_file = [x.to_dictionary() for x in list_objs]
                theFile.write(Base.to_json_string(j_file))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        _dummy = cls(1, 1)
        _dummy.update(**dictionary)
        return _dummy

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializing of list of objects to csv file"""

        filename = "{}.csv".format(cls.__name__)
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = []
                for attr in attrs:
                    if attr not in d:
                        continue
                    t.append(str(d.get(attr)))
                f.write(",".join(t))
                f.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """de-serializing of deserializing of csv file"""
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs
