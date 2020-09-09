import pygame
from pygame.locals import *


def rule():

    pygame.init()

    SURFACE = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('D   I   C   E   R   S')


    GRAY = (180, 180, 180)
    WHITE = (250, 250, 250)
    RED = (200, 0, 0)

    DICERSFONT = 'material//NEXONFootballGothicL.ttf'
    MAINFONT = pygame.font.Font(DICERSFONT, 25)

    GO_SURFACE = MAINFONT.render('click to play!', True, GRAY)
    GO_RECT = GO_SURFACE.get_rect(center=[685, 560])

    BTM_SURFACE = MAINFONT.render('back to menu', True, GRAY)
    BTM_RECT = BTM_SURFACE.get_rect(center = [85, 560])

    PAGE1_SURFACE = MAINFONT.render('1', True, RED, WHITE)
    PAGE2_SURFACE = MAINFONT.render('2', True, GRAY, WHITE)
    PAGE3_SURFACE = MAINFONT.render('3', True, GRAY, WHITE)
    PAGE4_SURFACE = MAINFONT.render('4', True, GRAY, WHITE)
    PAGE1_RECT = PAGE1_SURFACE.get_rect(center=[235, 560])
    PAGE2_RECT = PAGE1_SURFACE.get_rect(center=[335, 560])
    PAGE3_RECT = PAGE1_SURFACE.get_rect(center=[435, 560])
    PAGE4_RECT = PAGE1_SURFACE.get_rect(center=[535, 560])

    RULE_IMG1 = pygame.image.load('material//rule1.png')
    RULE_IMG2 = pygame.image.load('material//rule2.png')
    RULE_IMG3 = pygame.image.load('material//rule3.png')
    RULE_IMG4 = pygame.image.load('material//rule4.png')

    RULE_POS = (40,20)

    SHOWIMG = RULE_IMG1
    while True:
        SURFACE.fill(WHITE)

        SURFACE.blit(SHOWIMG, RULE_POS)
        SURFACE.blit(PAGE1_SURFACE, PAGE1_RECT)
        SURFACE.blit(PAGE2_SURFACE, PAGE2_RECT)
        SURFACE.blit(PAGE3_SURFACE, PAGE3_RECT)
        SURFACE.blit(PAGE4_SURFACE, PAGE4_RECT)
        SURFACE.blit(GO_SURFACE, GO_RECT)
        SURFACE.blit(BTM_SURFACE, BTM_RECT)

        events = pygame.event.get()
        for event in events:

            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAGE1_RECT.collidepoint(event.pos):
                    PAGE1_SURFACE = MAINFONT.render('1', True, RED, WHITE)
                    PAGE2_SURFACE = MAINFONT.render('2', True, GRAY, WHITE)
                    PAGE3_SURFACE = MAINFONT.render('3', True, GRAY, WHITE)
                    PAGE4_SURFACE = MAINFONT.render('4', True, GRAY, WHITE)
                    SHOWIMG = RULE_IMG1
                    # SURFACE.blit(SHOWIMG, RULE_POS)


                if PAGE2_RECT.collidepoint(event.pos):
                    PAGE1_SURFACE = MAINFONT.render('1', True, GRAY, WHITE)
                    PAGE2_SURFACE = MAINFONT.render('2', True, RED, WHITE)
                    PAGE3_SURFACE = MAINFONT.render('3', True, GRAY, WHITE)
                    PAGE4_SURFACE = MAINFONT.render('4', True, GRAY, WHITE)
                    SHOWIMG = RULE_IMG2
                    # SURFACE.blit(SHOWIMG, RULE_POS)

                if PAGE3_RECT.collidepoint(event.pos):
                    PAGE1_SURFACE = MAINFONT.render('1', True, GRAY, WHITE)
                    PAGE2_SURFACE = MAINFONT.render('2', True, GRAY, WHITE)
                    PAGE3_SURFACE = MAINFONT.render('3', True, RED, WHITE)
                    PAGE4_SURFACE = MAINFONT.render('4', True, GRAY, WHITE)
                    SHOWIMG = RULE_IMG3
                    # SURFACE.blit(SHOWIMG, RULE_POS)

                if PAGE4_RECT.collidepoint(event.pos):
                    PAGE1_SURFACE = MAINFONT.render('1', True, GRAY, WHITE)
                    PAGE2_SURFACE = MAINFONT.render('2', True, GRAY, WHITE)
                    PAGE3_SURFACE = MAINFONT.render('3', True, GRAY, WHITE)
                    PAGE4_SURFACE = MAINFONT.render('4', True, RED, WHITE)
                    SHOWIMG = RULE_IMG4
                    # SURFACE.blit(SHOWIMG, RULE_POS)

                if GO_RECT.collidepoint(event.pos):
                    import DICERS_game
                    DICERS_game.game()

                if BTM_RECT.collidepoint(event.pos):
                    import DICERS_main
                    DICERS_main.main()

            if event.type == pygame.MOUSEMOTION:
                if GO_RECT.collidepoint(event.pos):
                    GO_SURFACE = MAINFONT.render('click to play!', True, RED)
                    BTM_SURFACE = MAINFONT.render('back to menu', True, GRAY)
                elif BTM_RECT.collidepoint(event.pos):
                    GO_SURFACE = MAINFONT.render('click to play!', True, GRAY)
                    BTM_SURFACE = MAINFONT.render('back to menu', True, RED)
                else:
                    GO_SURFACE = MAINFONT.render('click to play!', True, GRAY)
                    BTM_SURFACE = MAINFONT.render('back to menu', True, GRAY)


            pygame.display.update()