import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
pygame.display.set_caption("SNAKE")
score = 0
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [
            # Point(
            #     x=WIDTH // BLOCK_SIZE // 2,
            #     y=HEIGHT // BLOCK_SIZE // 2,
            # ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        new_head = Point(self.body[0].x + dx, self.body[0].y + dy)
        # if new_head.x < 0 or new_head.x >= WIDTH // BLOCK_SIZE or new_head.y < 0 or new_head.y >= HEIGHT // BLOCK_SIZE:
        #     return False
        if new_head.x > WIDTH // BLOCK_SIZE:
            new_head.x = 0
        elif new_head.x < 0:
            new_head.x = WIDTH // BLOCK_SIZE
        elif new_head.y < 0:
            new_head.y = WIDTH // BLOCK_SIZE
        elif new_head.y > HEIGHT // BLOCK_SIZE:
            new_head.y = 0
        for body in self.body[1:]:
            if new_head.x == body.x and new_head.y == body.y:
                pygame.quit()
                quit()
                # return False
        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)
        
class Food:
    def __init__(self, x, y):
        self.location = self.generate_location()

    def generate_location(self):
        while True:
            x = random.randint(0,WIDTH//BLOCK_SIZE-1)
            y = random.randint(0,HEIGHT//BLOCK_SIZE-1)
            if not any(body.x == x and body.y == y for body in snake.body):
                return Point(x,y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

running = True
snake = Snake()
food = Food(5, 5)
dx, dy = 0, 0
dict = {"up": True,"down" : True,'right': True,'left' : True}
SCORE_FONT = pygame.font.SysFont("comicsansms", 25)

while running:
    SCREEN.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dict['up']:
                dx, dy = 0, -1
                dict = {"up": True,"down" : False,'right': True,'left' : True}
            elif event.key == pygame.K_DOWN and dict['down']:
                dx, dy = 0, 1
                dict = {"up": False,"down" : True,'right': True,'left' : True}
            elif event.key == pygame.K_RIGHT and dict['right']:
                dx, dy = 1, 0
                dict = {"up": True,"down" : True,'right': True,'left' : False}
            elif event.key == pygame.K_LEFT and dict['left']:
                dx, dy = -1, 0
                dict = {"up": True,"down" : True,'right': False,'left' : True}
        
    snake.move(dx, dy)
    if snake.check_collision(food):
        score += 1
        snake.body.append(
            Point(snake.body[-1].x, snake.body[-1].y)
        )
        food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
    draw_grid()
    snake.draw()
    food.draw()
    SCORE = SCORE_FONT.render(f"Your score: {score}", True, BLACK)
    SCREEN.blit(SCORE,(0,0))
    pygame.display.flip()
    clock.tick(5)