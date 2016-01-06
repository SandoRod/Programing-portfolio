# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c

def ratio(f1, f2):
	if f1 > f2:
		return f1 / f2
	else:
		return f2 / f1

def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainder(40, 19): ", remainder(40, 19)
	print "test remainder(126, 19): ", remainder(126, 19)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "testing ratio(7.7, 2.8): ", ratio(7.7, 2.8)
	print "testing ratio(2.8, 7.7): ", ratio(2.8, 7.7)
	print "testing pythagoras(3, 4): ", pythagoras(3, 4)
	print "testing pythagoras(28, 32): ", pythagoras(28, 32) 


def reverse(jimmy):
	return not jimmy
	
def band(bool1, bool2):
	return bool1 and bool2

def bor(bool1, bool2):
	return bool1 or bool2

def xsame(bool1, bool2):
	return bool1 == bool2

def xor(bool1, bool2):
	return bool1 != bool2
	


def main_boolean():
	print "testing reverse(True): ", reverse(True)
	print "testing reverse(False): ", reverse(False)
	print "testing band(True, True): ", band(True, True)
	print "testing band(True, False): ", band(True, False)
	print "testing band(False, True): ", band(False, True)
	print "testing band(False, False): ", band(False, False)
	print "testing bor(True, True): ", bor(True, True)
	print "testing bor(True, False): ", bor(True, False)
	print "testing bor(False, True): ", bor(False, True)
	print "testing bor(False, False): ", bor(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xsame(True, False): ", xsame(True, False)
	print "test xsame(False, True): ", xsame(False, True)
	print "test xor(True, True): ", xor(True, True)
	print "test xor(False, False): ", xor(False, False)
	print "test xor(True, False): ", xor(True, False)
	print "test xor(False, True): ", xor(False, True)
	
def positive(n):
	return n > 0
		
def bigger(x, y):
	return x > y

def no_diff(d, b):
	return d == b
	
def not_same(w, h):
	return w != h

def less_than(alvey, you):
	return alvey < you
	
def at_least_13(d):
	return d >= 13
	
def at_most_13(d):
	return d <= 13

def main_boolean_numbers():
	print "testing positive(-29): ", positive(-29)
	print "testing positive(29): ", positive(29)
	print "test bigger(3, 2): ", bigger(3, 2)
	print "test bigger(7, 14): ", bigger(7, 14)
	print "testing no_diff(45, 82): ", no_diff(45, 82)
	print "testing no_diff(77, 77): ", no_diff(77, 77)
	print "test not_same(45, 82): ", not_same(45, 82)
	print "test not_same(77, 77): ", not_same(77, 77)
	print "testing less_than(37, 12): ", less_than(37, 12)
	print "testing less_than(10, 100): ", less_than(10, 100)
	print "test at_least_13(13): ", at_least_13(13)
	print "test at_least_13(11): ", at_least_13(11)
	print "test at_least_13(56): ", at_least_13(56)
	print "test at_most_13(13): ", at_most_13(13)
	print "test at_most_13(11): ", at_most_13(11)
	print "test at_most_13(56): ", at_most_13(56)
	

def biggest(a, b):
	if a > b:
		return a
	else:
		return b

def smallest(y, z):
	if y < z:
		return y
	else:
		return z

def letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"

def food_tax(subtotal, grocery):
	if grocery: # 3 percent
		return subtotal * .03
	else:
		return subtotal * .0725
		
def same(l, m, c):
	return l == m and m == c

def big3(lebron, irvin, love):
	if lebron >= irvin and lebron >= love:
		return lebron
	elif irvin >= lebron and irvin >= love:
		return irvin
	else:
		return love

def small_sum(a, b, c):
	if a < c and b < c:
		return a + b
	elif b < a and c < a:
		return b + c
	else:
		return a + c

def meat_loaf(ketchup, eggs, meat):
	if ketchup and eggs and not meat:
		return True
	elif ketchup and meat and not eggs:
		return True
	elif eggs and meat and not ketchup:
		return True
	else:
		return False

def big3reorder(a, b, c):
	if a == big3(a, b, c):
		return a, biggest(b, c), smallest(b, c)
	elif b == big3(a, b, c):
		return b, biggest(a, c), smallest(a, c)
	else:
		return c, biggest(a, b), smallest(a, b)
	
def positive_multiple(z, y):
	product = z * y
	if positive(product):
		return product
	else:
		return -product

def main_conditionals():
	print "test out biggest(21, 3): ", biggest(21, 3)
	print "test out biggest(5, 19): ", biggest(5, 19)
	print "test out biggest(35, 35): ", biggest(35, 35)
	print "test out smallest(21, 3): ", smallest(21, 3)
	print "test out smallest(5, 19): ", smallest(5, 19)
	print "test out smallest(35, 35): ", smallest(35, 35)
	print "testing letter_grade(92): ", letter_grade(92)
	print "testing letter_grade(85): ", letter_grade(85)
	print "testing letter_grade(70): ", letter_grade(70)
	print "testing letter_grade(63): ", letter_grade(63)
	print "testing letter_grade(28): ", letter_grade(28)
	print "test food_tax(12.43, True): ", food_tax(12.43, True)
	print "test food_tax(12.43, False): ", food_tax(12.43, False)
	print "testing same(7, 7, 7): ", same(7, 7, 7)
	print "testing same(7, 2, 8): ", same(7, 2, 8)
	print "testing big3(3, 2, 1): ", big3(3, 2, 1)
	print "testing big3(2, 3, 1): ", big3(2, 3, 1)
	print "testing big3(1, 2, 3): ", big3(1, 2, 3)
	print "testing big3(1, 1, 2): ", big3(1, 1, 2)
	print "testing big3(2, 2, 1): ", big3(2, 2, 1)
	print "testing big3(2, 1, 1): ", big3(2, 1, 1)
	print "testing small_sum(3, 2, 1): ", small_sum(3, 2, 1)
	print "testing small_sum(2, 3, 1): ", small_sum(2, 3, 1)
	print "testing small_sum(1, 2, 3): ", small_sum(1, 2, 3)
	print "testing small_sum(1, 1, 2): ", small_sum(1, 1, 2)
	print "testing small_sum(2, 2, 1): ", small_sum(2, 2, 1)
	print "testing small_sum(2, 1, 1): ", small_sum(2, 1, 1)
	print "testing meat_loaf(True, True, True): ", meat_loaf(True, True, True)
	print "testing meat_loaf(True, True, False): ", meat_loaf(True, True, False)
	print "testing meat_loaf(True, False, False): ", meat_loaf(True, False, False)
	print "testing meat_loaf(False, False, False): ", meat_loaf(False, False, False)
	print "test positive_multiple(5, 7): ", positive_multiple(5, 7)
	print "test positive_multiple(-5, -7): ", positive_multiple(-5, -7)
	print "test positive_multiple(-5, 7): ", positive_multiple(-5, 7)
	
def total(x):
	t = 0
	for num in range(x):
		t += num
	return t

def total_slice(g, p):
	t = 0
	for num in range(g, p):
		t += num
	return t

def total_slice2(a, b):
	t = 0
	for num in range(smallest(a, b), biggest(a, b)):
		t += num
	return t

def total_odds(s, k):
	t = 0
	if s % 2 == 0: # test if s is even
		s = s+1
	for num in range(s, k, 2):
		t += num
	return t
	
def total_evens(s, k):
	t = 0
	if s % 2 == 1: # test if s is odd
		s = s+1
	for num in range(s, k, 2):
		t += num
	return t

def total_7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 == 0:
			t += num
	return t

def total_non7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 != 0:
			t += num
	return t
	
def squares(n):
	total = 0
	for num in range(n):
		total += num*num
	return total
	
	

def main_counted_loops():
	print "testing total(3): ", total(4)
	print "testing total(21): ", total(21)
	print "testing total_slice(5, 8): ", total_slice(5, 8)
	print "testing total_slice2(5, 8): ", total_slice2(5, 8)
	print "testing total_slice2(8, 5): ", total_slice2(8, 5)
	print "testing total_odds(2, 10): ", total_odds(2, 10) # 3+5+7+9
	print "testing total_odds(1, 6): ", total_odds(1, 6) # 1+3+5
	print "testing total_evens(2, 10): ", total_evens(2, 10) # 2+4+6+8
	print "testing total_evens(1, 6): ", total_evens(1, 6) # 2+4
	print "testing total_7s(1, 22): ", total_7s(1, 22) # 7+14+21
	print "testing total_non7s(1, 10): ", total_non7s(1,10) # 1+2+3+4+5+6+8+9
	print "testing squares(5): ", squares(5) # 0+1+4+9+16 


def hello():
	return "hello"
	
def nothing():
	return ""

def second_letter(s):
	return s[1]

def one_letter(s, n):
	return s[n]

def concatenate(garfield, tom):
	return garfield + tom

def beauty(word):
	return word + " beauty"
	
def slice_of_life(life):
	return life[2:5]
	
def slice_of_heaven(str, num):
	return str[num: num+4]
	
def slice_of_perfection(str, n1, n2):
	return str[n1: n1+n2]
	
def length(str):
	return len(str)

def main_strings():
	print "testing hello(): ", hello()
	print "testing nothing(): ", nothing()
	print "testing second_letter('bob'): ", second_letter('bob')  # o
	print "testing one_letter('no games', 6): ", one_letter("no games", 6)  # e
	print "testing concatenate('orange ', 'blue'): ", concatenate('orange', 'blue')
	print "testing beauty('thats a'): ", beauty('thats a')
	print "testing slice_of_life('elephant'): ", slice_of_life('elephant')
	print "testing slice_of_heaven('abcdefgh', 2): ", slice_of_heaven('abcdefgh', 2)
	print "testing slice_of_perfection('Attack of the Deranged', 3, 8): ", slice_of_perfection('Attack of the Deranged', 3, 8)
	print "testing length('Kelton'): ", length("Kelton")

def short_list():
	return [1, 2, 3]
	
def hollow():
	return []

def third_value(a):
	return a[2]
	
def one_value(z, n):
	return z[n]
	
def add_lists(b, s):
	return b + s

def pie(z):
	#return z + [314]
	z.append(314)
	return z

def grow_one(r, n):
	r.append(n)
	return r

def sub_list(k):
	return k[2: 6]
	
	
def main_lists():
	print "testing short_list(): ", short_list()
	print "testing hollow(): ", hollow()
	a = [17, 38, 96, 79, 63, 74, 12, 24, 19, 6]
	b = [5, 21, 78, 42, 63, 84]
	print "test third_value(b): ", third_value(b)
	print "test one_value(b, 5): ", one_value(b, 5)
	print "test add_lists(a, b): ", add_lists(a, b)
	print "test pie(a): ", pie(a)
	print "test grow_one(b, 36): ", grow_one(b, 36)
	print "test sub_list(a): ", sub_list(a)
	
	
	
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	main_boolean_numbers()
	main_conditionals()
	main_counted_loops()
	main_strings()
	main_lists()
	
main()