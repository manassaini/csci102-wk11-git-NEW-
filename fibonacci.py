# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        a=0
        b=1
        while b <= 89:
            print(b)
            a, b = b, a+b

        ''' 
        implement Fibonacci sequence to calculate the 
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''

    return fibs

def main():
    print('OUTPUT', fib())

#if __name__ == "__main__":
   # main()
