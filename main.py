import random
user_id = []
password = []

start_loop = True

while start_loop:
	get_ldap = input("user ldap = ".upper())
	if get_ldap not in user_id:
		if get_ldap.isalpha() == get_ldap.isnumeric():
			user_id.append(get_ldap)
			print(f"user_id create {get_ldap}")
			while True:
				var_otp = "dammala you OTP is " + str(random.randint(1111, 9999)) + " "
				store_otp = int(var_otp[-5:-1])
				print(f"{get_ldap} you OTP is {store_otp}")
				passwd = input("Enter the password = ")
				if len(passwd) >= 8:
					user_otp = int(input("Enter you OTP = "))
					if store_otp == user_otp:
						password.append(passwd)
						print(f"account create, {get_ldap}")
						break
						get_status = input(f"{get_ldap} Do you want to continue still Yes/No = ")
						if get_status.lower() == "no":
							start_loop = False
							print("We say sorry to missing you".upper())
					else:
						print("Invalid OTP")
				else:
					print("password policy one letter and one number is missing".upper())
		else:
			print(f"user_id should have condination of letter and number {get_ldap}")
			get_status = input(f"{get_ldap} Do you want to continue still Yes/No = ")
			if get_status.lower() == "no":
				start_loop = False
				print("We say sorry to missing you".upper())
	else:
		print(f"{user_id} already taken, Try with newone")

print(user_id)
print(password)


