import json
class Base:
    """
    This is the Base class.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation of list_objs to a file """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ that returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy