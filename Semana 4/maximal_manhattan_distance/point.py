class Point(object):
    def __init__(self, coordinate):
        self.x_coordinate = coordinate[0]
        self.y_coordinate = coordinate[1]
        self.order = 0
        self.maximal_manhattan_distance = 0
        self.maximal_manhattan_distance_coordinate = (
            self.x_coordinate, self.y_coordinate)

    def update_manhattan_distance(self, point):
        distance = self.calculate_manhattan_distance((point.x_coordinate, point.y_coordinate))
        if (self.maximal_manhattan_distance < distance):
            self.maximal_manhattan_distance = distance
            self.maximal_manhattan_distance_coordinate = (point.x_coordinate, point.y_coordinate)

    def calculate_manhattan_distance(self, coordinate):
        return abs(self.x_coordinate-coordinate[0]) + abs(self.y_coordinate-coordinate[1])
