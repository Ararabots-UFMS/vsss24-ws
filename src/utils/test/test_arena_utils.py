import pytest
from utils import arena_utils
from utils.linalg import Vec2D

LEFT = 0
RIGHT = 1

################## get_defense_range_height ##################

@pytest.mark.parametrize(
    "height,    expected", 
    [(0,        0), 
     (30,       0),
     (50,       1),
     (100,      2),
     (150,      2),
     (200,      2),])
def test_get_defense_range_height(height, expected):

    result = arena_utils.get_defense_range_height(height=height)

    assert expected == result

################## on_attack_side ##################
    
@pytest.mark.parametrize(
    "pos,               team_side,  bias,   expected",
    [(Vec2D(0, 0),      LEFT,       0,      False),
     (Vec2D(50, 0),     RIGHT,      0,      True),
     (Vec2D(70, 0),     LEFT,       6,      True),
     (Vec2D(70, 0),     LEFT,       1,      False),
     (Vec2D(80, 0),     RIGHT,      6,      True),
     (Vec2D(80, 0),     LEFT,       -1,     True),
     (Vec2D(120, 0),    RIGHT,      10,     False),
     (Vec2D(70, 0),     RIGHT,      -1,     True)
    ])
def test_on_attack_side(pos, team_side, bias, expected):
    result = arena_utils.on_attack_side(pos, team_side, bias)
    
    assert expected == result

################## is_on_y_upper_half ##################
    
@pytest.mark.parametrize(
    "pos,               expected",
    [(Vec2D(70, 0),     False),
     (Vec2D(70, 50),    False),
     (Vec2D(80, 100),     True),
     (Vec2D(80, 150),    True),
     (Vec2D(120, 80),    True),
     (Vec2D(70, 75),    True)
    ])
def test_is_on_y_upper_half(pos, expected):
    result = arena_utils.is_on_y_upper_half(pos)
    
    assert expected == result