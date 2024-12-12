#example:     python3 cmd.py --physics 60 --chemistry 70 --maths 90
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--Physics", help ="Physics Total Marks")
    parser.add_argument("--Chemistry", help="Chemistry Total Marks")
    parser.add_argument("--Maths", help = "Maths Total Marks")
    
    args= parser.parse_args()

    print(args.Physics)
    print(args.Chemistry)
    print(args.Maths)
    p = int(args.Physics)
    c = int(args.Chemistry)
    M = int(args.Maths)
    average = (p+c+M)/300
    percentage = average*100
    print(f"The Average result of Your Semester is {percentage}:%",format(percentage))
