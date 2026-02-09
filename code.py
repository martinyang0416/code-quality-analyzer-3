import sys

while True:
    try:
        input().strip()  # Read the input line, ignore its content
        print("NO", flush=True)
    except EOFError:
        break