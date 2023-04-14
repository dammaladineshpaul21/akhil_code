# # start = True

# # while start:
# # 	print("Akhile")
# # 	ver_user = input("Do you wnat ot cont = ")
# # 	if ver_user.lower() == "no":
# # 		start = False

# # user_name = "Dammala4091"
# # Id_password = "Dammala1245"

# # count = 0

# # for i in range(round(len(user_name)/2)):
# # 	print(i)
# # 	# if i in Id_password:
# # 	# 	count = count+1

# import random

# user_name = []
# Id_password = []


# i = True
# while i:
# 	Ldap = input("enter username = ")
# 	if len(Ldap) >= 8:
# 		if Ldap.isalpha() == Ldap.isnumeric():
# 			if Ldap not in user_name:
# 				user_name.append(Ldap)
# 				random_number = random.randint(1000,9999)
# 				print(f"{Ldap} your OTP is {random_number}")
# 				j = True
# 				while j:
# 					pswd = input("enter password = ")
# 					if len(pswd) >= 8:  
# 						if pswd.isalpha() == pswd.isnumeric():
# 							Ldap_OTP = int(input(f"enter the {Ldap} OTP = "))
# 							if random_number == Ldap_OTP:
# 								Id_password.append(pswd)
# 							# 	j = False
# 							# 	count = 0
# 							# 	for i in range(len(set(user_name))):
# 							# 		if list(set(user_name))[i] in Id_password:
# 							# 			count = count + 1
# 							# 	if count < len(set(user_name)):
# 							# 	else:
# 							# 		print("password should not match with half of username letters")
# 							# 		get_user_status = input("Do you want to contiue still (yes/no) = ")
# 							# 		if get_user_status.lower() == "no":
# 							# 			i = False
# 							else:
# 								print("Invalid OTP")

# 						else:
# 							print("password contain atleast one letter and number")
# 					else:
# 						print("password should be greater than 8 letters along with atleast one letter and number")
# 			else:
# 				print("username is already exist")
# 		else:
# 			print("username contain atleast one letter and number")
# 	else:
# 		print("username should be greater than 8 letters along with atleast one letter and number")



# my_room = {}

# for i in range(len(user_name)):
#     my_room[user_name[i]] = Id_password[i]

# print(my_room)





A = ["haven", "more", "cute", "some", "one"]
B = ["more", "some", "one", "by", "given"]
C = ["some", "motive", "more", "by", "haven", "one"]

A.extend(B)
A.extend(C)

print(A)