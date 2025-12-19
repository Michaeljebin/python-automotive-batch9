students = [
    "Rahul Sharma", "Amit Verma", "Rahul Singh", "Sneha Patel",
    "Amit Kumar", "Priya Mehta", "Rohit Sharma", "Neha Singh",
    "Priya Shah", "Karan Malhotra", "Neha Gupta", "Vikas Jain",
    "Rohit Verma", "Ankit Yadav", "Sneha Iyer", "Karan Singh",
    "Vikas Patel", "Ankit Sharma", "Amit Shah", "Rahul Verma"
]

name_dict = {}

for full_name in students:
    first, last = full_name.split()
    if first not in name_dict:
        name_dict[first] = []
    name_dict[first].append(last)

for first_name in name_dict:
    print(first_name, len(name_dict[first_name]))

for first_name in name_dict:
    if len(name_dict[first_name]) > 1:
        print("There are %d students having first name %s" % (len(name_dict[first_name]), first_name))