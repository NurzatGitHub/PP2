import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill("white")
pygame.display.update()
clock = pygame.time.Clock()

red_mode = 'red'
blue_mode = 'blue'
mode = blue_mode
green_mode = 'green'
yellow_mode = (255, 234, 0)

radius = 15
drawing = False
eraser = False

while True:
    clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_r:
                mode = red_mode
                eraser = False
            elif event.key == pygame.K_b:
                mode = blue_mode
                eraser = False
            elif event.key == pygame.K_g:
                mode = green_mode
                eraser = False
            elif event.key == pygame.K_y:
                mode = yellow_mode
                eraser = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, mode, pos, radius)
                drawing = True
            elif event.button == 3:
                mode = "white"
                eraser = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                mode = blue_mode
                eraser = False
        if event.type == pygame.MOUSEMOTION:
            if drawing and not eraser:
                pygame.draw.circle(screen, mode, pos, radius)
            elif eraser:
                pygame.draw.circle(screen, mode, pos, radius)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                radius += 1
            elif event.y < 0:
                radius -= 1
    pygame.display.update()