import timeit
import matplotlib.pyplot as plt
import numpy as np

fibSeq = {}

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def fib(n):
    if n in fibSeq:
        return fibSeq[n]
    elif n == 0 or n == 1:
        fibSeq[0] = 0
        fibSeq[1] = 1
    else:
        fibSeq[n] = fib(n-1)+fib(n-2)
    return fibSeq[n]

def main():
    funcTimes = [0 for i in range(0,35)]
    fibTimes = [0 for i in range(0,35)]
    for i in range(0,35):
        sTime = timeit.default_timer()
        func(i)
        funcTimes[i] = timeit.default_timer() - sTime
        sTime = timeit.default_timer()
        fib(i)
        fibTimes[i] = timeit.default_timer() - sTime
        fibSeq.clear()
    
    plt.plot(funcTimes, label = "func")
    plt.plot(fibTimes, label = "fib")
    plt.ylabel("Time")
    plt.xlabel("Numbers Generated")
    plt.legend()
    plt.show()
    print("Done")


if __name__ == "__main__":
    main()