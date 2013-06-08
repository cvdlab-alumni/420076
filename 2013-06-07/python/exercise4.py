from pyplasm import *
import random






mtrx = []


def RNDM (x,y):
	f = (COS(x)+SIN(y))*random.random()
	m = [x,y,f]
	mtrx.append(m)
	return f 


dom1 = INTERVALS(20)(60)
dom2 = INTERVALS(40)(60)
domain = PROD([dom1,dom2])

def mountain (v):
	a = v[0]
	b = v[1]
	return [a, b, RNDM(a,b)]


model = MAP(mountain)(domain)
mountains = COLOR([0.6,0.4,0.2])(model)


lake = COLOR([0,0.58,0.71])(CUBOID([4,5,1]))

lake1 = T([1,2,3])([1,8.5,-1])(lake)
lake2 = T([1,2,3])([7.3,27,-1])(lake)


def tree (r,h,d):
	dmn = PROD([INTERVALS(1)(d),INTERVALS(2*PI)(d)])
	select_foliage = 10
	p0 = [[0,0,0],[h,0,0]]
	c0 = BEZIER(S1)(p0)
	p1 = [[h,0,0],[0,0,2*h]]
	c1 = BEZIER(S1)(p1)
	map0 = ROTATIONALSURFACE(c0)
	s0 = MAP(map0)(dmn)
	map1 = ROTATIONALSURFACE(c1)
	s1 = MAP(map1)(dmn)
	foliage1 = COLOR([0.09,0.447,0.27])(STRUCT([s0,s1]))
	foliage2 = COLOR([0,0.5,0.5])(STRUCT([s0,s1]))
	foliage = foliage1
	if(select_foliage*random.random()>=5):
		foliage = foliage1
	if (select_foliage*random.random()<5):
		foliage = foliage2
	trunk = COLOR([0.396,0.26,0.13])(CYLINDER([r,h])(30))
	return STRUCT([T([3])([h/2])(foliage),trunk])



def find_lake (point,n):
	t0 = tree(0.05,0.15,10)
 	p0 = mtrx[point]
 	tree_number = n
 	x = p0[0]
 	y = p0[1]
 	z = p0[2]
 	forest = T([1,2,3])([x,y,z])(t0)
 	k = point
 	h = point+100+tree_number
	if ((x<=1 or x>=5)and(y<=8.5 or y>=13.5)):
		for i in range(0,tree_number):
			t0 = tree(0.05,0.15,10)
			k = k+1
			v = mtrx[k]
			x = v[0]
			y = v[1]
			z = v[2]
			forest = STRUCT([forest,T([1,2,3])([x,y,z])(t0)])
	if ((x<=7.3 or x>=11.3)and(y<=27 or y>=32)):
		for i in range(0,tree_number): 
			t0 = tree(0.05,0.15,10)
			h = h+1
			v = mtrx[h]
			x = v[0]
			y = v[1]
			z = v[2]
			forest = STRUCT([forest,T([1,2,3])([x,y,z])(t0)])
	return forest



def FOREST (point,n):
	check = find_lake(point,n)
 	check2 = STRUCT([check,find_lake(point+100+n,n)])
 	check3 = STRUCT([check2,find_lake(point+100+n,n)])
	return check3


f = FOREST(2000,25)

#ES4 DRAW SOME HUMAN SETTLEMENTS MODEL

def  chalet (r_x,r_y):
	x = random.random()*0.15
	y = random.random()*0.15
	z = random.random()*0.15
	return T([1,2,3])([r_x,r_y,0])(CUBOID([x,y,z]))


def SETTLEMENTS (r_x,r_y):
	settlement = chalet(0,0)
	for i in range(0, r_x):
		for j in range(0,r_y):	
			settlement = STRUCT([settlement,chalet(i,j)])		
	return settlement


basement = COLOR([0.8,0.52,0.247])(T([3])([-0.5])(CUBOID([2,2,0.5])))
s1 = SETTLEMENTS(1,1)
s2 = SETTLEMENTS(1,1)
stl1 = T([1,2])([8,19.5])(STRUCT([basement,T([1,2])([1,1])(s1)]))
stl2 = T([1,2])([5.2,3])(STRUCT([basement,T([1,2])([1,1])(s2)]))


VIEW(STRUCT([lake1,lake2,mountains,f,stl1,stl2]))