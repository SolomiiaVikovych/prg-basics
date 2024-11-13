def f(detector):
    count = 0  # Track current people in the room
    max_count = 0  # Track the maximum number of people in the room

    for sign in detector:
        if sign == '+':
            count += 1
            max_count = max(max_count, count)
        elif sign == '-':
            count -= 1

    return max_count >= 3