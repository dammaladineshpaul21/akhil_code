# Create User_Account
# ITs should not add duliplicate
# User id should Alpha numeric
# Pass and user id should be len should be grater than 8
# final out should be equal to the number of user in a list and smae lenght of password in Dict combination
# ______________________________________________________________________________________________________________

# After two user input's it should as the new user to contiue or to exit (Done)
# Generate the OPT once user is created and ask the same after the passowrd entry(Done)
# Update the while loop infinity time (Done)
# Add a loop for password till it matche's and then after it should go to password list (Done)

import random

user_name = []
Id_password = []

i = True
while i:
	Ldap = input("enter username = ")
	if len(Ldap) >= 8:
		if Ldap.isalpha() == Ldap.isnumeric():
			if Ldap not in user_name:
				user_name.append(Ldap)
				random_number = random.randint(1000,9999)
				print(f"{Ldap} your OTP is {random_number}")
				
				while True:
					pswd = input("enter password = ")
					if len(pswd) >= 8:  
						if pswd.isalpha() == pswd.isnumeric():
							Ldap_OTP = int(input(f"enter the {Ldap} OTP = "))
							if random_number == Ldap_OTP:
								count = 0
								for i in range(len(set(Ldap))):
									if list(set(Ldap))[i] in pswd:
										count = count + 1
								if count < len(set(Ldap)):
									Id_password.append(pswd)
									run_loop_again = input("New_User you want to contiue still (yes/no) = ")
									if run_loop_again.lower() == "no":
										i = False
										break
									break
								else:
									print("password should not match with half of username letters")
									get_user_status = input(f"{Ldap} you want to contiue still (yes/no) = ")
									if get_user_status.lower() == "no":
										break
									print(f"{count} are same as in {Ldap}")
							else:
								print("Invalid OTP")
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
