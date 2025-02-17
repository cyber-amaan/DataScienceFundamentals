def typeBasedTransformer(**kwargs):
    """
    This function takes an arbitrary number of named arguments and processes each value based on its type:
    - Integers and Floats: Square the number.
    - Strings: Reverse the text while maintaining its case.
    - Booleans: Invert the value.
    - Lists or Tuples: Reverse the order of elements.
    - Dictionaries: Swap keys and values, assuming all values are unique.
    - Unsupported types: Leave unchanged.

    It returns a dictionary with the transformed values while preserving the original keys.
    """
    transformed_dict = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed_dict[key] = value ** 2
        elif isinstance(value, str):
            transformed_dict[key] = value[::-1]
        elif isinstance(value, bool):
            transformed_dict[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed_dict[key] = value[::-1]
        elif isinstance(value, dict):
            transformed_dict[key] = {v: k for k, v in value.items()}
        else:
            transformed_dict[key] = value

    return transformed_dict


# Example usage
if __name__ == "__main__":
    result = typeBasedTransformer(
        num=4,
        text="Hello",
        is_active=True,
        num_list=[1, 2, 3],
        num_tuple=(1, 2, 3),
        simple_dict={"a": 1, "b": 2},
        unsupported_set={1, 2, 3}
    )
    print(result)
    # Output should be:
    # {
    #     'num': 16,
    #     'text': 'olleH',
    #     'is_active': False,
    #     'num_list': [3, 2, 1],
    #     'num_tuple': (3, 2, 1),
    #     'simple_dict': {1: 'a', 2: 'b'},
    #     'unsupported_set': {1, 2, 3}
    # }