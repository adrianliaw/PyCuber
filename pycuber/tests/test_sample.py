import pycuber as pc

# some basic tests to guard against regressions
# made for running with py.test


orig_algs = ["U2 R2 U2 R' U' R U' R2",
             "F F F",
             "B D F L R U",
             "z D' R U' R2 D R' U D' R U' R2 D R' U z'",
             "y2 M2 U' M U2 M' U' M2",
             "r' D r U2 r' D r U2 r' D r U2 r' D r U2 r' D r",
             ]
# THIS ORDER AND CONTENTS NEEDS TO BE synchronized TO THE ABOVE
inverted_algs = ["R2 U R' U R U2 R2 U2",
                 "F' F' F'",
                 "U' R' L' F' D' B'",
                 "z U' R D' R2 U R' D U' R D' R2 U R' D z'",
                 "M2 U M U2 M' U M2 y2",
                 "r' D' r U2 r' D' r U2 r' D' r U2 r' D' r U2 r' D' r"
                 ]


def test_algs_list_similar():
    # get an idea of the algorithm lists are coordinated
    assert len(orig_algs) == len(inverted_algs)
    for i in range(len(orig_algs)):
        assert len(orig_algs[i].split()) == len(inverted_algs[i].split())


def test_inverse():
    # test to make sure they invert correctly based off of hand inverted algs

    for i, alg in enumerate(orig_algs):
            plausible = pc.Formula(alg).reverse()
            assert str(plausible) == inverted_algs[i]


def test_double_inverting():
    # two inverts successive should revert back to the original algorithm
    for alg in orig_algs:
        assert alg == str(pc.Formula(alg).reverse().reverse())

