;var IPythonDisplayCube = (function () {

    var _extend = function (destination, source) {
        for (var property in source)
            destination[property] = source[property];
        return destination;
    }

    var Square = function (colour) {
        var element = document.createElement("div");
        element.style.width = "95px";
        element.style.height = "95px";
        element.style.border = "5px solid black";
        element.style.background = colour;
        var object = new THREE.CSS3DObject(element);
        return object;
    };

    var FACING_POSITION = {
        F: {z: 1},
        B: {z: -1}, 
        L: {x: -1}, 
        R: {x: 1}, 
        U: {y: 1}, 
        D: {y: -1}
    };

    var FACING_ROTATION = {
        F: {}, 
        B: {}, 
        R: {y: Math.PI / 2}, 
        L: {y: Math.PI / 2}, 
        U: {x: Math.PI / 2}, 
        D: {x: Math.PI / 2}
    };


    var Cubie = function (facings, fillBlack) {
        var cubieObject = new THREE.Object3D;
        if (fillBlack) {
            var looping = FACING_POSITION;
        } else {
            var looping = facings;
        }
        for (var face in looping) {
            var square = facings[face] || "black";
            if (!(square instanceof THREE.Object3D)) {
                if (square === "unknown") {
                    square = "grey";
                }
                square = Square(square);
            }
            _extend(square.position, FACING_POSITION[face]);
            square.position.multiplyScalar(52);
            _extend(square.rotation, FACING_ROTATION[face]);
            cubieObject.add(square);
        }
        cubieObject._facings = facings;
        return cubieObject;
    };


    var DisplayCube = function (cubies) {
        var defaultColours = {
            F: "green", 
            B: "blue", 
            L: "red", 
            R: "orange", 
            U: "yellow", 
            D: "white"
        };
        var cubiePositions = ["LUF", "LUB", "LDF", "LDB", "RUF", "RUB", "RDF", "RDB", 
                              "LU", "FU", "RU", "BU", "LF", "FR", "RB", "BL", "LD", "FD", "RD", "BD", 
                              "L", "U", "F", "D", "R", "B"];
        var cubeObject = new THREE.Object3D;
        if (!cubies) {
            cubies = cubiePositions.map(function (pos) {
                var facings = {};
                for (var _i in pos) {
                    facings[pos[_i]] = defaultColours[pos[_i]];
                }
                return Cubie(facings);
            });
        }
        var _cubies = cubies, cubies = [];
        for (var _i in _cubies) {
            if (!(_cubies[_i] instanceof THREE.Object3D)) {
                cubies.push(Cubie(_cubies[_i]));
            } else {
                cubies.push(_cubies[_i]);
            }
        }

        for (var _i in cubies) {
            var cubie = cubies[_i];
            for (var face in cubie._facings) {
                _extend(cubie.position, FACING_POSITION[face]);
            }
            cubie.position.multiplyScalar(100);
            cubeObject.add(cubie);
        }

        return cubeObject;

    };

    var createDisplayCubeScene = function (element, cubies) {
        var renderer = new THREE.CSS3DRenderer;
        var $element = $(element);
        renderer.setSize($element.width(), $element.height());
        var scene = new THREE.Scene;
        var camera = new THREE.PerspectiveCamera(45, $element.width() / $element.height(), 1, 1000);
        camera.position.set(500, 500, 500);
        var controls = new THREE.OrbitControls(camera);
        controls.noZoom = controls.noPan = true;
        var cube = DisplayCube(cubies);
        scene.add(cube);
        renderer.render(scene, camera);
        (function animate () {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        })();
        $element.append(renderer.domElement);
        return renderer.domElement;
    }

    return createDisplayCubeScene

})();