from plane import Plane


def test_create():
    assert Plane() is not None
    assert Plane().points_count == 0
    assert Plane().maximum_distance_between_points == 0

def test_add_first_point():
    plane = Plane()
    plane.add_point((1,2))
    assert plane.points_count == 1
    assert plane.maximum_distance_between_points == 0
    assert plane.maximum_distance_points[0].point.x_coordinate == 1
    assert plane.maximum_distance_points[0].point.y_coordinate == 2
    assert plane.maximum_distance_points[1].point.x_coordinate == 1
    assert plane.maximum_distance_points[1].point.y_coordinate == 2


def test_add_two_points():
    plane = Plane()
    plane.add_point((1,2))
    plane.add_point((2,2))
    assert plane.points_count == 2
    assert plane.maximum_distance_between_points > 0


def test_statment_one():
    '''
    1 1 - 1 1
    2 1 - 1 2
    1 3 - 2 3
    '''

    plane = Plane()
    plane.add_point((1, 1))
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((2, 1))
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    assert 2 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((1, 3))
    assert 3 in plane.get_points_with_maximal_manhattan_distance()
    assert 2 in plane.get_points_with_maximal_manhattan_distance()


def test_statment_two():
    '''
    2 2 - 1 1 
    1 3 - 1 2 
    1 1 - 1 3 
    3 1 - 4 2 
    3 3 - 4 2
    '''

    plane = Plane()
    plane.add_point((2, 2))
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((1, 2))
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    assert 2 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((1, 1))
    assert 1 in plane.get_points_with_maximal_manhattan_distance()
    assert 3 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((3, 1))
    assert 4 in plane.get_points_with_maximal_manhattan_distance()
    assert 2 in plane.get_points_with_maximal_manhattan_distance()
    plane.add_point((3, 3))
    assert 3 in plane.get_points_with_maximal_manhattan_distance()
    assert 5 in plane.get_points_with_maximal_manhattan_distance()
    