//function tha draw a circle
var circle = function(r){
return function(v){
return [r*COS(v[0]),r*SIN(v[0])];
};
};

//function that draw a cylinder
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

var NOVOCOMUM = function(r,h){
	var shelf_1 = COLOR([101/255,67/255,33/255])(CYLINDER(r/1.216216,h/35.88))
	var shelf_2 = T([0])([r/(6.428571*2)])(COLOR([101/255,67/255,33/255])(CYLINDER(r/1.096761,h/35.88)))
	var shelf_3 = T([0])([r/(3.214285*2)])(COLOR([101/255,67/255,33/255])(CYLINDER(r,h/35.88)))
	var panel_1 = COLOR([101/255,67/255,33/255])(CUBOID([r/1.216216,h,h/35.88]))
	var panel_2 = COLOR([101/255,67/255,33/255])(CUBOID([h/35.88,h,r/(1.216216/2)]))
	var panel_3 = COLOR([101/255,67/255,33/255])(CUBOID([r/1.216216,h/4.357142,h/35.88]))
	var panel_1_t = T([0])([-r/1.216216])(panel_1)
	var panel_2_t = T([2])([-r/1.216216])(panel_2)
	var panels = STRUCT([panel_1_t,panel_2_t,panel_3])
	var panels_r = R([1,2])(PI/2)(panels)
	var shelfs = STRUCT([T([2])([h])(shelf_1),T([2])([h/1.525])(shelf_2),T([2])([h/4.357])(shelf_3)])
	return STRUCT([shelfs,panels_r])
}

var novocomum = S([0,1,2])([8,8,8])(NOVOCOMUM(0.45,0.61))
DRAW(novocomum)