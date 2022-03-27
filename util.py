def str_to_arr(string):
	string = string.upper().split(",")
	string = [i.strip() for i in string]
	return string
