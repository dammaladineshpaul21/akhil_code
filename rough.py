import re

get_val = "Asadf2344@"
if len(get_val) >= 8 and len(re.findall('[^a-zA-Z0-9]', get_val))>=1: 
	print("Yes", len(re.findall("[a-z]", get_val)) >= 1 and len(re.findall("[A-Z]", get_val)) >= 1 and len(re.findall("[0-9]", get_val)) >= 1)
else:
	print("NO")