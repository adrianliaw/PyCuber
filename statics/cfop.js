var j, renderer, camera, scene, bgcanvas, light, cube, material, controls, obj;


init();
animate();

function size() {
	var width = window.innerWidth, height = window.innerHeight;
	if (width * 0.6 <= height) {
		return {"width":width, "height":width * 0.6};
	} else {
		return {"width":height * 5/3, "height":height};
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
	camera.position.set(7, 7, 7);
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
	obj = new THREE.Object3D();
	cube = new THREE.BoxGeometry(1, 1, 1, 1, 1, 1);
	material = new THREE.MeshLambertMaterial({color: 0x55B663});
	cube = new THREE.Mesh(cube, material);
	cube.position.set(10, 0, 0);
	obj.add(cube);
	scene.add(obj);
	controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	Coordinates.drawGrid({orientation: "y"});
	Coordinates.drawGrid({orientation: "z"});
	Coordinates.drawGrid();
	Coordinates.drawAllAxes();
}

function animate() {
	requestAnimationFrame(animate);
	renderer.render(scene, camera);
	controls.update();
}







