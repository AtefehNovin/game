import pygame
import time
from pygame.locals import *
import sys
###set screen
pygame.init()
screen = pygame.display.set_mode((320,300))
pygame.display.set_caption("game :)")

#set fist screen
white=(255,255,255)
screen.fill(white)
play= pygame.image.load('play.jpg')
mypic5=pygame.image.load('how1.png')
screen.blit(play, (45, 10))
screen.blit(mypic5, (70, 130))


pygame.display.flip()


#load needed images
mypic = pygame.image.load('x.jpg')

mypic2 = pygame.image.load('c.png')
mypic3= pygame.image.load('quit.png')
mypic4= pygame.image.load('win.png')


######main loop of game
w=True
while w==True:
  for evento in pygame.event.get():
    #print(evento)
    screen.fill(white)
    #checking the events
    if evento.type == QUIT:
        pygame.quit()
        sys.exit()
        w= False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()

        if 42<x<273 and 10<y<130:
            pygame.mixer.music.load('tap.wav')
            pygame.mixer.music.play()
            ####set  primary informations
            w=False
            #set pictures
            screen.blit(mypic2, (30, 0))
            screen.blit(mypic3, (100, 245))
            screen.blit(mypic, (0, 110))
            pygame.display.flip()

            tapedb = 0
            tapeda = 0
            tapedc = 0
            tapedd = 0
            tapede = 0
            tapedf = 0
            score = 0
            menuAtivo = True


            while menuAtivo:
                for evento in pygame.event.get():
                    # print(evento)
                    pygame.display.set_caption(str(score))
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        menuAtivo = False
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.music.load('tap.wav')
                        pygame.mixer.music.play()
                        (x, y) = pygame.mouse.get_pos()
                        #print(x)
                        #print(y)
                        if 275 < x < 285 and 170 < y < 180 and tapedb == 0:  # b

                            score = score + 1
                            tapedb = 1
                            pygame.draw.circle(screen,(244,0,0),(x,y),5)

                            pygame.display.flip()
                            print(tapedb)
                        if 205 < x < 235 and 190 < y < 200 and tapeda == 0:  # a

                            score = score + 1
                            tapeda = 1
                            pygame.draw.circle(screen, (244, 0, 0), (x, y), 5)

                            pygame.display.flip()
                        if 290 < x < 310 and 175 < y < 225 and tapedc == 0:  # c

                            score = score + 1
                            tapedc =1
                            pygame.draw.circle(screen, (244, 0, 0), (x, y), 5)

                            pygame.display.flip()
                            print(tapedc)
                        if 250 < x < 280 and 120 < y < 135 and tapedd == 0:  # d

                            score = score + 1
                            tapedd= 1
                            pygame.draw.circle(screen, (244, 0, 0), (x, y), 5)

                            pygame.display.flip()
                        if 163 < x < 185 and 129 < y < 138 and tapede == 0:  # e

                            score = score + 1
                            tapede =1
                            pygame.draw.circle(screen, (244, 0, 0), (x, y), 5)

                            pygame.display.flip()
                        if 175 < x < 195 and 225 < y < 245 and tapedf == 0:  # f

                            score = score + 1
                            tapedf =1
                            pygame.draw.circle(screen, (244, 0, 0), (x, y), 5)

                            pygame.display.flip()
                        if 100 < x < 210 and 260 < y < 300:
                            pygame.mixer.music.load('tap.wav')
                            pygame.mixer.music.play()
                            time.sleep(1)
                            pygame.quit()
                            menuAtivo = False
                        if score==6:
                            time.sleep(2)

                            screen.blit(mypic4,(0, 0))
                            pygame.mixer.music.load('win.mp3')
                            pygame.mixer.music.play()
                            pygame.display.flip()














