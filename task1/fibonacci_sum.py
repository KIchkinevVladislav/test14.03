def sum_fib(n=7000000):
    fib1, fib2 = 3, 4
    sum = 4

    while True:
        
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 > n:
            break
        if fib2 % 2 == 0:
            sum += fib2 
    print(sum)   

if __name__ == '__main__':
    sum_fib()