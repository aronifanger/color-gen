from random import randint as rnd

def color_dec(color):
	v = [color[1:3],color[3:5],color[5:7]]
	return([int(v[0],16),int(v[1],16),int(v[2],16)])

def dec_color(v):
	return("#%02X%02X%02X"%(v[0],v[1],v[2]))


#	    |a  b  c | -> v1
#	M = |d* e  f | -> v2
#	    |g  h* i*| -> v3

# We need to find d*, h*, i* where <v1,v2>=0 (1), 
# <v3,v2>=0 (2) and <v1,v3>=0 (3)
# From (1): d = (be+cf)/a
# From (2) and (3): ...

def gen_color(color):
	v = color_dec(color)

	# a != 0

	a = v[0]
	b = v[1]
	c = v[2]

	# Test values to e, f and g
	e = rnd(0,255)
	f = rnd(0,255)
	g = rnd(0,255)
	while(e*c == f*b):
		e = rnd(0,255)
		f = rnd(0,255)

	# From (1)
	d = (be+cf)/a

	detM = (e*c) - (f*b)
	invM = [[e/detM, -f/detM], [-b/detM, c/detM]]
	eq = [-(b*e+c*f)*g/a, a*g]

	h = invM[0][0] * eq[0] + invM[0][1] * eq[1]
	i = invM[1][0] * eq[0] + invM[1][1] * eq[1]

	len2 = 
	len3

	