Cube Solver
====================

This is a Rubik's cube solver by Python2

- CFOP : This package is the solving algorithm called <a href="http://www.speedsolving.com/wiki/index.php/CFOP">CFOP</a> by Jessica Fridrich, also known as Fridrich Method

- LBL : This is the biginner <a href="http://www.speedsolving.com/wiki/index.php/Layer_by_layer">Layer By Layer</a> method on solving Rubik's cube, coming soon

- 8355 : This is a method by a Taiwanese, see <a href="http://www.speedsolving.com/wiki/index.php/8355\_Method">the wiki</a>, solver coming soon

- BLD : A method of solving it blindfolded called <a href="http://homepage.ntlworld.com/angela.hayden/cube/blindfold_frontpage.html">3OP</a>, a lot different with other methods, coming soon


TODO : 
	Go to any solving method package, call the solve.py, and run the script.

	For the inputs:
	  L (0) is the left face color   (red)
	  U (1) is the top face color    (yellow)
	  F (2) is the front face color  (green)
	  D (3) is the bottom face color (white)
	  R (4) is the right face color  (orange)
	  B (5) is the back face color   (blue)

	The order of the stickers be like:
```
                                         |----|
                                         | U  |
                |----|----|----|    |----|----|----|----|
                | 9  | 10 | 11 |    | L  | F  | R  | B  |
                |----|----|----|    |----|----|----|----|
                | 12 | 13 | 14 |         | D  |
                |----|----|----|         |----|
                | 15 | 16 | 17 |
 |----|----|----|----|----|----|----|----|----|----|----|----|
 | 0  | 1  | 2  | 18 | 19 | 20 | 36 | 37 | 38 | 45 | 46 | 47 |
 |----|----|----|----|----|----|----|----|----|----|----|----|
 | 3  | 4  | 5  | 21 | 22 | 23 | 39 | 40 | 41 | 48 | 49 | 50 |
 |----|----|----|----|----|----|----|----|----|----|----|----|
 | 6  | 7  | 8  | 24 | 25 | 26 | 42 | 43 | 44 | 51 | 52 | 53 |
 |----|----|----|----|----|----|----|----|----|----|----|----|
                | 27 | 28 | 29 |
                |----|----|----|
                | 30 | 31 | 32 |
                |----|----|----|
                | 33 | 34 | 35 |
                |----|----|----|
```

	Input a sequence, ex: "LLLLLLLLLUUUUUUUUUFFFFFFFFFDDDDDDDDDRRRRRRRRRBBBBBBBBB"



This Rubik's cube solver only displays the official notation, to see graphics, there is another repository, pycuber, with the 3D graphics <a href="http://pycuber.appspot.com">here</a>.
