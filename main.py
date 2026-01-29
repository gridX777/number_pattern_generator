def number_pattern(n):
    # Validation: must be integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Validation: must be greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."

    result = ""

    # Required for loop
    for i in range(1, n + 1):
        result += str(i) + " "

    # Remove trailing space
    return result.strip()
