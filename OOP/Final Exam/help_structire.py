@staticmethod
def find_obj(value, attribute, collection):
    for obj in collection:
        if getattr(obj, attribute) == value:
            return obj
    return None
