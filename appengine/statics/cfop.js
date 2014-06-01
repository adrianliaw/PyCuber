var j, renderer, camera, scene, bgcanvas, light, cube, material, mesh, controls, obj, clock;
var onMovement = false;


function size() {
	var width = window.innerWidth, height = window.innerHeight;
	if (width * 0.5 <= height) {
		return {"width":width, "height":width * 0.5};
	} else {
		return {"width":height * 2, "height":height};
	}
}


var colors = {"U":"yellow", "L":"red", "F":"green", "D":"white", "R":"orange", "B":"blue"};

var rubixCube = {};

function createCubie(v) {
	cube = new THREE.BeveledBlockGeometry(0.97, 0.97, 0.97, 0.05);
	material = new THREE.MeshLambertMaterial({color: 0xCCCCCC});
	mesh = new THREE.Mesh(cube, material);
	mesh.position = v;
	rubixCube[v.x + " " + v.y + " " + v.z] = mesh;
	return mesh;
}

function updateRubixCube() {
	var newCube = {};
	for (var x=-1; x<=1; x++) {
		for (var y=-1; y<=1; y++) {
			for (var z=-1; z<=1; z++) {
				var cubie = rubixCube[x + " " + y + " " + z];
				newCube[cubie.position.x + " " + cubie.position.y + " " + cubie.position.z] = cubie;
			}
		}
	}
	rubixCube = newCube;
}

var stickers = {};

function createSticker(face, v) {
	var positing = {"0": new THREE.Vector3(-1.505, 0, 0), 
					"1": new THREE.Vector3(0, 1.505, 0), 
					"2": new THREE.Vector3(0, 0, 1.505), 
					"3": new THREE.Vector3(0, -1.505, 0), 
					"4": new THREE.Vector3(1.505, 0, 0), 
					"5": new THREE.Vector3(0, 0, -1.505)};
	cube = new THREE.CubeGeometry(0.8, 0.8, 0.01);
	material = new THREE.MeshLambertMaterial({color: colors[face]});
	mesh = new THREE.Mesh(cube, material);
	mesh.rotation = new THREE.Vector3((positing[v.x.toString()].y !== 0) * 1, (positing[v.x.toString()].x !== 0) * 1, 0);
	mesh.rotation.multiplyScalar(Math.PI / 2);
	mesh.position = positing[v.x];
	if (v.x == 0) {
		mesh.position.y = -(v.y - 1);
		mesh.position.z = v.z - 1;
	} else if (v.x == 1) {
		mesh.position.z = v.y - 1;
		mesh.position.x = v.z - 1;
	} else if (v.x == 2) {
		mesh.position.x = v.z - 1;
		mesh.position.y = -(v.y - 1);
	} else if (v.x == 3) {
		mesh.position.z = -(v.y - 1);
		mesh.position.x = v.z - 1;
	} else if (v.x == 4) {
		mesh.position.y = -(v.y - 1);
		mesh.position.z = -(v.z - 1);
	} else if (v.x == 5) {
		mesh.position.x = -(v.z - 1);
		mesh.position.y = -(v.y - 1);
	}
	stickers[v.x + " " + v.y + " " + v.z] = mesh;
	return mesh;
}

var animatedStickers = {
	"L":["0 0 0", "0 0 1", "0 0 2", "0 1 0", "0 1 1", "0 1 2", "0 2 0", "0 2 1", "0 2 2", "1 0 0", "1 1 0", "1 2 0", "2 0 0", "2 1 0", "2 2 0", "3 0 0", "3 1 0", "3 2 0", "5 0 2", "5 1 2", "5 2 2"], 
	"U":["1 0 0", "1 0 1", "1 0 2", "1 1 0", "1 1 1", "1 1 2", "1 2 0", "1 2 1", "1 2 2", "0 0 0", "0 0 1", "0 0 2", "2 0 0", "2 0 1", "2 0 2", "4 0 0", "4 0 1", "4 0 2", "5 0 0", "5 0 1", "5 0 2"], 
	"F":["2 0 0", "2 0 1", "2 0 2", "2 1 0", "2 1 1", "2 1 2", "2 2 0", "2 2 1", "2 2 2", "0 0 2", "0 1 2", "0 2 2", "1 2 0", "1 2 1", "1 2 2", "4 0 0", "4 1 0", "4 2 0", "3 0 0", "3 0 1", "3 0 2"], 
	"D":["3 0 0", "3 0 1", "3 0 2", "3 1 0", "3 1 1", "3 1 2", "3 2 0", "3 2 1", "3 2 2", "0 2 0", "0 2 1", "0 2 2", "2 2 0", "2 2 1", "2 2 2", "4 2 0", "4 2 1", "4 2 2", "5 2 0", "5 2 1", "5 2 2"], 
	"R":["4 0 0", "4 0 1", "4 0 2", "4 1 0", "4 1 1", "4 1 2", "4 2 0", "4 2 1", "4 2 2", "1 0 2", "1 1 2", "1 2 2", "2 0 2", "2 1 2", "2 2 2", "3 0 2", "3 1 2", "3 2 2", "5 0 0", "5 1 0", "5 2 0"], 
	"B":["5 0 0", "5 0 1", "5 0 2", "5 1 0", "5 1 1", "5 1 2", "5 2 0", "5 2 1", "5 2 2", "0 0 0", "0 1 0", "0 2 0", "1 0 0", "1 0 1", "1 0 2", "4 0 2", "4 1 2", "4 2 2", "3 2 0", "3 2 1", "3 2 2"]
};

function action(a) {
	var animated = new THREE.Object3D();
	var axis;
	if (a[0] == "L") {
		for (var y=-1; y<=1; y++) {
			for (var z=-1; z<=1; z++) {
				animated.add(rubixCube["-1 " + y + " " + z]);
			}
		}
		for (var i=0; i<21; i++) {
			animated.add(stickers(animatedStickers["L"][i]));
		}
	}
}

function updateStickers() {
	var newStickers = {};
	for (var x=0; x<=5; x++) {
		for (var y=0; y<=2; y++) {
			for(var z=0; z<=2; z++) {
				var sticker = stickers[x + " " + y + " " + z];
				var newx, newy, newz;
				if (sticker.position.x == -1.505) {
					newx = 0;
					newy = -sticker.position.y + 1;
					newz = sticker.position.z + 1;
				} else if (sticker.position.y == 1.505) {
					newx = 1;
					newy = sticker.position.z + 1;
					newz = sticker.position.x + 1;
				} else if (sticker.position.z == 1.505) {
					newx = 2;
					newy = sticker.position.x + 1;
					newz = -sticker.position.y + 1;
				} else if (sticker.position.y == -1.505) {
					newx = 3;
					newy = -sticker.position.z + 1;
					newz = sticker.position.x + 1;
				} else if (sticker.position.x == 1.505) {
					newx = 4;
					newy = -sticker.position.y + 1;
					newz = -sticker.position.z + 1;
				} else if (sticker.position.z == -1.505) {
					newx = 5;
					newy = -sticker.position.y + 1;
					newz = -sticker.position.x + 1;
				}
				newStickers[newx + " " + newy + " " + newz] = sticker;
			}
		}
	}
	stickers = newStickers;
}

function createRubixCube() {
	for (var x=-1; x<=1; x++) {
		for (var y=-1; y<=1; y++) {
			for (var z=-1; z<=1; z++) {
				scene.add(createCubie(new THREE.Vector3(x, y, z)));
			}
		}
	}
	for (var x=0; x<=5; x++) {
		for (var y=0; y<=2; y++) {
			for (var z=0; z<=2; z++) {
				scene.add(createSticker("LUFDRB"[x], new THREE.Vector3(x, y, z)));
			}
		}
	}
}

function init() {
	scene = new THREE.Scene();
	bgcanvas = document.createElement("canvas");
	var s = size();
	bgcanvas.width = s.width, bgcanvas.height = s.height;
	document.getElementById("bg").appendChild(bgcanvas);
	renderer = new THREE.WebGLRenderer({antialias:true});
	renderer.setSize(s.width, s.height);
	document.getElementById("anim").appendChild(renderer.domElement);
	camera = new THREE.PerspectiveCamera(45, 2);
	camera.position.set(7, 7, 7);
	scene.add(camera);
	window.addEventListener('resize', function() {
		var s = size();
		renderer.setSize(s.width, s.height);
		camera.aspect = s.width / s.height;
		camera.updateProjectionMatrix();
	});
	renderer.setClearColor(0x000000, 1);
	light = new THREE.AmbientLight(0x222222);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
	light.position.set(600, 0, 0);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
	light.position.set(0, 0, 600);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
	light.position.set(0, 600, 0);
	scene.add(light);
	createRubixCube();
	controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	/*Coordinates.drawGrid({orientation: "y"});
	Coordinates.drawGrid({orientation: "z"});
	Coordinates.drawGrid();
	Coordinates.drawAllAxes();
	clock = new THREE.Clock();*/
}


function animate() {
	window.requestAnimationFrame(animate);
	//rotateAroundWorldAxis(cube, "x", clock.getElapsedTime());
	//U();
	renderer.render(scene, camera);
	controls.update();
}



init();
animate();
//window.setInterval(animate, 1000/60);



