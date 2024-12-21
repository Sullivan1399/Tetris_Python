# import pygame
# from PIL import Image

# # Khởi tạo pygame
# pygame.init()

# # Kích thước màn hình
# screen_width, screen_height = 600, 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Tetris Game")

# # Resize ảnh bằng PIL và lưu tạm thời
# original_image = Image.open("TetrisBG.jpg")
# resized_image = original_image.resize((screen_width, screen_height))
# resized_image.save("resized_tetris.jpg")  # Lưu ảnh resized

# # Tải ảnh làm background bằng pygame
# bg = pygame.image.load("resized_tetris.jpg")

# # Vẽ background lên màn hình
# screen.blit(bg, (0, 0))
# pygame.display.update()

# # Vòng lặp game
# exit_game = False
# while not exit_game:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit_game = True
#     pygame.display.update()

# # Thoát pygame
# pygame.quit()
score_board = {
    1: 100,
    2: 300,
    3: 500,
    4: 800
}
score = 0
lines_cleared = 4
move_down_points = 5
if move_down_points != 0:
    score += move_down_points

score += score_board[lines_cleared]

print(score)