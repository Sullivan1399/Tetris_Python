import pygame, sys
from game import Game
from PIL import Image
from colors import Colors

pygame.init()

# Game Tile Text
tile_font = pygame.font.Font(None, 40)

# Game Over Text
game_over_surface = pygame.Surface((250, 50))
game_over_font = pygame.font.Font(None, 55)
game_over_rect = pygame.Rect(0, 0, 250, 50)
pygame.draw.rect(game_over_surface, Colors.light_blue, game_over_rect, 0, 10)
game_over_text = game_over_font.render("GAME OVER", True, Colors.white)

screen_width, screen_height = 620, 655
game_zone_width, game_zone_height = 300, 600
rect_x = (screen_width - game_zone_width) // 2
rect_y = (screen_height - game_zone_height) // 2

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris Game")

# Resize background
original_image = Image.open("TetrisBG.jpg")
resized_image = original_image.resize((screen_width, screen_height))
resized_image.save("resized_tetris.jpg")  # save resized_image

bg = pygame.image.load("resized_tetris.jpg")
screen.blit(bg, (0, 0))

game_surface = pygame.Surface((game_zone_width, game_zone_height))
game_surface.fill(Colors.dark_blue)

clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            elif event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            elif event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            elif event.key == pygame.K_SPACE and game.game_over == False:
                game.drop_now()
        elif event.type == pygame.KEYUP and game.game_over == False:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
                game.stop()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.drop_down()
            

    # Update sprite(s)
    game.update()
    # Drawing
    game.draw(game_surface)
    screen.blit(game_surface, (rect_x, rect_y))
    
    score_surface = pygame.Surface((130, 110), pygame.SRCALPHA)
    score_rect = pygame.Rect(0, 0, 130, 110)
    pygame.draw.rect(score_surface, (0, 0, 0, 0), score_rect)
    screen.blit(score_surface, (480, 60))
    score = tile_font.render(str(game.score), True, Colors.white)
    score_surface.blit(score, score.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

    if game.game_over == True:
        game_over_surface.blit(game_over_text, (10, 10))
        screen.blit(game_over_surface, (rect_x + 26, rect_y + 250))
    pygame.display.update()
    clock.tick(60)