def id_name():
    user_id = []
    Ldap = input("enter the user_name = ")
    if len(Ldap) >= 8:
        user_id.append(Ldap)
    else:
        print("user id must contain 8 letters")
    
    return user_id

print(id_name())
