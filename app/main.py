class Vector:
    def __init__(self, x: (int, float), y: (int, float)) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + other_distance)