def calculate_roots(a, b, c):
	discriminant = (b**2) - (4*a*c)
	x1 = (-b + (discriminant**0.5)) / (2*a)
	x2 = (-b - (discriminant**0.5)) / (2*a)
	print(