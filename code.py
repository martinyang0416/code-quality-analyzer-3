def main():
    import sys
    title = sys.stdin.readline().strip()
    title_upper = title.upper()
    
    # Define the groups based on traditional phone keypad layout
    groups = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    
    # Create a mapping from each character to its corresponding number
    mapping = {char: key for key, value in groups.items() for char in va