## Will there be enough space?

def enough(cap, on, wait):
    # Your code here
    if cap-on-wait >= 0:
        return 0
    else:
        return -(cap-on-wait)