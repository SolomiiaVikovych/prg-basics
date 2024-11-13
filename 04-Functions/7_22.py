def f(name):
    name.split()
    acronym_name = [word[0].upper for word in name]
    return ''.join(acronym_name)