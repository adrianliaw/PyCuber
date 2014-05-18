var j, renderer, camera, scene, bgcanvas, light, cube, material, controls, obj, clock;
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
	object.lookAt(new THREE.Vector3());
	var dis = object.position.distanceTo(new THREE.Vector3());
	if (axis == "x") {
		object.position.y = dis * Math.sin(angle);
		object.position.z = dis * Math.cos(angle);
	} else if (axis == "y") {
		object.position.x = dis * Math.cos(angle);
		object.position.z = dis * Math.sin(angle);
	} else {
		object.position.x = dis * Math.sin(angle);
		object.position.y = dis * Math.cos(angle);
	}
	/*var aux = axis.clone();
	var angleVector = new THREE.Vector3(angle, angle, angle);
	object.rotation.addVectors(object.rotation, )*/
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
	camera.position.set(20, 20, 20);
	scene.add(camera);
	window.addEventListener('resize', function() {
		var s = size();
		renderer.setSize(s.width, s.height);
		camera.aspect = s.width / s.height;
		camera.updateProjectionMatrix();
	});
	renderer.setClearColor(0xFFFFFF, 0.5);
	light = new THREE.AmbientLight(0x222222);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
	light.position.set(200, 500, 500);
	scene.add(light);
	light = new THREE.DirectionalLight(0xFFFFFF, 0.9);
	light.position.set(-200, -100, -400);
	scene.add(light);
	cube = new THREE.BoxGeometry(1, 1, 1, 1, 1, 1);
	material = new THREE.MeshLambertMaterial({color: 0x55B663});
	cube = new THREE.Mesh(cube, material);
	cube.position.set(10, 0, 0);
	obj = new THREE.Object3D();
	obj.add(cube);
	//rotateAroundWorldAxis(cube, new THREE.Vector3(1, 0, 0), 30 * Math.PI/180);
	scene.add(obj);
	controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	Coordinates.drawGrid({orientation: "y"});
	Coordinates.drawGrid({orientation: "z"});
	Coordinates.drawGrid();
	Coordinates.drawAllAxes();
	clock = new THREE.Clock();
}

var i = 0;

/*function rotate() {
	cube.position.set(0, 0, 0);
	cube.rotation.y += Math.PI / 50;
	var angle = (Math.PI / 2) + (i / 100) * 2 * Math.PI;
	cube.position.x = Math.cos(angle) * 10;
	cube.position.y = Math.sin(angle) * 10;
	if (i < 100) { i += 1;} else {i = 0;}*/

function animate() {
	//rotate();
	requestAnimationFrame(animate);
	/*var t = clock.getElapsedTime();
	var m_angle = t * 1;
	var d = clock.getDelta();
	cube.lookAt(new THREE.Vector3());
	cube.position.set(10 * Math.sin(m_angle), 10 * Math.cos(m_angle), 0);*/
	rotateAroundWorldAxis(cube, "y", clock.getElapsedTime());
	renderer.render(scene, camera);
	controls.update();
}



init();
animate();



