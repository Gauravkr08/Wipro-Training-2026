class mydescriptor:
    def __get__(self, obj, owner):
        print("Getting Value")
        return obj._x

    def __set__(self, obj, value):
        print("Setting the Value")
        obj._x = value


class Test:
    x = mydescriptor


t = Test()
t.x = 10
print(t.x)


def write_numbers_to_file(filename):
    numbers = []

    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(f"{i}\n")
                numbers.append(i)

    except FileNotFoundError:
        print("Error: The specified file path was not found.")

    except PermissionError:
        print("Error: Permission denied. You do not have access to write this file.")

    except OSError as error:
        print(f"Unexpected OS error occurred: {error}")

    return numbers


def write_numbers_to_file(filename):
    numbers = []

    try:
        with open(filename, "w") as file:
            for num in range(1, 101):
                file.write(str(num) + "\n")
                numbers.append(num)

    except FileNotFoundError:
        print("Error: File path not found.")

    except PermissionError:
        print("Error: Permission denied while writing the file.")

    except OSError as err:
        print(f"OS error occurred: {err}")

    return numbers