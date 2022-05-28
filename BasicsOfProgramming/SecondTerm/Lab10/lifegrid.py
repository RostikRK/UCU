"""
Lifegrid
"""

from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for row in range(0, self.num_rows()):
            for col in range(0, self.num_cols()):
                self.clear_cell(row, col)
        for tup in coord_list:
            self.set_cell(tup[0], tup[1])

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid[row, col] == self.LIVE_CELL:
            return True
        else:
            return False

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.DEAD_CELL

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.LIVE_CELL

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        counter = 0
        if 0 < row < (self.num_rows()-1) and 0 < col < (self.num_cols()-1):
            for rows in range(row-1, row+2):
                for cols in range(col-1, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == 0 and 0 < col < (self.num_cols()-1):
            for rows in range(row, row+2):
                for cols in range(col-1, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == 0 and col == 0:
            for rows in range(row, row+2):
                for cols in range(col, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == (self.num_rows()-1) and 0 < col < (self.num_cols()-1):
            for rows in range(row-1, row+1):
                for cols in range(col-1, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == (self.num_rows()-1) and col == (self.num_cols()-1):
            for rows in range(row-1, row+1):
                for cols in range(col-1, col+1):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif 0 < row < (self.num_rows()-1) and col == 0:
            for rows in range(row-1, row+2):
                for cols in range(col, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif 0 < row < (self.num_rows()-1) and col == (self.num_cols()-1):
            for rows in range(row-1, row+2):
                for cols in range(col-1, col+1):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == 0 and col == (self.num_cols()-1):
            for rows in range(row, row+2):
                for cols in range(col-1, col+1):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        elif row == (self.num_rows()-1) and col == 0:
            for rows in range(row-1, row+1):
                for cols in range(col, col+2):
                    if (rows, cols) != (row, col):
                        if self.is_live_cell(rows, cols) == True:
                            counter += 1
        return counter

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        string = ''
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                string += "L" if self._grid[i, j] == self.LIVE_CELL else "D"
            string += "\n"
        return string[:-1]
