from __future__ import annotations

class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:

        self._X = round(x_coordinate, 2)
        self._Y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:

        new_x = self._X + other._X
        new_y = self._Y + other._Y

        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:

        new_x = self._X - other._X
        new_y = self._Y - other._Y

        return Vector(new_x, new_y)

    def __mul__(self, other: (Vector, float, int))\
            -> (Vector, float, int):

        if isinstance(other, Vector):

            return (self._X * other._X) + (self._Y * other._Y)

        new_x = self._X * other
        new_y = self._Y * other

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
                                    cls,
                                    start_point: tuple,
                                    end_point: tuple
    ) -> Vector:

        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return Vector(new_x, new_y)

    def get_length(self) -> :