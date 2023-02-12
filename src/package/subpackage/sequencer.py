def n_zeroes():
    """Prompts user to specify number of zeroes to apply to file suffixes.
    Returns an integer."""
    while True:
        try:
            num0s = abs(int(input("""Files will be suffixed with the specified number of digits. 
E.g., enter \"3\" to produce filenames ending from 001 to 999.
Enter number of digits: """)))
            return num0s
        except ValueError:
            print("Please enter an integer.")

def n_start(num0s):
    """Prompts user to specify starting number for file suffixes.
    Returns an integer, with 1 by default."""
    print(f"By default, the sequence will begin at {str(1).zfill(num0s)}.")
    num = input("Specify a starting number >= 0, or enter any other key to continue: ")
    try:
        return int(num)
    except ValueError:
        return 1
