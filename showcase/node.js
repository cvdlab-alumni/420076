!(function (exports){

  var fs = require('fs');

  var plasm_lib = require('plasm.js');
  var obj = plasm_lib.plasm;
  var fun = plasm_lib.plasm_fun;
  var plasm = obj.plasm;
  var Plasm = obj.Plasm;

  var root = this;

  Object.keys(fun).forEach(function (k) { 
    root[k] = fun[k];
  });

  var p = new Plasm();
  fun.PLASM(p);


  var scmodel = (function () {
  /*///////////////////////////////////////////

 /**
 * @author Fabio Mastromatteo
 * 
 * PACMAN, PILLS AND GHOSTS
 * Inspired by this picture: http://technetcrew.com/wp-content/uploads/2012/09/pacman-2.jpg
 */


//function that draw a sphere, used for the ghost's eyes
var SPHERE = function (r) {
  var domain = DOMAIN([[0, PI], [0, 2*PI]])([50,50]);
  var mapping = function (v) {
    var a = v[0];
    var b = v[1];
    return [r*SIN(a)*COS(b), r*SIN(a)*SIN(b), r*COS(a)];
  };
  var model = MAP(mapping)(domain);
  return model;
};


//PACMAN
var domain = DOMAIN([[0,1],[0,PI]])([20,20]);
var profile = BEZIER(S0)([[0,0,0],[1,0,0],[1,0,1],[0,0,1]]);
var mapping = ROTATIONAL_SURFACE(profile);
var semibody = MAP(mapping)(domain);
var up = R([0,1])(PI/6)(COLOR([1,1,0])(semibody));
var down = R([0,1])(2*PI/3)(up);
var PACMAN = T([2])([-0.5])(STRUCT([up,down]));

//CUBIC PILLS
var pill0 = COLOR([1,1,1])(CUBOID([0.2,0.2,0.2]));
var pill1 = T([0])([0.6])(pill0);
var pill2 = T([0])([0.6])(pill1);
var pill3 = T([0])([0.6])(pill2);
var pill4 = T([0])([0.6])(pill3);
var PILLS = T([0,1])([1.1,-0.1])(STRUCT([pill0,pill1,pill2,pill3,pill4]));

//GHOST MODEL
var domain = DOMAIN([[0,1],[0,2*PI]])([40,40]);
var profile = BEZIER(S0)([[0.5,0,0],[0.45,0,0.5],[0.4,0,0.85],[0,0,0.82]]);
var mapping = ROTATIONAL_SURFACE(profile);
var body = MAP(mapping)(domain);

//Ghost's feet
var ellittic = BEZIER(S0)([[0,0,0],[-0.3,0,0],[-0.3,0,1],[0,0,1]]);
var el = MAP(ellittic)(INTERVALS(1)(30));
var mapping = ROTATIONAL_SURFACE(ellittic);
var ell = R([1,2])(PI/9)(MAP(mapping)(domain));
var foot0 = T([1,2])([0.39,-0.2])(ell);
var foot1 = R([0,1])(PI/3)(foot0);
var foot2 = R([0,1])(PI/3)(foot1);
var foot3 = R([0,1])(PI/3)(foot2);
var foot4 = R([0,1])(PI/3)(foot3);
var foot5 = R([0,1])(PI/3)(foot4);
var feet = STRUCT([foot0,foot1,foot2,foot3,foot4,foot5]);
var rotated_ghost = R([1,2])(-PI/2)(STRUCT([body,feet]));

//Ghost's eyes
var eye_iris = COLOR([255,255,255])(SPHERE(0.12));
var eye_pupil = T([0,2])([-0.05,0.07])(COLOR([0,0,1])(SPHERE(0.06)));
var eye = T([0,1,2])([4.3,0.1,0.3])(STRUCT([eye_iris]));
var eye_sx = T([0,1,2])([4.3,0.1,0.3])(STRUCT([eye_iris,eye_pupil]));
var eye_dx = T([0,2])([0.25,0.0495])(STRUCT([eye,T([0,1,2])([4.34,0.105,0.31])(eye_pupil)]));
var eyes = STRUCT([eye_sx,eye_dx]);

//COLORED GHOSTS
var GHOST1 = STRUCT([T([0,1])([4.5,-0.4])(COLOR([1,0.75,0.8])(rotated_ghost)),eyes]);
var GHOST2 = T([0])([1.5])(STRUCT([T([0,1])([4.5,-0.4])(COLOR([0,1,1])(rotated_ghost)),eyes]));
var GHOST3 = T([0])([3])(STRUCT([T([0,1])([4.5,-0.4])(COLOR([1,0.6,0])(rotated_ghost)),eyes]));
var GHOST4 = T([0])([4.5])(STRUCT([T([0,1])([4.5,-0.4])(COLOR([1,0,0])(rotated_ghost)),eyes]));
var GHOSTS = STRUCT([GHOST1,GHOST2,GHOST3,GHOST4]);


//FINAL MODEL
var model = STRUCT([PACMAN,PILLS,GHOSTS]);


  ///////////////////////////////////////////*/
  return model
  })();

  exports.author = 'FabioMaster';
  exports.category = 'games';
  exports.scmodel = scmodel;

  if (!module.parent) {
    fs.writeFile('./data.json', JSON.stringify(scmodel.toJSON()));
  }

}(this));