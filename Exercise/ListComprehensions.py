integer = [1,2,3,4,5]
binary = ["1","10","11","100","110"]
int_bin = list(zip(integer,binary))
print("List making through zip function")
print(int_bin)
int_bin_dict = {country:city for country,city in zip(integer,binary)}
print("Dictinary:")
print(int_bin_dict)
