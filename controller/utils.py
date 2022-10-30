def convert_list_coords_brackets_parenthesis(list_coords):
    list_without_brackets = []

    for elements in list_coords:
        coord_x, coord_y = elements[0], elements[1]

        list_without_brackets.append((coord_x, coord_y))

    return list_without_brackets