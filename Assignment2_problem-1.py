my_dict = {}
print(my_dict)
my_dict[1] = 1
print(my_dict)
my_dict['1'] = 2
print(my_dict)
my_dict[1.0] = 4
print(my_dict)
my_dict["1"] = 5
print(my_dict)

sum =0
for k in my_dict:
    sum =  sum+my_dict[k]

print(sum)
