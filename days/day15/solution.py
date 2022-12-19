import re
from time import perf_counter
from typing import NamedTuple

from shapely import LineString, MultiPolygon, Polygon, box, unary_union


class Point(NamedTuple):
    x: int
    y: int


def get_data() -> list[tuple[Point, Point]]:
    with open("input.txt", "r") as f:
        return [
            (Point(int(x1), int(y1)), Point(int(x2), int(y2)))
            for x1, y1, x2, y2 in re.findall(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                f.read(),
            )
        ]


def get_sensor_polygon(sensor: Point, beacon: Point) -> Polygon:
    d_mh = abs(beacon.x - sensor.x) + abs(beacon.y - sensor.y)

    return Polygon(
        [
            (sensor.x, sensor.y - d_mh),  # up
            (sensor.x + d_mh, sensor.y),  # right
            (sensor.x, sensor.y + d_mh),  # down
            (sensor.x - d_mh, sensor.y),  # left
        ]
    )


def get_all_sensors_poly(data: list[tuple[Point, Point]]) -> Polygon | MultiPolygon:
    return unary_union([get_sensor_polygon(sensor, beacon) for sensor, beacon in data])


def part1(row: int, data: list[tuple[Point, Point]]) -> int:
    sensors_poly = get_all_sensors_poly(data)
    beacons_on_row = {beacon for _, beacon in data if beacon.y == row}

    row_line = LineString(
        [(sensors_poly.bounds[0], row), (sensors_poly.bounds[2], row)]
    )

    intersections = row_line.intersection(sensors_poly)

    return int(intersections.length) + 1 - len(beacons_on_row)


def part2(lower_limit: int, upper_limit: int, data: list[tuple[Point, Point]]) -> int:
    sensors_poly = get_all_sensors_poly(data)

    square = box(lower_limit, lower_limit, upper_limit, upper_limit)

    differences = square.difference(sensors_poly)

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
