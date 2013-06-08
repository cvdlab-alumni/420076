//function tha draw a circle
var circle = function(r){
return function(v){
return [r*COS(v[0]),r*SIN(v[0])];
};
};

//function that draw a cylinder
function CYLINDER(r,h){
var domain = DOMAIN([[-2*PI,2*PI]])([50]);
var crc = circle(r);
var model = MAP(crc)(domain);
return EXTRUDE([h])(model);
};

var mtrx = new Array();


var RNDM = function(x,y){
var f = (COS(x)+SIN(y))*Math.random();
var m = [x,y,f];
mtrx.push(m);
return f; 
};

var search_m = function(x,y,z){
	var z = null
	for (var i = 0; i <= mtrx.length-1; i++) {
		var c = mtrx[i];
		if ((c[0]==x)&&(c[1]==y))
			z = c[3];
	};
	return z
}


var dom = DOMAIN([[0,20],[0,40]])([60,60]);
var mountain = function (k) {
return function (v) {
var a = v[0];
var b = v[1];
return [a, b, RNDM(a,b)];
};
};
var mapping = mountain(3);
var model = MAP(mapping)(dom);
var DTM = COLOR([205/255,133/255,63/255])(model);

var domain_x = 20;
var domain_y = 40;
var lake = COLOR([0/255,149/255,182/255,0.9])(CUBOID([4,5,1]));

var lake1 = T([0,1,2])([1,8.5,-1])(lake);
var lake2 = T([0,1,2])([7.3,27,-1])(lake);


var tree = function(r,h,d){
var domain = DOMAIN([[0,1],[0,2*PI]])([d,d]);
var select_foliage = 10;
var p0 = [[0,0,0],[h,0,0]];
var c0 = BEZIER(S0)(p0);
var p1 = [[h,0,0],[0,0,2*h]];
var c1 = BEZIER(S0)(p1);
var map0 = ROTATIONAL_SURFACE(c0);
var s0 = MAP(map0)(domain);
var map1 = ROTATIONAL_SURFACE(c1);
var s1 = MAP(map1)(domain);
var foliage1 = COLOR([23/255,114/255,69/255])(STRUCT([s0,s1]));
var foliage2 = COLOR([0/255,128/255,128/255])(STRUCT([s0,s1]));
var foliage = foliage1;
if(select_foliage*Math.random()>=5)
	foliage = foliage1;
if (select_foliage*Math.random()<5)
	foliage = foliage2;
var trunk = COLOR([101/255,67/255,33/255])(CYLINDER(r,h));
return STRUCT([T([2])([h/2])(foliage),trunk])
};


var find_lake = function(point,n){
	var t0 = tree(0.05,0.15,10);
	var p0 = mtrx[point];
	var tree_number = n;
	var x = p0[0];
	var y = p0[1];
	var z = p0[2];
	var forest = T([0,1,2])([x,y,z])(t0);
	var k = point;
	var h = point+100+tree_number;
	if ((x<=1 || x>=5)&&(y<=8.5 || y>=13.5)) {
			for (var i = 0; i <= tree_number; i++) {
				t0 = tree(0.05,0.15,10);
				k++;
				v = mtrx[k];
				x = v[0];
				y = v[1];
				z = v[2];
				forest = STRUCT([forest,T([0,1,2])([x,y,z])(t0)])
			};
	};
	if ((x<=7.3 || x>=11.3)&&(y<=27 || y>=32)) {
		for (var i = 0; i <= tree_number; i++) {
				t0 = tree(0.05,0.15,10);
				h++;
				v = mtrx[h];
				x = v[0];
				y = v[1];
				z = v[2];
				forest = STRUCT([forest,T([0,1,2])([x,y,z])(t0)])
	};
};
return forest;
};


var FOREST = function(point,n){
	var check = find_lake(point,n);
	var check2 = STRUCT([check,find_lake(point+100+n,n)]);
	var check3 = STRUCT([check2,find_lake(point+100+n,n)]);
	return check3;
};

var f = FOREST(1300,25);

//ES4 DRAW SOME HUMAN SETTLEMENTS MODEL

var chalet = function(r_x,r_y){
	var x = Math.random()*0.15;
	var y = Math.random()*0.15;
	var z = Math.random()*0.15;
	return T([0,1,2])([r_x,r_y,0])(CUBOID([x,y,z]));
};

var SETTLEMENTS = function(r_x,r_y){
	var settlement = chalet(0,0);
	for (var i = 0; i < r_x; i=i+0.2) {
		for (var j = 0; j < r_y; j=j+0.2) {	
			var settlement = STRUCT([settlement,chalet(i,j)]);		
		};
	};
return settlement;
};

var basement = COLOR([205/255,133/255,63/255])(T([2])([-0.5])(CUBOID([2,2,0.5])));
var s1 = SETTLEMENTS(1,1);
var s2 = SETTLEMENTS(1,1);
var stl1 = T([0,1,2])([8,19.5,0.05])(STRUCT([basement,T([0,1])([1,1])(s1)]));
var stl2 = T([0,1,2])([5.4,3.2,0.1])STRUCT([basement,T([0,1])([1,1])(s2)]));


DRAW(STRUCT([lake1,lake2,DTM,f,stl1,stl2]));