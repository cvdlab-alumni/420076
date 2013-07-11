//function tha draw a circle
var circle = function(r){
return function(v){
return [r*COS(v[0]),r*SIN(v[0])];
};
};

//function that draw a close cylinder
function CYLINDER(r,h){
var domain1 = DOMAIN([[0,2*PI], [0,r]])([36,1]);
var mapping = function(v){
var a = v[0];
var r = v[1];
return [r*COS(a), r*SIN(a)];
};
var base = MAP(mapping)(domain1);

var domain2 = DOMAIN([[-2*PI,2*PI]])([70]);
var crc = circle(r);
var model = MAP(crc)(domain2);
var cil = EXTRUDE([h])(model);

var cylinder = STRUCT([base,cil,T([2])([h])(base)]);
return cylinder;
};


//Domains
var Dom1D = INTERVALS(1)(20);
var Dom2D = DOMAIN([[0,1], [0,1]])([20,20]);
var rot_domain = DOMAIN([[0,1],[0,PI/2]])([40,40]);

//BACK SUPPORT

var p1 = [[2,0,2],[1.98,0,1.85],[1.78,0,1.85],[1.8,0,2]]
var c1 = BEZIER(S0)(p1)
var mapp1 = ROTATIONAL_SURFACE(c1)
var s1 = MAP(mapp1)(rot_domain)


var p2 = [[2,0,2],[1.98,0,2.15],[1.78,0,2.15],[1.8,0,2]]
var c2 = BEZIER(S0)(p2)
var mapp2 = ROTATIONAL_SURFACE(c2)
var s2 = MAP(mapp2)(rot_domain)


var sx_back_support = STRUCT([s1,s2])
var dx_back_support = R([0,1])([PI/2])(sx_back_support)

//ARMRESTS

var p3 = [[2,-1,2],[1.98,-1,1.85],[1.78,-1,1.85],[1.8,-1,2]]
var c3 = BEZIER(S0)(p3)

var p4 = [[2,-1,2],[1.98,-1,2.15],[1.78,-1,2.15],[1.8,-1,2]]
var c4 = BEZIER(S0)(p4)

var s13 = BEZIER(S1)([c1,c3])
var surf13 = MAP(s13)(Dom2D)

var s24 = BEZIER(S1)([c2,c4])
var surf24 = MAP(s24)(Dom2D)

var sx_armrest = STRUCT([surf13,surf24])
var dx_arst = R([0,1])([PI])(sx_armrest)
var dx_armrest = T([1])([-1])(dx_arst)

//SUPERIOR FRAME

var superior_frame = STRUCT([sx_back_support,dx_back_support,sx_armrest,dx_armrest])

//FRONT TOP JUNCTIONS

var p5 = [[2,-1.15,2],[2,-1,1.8],[1.8,-1,1.8],[1.8,-1.15,2]]
var c5 = BEZIER(S0)(p5)

var p6 = [[2,-1.15,2],[2,-1.3,2.1],[1.8,-1.3,2.1],[1.8,-1.15,2]]
var c6 = BEZIER(S0)(p6)


var p7 = [[2.02,-1.15,1.8],[2,-1,1.8],[1.8,-1,1.8],[1.78,-1.15,1.8]]
var c7 = BEZIER(S0)(p7)

var p8 = [[2.02,-1.15,1.8],[2,-1.3,1.8],[1.8,-1.3,1.8],[1.78,-1.15,1.8]]
var c8 = BEZIER(S0)(p8)

var s37 = BEZIER(S1)([c3,c5,c7])
var surf37 = MAP(s37)(Dom2D)

var s48 = BEZIER(S1)([c4,c6,c8])
var surf48 = MAP(s48)(Dom2D)

var front_top_sx_junction = STRUCT([surf37,surf48])
var front_top_dx_junction = T([0])([-3.8])(front_top_sx_junction)

var front_top_junctions = STRUCT([front_top_sx_junction,front_top_dx_junction])

//VERTICAL FRONT SUPPORTS

var p9 = [[2.02,-1.15,-3.2],[2,-1,-3.2],[1.8,-1,-3.2],[1.78,-1.15,-3.2]]
var c9 = BEZIER(S0)(p9)

var p10 = [[2.02,-1.15,-3.2],[2,-1.3,-3.2],[1.8,-1.3,-3.2],[1.78,-1.15,-3.2]]
var c10 = BEZIER(S0)(p10)

var s79 = BEZIER(S1)([c7,c9])
var surf79 = MAP(s79)(Dom2D)

var s810 = BEZIER(S1)([c8,c10])
var surf810 = MAP(s810)(Dom2D)

var sx_front_vertical_support = STRUCT([surf79,surf810])
var dx_front_vertical_support = T([0])([-3.8])(sx_front_vertical_support)
var cfs = R([0,1])([-PI/2])(sx_armrest)
var central_front_support1 = T([0,1,2])([-0.9,0.75,-2])(cfs)
var central_front_support2 = T([0])([1])(central_front_support1)
var central_front_support3 = T([0])([1])(central_front_support2)
var central_front_support4 = T([0])([0.85])(central_front_support3)

var central_front_support = T([2])([0.15])(STRUCT([central_front_support1,central_front_support2,central_front_support3,central_front_support4]))

var front_vertical_supports = STRUCT([sx_front_vertical_support,dx_front_vertical_support,central_front_support])

//FRONT BOTTOM JUNCTIONS

var fbsj = R([1,2])([PI/2])(front_top_sx_junction)
var front_bottom_sx_junction = T([1,2])([0.85,-2.2])(fbsj)
var front_bottom_dx_junction = T([0])([-3.8])(front_bottom_sx_junction)

var front_bottom_junctions = STRUCT([front_bottom_sx_junction,front_bottom_dx_junction])

//FOOTS

var sx_foot1 = T([2])([-5.35])(sx_armrest)
var dx_foot1 = T([2])([-5.35])(dx_armrest)
var sx_foot2 = T([1])([1])(sx_foot1)
var dx_foot2 = T([1])([1])(dx_foot1)
var sx_foot3 = T([1])([1])(sx_foot2)
var dx_foot3 = T([1])([1])(dx_foot2)
var sx_foot4 = T([1])([1])(sx_foot3)
var dx_foot4 = T([1])([1])(dx_foot3)
var foots = STRUCT([sx_foot1,dx_foot1,sx_foot2,dx_foot2,sx_foot3,dx_foot3,sx_foot4,dx_foot4])

//BACK BOTTOM JUNCTIONS

var bbsj = R([1,2])([PI/2])(front_bottom_sx_junction)
var back_bottom_sx_junction = T([1,2])([-0.25,-2.2])(bbsj)
var back_bottom_dx_junction = T([0])([-3.8])(back_bottom_sx_junction)
var back_bottom_junctions = STRUCT([back_bottom_sx_junction,back_bottom_dx_junction])

//BACK TOP JUNCTIONS
var btsj = R([0,1])([-PI/2])(bbsj)
var back_top_sx_junction_rotated = R([1,2])([PI])(btsj)
var back_top_dx_junction_rotated = R([0,2])([PI])(btsj)
var back_top_sx_junction = T([0,1,2])([-2.2,-0.24,-1.15])(back_top_sx_junction_rotated)
var back_top_dx_junction = T([0,1,2])([2.2,3.55,-1.15])(back_top_dx_junction_rotated)

var back_top_junctions = STRUCT([back_top_sx_junction,back_top_dx_junction])

//VERTICAL BACK SUPPORT

var central_back_support_traslated = T([0,1])([-0.1,2.8])(STRUCT([central_front_support2,central_front_support3]))
var central_back_support_rotated = R([1,2])([PI/8])(STRUCT([back_top_junctions,central_back_support_traslated]))

var central_back_support = T([1,2])([0.15,-0.5])(central_back_support_rotated)

var sbs = COLOR([0.8235,0.8235,0.8235])(CYLINDER(0.095,3.6))
var sbs_r = R([1,2])([PI/8])(sbs)
var sbs_r2 = R([0,2])([-PI/13])(sbs_r)
var sx_back_support = T([0,1,2])([1.93,3.1,-3.22])(sbs_r2)
var rbs_r = R([0,2])([PI/13])(sbs_r)
var rx_back_support = T([0,1,2])([-1.92,3.1,-3.2])(rbs_r)

var vertical_back_support = STRUCT([central_back_support,sx_back_support,rx_back_support])

//SEANCE

var seance1 = COLOR([150/255,75/255,0])(T([0,1,2])([-1.8,-1.2,0.1])(CUBOID([3.6,1.7,0.2])))

var p11 = [[0,0,0],[0,1.9,0],[3.6,1.9,0],[3.6,0,0]]
var c11 = BEZIER(S0)(p11)

var p12 = [[0,0,0.2],[0,1.9,0.2],[3.6,1.9,0.2],[3.6,0,0.2]]
var c12 = BEZIER(S0)(p12)

var p13 = [[0,0,0],[0,0,0],[3.6,0,0],[3.6,0,0]]
var c13 = BEZIER(S0)(p13)

var p14 = [[0,0,0.2],[0,0,0.2],[3.6,0,0.2],[3.6,0,0.2]]
var c14 = BEZIER(S0)(p14)

var s1112 = BEZIER(S1)([c11,c12])
var surf1112 = MAP(s1112)(Dom2D)
var s2 = COLOR([150/255,75/255,0])(surf1112)

var s1113 = BEZIER(S1)([c11,c13])
var surf1113 = MAP(s1113)(Dom2D)
var s3 = COLOR([150/255,75/255,0])(surf1113)

var s1214 = BEZIER(S1)([c12,c14])
var surf1214 = MAP(s1214)(Dom2D)
var s4 = COLOR([150/255,75/255,0])(surf1214)


var seance2 = T([0,1,2])([-1.8,0.5,0.1])(STRUCT([s2,s3,s4]))

var seance = T([2])([0.14])(STRUCT([seance1,seance2]))

//BACKREST

var p15 = [[-0.1,0,0],[0,1,0],[1.5,1,0],[1.6,0,0]]
var c15 = BEZIER(S0)(p15)

var p16 = [[-0.2,0,0],[-0.2,1.2,0],[1.6,1.2,0],[1.7,0,0]]
var c16 = BEZIER(S0)(p16)

var p17 = [[-0.1,0,-1],[0,1,-1],[1.5,1,-1],[1.6,0,-1]]
var c17 = BEZIER(S0)(p17)

var p18 = [[-0.2,0,-1],[-0.2,1.2,-1],[1.6,1.2,-1],[1.7,0,-1]]
var c18 = BEZIER(S0)(p18)

var s1516 = BEZIER(S1)([c15,c16])
var surf1516 = MAP(s1516)(Dom2D)

var s1718 = BEZIER(S1)([c17,c18])
var surf1718 = MAP(s1718)(Dom2D)

var s1517 = BEZIER(S1)([c15,c17])
var surf1517 = MAP(s1517)(Dom2D)

var s1618 = BEZIER(S1)([c16,c18])
var surf1618 = MAP(s1618)(Dom2D)

var p19 = [[-0.1,0,0],[-0.2,0,0]]
var c19 = BEZIER(S0)(p19)

var p20 = [[-0.1,0,-1],[-0.2,0,-1]]
var c20 = BEZIER(S0)(p20)

var s1920 = BEZIER(S1)([c19,c20])
var surf1920 = MAP(s1920)(Dom2D)

var p21 = [[1.6,0,0],[1.7,0,0]]
var c21 = BEZIER(S0)(p21)

var p22 = [[1.6,0,-1],[1.7,0,-1]]
var c22 = BEZIER(S0)(p22)

var s2122 = BEZIER(S1)([c21,c22])
var surf2122 = MAP(s2122)(Dom2D)

var backrest_s = S([0])([1.5])(STRUCT([surf1516,surf1718,surf1517,surf1618,surf1920,surf2122]))

var backrest = COLOR([150/255,75/255,0])(T([0,1,2])([-1.1,0.9,2.5])(backrest_s))

DRAW(STRUCT([superior_frame,front_top_junctions,front_vertical_supports,front_bottom_junctions,
	foots,back_bottom_junctions,vertical_back_support,seance,backrest]))
