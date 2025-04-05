import pygame
import os

pygame.init()

screen_width = 300
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player") # Название


background_image = pygame.image.load(r"C:\Users\madik\Desktop\pp2\lab7\music_player\bg.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


sponge_image = pygame.image.load(r"C:\Users\madik\Desktop\pp2\lab7\music_player\sponge.jpg")

sponge_width, sponge_height = 220, 180
sponge_image = pygame.transform.scale(sponge_image, (sponge_width, sponge_height)) # Меняю размер картинки
sponge_x = 45
sponge_y =  90

content = pygame.image.load(r"C:\Users\madik\Desktop\pp2\lab7\music_player\copy.png")
sponge_width, sponge_height = 50, 40
content = pygame.transform.scale(content, (sponge_width, sponge_height))
content_x = 215
content_y = 230

music_dir = r"C:\Users\madik\Desktop\pp2\lab7\music_player\music"
songs = [song for song in os.listdir(music_dir) if song.endswith(('.mp3'))]
curr_song_ind = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_dir, songs[curr_song_ind]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global curr_song_ind
    curr_song_ind = (curr_song_ind + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[curr_song_ind]))
    play_music()


def previous_song():
    global curr_song_ind
    curr_song_ind = (curr_song_ind - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[curr_song_ind]))
    play_music()

run = True
while run:
    screen.blit(background_image, (0, 0))
    screen.blit(sponge_image, (sponge_x, sponge_y))
    screen.blit(content, (content_x, content_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # Вверх чтобы воспроизвести
                play_music()
            elif event.key == pygame.K_DOWN: # Стрелка вниз чтобы остановить музыку
                stop_music()
            elif event.key == pygame.K_RIGHT: # Правая стрелка для след.песни
                next_song()
            elif event.key == pygame.K_LEFT: # ЛЕвая стрелка для пред
                previous_song()
            elif event.key == pygame.K_q: # Выход
                run = False

    pygame.display.flip()
