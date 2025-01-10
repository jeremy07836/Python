from recipe_options import recipes_dict


def copy_dict(d: dict) -> dict:
    """
    Copy a dictionary, create a copy of `list` or `dict` values
    :param d: The dictionary to copy
    :return: A copy of `d`, and not a reference to it
    """
    temp = {}
    for key, value in d.items():
        temp_value = value.copy()
        temp[key] = temp_value
    return temp


old_dict = recipes_dict
new_dict = copy_dict(old_dict)
# new_dict["Butter chicken"]["ginger"] = 300
print(id(old_dict), old_dict)
print(id(new_dict), new_dict)
