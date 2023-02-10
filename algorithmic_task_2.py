"""
    Write a function that takes an object and a string, which represents an object lookup
    path, for example "property1.property2".
    The function should return the value on the specific path.
    Take care of error handling.

    Example:
    function lookup(obj, path){....}
    object = { property1: { property2: "Apple", property3: 'Orange' } }
    path = ”'property1.property2'”
    lookup(object, path)) Result: 'Apple'
"""


def lookup(obj, path):
    properties = path.split(".", 1)

    if len(properties) == 1:
        return obj[properties[0]]
    try:
        return lookup(obj[properties[0]], properties[1])
    except KeyError:
        print("You've entered a bad path. :p")


if __name__ == "__main__":
    example_obj = {
        "property1": {
            "property2": "Apple",
            "property3": "orange"
        }
    }
    path = "property1.property2"

    print(lookup(example_obj, path))
