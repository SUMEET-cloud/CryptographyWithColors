import threading


def fx1():
    print("A Starts")
    for i in range(1000):
        print("A", end=" ")
    print("A Ends")


def fx2():
    print("b Starts")
    for i in range(1000):
        print("B", end=" ")
    print("b Ends")


def main():
    t1 = threading.Thread(target=fx1)
    t2 = threading.Thread(target=fx2)
    t1.start()
    t2.start()


main()
