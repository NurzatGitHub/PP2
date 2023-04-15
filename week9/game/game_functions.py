import pygame
from constants import WIDTH, HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def music_background():
    pygame.mixer.music.load(r'C:\Users\Nurza\Documents\PP2\week9\game\game_souds\fight.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def show_game_over(score):
    font = pygame.font.SysFont('Impact', 50)
    font_small = pygame.font.SysFont('Impact', 30)
    text = font.render("GAME OVER", True, (139, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.mixer.music.load(r'C:\Users\Nurza\Documents\PP2\week9\game\game_souds\game_sounds_gameover.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(4000)
    music_background()

def show_game_win():
    font = pygame.font.SysFont('Impact', 50)
    text = font.render("AWESOME! GO ON!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/win.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(1000)
    music_background()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        bullet.blit_bullet()

def score_w(score,level):
    font = pygame.font.SysFont('Impact', 24)
    text = font.render(f"| SCORE: {score} || LEVEL: {level} |",True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH - 150, 30))
    screen.blit(text,text_rect)