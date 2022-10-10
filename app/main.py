class Vector:
    def __init__(self, x: (int, float), y: (int, float)) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: (int, float)) -> object:  # done -?
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):  # done - V
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)
    @staticmethod
    def create_vector_by_two_points(start_point, end_point):
