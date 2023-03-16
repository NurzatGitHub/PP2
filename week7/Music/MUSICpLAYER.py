import pygame

pygame.init()
pygame.display.set_caption("Music Player")
screen = pygame.display.set_mode((500,400))
pygame.mixer.init()
song1 = open(r"C:\Users\Nurza\Documents\PP2\week7\Music\Happiness.mp3")
song2 = open(r"C:\Users\Nurza\Documents\PP2\week7\Music\The_Tokens_-_The_Lion_Sleeps_Tonight_64402105.mp3")
song3 = open(r"C:\Users\Nurza\Documents\PP2\week7\Music\this-is-war-loopable-95413.mp3")
songs = [song1,song2,song3]
i = 0
def play_song(i):
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()
def pause_song():
    pygame.mixer.music.pause()
def next_song(i):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()
def prev_song(i):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_song(i)
            elif event.key == pygame.K_PAUSE:
                pause_song()
            elif event.key == pygame.K_PAGEUP:
                i += 1
                if i > len(songs)-1:
                    i = 0
                next_song(i)
            elif event.key == pygame.K_PAGEDOWN:
                i -= 1
                if i < 0:
                    i = len(songs)-1
                prev_song(i)
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()