import queue


class Utilities:
    """
    Class made to hold methods used by multiple algorithms
    """
    @staticmethod
    def find_start_pos(board: list[list[str]], symbol: str = "O") -> tuple[int, int]:
        """
        Finds starting position for given board and symbol
        :param board: takes a maze written as a 2D list.
        :param symbol: takes a string representing the starting position
        :return: tuple containing the position of the starting symbol
        """

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == symbol:
                    return i, j

    @staticmethod
    def find_neighbours(row: int, col: int, board: list[list[str]]) -> list[tuple[int, int]]:
        """
        For a given node of a graph generate a list of its neighbours, saved as tuples of their coordinates in graph
        :param row: row of the current node
        :param col: col of the current node
        :param board: graph consisting the node
        :return: list of nodes neighbouring given node
        """
        neighbours = []

        if row > 0:  # Upper neighbour
            neighbours.append((row-1, col))
        if row < len(board) - 1:  # Lower neighbour
            neighbours.append((row+1, col))
        if col > 0:  # Left neighbour
            neighbours.append((row, col-1))
        if col < len(board[0]) - 1:  # Right neighbour
            neighbours.append((row, col+1))

        return neighbours


def bfs(board: list[list[str]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """
    Finds the shortest path to the exit using breadth-first search algorithm.
    :param board: takes a maze written as a 2D list.
    :return: (Path, Visited) Path - a list containing tuples with positions of nodes of the shortest path and Visited -
            list of visited nodes
    """
    end = "X"
    start = Utilities.find_start_pos(board)
    visited = [start]
    q = queue.Queue()
    q.put((start, [start]))

    while not q.empty():
        current, path = q.get()
        row, col = current

        if board[row][col] == end:
            visited.append((row, col))
            return path, visited

        if (row, col) not in visited:
            visited.append((row, col))

        neighbours = Utilities.find_neighbours(row, col, board)
        for neighbour in neighbours:
            r, c = neighbour
            if neighbour in visited:
                continue
            if board[r][c] == "#":
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
 