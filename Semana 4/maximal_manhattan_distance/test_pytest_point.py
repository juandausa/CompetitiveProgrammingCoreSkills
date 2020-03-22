from point import Point


def test_create():
    assert Point((0, 0)) is not None


def test_create_point_get_distance():
    point = Point((10, 10))
    assert point.maximal_manhattan_distance == 0
    assert point.maximal_manhattan_distance_coordinate == (10, 10)


def test_create_point_update_distance():
    point = Point((0, 0))
    other_point = Point((10, 10))
    point.update_manhattan_distance(other_point)
    assert point.maximal_manhattan_distance_coordinate == (10, 10)
    assert point.maximal_manhattan_distance > 0


def test_create_point_update_distance_several_times():
    point_a = Point((0, 0))
    point_b = Point((10, 10))
    point_a.update_manhattan_distance(point_b)
    point_c = Point((1, 1))
    point_a.update_manhattan_distance(point_c)
    assert point_a.maximal_manhattan_distance_coordinate == (point_b.x_coordinate, point_b.y_coordinate)
    assert point_a.maximal_manhattan_distance > 0

