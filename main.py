# 1: Import the library pygame
import pygame
from pygame.locals import *


def up_action():
    print("up clicked")


def down_action():
    print("down clicked")


def left_action():
    print("left clicked")


def right_action():
    print("right clicked")


def w_action():
    print("w clicked")


def s_action():
    print("s clicked")


def a_action():
    print("a clicked")


def d_action():
    print("d clicked")


# Initialize pygame
pygame.init()
pygame.font.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False, False, False, False, False]
# Game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
            if event.key == pygame.K_LEFT:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
            if event.key == pygame.K_w:
                keys[4] = True
            if event.key == pygame.K_s:
                keys[5] = True
            if event.key == pygame.K_a:
                keys[6] = True
            if event.key == pygame.K_d:
                keys[7] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] = False
            if event.key == pygame.K_LEFT:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False
            if event.key == pygame.K_w:
                keys[4] = False
            if event.key == pygame.K_s:
                keys[5] = False
            if event.key == pygame.K_a:
                keys[6] = False
            if event.key == pygame.K_d:
                keys[7] = False
    if keys[0]:
        up_action()
    if keys[1]:
        down_action()
    if keys[2]:
        left_action()
    if keys[3]:
        right_action()
    if keys[4]:
        w_action()
    if keys[5]:
        s_action()
    if keys[6]:
        a_action()
    if keys[7]:
        d_action()
