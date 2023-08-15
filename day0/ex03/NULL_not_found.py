def NULL_not_found(object: any) -> int:

    if isinstance(object, type(None)):
        print("Nothing: None <class 'NoneType'>")
    elif object != object:
        print("Cheese: nan <class 'float'>")
    elif type(object) is int and object == 0:
        print("Zero: 0 <class 'int'>")
    elif isinstance(object, str) and object == "":
        print("Empty: <class 'str'>")
    elif type(object) is bool and object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
        return 1

    return 0
