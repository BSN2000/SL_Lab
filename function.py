def print_text():
	print("Hello World!")
	return


print_text()


def print_values(a,b):
	print("The values of a and b are",a,"and",b)
	return


print_values(10,20)


def print_text(a,b=5):
	print("The values of a and b are",a,"and",b)
	return


print_text(10)

def print_values(a,b):
	print("The values of a and b are",a,"and",b)
	return

print_values(b=20,a=10)
