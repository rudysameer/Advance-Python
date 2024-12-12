a = int(input("enter the number a :"))
b = int(input("enter the number b :"))

try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("zero division exceotion")
    c = None

except Exception as e:
    print("Error detected ",type(e).__name__)
    c = None
print(c)