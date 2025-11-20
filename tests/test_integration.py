from sunflower.maker import make_sunflower

def test_end_to_end():
    sunflower = make_sunflower()
    with open("tests/data/sunflower-expected.svg", "r") as filein:
        expected_sunflower = filein.read()

    assert sunflower == expected_sunflower

