def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def greet(name):
    return "Hello, {name}!".format(name=('my love' if name == 'Johnny' else name))


def greet(n): return "Hello, {}!".format(n.replace("Johnny", "my love"))


def greet(name):
    return "Hello, {}!".format((name, "my love")[name == "Johnny"])


def greet(name): return "Hello, " + \
    ("my love" if name == "Johnny" else name) + "!"


def greet(name):
    return f"Hello, {'my love' if name == 'Johnny' else name}!"
