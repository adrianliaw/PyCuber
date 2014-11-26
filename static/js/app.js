(function () {

    var app = angular.module("rubikApp", []);

    app.controller("MainCtrl", function ($scope) {
        
        $scope.selectedColour = {background: "red"};

        $scope.selectColour = function (face) {
            $scope.selectedColour = {
                background: {"L":"red", "U":"yellow", "F":"green", "D":"white", "R":"orange", "B":"blue"}[face]
            };
        };

        $scope.colourMap = {};
        for (var _ in "LUFDRB") {
            x = "LUFDRB"[_];
            for (var y=0; y<3; y++) {
                for (var z=0; z<3; z++) {
                    if (y == 1 && z == 1) {
                        $scope.colourMap[x + y + z] = {
                            background: {"L":"red", "U":"yellow", "F":"green", "D":"white", "R":"orange", "B":"blue"}[x]
                        };
                    }
                    else {
                        $scope.colourMap[x + y + z] = {background: "gray"};
                    }
                }
            }
        }

        $scope.setColour = function (position) {
            $scope.colourMap[position] = $scope.selectedColour;
        };

        $scope.randomCube = function () {
            var socket = new WebSocket("ws://127.0.0.1:8765/random");
            socket.onopen = function () {
                socket.send("");
            };
            socket.onmessage = function (msg) {
                data = JSON.parse(msg.data);
                $scope.$apply(function () {
                    $scope.colourMap = data;
                });
            };
        }

        $scope.solvedCube = function () {
            $scope.colourMap = {};
            for (var _ in "LUFDRB") {
                x = "LUFDRB"[_];
                for (var y=0; y<3; y++) {
                    for (var z=0; z<3; z++) {
                        $scope.colourMap[x + y + z] = {
                            background: {"L":"red", "U":"yellow", "F":"green", "D":"white", "R":"orange", "B":"blue"}[x]
                        };
                    }
                }
            }
        };

        $scope.clearCube = function () {
            $scope.colourMap = {};
            for (var _ in "LUFDRB") {
                x = "LUFDRB"[_];
                for (var y=0; y<3; y++) {
                    for (var z=0; z<3; z++) {
                        if (y == 1 && z == 1) {
                            $scope.colourMap[x + y + z] = {
                                background: {"L":"red", "U":"yellow", "F":"green", "D":"white", "R":"orange", "B":"blue"}[x]
                            };
                        }
                        else {
                            $scope.colourMap[x + y + z] = {background: "gray"};
                        }
                    }
                }
            }
        };

        $scope.solveCube = function () {
            $scope.solutionList = [{result: "Sometimes it takes longer to solve it, please be patient...."}];
            var socket = new WebSocket("ws://127.0.0.1:8765/cfop");
            socket.onopen = function () {
                var message = "";
                for (var _ in "LUFDRB") {
                    x = "LUFDRB"[_];
                    for (var y=0; y<3; y++) {
                        for (var z=0; z<3; z++) {
                            message += {"red":0, "yellow":1, "green":2, "white":3, "orange":4, "blue":5, "gray":6}[$scope.colourMap[x+y+z].background];
                        }
                    }
                }
                socket.send(message);
            };
            socket.onmessage = function (msg) {
                data = JSON.parse(msg.data);
                if (data.error) {
                    alert(data.error);
                    socket.close();
                    return;
                }
                if (!$scope.solutionList[0].step_name) {
                    $scope.solutionList = [];
                }
                data.step_name = data.step_name.replace(/\'/g, "");
                data.result = data.result.join(" ");
                if (data.step_name == "FULL") {
                    $scope.solutionList.push({step_name:" "});
                }
                $scope.$apply(function () {
                    $scope.solutionList.push(data);
                });
            };

            socket.onclose = function () {
                if ($scope.solutionList.length >= 4) {
                    window.colourSet = {};
                    for (var k in $scope.colourMap) {
                        window.colourSet[k] = $scope.colourMap[k].background;
                    }
                }
                for (var cubie in window.rubiksCube) {
                    window.scene.remove(window.rubiksCube[cubie]);
                }
                $scope.$apply(function () {
                    $scope.solving = false;
                });
                window.rubiksCube = {};
                window.createCube();
            }
        }

        $scope.playOriginalSolving = function () {
            var full_algo = [];
            for (var i=0; i<$scope.solutionList.length-1; i++) {
                full_algo.push($scope.solutionList[i].result);
            }
            full_algo = full_algo.join(" ");
            window.performAlgo(full_algo);
            $scope.solving = true;
        }

        $scope.playOptimised = function () {
            window.performAlgo($scope.solutionList[$scope.solutionList.length-1].result);
            $scope.solving = true;
        };

        $scope.solving = true;
        
        $scope.solutionList = [];

    });


})();
