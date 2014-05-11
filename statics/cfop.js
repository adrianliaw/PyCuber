var j, renderer, camera, scene, bgcanvas, light, cube, material, controls;


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
	camera = new THREE.PerspectiveCamera();
	camera.position.set(7, 7, 7);
	camera.lookAt(new THREE.Vector3(0, 0, 0));
	scene.add(camera);
	window.addEventListener('resize', function() {
		var s = size();
		renderer.setSize(s.width, s.height);
		camera.aspect = s.width/s.height;
		camera.updateProjectionMatrix();
	});
	renderer.setClearColor(0x333F47, 0.5);
	light = new THREE.AmbientLight(0xFFFFFF);
	light.position.set(100,1000,100);
	scene.add(light);
	cube = new THREE.BoxGeometry(1, 2, 1, 1, 1, 1);
	material = new THREE.MeshLambertMaterial({color: 0x55B663});
	scene.add(new THREE.Mesh(cube, material));
	controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
}

function animate() {
	requestAnimationFrame(animate);
	renderer.render(scene, camera);
	controls.update();
}







/*j.open("GET", "/CFOPsolve", false);
j.send();
j = JSON.parse(j.responseText);*/
/*var a, b;
a = j.scramble;
b = document.getElementById("scramble");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.full_solve;
b = document.getElementById("full_solve");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.C;
b = document.getElementById("cross");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.F[0].solve;
b = document.getElementById("f2l1");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.F[1].solve;
b = document.getElementById("f2l2");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.F[2].solve;
b = document.getElementById("f2l3");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.F[3].solve;
b = document.getElementById("f2l4");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.O;
b = document.getElementById("oll");
b.innerText += a.join(" ").replace(/i/gi, "'");
a = j.structure.P;
b = document.getElementById("pll");
b.innerText += a.join(" ").replace(/i/gi, "'");*/