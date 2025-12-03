import os, re
import sunflower.maker


def test_sunflower_is_string():
    # ARRANGE

    # ACT
    img = sunflower.maker.make_sunflower(0)

    # ASSERT
    assert isinstance(img, str)

def test_sunflower_maker_produces_svg():
    # ARRANGE
    img = sunflower.maker.make_sunflower(0)

    # ACT
    matches = re.findall("<svg .*>.*</svg>", img)

    # ASSERT
    assert len(matches) > 0
