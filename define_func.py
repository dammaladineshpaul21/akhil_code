def id_name():
    user_id = []
    Ldap = input("enter the user_name = ")
    if len(Ldap) >= 8:
        user_id.append(Ldap)
    else:
        print("user id must contain 8 letters")
    
    return user_id

print(id_name())


def alpnum():
    user_id = []
    Ldap = input("enter the user_id = ")
    if Ldap.isalpha() == Ldap.isnumeric():
        user_id.append(Ldap)
    else:
        print("user id must contain alpha and numeric")
    return user_id

print(alpnum())


def duplicate():
    user_id = []
    Ldap = input("enter user_id = ")
    if Ldap not in user_id:
        user_id.append(Ldap)
    else:
        print("user id already exist")
        
    return user_id

print(duplicate())
