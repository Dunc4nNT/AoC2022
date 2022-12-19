import re
from time import perf_counter

from shapely import LineString, Point, Polygon, box, unary_union


def get_data() -> dict[Point, Point]:
    with open("input.txt") as f:
        return {
            Point(int(x1), int(y1)): Point(int(x2), int(y2))
            for x1, y1, x2, y2 in re.findall(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                f.read(),
            )
        }


def get_manhattan_distance_to(point_0: Point, point_1: Point) -> int:
    return abs(point_1.x - point_0.x) + abs(point_1.y - point_0.y)


def get_most_outer_points(sensor: Point, beacon: Point) -> list[tuple[int, int]]:
    d_mh = get_manhattan_distance_to(sensor, beacon)

    return [
        (sensor.x, sensor.y - d_mh),  # up
        (sensor.x + d_mh, sensor.y),  # right
        (sensor.x, sensor.y + d_mh),  # down
        (sensor.x - d_mh, sensor.y),  # left
    ]


def part1(row: int, data: dict[Point, Point]) -> int:
    all_sensors_list = []
    beacons_on_row = set()

    for sensor, beacon in data.items():
        all_sensors_list.append(Polygon(get_most_outer_points(sensor, beacon)))
        if beacon.y == row:
            beacons_on_row.add(beacon)

    all_sensors_poly = unary_union(all_sensors_list)
    min_x, min_y, max_x, max_y = all_sensors_poly.bounds
    row_line = LineString([(min_x, row), (max_x, row)])

    intersections = row_line.intersection(all_sensors_poly)

    return int(intersections.length) + 1 - len(beacons_on_row)


def part2(lower_limit: int, upper_limit: int, data: dict[Point, Point]) -> int:
    all_sensors_list = []

    for sensor, beacon in data.items():
        all_sensors_list.append(Polygon(get_most_outer_points(sensor, beacon)))

    all_sensors_poly = unary_union(all_sensors_list)
    square = box(lower_limit, lower_limit, upper_limit, upper_limit)

    differences = square.difference(all_sensors_poly)

    if isinstance(differences, Polygon):
        central_point = differences.centroid
    else:
        central_point = differences.geoms[0].centroid

    return int(central_point.x) * 4000000 + int(central_point.y)


if __name__ == "__main__":
    data = get_data()

    start1 = perf_counter()
    solution1 = part1(2000000, data)
    stop1 = perf_counter()

    print(f"Part 1: {solution1} ({round((stop1 - start1) * 1000, 3)}ms)")

    start2 = perf_counter()
    solution2 = part2(0, 4000000, data)
    stop2 = perf_counter()

    print(f"Part 2: {solution2} ({round((stop2 - start2) * 1000, 3)}ms)")
