def enough(cap, on, wait):
    if cap-on>=wait:
        return 0
    return wait+on-cap

