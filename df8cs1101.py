def read_file(filename):
    try:
        fd = open(filename, 'r')
        ret = fd.readline().strip()
        while len(ret) > 0:
            print(ret)
            ret = fd.readline().strip()
        fd.close()
    except:
        print("read_file: An error has occurred.")

file = "test.txt"
read_file(file)


def write_msg(filename, msg):
    try:
        fd = open(filename, 'w')
        fd.write(msg)
        fd.close()
    except:
        print("write_msg: An error has occurred.")

file = "test.txt"
print("Before writing a new message into the file:")
read_file(file)
write_msg(file, "new message")
print("After writing a new message into the file:")
read_file(file)


import os

def print_type(file):
    try:
        if os.path.exists(file):
            print("%s exists" % file)
        else:
            print("%s does not exists" % file)
        if os.path.isdir(file):
            print("%s is a directory" % file)
        else:
            print("%s is not a directory" % file)
        if os.path.isfile(file):
            print("%s is a file" % file)
        else:
            print("%s is not a file" % file)
    except:
        print("print_type: An error has occurred.")

file = "test.txt"
print_type(file)
