import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="First number")
    parser.add_argument("--number2", help="Second number")
    parser.add_argument("--Operation", help="Operation you want to execute", \
                        choices = ["add","subtract","multiply"])
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.Operation)
    
    n1 = int(args.number1)
    n2 = int(args.number2)
    operation = args.Operation
    result = None
    if operation == "add":
        result = n1 + n2
    elif operation == "subtract":
        result = n1-n2

    elif operation == "multiply":
        result = n1 * n2
  

    print("THe result is ",result)
