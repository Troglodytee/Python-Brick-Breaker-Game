import pygame
from pygame.locals import *
from random import *

def affich() :
    if ecran == 1 :
        fenetre.blit(im_accueil,(0,0))
        myfont = pygame.font.SysFont("Fixedsys",48)
        texte = myfont.render("CASSE BRIQUE",False,(170,20,170))
        fenetre.blit(texte,(170,240))
        myfont = pygame.font.SysFont("Courier New",12)
        texte = myfont.render("Aide (a)",False,(255,255,255))
        fenetre.blit(texte,(5,480))
        if aide == 1 :
            texte = myfont.render("Commandes :",False,(255,255,255))
            fenetre.blit(texte,(5,5))
            texte = myfont.render("<-' : mettre ou retirer la pause",False,(255,255,255))
            fenetre.blit(texte,(5,20))
            texte = myfont.render("< : Déplacer la barre vers la gauche",False,(255,255,255))
            fenetre.blit(texte,(5,35))
            texte = myfont.render("> : Déplacer la barre vers la droite",False,(255,255,255))
            fenetre.blit(texte,(5,50))
    elif ecran == 2 or ecran == 3 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,600,500))

        for i in range (12) :
            for j in range (12) :
                if not briques[i*12+j] == 0 :
                    pygame.draw.rect(fenetre,(0,0,0),(j*50,i*25,50,25))
                    pygame.draw.rect(fenetre,couleurs[briques[i*12+j]-1],(j*50+2,i*25+2,46,21))

        for i in range (0,len(bonus_en_mouv)-2,3) :
            im_bonus = pygame.image.load(raccourci+"sprite\\bonus"+str(bonus_en_mouv[i+2])+".png").convert()
            fenetre.blit(im_bonus,(bonus_en_mouv[i],int(bonus_en_mouv[i+1]+0.5)))

        pygame.draw.rect(fenetre,(0,0,0),(coord[0]-coord[1],450,(coord[1]*2)+80,10))
        pygame.draw.rect(fenetre,(255,255,255),(coord[0]-coord[1]+2,452,(coord[1]*2)+76,6))

        for i in range (0,len(balles)-3,4) :
            pygame.draw.rect(fenetre,(0,0,0),(balles[i+1],balles[i+2],10,10))
            if balles[i+3] == 1 :
                pygame.draw.rect(fenetre,(255,255,255),(balles[i+1]+2,balles[i+2]+2,6,6))

        if ecran == 2 :
            myfont = pygame.font.SysFont("Fixedsys",36)
            texte = myfont.render("LEVEL "+str(level),False,(255,255,255))
            fenetre.blit(texte,(int(300-(len("LEVEL "+str(level))/2)*14+0.5),465))
        if pause == 1 :
            myfont = pygame.font.SysFont("Fixedsys",36)
            texte = myfont.render("PAUSE",False,(255,255,255))
            fenetre.blit(texte,(255,240))

    pygame.display.flip()

def set_briques() :
    global briques
    briques = []
    if level == 1 :
        for i in range (144) :
            briques += [1]
    elif level == 2 :
        for i in range (6) :
            for j in range (24) :
                briques += [6-i]
    elif level == 3 :
        for i in range (12) :
            for j in range (2) :
                for k in range (6) :
                    briques += [k+1]
    elif level == 4 :
        l = []
        for i in range (12) :
            l += [1]
        for i in range (6) :
            for j in range (i) :
                l[5-j] += 1
                l[6+j] += 1
            briques += l
        briques += l
        for i in range (5) :
            for j in range (12) :
                if l[j] > 1 :
                    l[j] -= 1
            briques += l
    elif level == 5 :
        a = 6
        for i in range (12) :
            for j in range (12) :
                briques += [a]
                a += 1
                if a > 6 :
                    a = 1
            a -= 1
            if a < 1 :
                a = 6
    elif level == 6 :
        for i in range (12) :
            for j in range (6) :
                for k in range (2) :
                    briques += [k*5+1]
    elif level == 7 :
        briques += [6,6,6,6,6,6,6,6,6,6,6,6]
        briques += [6,1,1,1,1,1,1,1,1,1,1,6]
        briques += [6,1,6,6,6,6,6,6,6,6,1,6]
        briques += [6,1,6,1,1,1,1,1,1,6,1,6]
        briques += [6,1,6,1,6,6,6,6,1,6,1,6]
        briques += [6,1,6,1,6,1,1,6,1,6,1,6]
        briques += [6,1,6,1,6,1,1,6,1,6,1,6]
        briques += [6,1,6,1,6,1,6,6,1,6,1,6]
        briques += [6,1,6,1,6,1,1,1,1,6,1,6]
        briques += [6,1,6,1,6,6,6,6,6,6,1,6]
        briques += [6,1,6,1,1,1,1,1,1,1,1,6]
        briques += [6,1,6,6,6,6,6,6,6,6,6,6]
    elif level == 8 :
        for i in range (144) :
            briques += [6]
    else :
        for i in range (144) :
            briques += [randint(1,6)]

def mouve() :
    global ecran
    global balles
    global briques
    global level
    global bonus_en_mouv
    global bonus
    global coord
    i = 0
    while i < len(balles)-3 :
        if balles[i] == 1 :
            balles[i+1] -= 5
            balles[i+2] -= 5
        elif balles[i] == 2 :
            balles[i+1] += 5
            balles[i+2] -= 5
        elif balles[i] == 3 :
            balles[i+1] += 5
            balles[i+2] += 5
        elif balles[i] == 4 :
            balles[i+1] -= 5
            balles[i+2] += 5
        if balles[i+2]+10 == 500 :
            del balles[i:i+4]
            if len(balles) == 0 :
                gameover()
        else :
            if balles[i+1] == 0 :
                if balles[i] == 1 :
                    balles[i] = 2
                elif balles[i] == 4 :
                    balles[i] = 3
            if balles[i+1]+10 == 600 :
                if balles[i] == 2 :
                    balles[i] = 1
                elif balles[i] == 3 :
                    balles[i] = 4
            if balles[i+2] == 0 :
                if balles[i] == 1 :
                    balles[i] = 4
                elif balles[i] == 2 :
                    balles[i] = 3
            if balles[i+2] == 440 and balles[i+1]+10 > coord[0]-coord[1] and balles[i+1] < coord[0]+coord[1]+80 :
                if balles[i] == 3 :
                    balles[i] = 2
                else :
                    balles[i] = 1
            non = 0
            if balles[i+2] <= 300 and balles[i+2] >= 25 and balles[i+2]%25 == 0 and (balles[i] == 1 or balles[i] == 2) :
                if not briques[((balles[i+2]//25)-1)*12+(balles[i+1]//50)] == 0 :
                    non = 1
                    briques[((balles[i+2]//25)-1)*12+(balles[i+1]//50)] -= 1
                    if balles[i+3] == 2 :
                        briques[((balles[i+2]//25)-1)*12+(balles[i+1]//50)] = 0
                    if briques[((balles[i+2]//25)-1)*12+(balles[i+1]//50)] == 0 :
                        ajout_bonus((balles[i+1]//50),((balles[i+2]//25)-1))
                    if balles[i] == 1 :
                        balles[i] = 4
                    elif balles[i] == 2 :
                        balles[i] = 3
                if not balles[i+1]//50 == (balles[i+1]+9)//50 and balles[i+1] < 590 :
                    if not briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] == 0 :
                        non = 1
                        briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] = 0
                        if briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] == 0 :
                            ajout_bonus(((balles[i+1]+10)//50),((balles[i+2]//25)-1))
                        if balles[i] == 1 :
                            balles[i] = 4
                        elif balles[i] == 2 :
                            balles[i] = 3

            if balles[i+2] < 275 and (balles[i+2]+10)%25 == 0 and (balles[i] == 3 or balles[i] == 4) :
                if not briques[((balles[i+2]+10)//25)*12+(balles[i+1]//50)] == 0 :
                    non = 1
                    briques[((balles[i+2]+10)//25)*12+(balles[i+1]//50)] -= 1
                    if balles[i+3] == 2 :
                        briques[((balles[i+2]+10)//25)*12+(balles[i+1]//50)] = 0
                    if briques[((balles[i+2]+10)//25)*12+(balles[i+1]//50)] == 0 :
                        ajout_bonus((balles[i+1]//50),((balles[i+2]+10)//25))
                    if balles[i] == 3 :
                        balles[i] = 2
                    elif balles[i] == 4 :
                        balles[i] = 1
                if not balles[i+1]//50 == (balles[i+1])+9//50 and balles[i+1] < 590 :
                    if not briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] == 0 :
                        non = 1
                        briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] = 0
                        if briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] == 0 :
                            ajout_bonus(((balles[i+1]+10)//50),((balles[i+2]+10)//25))
                        if balles[i] == 3 :
                            balles[i] = 2
                        elif balles[i] == 4 :
                            balles[i] = 1

            if balles[i+2] < 300 and balles[i+1]%50 == 0 and balles[i+1] > 0 and balles[i+1] <= 550 and (balles[i] == 1 or balles[i] == 4) :
                if not briques[(balles[i+2]//25)*12+((balles[i+1]//50)-1)] == 0 :
                    non = 1
                    briques[(balles[i+2]//25)*12+((balles[i+1]//50)-1)] -= 1
                    if balles[i+3] == 2 :
                        briques[(balles[i+2]//25)*12+((balles[i+1]//50)-1)] = 0
                    if briques[(balles[i+2]//25)*12+((balles[i+1]//50)-1)] == 0 :
                        ajout_bonus(((balles[i+1]//50)-1),(balles[i+2]//25))
                    if balles[i] == 1 :
                        balles[i] = 2
                    elif balles[i] == 4 :
                        balles[i] = 3
                if not balles[i+2]//25 == (balles[i+2]+9)//25 and balles[i+2] < 275 :
                    if not briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]//50)-1)] == 0 :
                        non = 1
                        briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]//50)-1)] -= 1
                        if balles[i+3] == 2 :
                            briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]//50)-1)] = 0
                        if briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]//50)-1)] == 0 :
                            ajout_bonus(((balles[i+1]//50)-1),(((balles[i+2]+10)//25)+1))
                        if balles[i] == 1 :
                            balles[i] = 2
                        elif balles[i] == 4 :
                            balles[i] = 3

            if balles[i+2] < 300 and (balles[i+1]+10)%50 == 0 and balles[i+1]+10 < 600 and balles[i+1]+10 >= 50 and (balles[i] == 2 or balles[i] == 3) :
                if not briques[(balles[i+2]//25)*12+((balles[i+1]+10)//50)] == 0 :
                    non = 1
                    briques[(balles[i+2]//25)*12+((balles[i+1]+10)//50)] -= 1
                    if balles[i+3] == 2 :
                        briques[(balles[i+2]//25)*12+((balles[i+1]+10)//50)] = 0
                    if briques[(balles[i+2]//25)*12+((balles[i+1]+10)//50)] == 0 :
                        ajout_bonus(((balles[i+1]+10)//50),(balles[i+2]//25))
                    if balles[i] == 2 :
                        balles[i] = 1
                    elif balles[i] == 3 :
                        balles[i] = 4
                if not balles[i+2]//25 == (balles[i+2]+9)//25 and balles[i+2] < 275 :
                    if not briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]+10)//50)] == 0 :
                        non = 1
                        briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]+10)//50)] -= 1
                        if balles[i+3] == 2 :
                            briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]+10)//50)] = 0
                        if briques[(((balles[i+2]+10)//25)+1)*12+((balles[i+1]+10)//50)] == 0 :
                            ajout_bonus(((balles[i+1]+10)//50),(((balles[i+2]+10)//25)+1))
                        if balles[i] == 2 :
                            balles[i] = 1
                        elif balles[i] == 3 :
                            balles[i] = 4

            if non == 0 :
                if balles[i+1] >= 50 and balles[i+2] >= 25 and balles[i+2] <= 300 and balles[i+1]%50 == 0 and balles[i+2]%25 == 0 and balles[i] == 1 :
                    if not briques[((balles[i+2]//25)-1)*12+((balles[i+1]//50)-1)] == 0 :
                        briques[((balles[i+2]//25)-1)*12+((balles[i+1]//50)-1)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]//25)-1)*12+((balles[i+1]//50)-1)] = 0
                        if briques[((balles[i+2]//25)-1)*12+((balles[i+1]//50)-1)] == 0 :
                            ajout_bonus((balles[i+1]//50)-1,(balles[i+2]//25)-1)
                        balles[i] = 3
                elif balles[i+1]+10 <= 550 and balles[i+2] >= 25 and balles[i+2] <= 300 and (balles[i+1]+10)%50 == 0 and balles[i+2]%25 == 0 and balles[i] == 2 :
                    if not briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] == 0 :
                        briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] = 0
                        if briques[((balles[i+2]//25)-1)*12+((balles[i+1]+10)//50)] == 0 :
                            ajout_bonus((balles[i+1]+10)//50,(balles[i+2]//25)-1)
                        balles[i] = 4
                elif balles[i+1] >= 50 and balles[i+2]+10 <= 275 and balles[i+1]%50 == 0 and (balles[i+2]+10)%25 == 0 and balles[i] == 4 :
                    if not briques[((balles[i+2]+10)//25)*12+((balles[i+1]//50)-1)] == 0 :
                        briques[((balles[i+2]+10)//25)*12+((balles[i+1]//50)-1)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]+10)//25)*12+((balles[i+1]//50)-1)] = 0
                        if briques[((balles[i+2]+10)//25)*12+((balles[i+1]//50)-1)] == 0 :
                            ajout_bonus((balles[i+1]//50)-1,(balles[i+2]+10)//25)
                        balles[i] = 2
                elif balles[i+1]+10 <= 550 and balles[i+2]+10 <= 275 and (balles[i+1]+10)%50 == 0 and (balles[i+2]+10)%25 == 0 and balles[i] == 3 :
                    if not briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] == 0 :
                        briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] -= 1
                        if balles[i+3] == 2 :
                            briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] = 0
                        if briques[((balles[i+2]+10)//25)*12+((balles[i+1]+10)//50)] == 0 :
                            ajout_bonus((balles[i+1]+10)//50,(balles[i+2]+10)//25)
                        balles[i] = 1
        i += 4

    i = 0
    while i < len(bonus_en_mouv)-2 :
        if bonus_en_mouv[i+1] == 480 :
            del bonus_en_mouv[i:i+3]
        elif bonus_en_mouv[i+1] == 430 and bonus_en_mouv[i]+10 > coord[0]-coord[1] and bonus_en_mouv[i] < coord[0]+coord[1]+80 :
            if not bonus_en_mouv[i+2] == 5 and not bonus_en_mouv[i+2] == 6 :
                bonus[bonus_en_mouv[i+2]*2-2] = 1
                bonus[bonus_en_mouv[i+2]*2-1] = 100

                if bonus_en_mouv[i+2] == 1 and coord[1] == 0 :
                    coord[1] = 10
                elif bonus_en_mouv[i+2] == 1 and coord[1] == -10 :
                    coord[1] = 0
                    for j in range (4) :
                        bonus[i] = 0
                elif bonus_en_mouv[i+2] == 2 and coord[1] == 0 :
                    coord[1] = -10
                elif bonus_en_mouv[i+2] == 2 and coord[1] == 10 :
                    coord[1] = 0
                    for j in range (4) :
                        bonus[i] = 0

                elif bonus_en_mouv[i+2] == 3 and bonus[6] == 1 :
                    bonus[6] = 0
                    bonus[7] = 0
                elif bonus_en_mouv[i+2] == 4 and bonus[4] == 1 :
                    bonus[4] = 0
                    bonus[5] = 0

                del bonus_en_mouv[i:i+3]
            elif bonus_en_mouv[i+2] == 5 :
                balles += [randint(1,2),295,350,1]
                del bonus_en_mouv[i:i+3]
            elif bonus_en_mouv[i+2] == 6 :
                balles += [randint(1,2),295,350,2]
                del bonus_en_mouv[i:i+3]
        else :
            bonus_en_mouv[i+1] += 2.5
        i += 3

    for i in range (0,len(bonus)-1,2) :
        if bonus[i] == 1 :
            bonus[i+1] -= 1
            if bonus[i+1] == 0 :
                bonus[i] = 0
                if i == 0 or i == 2 :
                    coord[1] = 0

    non = 0
    for i in range (len(briques)) :
        if not briques[i] == 0 :
            non = 1
            break
    if non == 0 :
        ecran = 2
        coord = [260,0]
        balles = [randint(3,4),295,350,1]
        bonus = [0,0,0,0,0,0,0,0]
        bonus_en_mouv = []
        level += 1
        set_briques()
    affich()

def ajout_bonus(x,y) :
    global bonus_en_mouv
    if randint(1,2) == 1 :
        bonus_en_mouv += [x*50+15,y*25+5,randint(1,6)]

def gameover() :
    global ecran
    fenetre.blit(game_over,(0,0))
    pygame.display.flip()
    for i in range (30) :
        pygame.time.wait(100)
    ecran = 1
    pygame.key.set_repeat(300,100)

pygame.init()

fenetre = pygame.display.set_mode((600,500))
pygame.display.set_caption("Casse brique")

raccourci = __file__
raccourci = raccourci[0:-8]

icone = pygame.image.load(raccourci+"sprite\\icone.png")
pygame.display.set_icon(icone)

game_over = pygame.image.load(raccourci+"sprite\\game over.png").convert()
im_accueil = pygame.image.load(raccourci+"sprite\\accueil.png").convert()

ecran = 1
aide = 0
affich()

couleurs = [(63,72,204),(0,162,232),(34,177,76),(255,242,0),(255,127,39),(237,28,36)]

pygame.key.set_repeat(300,100)

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()
        elif event.type == KEYDOWN :
            if event.key == K_RETURN :
                if ecran == 1 :
                    ecran = 2
                    pause = 0
                    coord = [260,0]
                    balles = [randint(3,4),295,350,1]
                    bonus = [0,0,0,0,0,0,0,0]
                    bonus_en_mouv = []
                    level = 1
                    set_briques()
                elif ecran == 2 :
                    ecran = 3
                    pygame.key.set_repeat(50,50)
                elif ecran == 3 :
                    if pause == 0 :
                        pause = 1
                    else :
                        pause = 0
            elif event.key == K_LEFT and pause == 0 :
                if ecran == 3 :
                    if coord[0]-coord[1] > 0 :
                        coord[0] -= 10
            elif event.key == K_RIGHT and pause == 0 :
                if ecran == 3 :
                    if coord[0]+coord[1]+80 < 600 :
                        coord[0] += 10
            elif event.key == K_q :
                if aide == 0 :
                    aide = 1
                else :
                    aide = 0

        affich()

    if ecran == 3 and pause == 0 :
        if bonus[4] == 1 :
            a = 25
        elif bonus[6] == 1 :
            a = 100
        else :
            a = 50
        pygame.time.wait(a)
        mouve()
