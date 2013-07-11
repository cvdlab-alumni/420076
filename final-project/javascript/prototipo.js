//Initial parameters
var up = CUBOID([7.1,0.1,1.5])
var down = T([1])([-3])(up)
var panel = T([0,1])([2,-1])(CUBOID([0.1,1,1.5]))
var shelf_h0 = T([1])([-0.75])(CUBOID([2,0.1,1.5]))
var k = 5
var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);
var rot_domain = DOMAIN([[0,1],[0,PI/2]])([40,40]);

//Function that draw the library's book spaces

function BOOK_SPACES(panel,n){
	var shelf_h1 = T([0,1])([2,-1])(CUBOID([5.1,0.1,1.5]))
	var level_1 = STRUCT([shelf_h1,panel])
	for (var i = k ; i >= 0; i--) {
		level_1 = STRUCT([level_1,T([0])([i])(panel)])
	};
	return level_1
}

//Function that draw the library's lateral shelfs 

function LATERAL_SHELFS(shelf_h0,n){
	var closing = T([1])([-0.75])(CUBOID([0.1,0.75,1.5]))
	var level_2 = STRUCT([shelf_h0,closing])
	for (var g = k-2 ; g >= 0; g--) {
		level_2 = STRUCT([level_2,T([1])([g*(-0.75)])(STRUCT([shelf_h0,closing]))])
	};
	return level_2
}

var library = COLOR([245/255,222/255,179/255])(STRUCT([up,down,LATERAL_SHELFS(shelf_h0,k),BOOK_SPACES(panel,k),
							T([1])([-1])(BOOK_SPACES(panel,k)),T([1])([-2])(BOOK_SPACES(panel,k))]))


//Junction for the library's legs

var p1 = [[2/3,0,2/3],[1.98/3,0,1.85/3],[1.78/3,0,1.85/3],[1.8/3,0,2/3]]
var c1 = BEZIER(S0)(p1)
var mapp1 = ROTATIONAL_SURFACE(c1)
var s1 = MAP(mapp1)(rot_domain)


var p2 = [[2/3,0,2/3],[1.98/3,0,2.15/3],[1.78/3,0,2.15/3],[1.8/3,0,2/3]]
var c2 = BEZIER(S0)(p2)
var mapp2 = ROTATIONAL_SURFACE(c2)
var s2 = MAP(mapp2)(rot_domain)

var junction_1 = STRUCT([s1,s2])


//Supporting sticks

var p3 = [[2/3,-0.5,2/3],[1.98/3,-0.5,1.85/3],[1.78/3,-0.5,1.85/3],[1.8/3,-0.5,2/3]]
var c3 = BEZIER(S0)(p3)

var p4 = [[2/3,-0.5,2/3],[1.98/3,-0.5,2.15/3],[1.78/3,-0.5,2.15/3],[1.8/3,-0.5,2/3]]
var c4 = BEZIER(S0)(p4)

var s13 = BEZIER(S1)([c1,c3])
var surf13 = MAP(s13)(Dom2D)

var s24 = BEZIER(S1)([c2,c4])
var surf24 = MAP(s24)(Dom2D)

var stick = STRUCT([surf13,surf24])

var junction_2_r1 = R([1,2])([PI])(junction_1)
var junction_2_r2 = R([0,2])([-PI/2])(junction_2_r1)
var junction_2 = T([0,1,2])([-0.03,-0.5,0.035])(junction_2_r2)

var stick_2_r = R([1,2])([PI/2])(stick)
var stick_2 = T([1,2])([-0.47,0.1])(stick_2_r)

//Library's legs

var leg_1 = STRUCT([stick,junction_2,stick_2])

var junction_3 = T([2])([-1.84])(junction_1)
var leg_2_r = R([0,2])([PI])(leg_1)
var leg_2 = T([0,2])([1.26,-0.5])(leg_2_r)

var leg_dx_str = STRUCT([junction_1,leg_1,junction_3,leg_2])
var leg_sx_r = R([0,2])([PI])(leg_dx_str)

var leg_sx_t = T([0,1,2])([1,-3.7,1.05])(leg_sx_r)
var leg_dx_t = T([0,1,2])([6.1,-3.7,1.50])(leg_dx_str)

var leg_sx = T([1])([-1.5])(S([1,2])([0.5,0.5])(leg_sx_t))
var leg_dx = T([1])([-1.5])(S([1,2])([0.5,0.5])(leg_dx_t))

var legs = STRUCT([leg_sx,leg_dx])

DRAW(STRUCT([library, legs]))