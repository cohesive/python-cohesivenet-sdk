import string
import random

random.seed(None)

# Generate Openapi values
#
#   OpenAPIv3 datatypes:
#       number
#       integer
#       boolean
#       array
#       object
# https://swagger.io/docs/specification/data-models/data-types/


def random_int(minimum=1, maximum=100):
    """Generate a random int"""
    return random.randint(minimum, maximum)


def random_string(minLength=10, maxLength=15):
    """Generate a random string of fixed length """
    length = random_int(minLength, maxLength)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_from_list(options=[]):
    return random.choice(options)


def generate_api_var(var_schema):
    api_type = var_schema["type"]
    if api_type == "string":
        enums = var_schema.get("enum")
        if enums:
            return random_from_list(options=enums)
        kwargs = {} # map string constrains
        # TODO: add format options
        return random_string(**kwargs)
    elif api_type == "integer":
        # TODO map string constrains
        return random_int()
    elif api_type == "boolean":
        return True
    raise RuntimeError("Unsupport type for generation %s" % str(api_type))
