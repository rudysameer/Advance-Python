set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# diffrence between set1 and set2 is {1,2,3}
difference = set1-set2
difference2 = set2-set1
intersection = set1&set2
union = set1|set2
print("only in set1 is ",difference)
print("only in set2 is ",difference2)
print("Number common in both sets",intersection)
print("NUmbers in over all set",union)