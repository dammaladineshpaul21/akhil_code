# import re

# get_val = "Asadf2344@"
# if len(get_val) >= 8 and len(re.findall('[^a-zA-Z0-9]', get_val))>=1: 
# 	print("Yes", len(re.findall("[a-z]", get_val)) >= 1 and len(re.findall("[A-Z]", get_val)) >= 1 and len(re.findall("[0-9]", get_val)) >= 1)
# else:
# 	print("NO")

# def check_user_pass(user_id, password):
# 	count = 0
# 	for i in user_id:
# 		if i in password:
# 			count = count+1
# 	# return count
# 	if len(user_id)/2 <= count:
# 		return False
# 	else:
# 		return True


# print(check_user_pass("Dammala4019", "adchd345"))

def custom_append(lst, item):
    """
    This function takes a list and an item as input and adds the item to the end of the list.
    """
    lst[len(lst):] = [item]


 my_list = [1, 2]
 custom_append(my_list, 3)
 print(my_list)