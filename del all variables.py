for variable in list(globals().keys()):
    print(variable)
    if variable != "__name__":
        del globals()[variable]
