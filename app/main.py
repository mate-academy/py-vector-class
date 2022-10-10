class Vector:
    def __init__(self, x: (int, float), y: (int, float)) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: (int, float)) -> object:
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - end_point[1]
                   )

start_point = (5.2, 2.6)
end_point = (10.7, 6)

vector = Vector.create_vector_by_two_points(start_point, end_point)
