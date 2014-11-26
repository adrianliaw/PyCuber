(function () {
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


    var colours = {"U":"yellow", "L":"red", "F":"green", "D":"white", "R":"orange", "B":"blue"};


    function createCubie(v) {
        obj = new THREE.Object3D();
        cube = new THREE.BeveledBlockGeometry(0.97, 0.97, 0.97, 0.05);
        material = new THREE.MeshLambertMaterial({color: 0xCCCCCC});
        mesh = new THREE.Mesh(cube, material);
        mesh.position = v;
        mesh.name = "cubie";
        mesh.originPosition = v;
        obj.add(mesh);
        var s = cubieStickerRelation[v.x + " " + v.y + " " + v.z];
        for (var i=0; i<s.length; i++) {
            mesh = createSticker("LUFDRB"[parseInt(s[i].split(" ")[0])], new THREE.Vector3(parseInt(s[i].split(" ")[0]), parseInt(s[i].split(" ")[1]), parseInt(s[i].split(" ")[2])), window.colourSet);
            obj.add(mesh);
        } 
        window.rubiksCube[v.x + " " + v.y + " " + v.z] = obj;
        return obj;
    }

    function epsilon(value, correct, e) {
        return Math.abs(value - correct) < e;
    }

    function updatePositionEpsilon(v) {
        var nvec = [];
        for (var i=0; i<3; i++) {
            var val = [v.x, v.y, v.z][i];
            for (var x=0; x<5; x++) {
                var cor = [0, 1, -1, 1.505, -1.505][x];
                if (epsilon(val, cor, 0.001)) {
                    nvec.push(cor);
                    break;
                }
            }
        }
        return new THREE.Vector3(nvec[0], nvec[1], nvec[2]);
    }

    function updateRubixCube() {
        var newCube = {};
        for (var x=-1; x<=1; x++) {
            for (var y=-1; y<=1; y++) {
                for (var z=-1; z<=1; z++) {
                    var cubie = window.rubiksCube[x + " " + y + " " + z];
                    for (var i=cubie.children.length; i>0; i--) {
                        var child = cubie.children[i-1];
                        child.position.getPositionFromMatrix(child.matrixWorld);
                        child.position = updatePositionEpsilon(child.position);
                        child.rotation.set((Math.abs(child.position.y) == 1.505)*Math.PI/2, 
                                           (Math.abs(child.position.x) == 1.505)*Math.PI/2, 
                                           0);
                    }
                    cubie.rotation.set(0, 0, 0);
                    newCube[child.position.x + " " + child.position.y + " " + child.position.z] = cubie;
                }
            }
        }
        window.rubiksCube = newCube;
    }

    function createSticker(face, v, colourSet) {
        var positing = {"0": new THREE.Vector3(-1.505, 0, 0), 
                        "1": new THREE.Vector3(0, 1.505, 0), 
                        "2": new THREE.Vector3(0, 0, 1.505), 
                        "3": new THREE.Vector3(0, -1.505, 0), 
                        "4": new THREE.Vector3(1.505, 0, 0), 
                        "5": new THREE.Vector3(0, 0, -1.505)};
        cube = new THREE.CubeGeometry(0.8, 0.8, 0.01);
        material = new THREE.MeshLambertMaterial({color: colourSet? colourSet[face + v.y + v.z]: colours[face]});
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
        mesh.name = "sticker";
        mesh.originPosition = mesh.position.clone();
        return mesh;
    }

    var cubieStickerRelation = {
        "-1 -1 -1": ["0 2 0", "3 2 0", "5 2 2"], 
        "-1 -1 0" : ["0 2 1", "3 1 0"], 
        "-1 -1 1" : ["0 2 2", "2 2 0", "3 0 0"], 
        "-1 0 -1" : ["0 1 0", "5 1 2"], 
        "-1 0 0"  : ["0 1 1"], 
        "-1 0 1"  : ["0 1 2", "2 1 0"], 
        "-1 1 -1" : ["0 0 0", "1 0 0", "5 0 2"], 
        "-1 1 0"  : ["0 0 1", "1 1 0"], 
        "-1 1 1"  : ["0 0 2", "1 2 0", "2 0 0"], 
        "0 -1 -1" : ["3 2 1", "5 2 1"], 
        "0 -1 0"  : ["3 1 1"], 
        "0 -1 1"  : ["2 2 1", "3 0 1"], 
        "0 0 -1"  : ["5 1 1"], 
        "0 0 0"   : [], 
        "0 0 1"   : ["2 1 1"], 
        "0 1 -1"  : ["1 0 1", "5 0 1"], 
        "0 1 0"   : ["1 1 1"], 
        "0 1 1"   : ["1 2 1", "2 0 1"], 
        "1 -1 -1" : ["3 2 2", "4 2 2", "5 2 0"], 
        "1 -1 0"  : ["3 1 2", "4 2 1"], 
        "1 -1 1"  : ["2 2 2", "3 0 2", "4 2 0"], 
        "1 0 -1"  : ["4 1 2", "5 1 0"], 
        "1 0 0"   : ["4 1 1"], 
        "1 0 1"   : ["2 1 2", "4 1 0"], 
        "1 1 -1"  : ["1 0 2", "4 0 2", "5 0 0"], 
        "1 1 0"   : ["1 1 2", "4 0 1"], 
        "1 1 1"   : ["1 2 2", "2 0 2", "4 0 0"]
    };

    function action(a) {
        var animated = [];
        var axis;
        if (a[0] == "L") {
            for (var y=-1; y<=1; y++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube["-1 " + y + " " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "x+";
            } else if (a[1] == "'") {
                axis = "x-";
            } else {
                axis = "x+2";
            }
        } else if (a[0] == "U"){
            for (var x=-1; x<=1; x++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube[x + " 1 " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "y-";
            } else if (a[1] == "'") {
                axis = "y+";
            } else {
                axis = "y-2";
            }
        } else if (a[0] == "F") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    animated.push(window.rubiksCube[x + " " + y + " 1"]);
                }
            }
            if (a[1] === undefined) {
                axis = "z-";
            } else if (a[1] == "'") {
                axis = "z+";
            } else {
                axis = "z-2";
            }
        } else if (a[0] == "D") {
            for (var x=-1; x<=1; x++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube[x + " -1 " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "y+";
            } else if (a[1] == "'") {
                axis = "y-";
            } else {
                axis = "y+2";
            }
        } else if (a[0] == "R") {
            for (var y=-1; y<=1; y++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube["1 " + y + " " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "x-";
            } else if (a[1] == "'") {
                axis = "x+";
            } else {
                axis = "x-2";
            }
        } else if (a[0] == "B") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    animated.push(window.rubiksCube[x + " " + y + " -1"]);
                }
            }
            if (a[1] === undefined) {
                axis = "z+";
            } else if (a[1] == "'") {
                axis = "z-";
            } else {
                axis = "z+2";
            }
        } else if (a[0] == "M") {
            for (var y=-1; y<=1; y++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube["0 " + y + " " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "x+";
            } else if (a[1] == "'") {
                axis = "x-";
            } else {
                axis = "x+2";
            }
        } else if (a[0] == "S") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    animated.push(window.rubiksCube[x + " " + y + " 0"]);
                }
            }
            if (a[1] === undefined) {
                axis = "z-";
            } else if (a[1] == "'") {
                axis = "z+";
            } else {
                axis = "z-2";
            }
        } else if (a[0] == "E") {
            for (var x=-1; x<=1; x++) {
                for (var z=-1; z<=1; z++) {
                    animated.push(window.rubiksCube[x + " 0 " + z]);
                }
            }
            if (a[1] === undefined) {
                axis = "y+";
            } else if (a[1] == "'") {
                axis = "y-";
            } else {
                axis = "y+2";
            }
        } else if (a[0] == "l") {
            for (var x=-1; x<=0; x++) {
                for (var y=-1; y<=1; y++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "x+";
            } else if (a[1] == "'") {
                axis = "x-";
            } else {
                axis = "x+2";
            }
        } else if (a[0] == "u") {
            for (var y=0; y<=1; y++) {
                for (var x=-1; x<=1; x++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "y-";
            } else if (a[1] == "'") {
                axis = "y+";
            } else {
                axis = "y-2";
            }
        } else if (a[0] == "f") {
            for (var z=0; z<=1; z++) {
                for (var x=-1; x<=1; x++) {
                    for (var y=-1; y<=1; y++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "z-";
            } else if (a[1] == "'") {
                axis = "z+";
            } else {
                axis = "z-2";
            }
        } else if (a[0] == "d") {
            for (var y=-1; y<=0; y++) {
                for (var x=-1; x<=1; x++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "y+";
            } else if (a[1] == "'") {
                axis = "y-";
            } else {
                axis = "y+2";
            }
        } else if (a[0] == "r") {
            for (var x=0; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "x-";
            } else if (a[1] == "'") {
                axis = "x+";
            } else {
                axis = "x-2";
            }
        } else if (a[0] == "b") {
            for (var z=-1; z<=0; z++) {
                for (var x=-1; x<=1; x++) {
                    for (var y=-1; y<=1; y++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "z+";
            } else if (a[1] == "'") {
                axis = "z-";
            } else {
                axis = "z+2";
            }
        } else if (a[0] == "x") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "x-";
            } else if (a[1] == "'") {
                axis = "x+";
            } else {
                axis = "x-2";
            }
        } else if (a[0] == "y") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "y-";
            } else if (a[1] == "'") {
                axis = "y+";
            } else {
                axis = "y-2";
            }
        } else if (a[0] == "z") {
            for (var x=-1; x<=1; x++) {
                for (var y=-1; y<=1; y++) {
                    for (var z=-1; z<=1; z++) {
                        animated.push(window.rubiksCube[x + " " + y + " " + z]);
                    }
                }
            }
            if (a[1] === undefined) {
                axis = "z-";
            } else if (a[1] == "'") {
                axis = "z+";
            } else {
                axis = "z-2";
            }
        }
        return [animated, axis];
    }

    function perform(act) {
        var set = action(act);
        var rotation = {};
        rotation[set[1][0]] = 0;
        var target = {};
        target[set[1][0]] = eval(set[1][1]+Math.PI/2)*(parseInt(set[1][2]) || 1);
        var tween = new TWEEN.Tween(rotation).to(target, 500*(parseInt(set[1][2])||1));
        tween.easing(TWEEN.Easing.Cubic.InOut);
        tween.onComplete(function () {updateRubixCube();});
        tween.onUpdate(function () {for (var i=0; i<set[0].length; i++){set[0][i].rotation[set[1][0]] = rotation[set[1][0]];}});
        tween.start();
    }

    function perform_algo(algo, callback) {
        algo = algo.split(" ");
        if (algo == false) {
            callback ? callback() : null;
            return true;
        } else {
            act = algo[0];
            var set = action(act);
            var rotation = {};
            rotation[set[1][0]] = 0;
            var target = {};
            target[set[1][0]] = eval(set[1][1]+Math.PI/2)*(parseInt(set[1][2]) || 1);
            var tween = new TWEEN.Tween(rotation).to(target, 500*(parseInt(set[1][2])||1));
            tween.easing(TWEEN.Easing.Cubic.InOut);
            tween.onComplete(function () {
                updateRubixCube();
                window.setTimeout(function () {
                    perform_algo(algo.slice(1).join(" "));
                }, 200);
            });
            tween.onUpdate(function () {for (var i=0; i<set[0].length; i++){set[0][i].rotation[set[1][0]] = rotation[set[1][0]];}});
            tween.start();
        }
    }


    function createRubixCube() {
        for (var x=-1; x<=1; x++) {
            for (var y=-1; y<=1; y++) {
                for (var z=-1; z<=1; z++) {
                    scene.add(createCubie(new THREE.Vector3(x, y, z)));
                }
            }
        }
    }

    function init() {
        scene = new THREE.Scene();
        var s = size();
        renderer = new THREE.WebGLRenderer({antialias:true});
        renderer.setSize(800, 400);
        document.getElementById("player").appendChild(renderer.domElement);
        camera = new THREE.PerspectiveCamera(45, 2);
        camera.position.set(7, 7, 7);
        /*window.addEventListener('resize', function() {
            var s = size();
            renderer.setSize(s.width, s.height);
            camera.aspect = s.width / s.height;
            camera.updateProjectionMatrix();
        });*/
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
        light = new THREE.AmbientLight(0x222222);
        scene.add(light);
        light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
        light.position.set(-600, 0, 0);
        scene.add(light);
        light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
        light.position.set(0, 0, -600);
        scene.add(light);
        light = new THREE.DirectionalLight(0xFFFFFF, 0.7);
        light.position.set(0, -600, 0);
        scene.add(light);
        createRubixCube();
        controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
        animate();
        window.scene = scene;
    }


    function animate() {
        window.requestAnimationFrame(animate);
        renderer.render(scene, camera);
        controls.update();
        TWEEN.update();
    }

    window.initScene = init;
    window.rubiksCube = {};
    window.createCube = createRubixCube;
    window.performAlgo = perform_algo;

})();
