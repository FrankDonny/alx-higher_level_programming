#!/usr/bin/python3
"""The base module in the model package"""
import json
import csv


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
        if len(list_dictionaries) == 0:
            return "[]"
        for i in list_dictionaries:
            if isinstance(i, dict):
                return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
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
        try:
            with open(f"{cls.__name__}.json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as csvFile:
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']
            csv_write = csv.DictWriter(csvFile, fieldnames=field_names)
            for line in list_objs:
                csv_write.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as csvFile:
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']
            csv_read = csv.DictReader(csvFile, fieldnames=field_names)
            csv_read = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
            return [cls.create(**d) for d in list_dicts]
