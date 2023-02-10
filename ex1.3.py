fibSeq = {}

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
    fib(100)
    print(fibSeq)

if __name__ == "__main__":
    main()