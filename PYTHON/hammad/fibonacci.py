def fibonacciSeries(a):
    try:
        if(a<=1):
            return a
        else:
            return(fibonacciSeries(a-1)+fibonacciSeries(a-2))
    except:
        return "Enter Interger Number"

# def fib(a):
#     if(a<=1):
#         return a
#     else:
#         return(fib(a-1)+fib(a-2))


# def getNum():
#     try:
#         n=int(input("Enter number"))
#         if n>0:
#             return n
#         else:
#             return 0
#     except:
#         return 0
# print(fib(getNum()))

