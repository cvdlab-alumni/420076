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

//ES2 DRAW ONE OR MORE LAKES ON THE MOUNTAINS MODEL
var lake = COLOR([0/255,149/255,182/255,0.9])(CUBOID([4,5,1]));

var lake1 = T([0,1,2])([1,8.5,-1])(lake);
var lake2 = T([0,1,2])([7.3,27,-1])(lake);

DRAW(STRUCT([lake1,lake2,DTM]));