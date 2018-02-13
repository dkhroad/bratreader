import simplejson as json

def _to_json(python_object) :
    if isinstance(python_object, tuple) :
        python_object = {'__class__': 'tuple',
                         '__value__': list(python_object)}
    else :
        raise TypeError(repr(python_object) + ' is not JSON serializable') 

    return python_object


def _from_json(json_object):                                   
    if '__class__' in json_object:
        if json_object['__class__'] == 'tuple':
            return tuple(json_object['__value__'])
    return json_object

def load_ner_json(pathtofile):
    with open(pathtofile,"r") as f:
          return json.load(f,object_hook=_from_json)


