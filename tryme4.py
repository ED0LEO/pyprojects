def new_line():
    print('.')

def three_lines():
    print("three_lines");
    new_line()
    new_line()
    new_line()

def nine_lines():
    print("nine_lines");
    three_lines()
    three_lines()
    three_lines()

# using available functions to print 25 lines (9 + 9 + 3 + 3 + 1)
def clear_screen():
    print("clear_screen (25 lines)");
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

nine_lines()
clear_screen()
