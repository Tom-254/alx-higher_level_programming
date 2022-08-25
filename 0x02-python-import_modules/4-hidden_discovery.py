#!/usr/bin/python3
import hidden_4

def main():
    names = dir(hidden_4)
    for i in range(0, len(names)):
        name = names[i]
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
