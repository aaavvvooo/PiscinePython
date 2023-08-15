def all_thing_is_obj(object: any) -> int:
    string = type(object).__name__.capitalize()
    if string == "Str":
        print(f"{object} is in the kitchen")
    elif string == "Int":
        print("Type not found")
    else:
        print(string + ": " + str(type(object)))
    return 42
