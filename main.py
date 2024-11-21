import pygame
import pygame.freetype
from algorithms import bfs
from maze_board import maze
pygame.init()

ROWS = len(maze)
COLS = len(maze[0])
WIDTH, HEIGHT = 1190, 770
SQUARE_SIZE_Y = HEIGHT // ROWS
SQUARE_SIZE_X = WIDTH // COLS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (120, 120, 120)
DARK_GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
FPS = 60
FONT = pygame.freetype.SysFont('arial', 50)
TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT = 300, 80

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path finding visualization")


def draw_maze(board: list[list[str]]) -> None:
    """
    Function draws a board representing a maze based on provided board.
    :param board: takes a maze written as a 2D list.
    :return: None
    """

    WIN.fill(GRAY)
    for x in range(SQUARE_SIZE_X, WIDTH, SQUARE_SIZE_X):
        pygame.draw.line(WIN, DARK_GRAY, (x, 0), (x, HEIGHT))

    for y in range(SQUARE_SIZE_Y, HEIGHT, SQUARE_SIZE_Y):
        pygame.draw.line(WIN, DARK_GRAY, (0, y), (WIDTH, y))

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            FONT.render_to(WIN, (j*70+20, i*70+20), col, DARK_GRAY)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)


def draw_rect(path: list, color: tuple) -> None:
    """
    Draws rectangles on the grid to mark walked path.
    :param path: list of tuples containing coordinates of maze nodes to be drawn
    :param color: color of the rectangles provided as a tuple of RGB color value
    :return: None
    """
    i, j = path[0]
    rect = pygame.Rect(j * 70 + 10, i * 70 + 10, SQUARE_SIZE_X - 20, SQUARE_SIZE_Y - 20)
    pygame.draw.rect(WIN, color, rect)
    path.pop(0)


def draw_buttons(num: int, names: list) -> None:
    """
    Draws selected number of buttons on the screen. current max=5
    :param num: how many buttons to draw
    :param names: list containing text to be drawn on the buttons
    :return: None
    """
    margin = 100
    padding = 40

    for i in range(num):
        x = (WIDTH - TEXT_BOX_WIDTH)/2
        y = margin + i * (TEXT_BOX_HEIGHT + padding)
        pygame.draw.rect(WIN, DARK_GRAY, [x, y, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT])
        FONT.render_to(WIN, ((WIDTH - TEXT_BOX_WIDTH)/2 + 10, margin + (i * (TEXT_BOX_HEIGHT + padding)+TEXT_BOX_HEIGHT/4)), names[i], WHITE)


def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(GRAY)
    draw_buttons(5, ["BFS", "N/A", "N/A", "N/A", "N/A"])

    maze_run = False
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not maze_run:
                mouse = pygame.mouse.get_pos()
                # if BFS chosen:
                if (((WIDTH - TEXT_BOX_WIDTH)/2 <= mouse[0] <= WIDTH/2 + TEXT_BOX_WIDTH/2) and
                        (100 <= mouse[1] <= 100 + TEXT_BOX_HEIGHT)):
                    draw_maze(board=maze)
                    path, visited = bfs(maze)
                    maze_run = True

            if maze_run:
                if event.type == SCREEN_UPDATE:
                    if len(visited) != 0:
                        draw_rect(visited, GREEN)
                    elif len(path) != 0:
                        draw_rect(path, RED)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
