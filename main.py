import os, sys  # E401 multiple imports, F401 unused


def main():
    x = 5  # F841 unused variable
    if None == None:  # E711 comparison to None
        print(f"Hello from repo!")  # F541 f-string without placeholders


if __name__ == "__main__":
    main()
