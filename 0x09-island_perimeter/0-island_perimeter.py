#!/usr/bin/python3
"""Finds the perimeter of the island in a given grid"""

surveyed_land = set()


def get_direction_from(direction_to):
    """Returns the direction current cell would be from
        in next cell position. """
    if direction_to == "up":
        return "down"
    if direction_to == "down":
        return "up"
    if direction_to == "right":
        return "left"
    if direction_to == "left":
        return "right"


def survey_cell(grid, row, column, direction_from):
    """survey the given cell and checks it's surrounding"""
    surrounding_land = []
    surrounding_sea = 0
    # check left
    if (column - 1) >= 0:
        if grid[row][column - 1] == 1:
            # check if land is not already surveyed
            if direction_from != "left":
                surrounding_land.append(((row, column - 1), "left"))
        else:
            surrounding_sea += 1
    else:
        surrounding_sea += 1
    # check right
    if (column + 1) < len(grid[0]):
        if grid[row][column + 1] == 1:
            if direction_from != "right":
                surrounding_land.append(((row, column + 1), "right"))
        else:
            surrounding_sea += 1
    else:
        surrounding_sea += 1
    # check up
    if (row - 1) >= 0:
        if grid[row - 1][column] == 1:
            if direction_from != "up":
                surrounding_land.append(((row - 1, column), "up"))
        else:
            surrounding_sea += 1
    else:
        surrounding_sea += 1
    # check down
    if (row + 1) < len(grid):
        if grid[row + 1][column] == 1:
            if direction_from != "down":
                surrounding_land.append(((row + 1, column), "down"))
        else:
            surrounding_sea += 1
    else:
        surrounding_sea += 1
    surveyed_land.add((row, column))
    return (surrounding_sea, surrounding_land)


def count_in_one_direction(grid, pos_dir):
    """Counts the perimeter in a given direction until the end"""
    perimeter = 0
    start_pos, direction = pos_dir
    direction_to, direction_from = direction
    row, column = start_pos
    while grid[row][column] == 1:
        if (row, column) in surveyed_land:
            return perimeter
        surrounding_sea, surrounding_land = survey_cell(grid, row,
                                                        column, direction_from)
        perimeter += surrounding_sea
        if len(surrounding_land) == 0:
            return perimeter
        elif len(surrounding_land) == 1:
            next_pos, dir = surrounding_land[0]
            if dir == direction_to:
                row, column = next_pos
                continue
            else:
                dir_from = get_direction_from(dir)
                perimeter += count_in_one_direction(grid, (next_pos,
                                                           (dir, dir_from)))
                return perimeter
        elif len(surrounding_land) == 2:
            land1, land2 = surrounding_land
            if land1[1] == direction_to:
                dir_from = get_direction_from(land2[1])
                perimeter += count_in_one_direction(grid, (land2[0],
                                                           (land2[1],
                                                            dir_from)))
                row, column = land1[0]
                continue
            elif land2[1] == direction_to:
                dir_from = get_direction_from(land1[1])
                perimeter += count_in_one_direction(grid, (land1[0],
                                                           (land1[1],
                                                            dir_from)))
                row, column = land2[0]
                continue
            else:
                dir_from = get_direction_from(land2[1])
                perimeter += count_in_one_direction(grid, (land2[0],
                                                           (land2[1],
                                                            dir_from)))
                dir_from = get_direction_from(land1[1])
                perimeter += count_in_one_direction(grid, (land1[0],
                                                           (land1[1],
                                                            dir_from)))
                return perimeter
        elif len(surrounding_land) == 3:
            land1, land2, land3 = surrounding_land
            if land3[1] == direction_to:
                dir_from = get_direction_from(land2[1])
                perimeter += count_in_one_direction(grid, (land2[0],
                                                           (land2[1],
                                                            dir_from)))
                dir_from = get_direction_from(land1[1])
                perimeter += count_in_one_direction(grid, (land1[0],
                                                           (land1[1],
                                                            dir_from)))
                row, column = land3[0]
                continue
            elif land2[1] == direction_to:
                dir_from = get_direction_from(land3[1])
                perimeter += count_in_one_direction(grid, (land3[0],
                                                           (land3[1],
                                                            dir_from)))
                dir_from = get_direction_from(land1[1])
                perimeter += count_in_one_direction(grid, (land1[0],
                                                           (land1[1],
                                                            dir_from)))
                row, column = land2[0]
                continue
            if land1[1] == direction_to:
                dir_from = get_direction_from(land2[1])
                perimeter += count_in_one_direction(grid, (land2[0],
                                                           (land2[1],
                                                            dir_from)))
                dir_from = get_direction_from(land3[1])
                perimeter += count_in_one_direction(grid, (land3[0],
                                                           (land3[1],
                                                            dir_from)))
                row, column = land1[0]
                continue


def island_perimeter(grid):
    """Returns the perimeter of a given island in the grid"""
    perimeter = 0
    for row_index, row in enumerate(grid):
        for col_index, column in enumerate(row):
            if column == 1:
                surrounding_sea, surrounding_land = survey_cell(grid,
                                                                row_index,
                                                                col_index,
                                                                "sea")
                perimeter += surrounding_sea
                if len(surrounding_land) == 0:
                    return perimeter
                elif len(surrounding_land) == 1:
                    next_pos, dir = surrounding_land[0]
                    dir_from = get_direction_from(dir)
                    perimeter += count_in_one_direction(grid, (next_pos,
                                                               (dir,
                                                                dir_from)))
                    return perimeter
                elif len(surrounding_land) == 2:
                    land1, land2 = surrounding_land
                    dir_from = get_direction_from(land2[1])
                    perimeter += count_in_one_direction(grid, (land2[0],
                                                               (land2[1],
                                                                dir_from)))
                    dir_from = get_direction_from(land1[1])
                    perimeter += count_in_one_direction(grid, (land1[0],
                                                               (land1[1],
                                                                dir_from)))
                    return perimeter
    return perimeter
