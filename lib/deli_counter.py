katz_deli = []

def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        line_is = []
        for n in range(len(katz_deli)):
            line_is.append(f"{n+1}. {katz_deli[n]}")
        string_line_is = " ".join(line_is)
        # print(line_is)
        print("The line is currently: " + f"{string_line_is}")
        # print(len(katz_deli))

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
    pass

def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
    pass