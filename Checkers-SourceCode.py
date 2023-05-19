import time
import random
import pygame
import sys
import copy
import webcolors


def level_selection():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 750
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Configuration")

    # Define colors
    BROWN = (16, 78, 139)
    WHITE = (255, 233, 197)
    BLACK = (0, 0, 0)

    # Define font
    font = pygame.font.Font(None, 32)

    # Initialize level, strategy, and algorithm selection
    level = None
    algorithm = None

    # Load header image
    # header_image = pygame.image.load("pics/bar2.png")

    # Create level section
    level_section = pygame.Rect(150, 350, screen_width - 280, 125)
    level_title = font.render("Game Difficulty", True, WHITE)
    level_title_rect = level_title.get_rect(center=(level_section.centerx, level_section.top + 30))

    easy_button = pygame.Rect(level_section.left + 20, level_section.top + 70, 20, 20)
    medium_button = pygame.Rect(level_section.left + 180, level_section.top + 70, 20, 20)
    hard_button = pygame.Rect(level_section.left + 340, level_section.top + 70, 20, 20)

    # Create algorithm section
    algorithm_section = pygame.Rect(80, 200, screen_width - 150, 125)
    algorithm_title = font.render("Select the Algorithm", True, WHITE)
    algorithm_title_rect = algorithm_title.get_rect(center=(algorithm_section.centerx, algorithm_section.top + 30))

    minimax_button = pygame.Rect(algorithm_section.left + 70, algorithm_section.top + 70, 20, 20)
    alpha_beta_button = pygame.Rect(algorithm_section.left + 280, algorithm_section.top + 70, 20, 20)

    # Create Play button
    play_button = pygame.Rect(level_section.centerx - 50, level_section.bottom + 30, 100, 50)
    play_text = font.render("Play", True, WHITE)
    play_text_rect = play_text.get_rect(center=play_button.center)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the level buttons are clicked
                if easy_button.collidepoint(mouse_pos):
                    level = 1
                elif medium_button.collidepoint(mouse_pos):
                    level = 2
                elif hard_button.collidepoint(mouse_pos):
                    level = 3

                # Check if the algorithm buttons are clicked
                if minimax_button.collidepoint(mouse_pos):
                    algorithm = "Minimax"
                elif alpha_beta_button.collidepoint(mouse_pos):
                    algorithm = "Alpha"

                # Check if the Play button is clicked
                if play_button.collidepoint(mouse_pos):
                    if level is not None and algorithm is not None and level != 0:
                        running = False

        # Fill the screen with background color
        screen.fill(color=(178, 34, 34))

        # Draw header image
        # screen.blit(header_image, (5, -10))

        # Draw the level section
        pygame.draw.rect(screen, WHITE, level_section, 2)
        screen.blit(level_title, level_title_rect)
        pygame.draw.rect(screen, BROWN if level == 1 else WHITE, easy_button, width=2 if level != 1 else 0)
        pygame.draw.rect(screen, BROWN if level == 2 else WHITE, medium_button, width=2 if level != 2 else 0)
        pygame.draw.rect(screen, BROWN if level == 3 else WHITE, hard_button, width=2 if level != 3 else 0)
        easy_text = font.render("Easy", True, WHITE)
        easy_text_rect = easy_text.get_rect()
        easy_text_rect.center = easy_button.center
        screen.blit(easy_text, (easy_button.right + 10, easy_button.centery - easy_text.get_height() // 2))
        medium_text = font.render("Medium", True, WHITE)
        medium_text_rect = medium_text.get_rect()
        medium_text_rect.center = medium_button.center
        screen.blit(medium_text, (medium_button.right + 10, medium_button.centery - medium_text.get_height() // 2))
        hard_text = font.render("Hard", True, WHITE)
        hard_text_rect = hard_text.get_rect()
        hard_text_rect.center = hard_button.center
        screen.blit(hard_text, (hard_button.right + 10, hard_button.centery - hard_text.get_height() // 2))

        # Draw the algorithm section
        pygame.draw.rect(screen, WHITE, algorithm_section, 2)
        screen.blit(algorithm_title, algorithm_title_rect)
        pygame.draw.rect(screen, BROWN if algorithm == "Minimax" else WHITE, minimax_button,
                         width=2 if algorithm != "Minimax" else 0)
        pygame.draw.rect(screen, BROWN if algorithm == "Alpha" else WHITE, alpha_beta_button,
                         width=2 if algorithm != "Alpha" else 0)
        minimax_text = font.render("Minimax", True, WHITE)
        minimax_text_rect = minimax_text.get_rect()
        minimax_text_rect.midleft = (minimax_button.right + 10, minimax_button.centery)
        screen.blit(minimax_text, minimax_text_rect)
        alpha_beta_text = font.render("Minimax with Alpha-Beta", True, WHITE)
        alpha_beta_text_rect = alpha_beta_text.get_rect()
        alpha_beta_text_rect.midleft = (alpha_beta_button.right + 10, alpha_beta_button.centery)
        screen.blit(alpha_beta_text, alpha_beta_text_rect)

        # Draw the Play button
        pygame.draw.rect(screen, BROWN, play_button)
        screen.blit(play_text, play_text_rect)

        # Update the display
        pygame.display.flip()

    # Return the selected level, strategy, and algorithm
    return level, algorithm


def start_gui(Board):
    Brown = (139, 26, 26)
    WHITE = (255, 233, 197)
    DarkPieces = sum(row.count("DD") + row.count("DDK") for row in Board)
    WhitePieces = sum(row.count("DW") + row.count("DWK") for row in Board)

    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the screen
    screen_width = 725
    screen_height = 800  # Increased height to fill the bottom plank space
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Set the dimensions of the board
    board_size = 725
    board_width = board_size
    board_height = board_size

    # Create a surface for the board
    board_surface = pygame.Surface([board_width, board_height])
    # header_image = pygame.image.load("pics/count.png")
    # Get the dimensions of the image
    # image_width = header_image.get_width()
    # image_height = header_image.get_height()

    # Set the position to write the numbers (middle of the image)
    # number_x = image_width // 2
    # number_y = image_height // 2

    # Set the font and size for the numbers
    font = pygame.font.Font(None, 36)

    # Render the numbers as text
    whitecount = font.render(str(WhitePieces), True, (0, 0, 0))  # Replace "123" with the desired number
    darkcount = font.render(str(DarkPieces), True, (0, 0, 0))  # Replace "123" with the desired number

    # Get the dimensions of the rendered text
    text_width = whitecount.get_width()
    text_height = whitecount.get_height()

    # Calculate the position to blit the numbers (centered)
    # number_pos_x = number_x - (text_width // 2)
    # number_pos_y = number_y - (text_height // 2)

    # Blit the image onto the screen
    # Blit the numbers onto the screen
    # screen.blit(header_image, (-5, -20))
    # screen.blit(darkcount, (number_pos_x - 115, number_pos_y - 30))
    # screen.blit(whitecount, (number_pos_x - 45, number_pos_y - 30))

    # Draw the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = Brown
            pygame.draw.rect(board_surface, color,
                             [col * (board_size / 8), row * (board_size / 8), (board_size / 8), (board_size / 8)])

    # Set the position of the board on the screen
    board_x = 0
    board_y = 0

    # Load the images for the checkers and scale them down
    DD = pygame.image.load('pics/darkpng.png')
    DW = pygame.image.load('pics/whitepng.png')
    DDK = pygame.image.load('pics/darkKing.png')
    DWK = pygame.image.load('pics/WhiteKing.png')
    DW = pygame.transform.scale(DW, (int(board_size / 8), int(board_size / 8)))
    DD = pygame.transform.scale(DD, (int(board_size / 8), int(board_size / 8)))
    DDK = pygame.transform.scale(DDK, (int(board_size / 8), int(board_size / 8)))
    DWK = pygame.transform.scale(DWK, (int(board_size / 8), int(board_size / 8)))

    # Place the checkers on the board
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'DW':
                board_surface.blit(DW, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DD':
                board_surface.blit(DD, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DDK':
                board_surface.blit(DDK, (col * (board_size / 8), row * (board_size / 8)))
            elif board[row][col] == 'DWK':
                board_surface.blit(DWK, (col * (board_size / 8), row * (board_size / 8)))

    # Draw the board on the screen
    screen.blit(board_surface, [board_x, board_y])

    # Update the display
    pygame.display.flip()


def create_board():
    Board = [["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
             ["DD", "W", "DD", "W", "DD", "W", "DD", "W"],
             ["W", "DD", "W", "DD", "W", "DD", "W", "DD"],
             ["D", "W", "D", "W", "D", "W", "D", "W"],
             ["W", "D", "W", "D", "W", "D", "W", "D"],
             ["DW", "W", "DW", "W", "DW", "W", "DW", "W"],
             ["W", "DW", "W", "DW", "W", "DW", "W", "DW"],
             ["DW", "W", "DW", "W", "DW", "W", "DW", "W"]
             ]

    return Board


def small_legal_moves(board, player):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player or board[row][col] == player + "K":
                # check for valid diagonal moves
                if player == "DD":
                    # Dark king reverse moves
                    if board[row][col] == player + 'K':
                        if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row - 1, col - 1)])
                        if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row - 1, col + 1)])
                        if row > 1 and col > 1 and (
                                board[row - 1][col - 1].startswith("DW") or board[row - 1][col - 1].startswith(
                            "DWK")) and board[row - 2][
                            col - 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col - 2)])
                        if row > 1 and col < 6 and (
                                board[row - 1][col + 1].startswith("DW") or board[row - 1][col + 1].startswith(
                            "DWK")) and board[row - 2][
                            col + 2] == "D":
                            legal_moves.append([(row, col), (row - 2, col + 2)])
                    # Dark king reverse moves
                    # dark pieces moves
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    if row < 6 and col > 1 and (
                            board[row + 1][col - 1].startswith("DW") or board[row + 1][col - 1].startswith("DWK")) and \
                            board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                    if row < 6 and col < 6 and (
                            board[row + 1][col + 1].startswith("DW") or board[row + 1][col + 1].startswith("DWK")) and \
                            board[row + 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                    # dark pieces moves
                elif player == "DW":
                    # White king reverse moves
                    if board[row][col] == player + 'K':
                        if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col - 1)])
                        if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col + 1)])
                        if row < 6 and col > 1 and (
                                board[row + 1][col - 1].startswith("DD") or board[row + 1][col - 1].startswith(
                            "DDK")) and board[row + 2][col - 2] == "D":
                            legal_moves.append(((row, col), (row + 2, col - 2)))
                        if row < 6 and col < 6 and (
                                board[row + 1][col + 1].startswith("DD") or board[row + 1][col + 1].startswith(
                            "DDK")) and board[row + 2][col + 2] == "D":
                            legal_moves.append([(row, col), (row + 2, col + 2)])
                    # White king reverse moves
                    # White pieces moves
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                    if row > 1 and col > 1 and (
                            board[row - 1][col - 1].startswith("DD") or board[row - 1][col - 1].startswith("DDK")) and \
                            board[row - 2][col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                    if row > 1 and col < 6 and (
                            board[row - 1][col + 1].startswith("DD") or board[row - 1][col + 1].startswith("DDK")) and \
                            board[row - 2][col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
                    # White pieces moves
    return legal_moves


def get_legal_moves(board, player):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player or board[row][col] == player + "K":
                # check for valid diagonal moves
                if player == "DD":
                    if board[row][col] == player + 'K':
                        if board[row][col] == player + 'K':
                            # Dark King moves
                            # -----------------------------------------------------------------------------------------
                            if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                                legal_moves.append([(row, col), (row - 1, col - 1)])
                            if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                                legal_moves.append([(row, col), (row - 1, col + 1)])
                            # first left eat(First cond)
                            if row > 1 and col > 1 and (
                                    board[row - 1][col - 1].startswith("DW") or board[row - 1][col - 1].startswith(
                                "DWK")) and board[row - 2][
                                col - 2] == "D":
                                legal_moves.append([(row, col), (row - 2, col - 2)])
                                newRow = row - 2
                                newCol = col - 2
                                # second right eat
                                if newRow > 1 and newCol < 6 and (
                                        board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                    newCol + 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    newRow = newRow - 2
                                    newCol = newCol + 2
                                    # third right eat
                                    if row > 1 and col < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if row > 1 and col > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # second left eat
                                if newRow > 1 and newCol > 1 and (
                                        board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                    newCol - 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                    newRow = newRow - 2
                                    newCol = newCol - 2
                                    # third right eat
                                    if newRow > 1 and col < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            # ------------------------------------------------------------------------------------------------
                            # first right eat (Second cond)
                            if row > 1 and col < 6 and (
                                    board[row - 1][col + 1].startswith("DW") or board[row - 1][col + 1].startswith(
                                "DWK")) and board[row - 2][
                                col + 2] == "D":
                                legal_moves.append([(row, col), (row - 2, col + 2)])
                                newRow = row - 2
                                newCol = col + 2
                                # second right eat
                                if newRow > 1 and newCol < 6 and (
                                        board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                    newCol + 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    newRow = newRow - 2
                                    newCol = newCol + 2
                                    # third right eat
                                    if newRow > 1 and newCol < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # second left eat
                                if newRow > 1 and newCol > 1 and (
                                        board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                    newCol - 1].startswith("DWK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                    newRow = newRow - 2
                                    newCol = newCol - 2
                                    # third right eat
                                    if newRow > 1 and newCol < 6 and (
                                            board[newRow - 1][newCol + 1].startswith("DW") or board[newRow - 1][
                                        newCol + 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol + 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                                    # third left eat
                                    if newRow > 1 and newCol > 1 and (
                                            board[newRow - 1][newCol - 1].startswith("DW") or board[newRow - 1][
                                        newCol - 1].startswith("DWK")) and \
                                            board[newRow - 2][newCol - 2] == "D":
                                        legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            # Dark King moves
                            # -----------------------------------------------------------------------------------------

                    # Diagonal jumps
                    if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col - 1)])
                    if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row + 1, col + 1)])
                    # Diagonal jumps

                    # Multiple jumps
                    # first left eat (First cond)
                    if row < 6 and col > 1 and (
                            board[row + 1][col - 1].startswith("DW") or board[row + 1][col - 1].startswith("DWK")) and \
                            board[row + 2][col - 2] == "D":
                        legal_moves.append(((row, col), (row + 2, col - 2)))
                        newRow = row + 2
                        newCol = col - 2
                        # second right eat
                        if newRow < 6 and newCol < 6 and (
                                board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                            newCol + 1].startswith("DWK")) and \
                                board[newRow + 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            newRow = newRow + 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # second left eat
                        if newRow < 6 and newCol > 1 and (
                                board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                            newCol - 1].startswith("DWK")) and \
                                board[newRow + 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            newRow = newRow + 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow < 6 and col < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                    # ------------------------------------------------------------------------------------------------
                    # first right eat (Second cond)
                    if row < 6 and col < 6 and (
                            board[row + 1][col + 1].startswith("DW") or board[row + 1][col + 1].startswith("DWK")) and \
                            board[row + 2][
                                col + 2] == "D":
                        legal_moves.append([(row, col), (row + 2, col + 2)])
                        newRow = row + 2
                        newCol = col + 2
                        # second right eat
                        if newRow < 6 and newCol < 6 and (
                                board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                            newCol + 1].startswith("DWK")) and \
                                board[newRow + 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            newRow = newRow + 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # second left eat
                        if newRow < 6 and newCol > 1 and (
                                board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                            newCol - 1].startswith("DWK")) and \
                                board[newRow + 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            newRow = newRow + 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DW") or board[newRow + 1][
                                newCol + 1].startswith("DWK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                            # third left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DW") or board[newRow + 1][
                                newCol - 1].startswith("DWK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                # multiple jumps
                elif player == "DW":
                    if board[row][col] == player + 'K':
                        # White King moves
                        # -----------------------------------------------------------------------------------------
                        # first left eat (First cond)
                        if row < 7 and col > 0 and board[row + 1][col - 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col - 1)])
                        if row < 7 and col < 7 and board[row + 1][col + 1] == "D":
                            legal_moves.append([(row, col), (row + 1, col + 1)])
                        if row < 6 and col > 1 and (
                                board[row + 1][col - 1].startswith("DD") or board[row + 1][col - 1].startswith(
                            "DDK")) and board[row + 2][col - 2] == "D":
                            legal_moves.append(((row, col), (row + 2, col - 2)))
                            newRow = row + 2
                            newCol = col - 2
                            # second right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                newRow = newRow + 2
                                newCol = newCol + 2
                                # third right eat
                                if row < 6 and col < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if row < 6 and col > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            # second left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                newRow = newRow + 2
                                newCol = newCol - 2
                                # third right eat
                                if newRow < 6 and col < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (board[newRow + 1][newCol - 1].startswith(
                                        "DD") or board[newRow + 1][newCol - 1].startswith("DDK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # ------------------------------------------------------------------------------------------------
                        # first right eat (Second cond)
                        if row < 6 and col < 6 and (
                                board[row + 1][col + 1].startswith("DD") or board[row + 1][col + 1].startswith(
                            "DDK")) and board[row + 2][
                            col + 2] == "D":
                            legal_moves.append([(row, col), (row + 2, col + 2)])
                            newRow = row + 2
                            newCol = col + 2
                            # second right eat
                            if newRow < 6 and newCol < 6 and (
                                    board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                newRow = newRow + 2
                                newCol = newCol + 2
                                # third right eat
                                if newRow < 6 and newCol < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                            # second left eat
                            if newRow < 6 and newCol > 1 and (
                                    board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow + 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                                newRow = newRow + 2
                                newCol = newCol - 2
                                # third right eat
                                if newRow < 6 and newCol < 6 and (
                                        board[newRow + 1][newCol + 1].startswith("DD") or board[newRow + 1][
                                    newCol + 1].startswith("DDK")) and \
                                        board[newRow + 2][newCol + 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol + 2)])
                                # third left eat
                                if newRow < 6 and newCol > 1 and (
                                        board[newRow + 1][newCol - 1].startswith("DD") or board[newRow + 1][
                                    newCol - 1].startswith("DDK")) and \
                                        board[newRow - 2][newCol - 2] == "D":
                                    legal_moves.append([(newRow, newCol), (newRow + 2, newCol - 2)])
                        # White King moves -----------------------------------------------------------------------------------------

                    # Digonal moves
                    if row > 0 and col > 0 and board[row - 1][col - 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col - 1)])
                    if row > 0 and col < 7 and board[row - 1][col + 1] == "D":
                        legal_moves.append([(row, col), (row - 1, col + 1)])
                        # Digonal moves
                        # multiple jumps

                        # first left eat(First cond)
                    if row > 1 and col > 1 and (
                            board[row - 1][col - 1].startswith("DD") or board[row - 1][col - 1].startswith("DDK")) and \
                            board[row - 2][
                                col - 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col - 2)])
                        newRow = row - 2
                        newCol = col - 2
                        # second right eat
                        if newRow > 1 and newCol < 6 and (
                                board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                            newCol + 1].startswith("DDK")) and \
                                board[newRow - 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            newRow = newRow - 2
                            newCol = newCol + 2
                            # third right eat
                            if row > 1 and col < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if row > 1 and col > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                        # second left eat
                        if newRow > 1 and newCol > 1 and (
                                board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                            newCol - 1].startswith("DDK")) and \
                                board[newRow - 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            newRow = newRow - 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow > 1 and col < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                    # ------------------------------------------------------------------------------------------------
                    # first right eat (Second cond)
                    if row > 1 and col < 6 and (
                            board[row - 1][col + 1].startswith("DD") or board[row - 1][col + 1].startswith("DDK")) and \
                            board[row - 2][
                                col + 2] == "D":
                        legal_moves.append([(row, col), (row - 2, col + 2)])
                        newRow = row - 2
                        newCol = col + 2
                        # second right eat
                        if newRow > 1 and newCol < 6 and (
                                board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                            newCol + 1].startswith("DDK")) and \
                                board[newRow - 2][newCol + 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            newRow = newRow - 2
                            newCol = newCol + 2
                            # third right eat
                            if newRow > 1 and newCol < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                        # second left eat
                        if newRow > 1 and newCol > 1 and (
                                board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                            newCol - 1].startswith("DDK")) and \
                                board[newRow - 2][newCol - 2] == "D":
                            legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                            newRow = newRow - 2
                            newCol = newCol - 2
                            # third right eat
                            if newRow > 1 and newCol < 6 and (
                                    board[newRow - 1][newCol + 1].startswith("DD") or board[newRow - 1][
                                newCol + 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol + 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol + 2)])
                            # third left eat
                            if newRow > 1 and newCol > 1 and (
                                    board[newRow - 1][newCol - 1].startswith("DD") or board[newRow - 1][
                                newCol - 1].startswith("DDK")) and \
                                    board[newRow - 2][newCol - 2] == "D":
                                legal_moves.append([(newRow, newCol), (newRow - 2, newCol - 2)])
                                # multiple jumps
                                # check for valid diagonal moves

    return legal_moves
