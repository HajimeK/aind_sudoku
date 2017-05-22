from utils import boxes

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    elements = []
    notDeterminedBoxValue = '123456789'
    for c in grid:
        if c == '.':
            elements.append(notDeterminedBoxValue)
        elif c in notDeterminedBoxValue:
            elements.append(c)
    return dict(zip(boxes, elements))
