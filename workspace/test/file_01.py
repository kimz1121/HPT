import file_00
from file_00 import data

def test_assign_val_01():
    global data
    data = 44432

def test_01():
    print(data)

if __name__ == "__main__":
    test_assign_val_01()
    file_00.test_assign_val_00()
    # from file_00 import data
    test_01()
