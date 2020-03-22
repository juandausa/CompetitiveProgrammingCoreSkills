from point import Point

class PlanePoint(object):
    def __init__(self, point, order):
        self.point = point
        self.order = order
        self.key = (point.x_coordinate, point.y_coordinate)


class Plane(object):
    def __init__(self):
        self.points = dict()
        self.points_count = 0
        self.maximum_distance_between_points = 0
        self.maximum_distance_points = None
    
    def add_point(self, coordinates):
        assert not coordinates in self.points.keys()
        self.points_count += 1
        new_plane_ponit = PlanePoint(Point(coordinates), self.points_count)
        self.points[new_plane_ponit.key] = new_plane_ponit
        for key in self.points:
            plane_point = self.points[key]
            plane_point.point.update_manhattan_distance(new_plane_ponit.point)
            new_plane_ponit.point.update_manhattan_distance(plane_point.point)
            if (self.maximum_distance_between_points < new_plane_ponit.point.maximal_manhattan_distance or self.maximum_distance_points is None):
                self.maximum_distance_between_points = new_plane_ponit.point.maximal_manhattan_distance
                self.maximum_distance_points = [plane_point, new_plane_ponit]

    def get_points_with_maximal_manhattan_distance(self):
        return (self.maximum_distance_points[0].order, self.maximum_distance_points[1].order)
