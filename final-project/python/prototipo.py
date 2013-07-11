from pyplasm import *

from pyplasm import *
import scipy
from scipy import *


def VERTEXTRUDE((V,coords)):
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])

#Initial parameters
up = CUBOID([7.1,0.1,1.5])
down = T([2])([-3])(up)
panel = T([1,2])([2,-1])(CUBOID([0.1,1,1.5]))
shelf_h0 = T([2])([-0.75])(CUBOID([2,0.1,1.5]))
k = 5
Dom1D = INTERVALS(1)(10)
Dom2D= GRID([10,10])
Inverted_Dom2D = MAP([S2,S1])(GRID([10,10]))
D1 = INTERVALS(1)(40);
D2 = INTERVALS(PI/2)(40);
rot_domain = PROD([D1,D2]);

#Function that draw the library's book spaces

def BOOK_SPACES(panel,n):
	shelf_h1 = T([1,2])([2,-1])(CUBOID([5.1,0.1,1.5]))
	level_1 = STRUCT([shelf_h1,panel])
	for i in range(k+1):
		level_1 = STRUCT([level_1,T([1])([i])(panel)])
	return level_1


#Function that draw the library's lateral shelfs 

def LATERAL_SHELFS(shelf_h0,n):
	closing = T([2])([-0.75])(CUBOID([0.1,0.75,1.5]))
	level_2 = STRUCT([shelf_h0,closing])
	for g in xrange(0,4):
		level_2 = STRUCT([level_2,T([2])([g*(-0.75)])(STRUCT([shelf_h0,closing]))])
	return level_2


library = COLOR([0.9608,0.8706,0.7020])(STRUCT([up,down,LATERAL_SHELFS(shelf_h0,k),BOOK_SPACES(panel,k),
							T([2])([-1])(BOOK_SPACES(panel,k)),T([2])([-2])(BOOK_SPACES(panel,k))]))


#Junction for the library's legs

p1 = [[0.6667,0,0.6667],[0.66,0,1.85/3],[0.593333,0,1.85/3],[0.6,0,0.6667]]
c1 = BEZIER(S1)(p1)
mapp1 = ROTATIONALSURFACE(c1)
s1 = MAP(mapp1)(rot_domain)


p2 = [[0.6667,0,0.6667],[0.66,0,2.15/3],[0.593333,0,2.15/3],[0.6,0,0.6667]]
c2 = BEZIER(S1)(p2)
mapp2 = ROTATIONALSURFACE(c2)
s2 = MAP(mapp2)(rot_domain)

junction_1 = STRUCT([s1,s2])


#Supporting sticks

p3 = [[0.6667,-0.5,0.6667],[0.66,-0.5,1.85/3],[0.593333,-0.5,1.85/3],[0.6,-0.5,0.6667]]
c3 = BEZIER(S1)(p3)

p4 = [[0.6667,-0.5,0.6667],[0.66,-0.5,2.15/3],[0.593333,-0.5,2.15/3],[0.6,-0.5,0.6667]]
c4 = BEZIER(S1)(p4)

s13 = BEZIER(S2)([c1,c3])
surf13 = MAP(s13)(Dom2D)

s24 = BEZIER(S2)([c2,c4])
surf24 = MAP(s24)(Dom2D)

stick = STRUCT([surf13,surf24])

junction_2_r1 = R([2,3])(-PI)(junction_1)
junction_2_r2 = R([1,3])(PI/2)(junction_2_r1)
junction_2 = T([1,2,3])([-0.03,-0.5,0.035])(junction_2_r2)

stick_2_r = R([2,3])(PI/2)(stick)
stick_2 = T([2,3])([-0.47,0.1])(stick_2_r)

#Library's legs

leg_1 = STRUCT([stick,junction_2,stick_2])

junction_3 = T([3])([-1.84])(junction_1)
leg_2_r = R([1,3])(-PI)(leg_1)
leg_2 = T([1,3])([1.26,-0.5])(leg_2_r)

leg_dx_str = STRUCT([junction_1,leg_1,junction_3,leg_2])
leg_sx_r = R([1,3])(-PI)(leg_dx_str)

leg_sx_t = T([1,2,3])([1,-3.7,1.05])(leg_sx_r)
leg_dx_t = T([1,2,3])([6.1,-3.7,1.50])(leg_dx_str)

leg_sx = T([2])([-1.5])(S([2,3])([0.5,0.5])(leg_sx_t))
leg_dx = T([2])([-1.5])(S([2,3])([0.5,0.5])(leg_dx_t))

legs = STRUCT([leg_sx,leg_dx])

VIEW(STRUCT([library, legs]))