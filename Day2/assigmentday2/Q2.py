def write_numbers_to_file(filename):
    try:
        with open(filename, 'w') as file:
            for numbers in range(1,101):
                file.write(f"{numbers} \n")

        print("numbers 1-100 written to file")
    except FileNotFoundError:
        print("File not found. Try again")
    except PermissionError:
        print("Permission denied. Try again")
    except Exception as e:
        print(f"unexpected error:{e}")

def read_numbers_from_file(filename):
    try:
        with open(filename,"r") as file:
            content=file.read()
            print("content of the file \n")
            print(content)
    except FileNotFoundError:
        print("File not found. Try again")
    except PermissionError:
        print("Permission denied. Try again")
    except Exception as e:
        print(f"unexpected error:{e}")

if __name__ == "__main__":
    filename='test.txt'
    write_numbers_to_file(filename)
    read_numbers_from_file(filename)