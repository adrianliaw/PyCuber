var j, renderer, camera, scene, bgcanvas, light, cube, material, mesh, controls, obj, clock;
var onMovement = false;


function size() {
	var width = window.innerWidth, height = window.innerHeight;
	if (width * 0.6 <= height) {
		return {"width":width, "height":width * 0.6};
	} else {
		return {"width":height * 5/3, "height":height};
	}
}


function rotateAroundWorldAxis(object, axis, angle) {
	if (axis == "x") {
		var dis = object.position.distanceTo(new THREE.Vector3(object.position.x, 0, 0));
		object.rotation.x = angle;
		object.position.y = dis * Math.sin(angle);
		object.position.z = dis * Math.cos(angle);
	} else if (axis == "y") {
		var dis = object.position.distanceTo(new THREE.Vector3(0, object.position.y, 0));
		object.rotation.y = -angle;
		object.position.x = dis * Math.cos(angle);//Math.cos(Math.abs(object.rotation.y));
		object.position.z = dis * Math.sin(angle);//Math.sin(Math.abs(object.rotation.y));
	} else {
		var dis = object.position.distanceTo(new THREE.Vector3(0, 0, object.position.z));
		object.rotation.z = -angle;
		object.position.x = dis * Math.sin(angle);
		object.position.y = dis * Math.cos(angle);
	}
}


var rubixCube = {};

function createCubie(v) {
	cube = new THREE.CubeGeometry(0.95, 0.95, 0.95);
	material = new THREE.MeshLambertMaterial({color: 0xFFFFFF});
	mesh = new THREE.Mesh(cube, material);
	mesh.position = v;
	rubixCube[v.x + " " + v.y + " " + v.z] = mesh;
	return mesh;
}

function U() {
	for (var x=-1; x<=1; x++) {
		for (var z=-1; z<=1; z++) {
			rotateAroundWorldAxis(rubixCube[x + " " + 1 + " " + z], "y", clock.getDelta());
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
	camera = new THREE.PerspectiveCamera(45, 5/3);
	camera.position.set(5, 10, 0);
	scene.add(camera);
	window.addEventListener('resize', function() {
		var s = size();
		renderer.setSize(s.width, s.height);
		camera.aspect = s.width / s.height;
		camera.updateProjectionMatrix();
	});
	//renderer.setClearColor(0xFFFFFF, 0.5);
	light = new THREE.AmbientLight(0x222222);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
	light.position.set(200, 500, 500);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.9);
	light.position.set(-200, -100, -400);
	scene.add(light);
	for (var x=-1; x<=1; x++) {
		for (var y=-1; y<=1; y++) {
			for (var z=-1; z<=1; z++) {
				//if (!(x == y == z == 0)) {
				scene.add(createCubie(new THREE.Vector3(x, y, z)));
				//}
			}
		}
	}
	controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	Coordinates.drawGrid({orientation: "y"});
	Coordinates.drawGrid({orientation: "z"});
	Coordinates.drawGrid();
	Coordinates.drawAllAxes();
	clock = new THREE.Clock();
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



