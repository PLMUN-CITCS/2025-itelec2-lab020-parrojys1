"""Checks if integer inputted by user is even or odd."""
def get_integer_input():
    """Prompts user for the integer"""
    inputx = int(input("Enter a integer: "))
    return inputx

def check_even_odd(inputy):
    """Checks if integer is odd or even"""
    if inputy % 2 == 0:
        string = f"{inputy} is an Even number."
    else:
        string = f"{inputy} is an Odd number."
    return string

if __name__ == "__main__":
    number = get_integer_input()
    RESULT = check_even_odd(number)
    print(RESULT)
