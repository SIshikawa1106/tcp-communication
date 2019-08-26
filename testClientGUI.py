import Tkinter as tk
from collections import OrderedDict

class Frame(tk.LabelFrame, object):
    def __init__(self, name, button_funcs, master=None):
        super(Frame, self).__init__(master, text=name)

        for (button_name, button_func) in button_funcs.items():
            bt = tk.Button(self, text=button_name, command=button_func)
            bt.pack(fill="x")

class CommandFactory(object):
    def __init__(self):
        pass

    def set_command(self):
        pass

    def make(self):
        pass



def test_func1():
    print("test1")

def test_func2():
    print("test2")

def test_func3():
    print("test3")

def test_func4():
    print("test4")

def test_func5():
    print("test5")

def test_func6():
    print("test6")

def test_func7():
    print("test7")

if __name__ == '__main__':
    root = tk.Tk()

    buttons_1 = OrderedDict()
    buttons_1["TEST1_1"] = test_func1
    buttons_1["TEST1_2"] = test_func2
    buttons_1["TEST1_3"] = test_func3

    buttons_2 = OrderedDict()
    buttons_2["TEST2_1"] = test_func4
    buttons_2["TEST2_2"] = test_func5
    buttons_2["TEST2_3"] = test_func6

    buttons_3 = OrderedDict()
    buttons_3["TEST3_1"] = test_func7


    frame1 = Frame("frame1", buttons_1, root)

    frame2 = Frame("frame2", buttons_2, root)

    frame3 = Frame("frame3", buttons_3, root)

    frame1.pack(fill=tk.BOTH)
    frame2.pack(fill=tk.BOTH)
    frame3.pack(fill=tk.BOTH)
    root.mainloop()

    """
    "regist sim"
    "regist real"
    "clear"
    "plan"
    "check pos"
    "next check"
    "plan"
    """


