import random
import re

user_id = []
password = []

start_loop = True

"""Account_Creation User Sitting"""

while start_loop:
	get_ldap = input("user ldap = ".upper())
	# Check whather the ID is existing or not in the list if not Added the user
	if get_ldap not in user_id:   
		if get_ldap.isalpha() == get_ldap.isnumeric():
			user_id.append(get_ldap)
			print(f"user_id create {get_ldap}")
			# Ask the user for OTP and Password to get set the Account
			while True:
				store_otp = random.randint(1111, 9999)
				print(f"{get_ldap} you OTP is {store_otp}")
				passwd = input("Enter the password = ")
				# Check the condition of the password policy one letter, number, Special Chareate
				if len(passwd) >= 8 and len(re.findall("[a-z]", passwd)) >= 1 and \
				len(re.findall("[A-Z]", passwd)) >= 1 and len(re.findall("[0-9]", passwd)) >= 1 and \
				len(re.findall("[^[a-zA-Z0-9]", passwd)) >= 1:
					user_otp = int(input("Enter you OTP = "))
					# Check the run_time OTP and user_input OTP for verification.
					if store_otp == user_otp:
						password.append(passwd)
						print(f"account create, {get_ldap}")
						new_get_status = input("New_User Do you want to continue still Yes/No = ")
						if new_get_status.lower() == "no":
							start_loop = False
							user_account_dict = dict(zip(user_id, password))
                            print(user_account_dict)
							break
					else:
						print("Invalid OTP")
				else:
					print("password policy one letter, number, Special Chareate".upper())
					get_status = input(f"{get_ldap} Do you want to continue still Yes/No = ")
					if get_status.lower() == "no":
						start_loop = False
							print("We say sorry to missing you".upper())
		else:
			print(f"user_id should have condination of letter and number {get_ldap}")
			get_status = input(f"{get_ldap} Do you want to continue still Yes/No = ")
			if get_status.lower() == "no":
				start_loop = False
				print("We say sorry to missing you".upper())
	else:
		print(f"{user_id} already taken, Try with newone")


