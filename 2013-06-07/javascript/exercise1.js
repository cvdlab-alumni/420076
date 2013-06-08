//ES1 DRAW A DTM (DIGITAL TERRAIN MODEL) WITH SOME MOUNTAINOUS AREAS

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

DRAW(DTM);