def to_string(*args, **dopargs):
    return dopargs.get("sep", " ").join([str(i) for i in args]) + dopargs.get("end", "\n")
