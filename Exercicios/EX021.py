
###############################################################################################################

# DESAFIO: 021
# TÍTULO: Tocando um MP3
# AULA: 08
# EXERCÍCIO: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

###############################################################################################################

import pygame
pygame.init()
pygame.mixer.music.load('EX021.mp3')
pygame.mixer.music.play()
pygame.event.wait()