import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        self.size = width, height = 640, 480
        self.black = 0, 0, 0
        self.red = 255, 0, 0
        self.green = 0, 255, 0
        self.snake_speed = 10
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

        pygame.init()
        self.game_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake Game')
        self.fps = pygame.time.Clock()

    def game_run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.change_to = 'RIGHT'

            self.validate_direction()
            self.update_snake_pos()
            self.game_window.fill(self.black)
            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.game_window, self.red, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
            if self.snake_pos == self.food_pos:
                self.score += 1
                self.food_spawn = False
            self.show_score()
            pygame.display.flip()
            self.fps.tick(self.snake_speed)

    def validate_direction(self):
        if self.change_to == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = self.change_to
        if self.change_to == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = self.change_to
        if self.change_to == 'UP' and not self.direction == 'DOWN':
            self.direction = self.change_to
        if self.change_to == 'DOWN' and not self.direction == 'UP':
            self.direction = self.change_to

    def update_snake_pos(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10
        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos == self.food_pos:
            self.food_spawn = False
        else:
            self.snake_body.pop()

        if self.snake_pos[0] < 0 or self.snake_pos[0] > width-10:
            self.game_over()
        if self.snake_pos[1] < 0 or self.snake_pos[1] > height-10:
            self.game_over()

    def show_score(self):
        font = pygame.font.SysFont('Arial', 20)
        score_text = font.render('Score: ' + str(self.score), True, self.red)
        self.game_window.blit(score_text, [0, 0])

    def game_over(self):
        self.game_window.fill(self.black)
        font = pygame.font.SysFont('Arial', 40)
        game_over_text = font.render('Game Over', True, self.red)
        self.game_window.blit(game_over_text, [width/2 - 100, height/2 - 20])
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.game_run()