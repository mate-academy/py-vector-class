import pytest

from app.main import Vector


def test_vector_instance():
    vector = Vector(3, 4)
    assert hasattr(vector, 'x'), (
        "Vector instance should have attribute 'x'"
    )
    assert hasattr(vector, 'y'), (
        "Vector instance should have attribute 'y'"
    )


def test_vector_decimals():
    vector = Vector(-2.343, 8.008)
    assert (vector.x, vector.y) == (-2.34, 8.01), (
        "Attributes 'x', 'y' should be rounded to two decimals."
    )


@pytest.mark.parametrize(
    'point1_x,point1_y,point2_x,point2_y,point3_x,point3_y',
    [
        (0, 0, 1, -2, 1, -2),
        (3.11, 5.56, 4.5, -10.2, 7.61, -4.64),
        (2, -2, -2, 2, 0, 0)
    ]
)
def test_vector_add(point1_x, point1_y, point2_x, point2_y, point3_x, point3_y):
    vector1 = Vector(point1_x, point1_y)
    vector2 = Vector(point2_x, point2_y)
    vector3 = vector1 + vector2
    assert isinstance(vector3, Vector), (
        "Result of addiction of Vectors should be Vector"
    )
    assert (vector3.x, vector3.y) == (point3_x, point3_y), (
        f"If coordinates of vector1 is {point1_x, point1_y}, "
        f"and coordinates of vector2 is {point2_x, point2_y},"
        f"addition of this vectors should be a vector with coordinates equal to {point3_x, point3_y}"
    )


@pytest.mark.parametrize(
    'point1_x,point1_y,point2_x,point2_y,point3_x,point3_y',
    [
        (0, 0, 1, -2, -1, 2),
        (3.11, 5.56, 4.5, -10.2, -1.39, 15.76),
        (2, -2, -2, 2, 4, -4)
    ]
)
def test_vector_sub(point1_x, point1_y, point2_x, point2_y, point3_x, point3_y):
    vector1 = Vector(point1_x, point1_y)
    vector2 = Vector(point2_x, point2_y)
    vector3 = vector1 - vector2
    assert isinstance(vector3, Vector), (
        "Result of subtraction of Vectors should be Vector"
    )
    assert (vector3.x, vector3.y) == (point3_x, point3_y), (
        f"If coordinates of vector1 is {point1_x}, {point1_y}, "
        f"and coordinates of vector2 is {point2_x}, {point2_y},"
        f"subtraction of this vectors should be a vector with coordinates equal to {point3_x}, {point3_y}"
    )


@pytest.mark.parametrize(
    'vector1_x,vector1_y,number,vector2_x,vector2_y',
    [
        (3.44, -4.19, 0, 0, 0),
        (2, 4, 3.743, 7.49, 14.97),
        (-20, -11.6, 7.989, -159.78, -92.67)
    ]
)
def test_vector_mul_number(vector1_x, vector1_y, number, vector2_x, vector2_y):
    vector1 = Vector(vector1_x, vector1_y)
    vector2 = vector1 * number
    assert isinstance(vector2, Vector), (
        "Result of multiplying Vector by number should be Vector"
    )
    assert (vector2.x, vector2.y) == (vector2_x, vector2_y), (
        f"If coordinates of vector1 is {vector1_x}, {vector1_y}, "
        f"result of multiplying vector1 by {number} should equal to {vector2_x}, {vector2_y}"
    )


@pytest.mark.parametrize(
    'vector1_x,vector1_y,vector2_x,vector2_y,result',
    [
        (0, 0, 1, -2, 0),
        (3.11, 5.56, 4.5, -10.2, -42.71699999999999),
        (2, 2, -2, 2, 0)
    ]
)
def test_vector_mul_vector(vector1_x, vector1_y, vector2_x, vector2_y, result):
    vector1 = Vector(vector1_x, vector1_y)
    vector2 = Vector(vector2_x, vector2_y)
    dot_product = vector1 * vector2
    assert dot_product == result, (
        f"Dot product of vector1 with coordinates {vector1_x}, {vector1_y}, "
        f"and vector2 with coordinates {vector2_x}, {vector2_y} should equal to {result}"
    )


@pytest.mark.parametrize(
    'start_point,end_point,vector_coords',
    [
        ((0, 0), (1, -2), (1, -2)),
        ((3.11, 5.56), (4.5, -10.2), (1.39, -15.76)),
        ((2, -2), (-2, 2), (-4, 4))
    ]
)
def test_create_vector_by_two_points(start_point, end_point, vector_coords):
    vector = Vector.create_vector_by_two_points(start_point, end_point)
    assert isinstance(vector, Vector), (
        "Result of 'create_vector_by_two_points' should be Vector"
    )
    assert (vector.x, vector.y) == vector_coords, (
        f"When 'start_point' equals to {start_point}, "
        f"and 'end_point' equals to {end_point}, "
        f"coordinates of result vector should equal to {vector_coords}"
    )


@pytest.mark.parametrize(
    'coords,length',
    [
        ((0, 10.44), 10.44),
        ((-4.44, 5.2), 6.837660418593483),
        ((-3.88, -4.98), 6.313065816225901),
    ]
)
def test_get_length(coords, length):
    vector = Vector(*coords)
    assert vector.get_length() == length, (
        f"When 'vector' coords equals to {coords}, "
        f"'vector.get_length()' should return {length}"
    )


@pytest.mark.parametrize(
    'coords,normalized_coords',
    [
        ((0, 10.44), (0.0, 1.0)),
        ((-4.44, 5.2), (-0.65, 0.76)),
        ((-3, -4), (-0.6, -0.8)),
    ]
)
def test_get_normalized(coords, normalized_coords):
    vector = Vector(*coords)
    normalized_vector = vector.get_normalized()
    assert (normalized_vector.x, normalized_vector.y) == normalized_coords, (
        f"When 'vector' coords equals to {coords}, "
        f"'vector.get_normalized()' should return vector "
        f"with coordinates {normalized_coords}"
    )


@pytest.mark.parametrize(
    'coords_1,coords_2,angle',
    [
        ((0, 10.44), (178, 0), 90),
        ((-4.44, 5.2), (15, -76), 151),
        ((-3, -4), (3, 4), 180),
    ]
)
def test_angle_between(coords_1, coords_2, angle):
    vector1 = Vector(*coords_1)
    vector2 = Vector(*coords_2)
    assert vector1.angle_between(vector2) == angle, (
        f"'vector1.angle_between(vector2)' should equal to {angle}, "
        f"when 'vector1' coordinates equal to {coords_1}, "
        f"and 'vector2' coordinates equal to {coords_2}"
    )


@pytest.mark.parametrize(
    'coords_1,angle',
    [
        ((0, 10.44), 0),
        ((-4.44, 5.2), 40),
        ((-3, -4), 143),
    ]
)
def test_get_angle(coords_1, angle):
    vector = Vector(*coords_1)
    assert vector.get_angle() == angle, (
        f"'vector.get_angle()' should equal to {angle}, "
        f"when 'vector' coordinates equal to {coords_1}"
    )


@pytest.mark.parametrize(
    'coords_1,degrees,coords_2',
    [
        ((33, 8), 1, (32.86, 8.57)),
        ((0, 10.44), 45, (-7.38, 7.38)),
        ((-3, -4), 233, (-1.39, 4.8))
    ]
)
def test_rotate(coords_1, degrees, coords_2):
    vector = Vector(*coords_1)
    vector2 = vector.rotate(degrees)
    assert isinstance(vector2, Vector), (
        "Result of 'vector.rotate(degrees)' should be Vector"
    )
    assert (vector2.x, vector2.y) == coords_2, (
        f"When 'vector' coordinates equal to {coords_1}, "
        f"and 'vector2' is 'vector.rotate({degrees})',"
        f"'vector2' coordinates should equal to {coords_2}"
    )
