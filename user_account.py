# Create User_Account
# ITs should not add duliplicate
# User id should Alpha numeric
# Pass and user id should be len should be grater than 8
# final out should be equal to the number of user in a list and smae lenght of password in Dict combination
# ______________________________________________________________________________________________________________

# After two user input's it should as the new user to contiue or to exit

user_name = []
Id_password = []

for i in (range(3)):
	Ldap = input("enter username = ")
	if len(Ldap) >= 8:
		if Ldap.isalpha() == Ldap.isnumeric():
			if Ldap not in user_name:
				user_name.append(Ldap)
				pswd = input("enter password = ")
				if len(pswd) >= 8:  
					if pswd.isalpha() == pswd.isnumeric(): 
						Id_password.append(pswd)
					else:
						print("password contain atleast one letter and number")
				else:
					print("password should be greater than 8 letters along with atleast one letter and number")
			else:
				print("username is already exist")
		else:
			print("username contain atleast one letter and number")
	else:
		print("username should be greater than 8 letters along with atleast one letter and number")


my_room = {}

for i in range(len(user_name)):
    my_room[user_name[i]] = Id_password[i]

print(my_room)