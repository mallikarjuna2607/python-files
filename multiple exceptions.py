try:
    a=int(input())
    b=int(input())
    result=a/b
    print(result)


except ValueError:
      print("invalid input")

except ZeroDivisionError:
      print("cannot divide by zero")
