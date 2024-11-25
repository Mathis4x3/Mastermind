# Créé par Mathis, Maxime, Lou le 11/05/2023 en Python 3.7
import random
import pygame
import time
import sys
from pygame.locals import *

from src.controleur.ControleurGen import ControleurGen
from src.object.Niveaux.Niveau import Niveau
from src.object.Niveaux.Niveau1 import Niveau1
from src.object.Niveaux.Niveau2 import Niveau2
from src.object.Niveaux.Niveau3 import Niveau3
from src.object.Screen import Screen

pygame.init()

def error(screen):
    #fait apparaitre le triangle erreur
    pygame.draw.line(screen,(255,0,0),(500,200),(600,400),2)
    pygame.draw.line(screen,(255,0,0),(600,400),(400,400),2)
    pygame.draw.line(screen,(255,0,0),(400,400),(500,200),2)
    pygame.draw.line(screen,(255,0,0),(500,250),(500,360), 5)
    pygame.draw.ellipse(screen, (255,0,0), (485, 365, 30, 30))
    pygame.display.flip()
    time.sleep(1/4) #le laisse pendant un court moment pour que le joueur ai le temps de voir le triangle
    #puis le fait disparaitre
    pygame.draw.line(screen,(255,255,255),(500,200),(600,400),2)
    pygame.draw.line(screen,(255,255,255),(600,400),(400,400),2)
    pygame.draw.line(screen,(255,255,255),(400,400),(500,200),2)
    pygame.draw.line(screen,(255,255,255),(500,250),(500,360), 5)
    pygame.draw.ellipse(screen, (255,255,255), (485, 365, 30, 30))
    pygame.display.flip()

#genere le code secret en fonction des parametres
def genererCode(longueur):
    couleurs = ['Rg', 'O', 'J', 'Rs', 'B', 'N']
    code_secret = []
    couleurComptage = {}
    temp = False
    comptage = 0
    if Niveau.getNiveau() == 3: #les couleurs se répètent car niveau 3
        while comptage != 4:
            couleur = random.choice(couleurs)
            if couleur in couleurComptage:
                if temp == False:
                    code_secret.append(couleur)
                    comptage += 1
                    temp = True
                else :
                    couleurs.remove(couleur)
            else:
                couleurComptage[couleur] = 1
                code_secret.append(couleur)
                comptage += 1
    else: #les couleurs ne se répètent pas
        for i in range(longueur):
            couleur = random.choice(couleurs)
            code_secret.append(couleur)
            couleurs.remove(couleur)
    print(code_secret)
    return code_secret

def evaluer_proposition(screen, liste, coup, code_secret):
    # si il n'y a pas 4 couleurs dans la proposition du joueur
    if len(liste) != 4:
        error(screen)
        return Niveau.getNiveau()
    bien_places = 0
    mal_places = 0
    code_secret1 = list(code_secret)
    liste1 = list(liste)
    for i in range(len(liste)):
        if liste[i] == code_secret[i]:
            bien_places += 1
            code_secret1.remove(liste[i])
            liste1.remove(liste[i])
    for j in range(len(liste1)):
        if liste1[j] in code_secret1:
            mal_places += 1
            trouvé = None
            y = 0
            while trouvé is None:
                if liste1[j] == code_secret1[y]:
                    code_secret1.remove(liste1[j])
                    trouvé = 1
                y += 1

    fontText = pygame.font.SysFont('verdana', 19)
    if mal_places == 0:
        mal = fontText.render('0', 0, (255,0,0))
    elif mal_places == 1:
        mal = fontText.render('1', 0, (255,0,0))
    elif mal_places == 2:
        mal = fontText.render('2', 0, (255,0,0))
    elif mal_places == 3:
        mal = fontText.render('3', 0, (255,0,0))
    elif mal_places == 4:
        mal = fontText.render('4', 0, (255,0,0))
    if bien_places == 0:
        bien = fontText.render('0',0,(0,255,0))
    elif bien_places == 1:
        bien = fontText.render('1',0,(0,255,0))
    elif bien_places == 2:
        bien = fontText.render('2',0,(0,255,0))
    elif bien_places == 3:
        bien = fontText.render('3',0,(0,255,0))
    elif bien_places == 4:
        bien = fontText.render('4',0,(0,255,0))
    #fait apparaitre les chiffres en fonction du nombre de coup du joueur pour bien les placer
    taille = 60*coup
    if Niveau.getNiveau() == 1:
        screen.blit(mal,(400,620-taille))
        screen.blit(bien,(425,620-taille))
    else:
        screen.blit(mal,(400,500-taille))
        screen.blit(bien,(425,500-taille))

    pygame.display.flip()

    if bien_places == 4:
        Niveau.setNiveauActuel(fin(screen,code_secret,True))
    return Niveau.getNiveau()


def accueil(screen):
    pygame.display.set_caption('Mastermind : Menu')
    fond = (255,255,255)
    bouton = pygame.image.load('ressources/img/bouton.png')
    bouton = pygame.transform.scale(bouton,(170,80))

    titre = pygame.font.SysFont('impact', 40)
    fontText = pygame.font.SysFont('verdana', 19)
    font1 = pygame.font.SysFont('verdana', 20)

    Titre = titre.render('MASTERMIND',0,(0,0,0))
    text = fontText.render('Toutes les couleurs sont uniques, vous ne pouvez pas les mettre plusieurs fois.', 0, (0,0,0))
    text1 = fontText.render('10 essais de 4 couleurs',0,(0,0,0))
    text2 = fontText.render('8 essais de 4 couleurs',0,(0,0,0))
    text3 = fontText.render('Les couleurs peuvent se doubler.',0,(0,0,0))
    niveau1 = font1.render('Niveau 1', 0, (204,172,0))
    niveau2 = font1.render('Niveau 2', 0, (255,80,0))
    niveau3 = font1.render('Niveau 3', 0, (255,0,0))

    #fait apparaitre les boutons pour les niveaux et les texte
    screen.fill(fond)
    screen.blit(text,(100,105))
    screen.blit(text1,(385,127))
    screen.blit(bouton, (410, 140))
    screen.blit(text,(100,245))
    screen.blit(text2,(385,267))
    screen.blit(bouton, (410, 280))
    screen.blit(text3,(330,385))
    screen.blit(text2,(385,407))
    screen.blit(bouton, (410, 420))
    screen.blit(Titre, (393,35))
    screen.blit(niveau1, (453,165))
    screen.blit(niveau2, (453,305))
    screen.blit(niveau3, (453,445))

    pygame.display.flip()



def supprime(screen,liste,coup):
    rond = pygame.image.load('ressources/img/rondBois.png')
    rond = pygame.transform.scale(rond,(50,50))
    L = len(liste)
    taille = 60*coup
    #supprime les couleurs (met un rond sur la derniere couleur posée)
    if L == 4:
        if Niveau.getNiveau() == 1:
            screen.blit(rond,(340,610-taille))
        else:
            screen.blit(rond,(340,490-taille))
        liste.pop(3)
    if L == 3:
        if Niveau.getNiveau() == 1:
            screen.blit(rond,(285,610-taille))
        else:
            screen.blit(rond,(285,490-taille))
        liste.pop(2)
    if L == 2:
        if Niveau.getNiveau() == 1:
            screen.blit(rond,(230,610-taille))
        else:
            screen.blit(rond,(230,490-taille))
        liste.pop(1)
    if L == 1:
        if Niveau.getNiveau() == 1:
            screen.blit(rond,(175,610-taille))
        else:
            screen.blit(rond,(175,490-taille))
        liste.pop(0)
    pygame.display.flip()
    return liste

def mettreCouleur(screen,liste,coup,couleur):
    L = len(liste)
    code = {'Rg' : (255,0,0), 'J':(255,255,0), 'Rs':(255,105,180), 'B':(0,0,255), 'N':(0,0,0), 'O':(255,165,0)}
    taille = 60*coup
    if Niveau.getNiveau() == 1 or Niveau.getNiveau() == 2:
        if couleur in liste:
            error(screen)
            return liste
    #si le joueur souhaite mettre une couleur alors qu'il y en a deja 4, affiche erreur
    if L == 4 :
        error(screen)
        return liste
    #fait apparaitre la couleur
    if L == 0:
        if Niveau.getNiveau() == 1:
            pygame.draw.ellipse(screen, code[couleur], (181, 615-taille, 40, 40))
        else:
            pygame.draw.ellipse(screen, code[couleur], (181, 495-taille, 40, 40))
        liste.append(couleur)
    elif L == 1:
        if Niveau.getNiveau() == 1:
            pygame.draw.ellipse(screen, code[couleur], (235, 615-taille, 40, 40))
        else:
            pygame.draw.ellipse(screen, code[couleur], (235, 495-taille, 40, 40))
        liste.append(couleur)
    elif L == 2:
        if Niveau.getNiveau() == 1:
            pygame.draw.ellipse(screen, code[couleur], (290, 615-taille, 40, 40))
        else:
            pygame.draw.ellipse(screen, code[couleur], (290, 495-taille, 40, 40))
        liste.append(couleur)
    elif L == 3:
        if Niveau.getNiveau() == 1:
            pygame.draw.ellipse(screen, code[couleur], (345, 615-taille, 40, 40))
        else:
            pygame.draw.ellipse(screen, code[couleur], (345, 495-taille, 40, 40))
        liste.append(couleur)
    pygame.display.flip()
    return liste

def fenetreJeu(screen):
    pygame.display.set_caption('Mastermind : Jeu')

    font1 = pygame.font.SysFont('verdana', 20)
    blanc = (255,255,255)
    noir = (0,0,0)

    bouton = pygame.image.load('ressources/img/bouton.png')
    bouton = pygame.transform.scale(bouton,(170,80))
    rond = pygame.image.load('ressources/img/rondBois.png')
    rond = pygame.transform.scale(rond,(50,50))
    rond1 = pygame.image.load('ressources/img/rondBoisClair.png')
    rond1 = pygame.transform.scale(rond1,(50,50))
    rondFer = pygame.image.load('ressources/img/rondFer.png')
    rondFer = pygame.transform.scale(rondFer,(50,50))
    menu = font1.render('Menu', 0, (0,0,0))
    confirmer = font1.render('Confirmer', 0, (0,0,0))
    abandonner = font1.render('Abandonner', 0, (0,0,0))
    niveau1 = font1.render('Niveau 1', 0, (0,0,0))
    niveau2 = font1.render('Niveau 2', 0, (0,0,0))
    niveau3 = font1.render('Niveau 3', 0, (0,0,0))

    #supprime tout et ajoute les boutons
    screen.fill(blanc)
    screen.blit(bouton, (830, 620))
    screen.blit(bouton, (660, 620))
    screen.blit(bouton, (490, 620))

    ControleurGen.afficherCouleurs()

    #fait apparaitre les ronds
    for i in range(4):
        screen.blit(rond1,((175+(55*i)),10))

    for i in range(4):
        for j in range(8):
            screen.blit(rond,((175+(i*55)),(70+(j*60))))

    if Niveau.getNiveau() == 1:
        for  i in range(4):
            for j in range(2):
                screen.blit(rond,((175+(55*i)),(550+(60*j))))

    #fait apparaitre les écritures
    screen.blit(menu,(890,645))
    screen.blit(confirmer,(695,645))
    screen.blit(abandonner,(515,645))

    if Niveau.getNiveau() == 1:
        screen.blit(niveau1,(510,20))
    elif Niveau.getNiveau() == 2:
        screen.blit(niveau2,(510,20))
    else:
        screen.blit(niveau3,(510,20))

    screen.blit(rondFer,(800,250))

    #3 lignes pour l'endroit où le code secret apparaitra
    pygame.draw.line(screen,noir,(185,25),(380,25),3)
    pygame.draw.line(screen,noir,(185,45),(380,45),3)
    pygame.draw.line(screen,noir,(512,45),(595,45),3)

    pygame.display.flip()

def fin(screen, code_secret, win):
    pygame.display.set_caption('Mastermind : Résultat')

    distance = 181
    temp = 0
    code = {'Rg' : (255,0,0), 'J':(255,255,0), 'Rs':(255,105,180), 'B':(0,0,255), 'N':(0,0,0), 'O':(255,165,0)}
    font = pygame.font.SysFont('impact', 100)

    rond1 = pygame.image.load('ressources/img/rondBoisClair.png')
    rond1 = pygame.transform.scale(rond1,(50,50))
    perdu = font.render('Perdu !', 0, (255,0,0))
    gagne = font.render('Gagné !', 0, (0,255,0))

    #remet les ronds clairs sur les lignes
    for i in range(4):
        screen.blit(rond1,(175+(i*55),10))

    #fait apparaitre le code secret
    for couleur in code_secret:
        pygame.draw.ellipse(screen, code[code_secret[temp]], (distance, 15, 40, 40))
        distance += 55
        temp += 1

    if win is True:
        screen.blit(gagne,(400,280))
        pygame.display.flip()
        return 'gagne'
    else:
        screen.blit(perdu,(400,280))
        pygame.display.flip()
        return 'abandonne'

def consignes(screen):
    pygame.display.set_caption('Mastermind : Consignes')

    blanc = (255,255,255)
    noir = (0,0,0)
    font =  pygame.font.SysFont('impact', 50)
    font1 = pygame.font.SysFont('verdana', 20)
    bouton = pygame.image.load('ressources/img/bouton.png')
    bouton = pygame.transform.scale(bouton,(170,80))

    suivant = font1.render('Suivant',0,(0,0,0))
    menu = font1.render('Menu', 0, (0,0,0))
    consigne1 = font.render('Consignes : Niveau 1',0,(0,0,0))
    consigne2 = font.render('Consignes : Niveau 2',0,(0,0,0))
    consigne3 = font.render('Consignes : Niveau 3',0,(0,0,0))

    textEssais1 = font1.render("* Vous avez un nombre d'essais de 10",0,(0,0,0))
    textEssais2 = font1.render("* Vous avez un nombre d'essais de 8",0,(0,0,0))
    textUnique = font1.render('* Toutes les couleurs sont uniques',0,(0,0,0))
    textInterdis = font1.render('Vous ne pouvez donc pas mettre 2 fois la même couleur',0,(0,0,0))
    textEfface = font1.render('* Pour effacer la dernière couleur posée, appuyez sur le bouton en fer rond',0,(0,0,0))
    textConfirmer = font1.render('* Pour confirmer une combinaison, appuyez sur "Confirmer"',0,(0,0,0))
    textAbandonner = font1.render('* Pour abandonner la partie, appuyez sur "Abandonner"',0,(0,0,0))
    textMenu = font1.render('* Pour retourner au menu, appuyez sur "Menu"',0,(0,0,0))
    textCode = font1.render('* Impossible de confirmer une combinaison si celle-ci ne possède pas 4 couleurs',0,(0,0,0))
    textDouble = font1.render('* Les couleurs peuvent se doubler, pas tripler ni quadrupler',0,(0,0,0))
    textDouble1 = font1.render('Si une couleur est doublée, les autres couleurs du code secret sont uniques',0,(0,0,0))
    textDouble2 = font1.render("Il se peut aussi qu'aucune couleur ne soit doublée",0,(0,0,0))
    textVert = font1.render('* Les chiffres apparaissant en vert signifient le nombre de couleur bien placée',0,(0,0,0))
    textRouge = font1.render('* Les chiffres apparaissant en rouge signifient le nombre de couleur mal placée',0,(0,0,0))

    #supprime tout et fait apparaitre les boutons les texte des boutons
    screen.fill(blanc)
    screen.blit(bouton,(830,620))
    screen.blit(bouton,(660,620))
    screen.blit(suivant,(880,645))
    screen.blit(menu,(717,645))

    #fait apparaitre les consignes en fonction du niveau
    if Niveau.getNiveau() == 1:
        screen.blit(consigne1,(300,10))
        screen.blit(textUnique,(60,335))
        screen.blit(textInterdis,(80,365))
        screen.blit(textEssais1,(60,395))
    if Niveau.getNiveau() == 2:
        screen.blit(consigne2,(300,10))
        screen.blit(textUnique,(60,335))
        screen.blit(textInterdis,(80,365))
        screen.blit(textEssais2,(60,395))
    if Niveau.getNiveau() == 3:
        screen.blit(consigne3,(300,10))
        screen.blit(textDouble,(60,335))
        screen.blit(textDouble1,(80,365))
        screen.blit(textDouble2,(80,395))

    pygame.draw.line(screen,noir,(302,70),(715,70),4)
    screen.blit(textConfirmer,(60,125))
    screen.blit(textAbandonner,(60,155))
    screen.blit(textMenu,(60,185))
    screen.blit(textEfface,(60,215))
    screen.blit(textCode,(60,245))
    screen.blit(textVert,(60,275))
    screen.blit(textRouge,(60,305))

    pygame.display.flip()


def jeu():
    #initialise le jeu
    screen = Screen().getScreen()
    jouer = True
    finPartie = "None"
    niveau = Niveau.getNiveau()
    accueil(screen)
    couleurs = []
    coups = 0
    consigne = False
    while jouer:
        for events in pygame.event.get():
            #si le joueur appuis sur la croix pour quitter
            if events.type == pygame.QUIT:
                jouer = False
                quit()
            #si le jouer clic sur un endroit du jeu
            if events.type == pygame.MOUSEBUTTONDOWN:
                #donne la position du curseur
                mouse = pygame.mouse.get_pos()
                #si le joueur est dans le menu
                if Niveau.getNiveau() is None:
                    if 410 < mouse[0] < 580 and 140 < mouse[1] < 220:
                        Niveau.setNiveauActuel(Niveau1())
                        consignes(screen)
                        code_secret = genererCode(4)
                    elif 410 < mouse[0] < 580 and 280 < mouse[1] < 360:
                        Niveau.setNiveauActuel(Niveau2())
                        consignes(screen)
                        code_secret = genererCode(4)
                    elif 410 < mouse[0] < 580 and 420 < mouse[1] < 500:
                        Niveau.setNiveauActuel(Niveau3())
                        consignes(screen)
                        code_secret = genererCode(4)
                elif Niveau.getNiveau() == 1 or Niveau.getNiveau() == 2 or Niveau.getNiveau() == 3:
                    #si le joueur est sur les cansignes
                    if consigne == False:
                        #touche suivant
                        if 830 < mouse[0] < 1000 and 620 < mouse[1] < 700:
                            fenetreJeu(screen)
                            consigne = True
                        #touche menu
                        elif 660 < mouse[0] < 830 and 620 < mouse[1] < 700:
                            couleurs = []
                            Niveau.setNiveauActuel(None)
                            accueil(screen)
                    #sinon si le joueur est sur la fenetre de jeu
                    #touche menu
                    elif 830 < mouse[0] < 1000 and 620 < mouse[1] < 700:
                        couleurs = []
                        Niveau.setNiveauActuel(None)
                        coups = 0
                        consigne = False
                        accueil(screen)
                    #touche abandonne
                    elif 490 < mouse[0] < 660 and 620 < mouse[1] < 700:
                        finPartie = fin(screen,code_secret,False)
                    #touche confirmer
                    elif 660 < mouse[0] < 830 and 620 < mouse[1] < 700:
                        finPartie = evaluer_proposition(screen, couleurs, coups,code_secret)
                        if len(couleurs) == 4:
                            coups += 1
                            couleurs = []
                    #pour chaque pion de couleur choisi
                    elif 800 < mouse[0] < 850 and 250 < mouse[1] < 300:
                        couleurs = supprime(screen,couleurs,coups)
                    elif 650 < mouse[0] < 700 and 70 < mouse[1] < 150:
                        couleurs = mettreCouleur(screen,couleurs,coups,'Rg')
                    elif 705 < mouse[0] < 755 and 480 < mouse[1] < 550:
                        couleurs = mettreCouleur(screen,couleurs,coups,'J')
                    elif 700 < mouse[0] < 760 and 150 < mouse[1] < 215:
                        couleurs = mettreCouleur(screen,couleurs,coups,'Rs')
                    elif 650 < mouse[0] < 700 and 230 < mouse[1] < 300:
                        couleurs = mettreCouleur(screen,couleurs,coups,'O')
                    elif 705 < mouse[0] < 755 and 310 < mouse[1] < 380:
                        couleurs = mettreCouleur(screen,couleurs,coups,'B')
                    elif 650 < mouse[0] < 710 and 380 < mouse[1] < 460:
                        couleurs = mettreCouleur(screen,couleurs,coups,'N')
                #si le jouer a perdu/abandoné/gagné, le jeueur peut que aller dans le menu
                elif finPartie == 'abandonne' or finPartie == 'gagne':
                    if 830 < mouse[0] < 1000 and 620 < mouse[1] < 700:
                        couleurs = []
                        Niveau.setNiveauActuel(None)
                        finPartie = None
                        coups = 0
                        accueil(screen)
                        consigne = False
            #si le joueur ne réussis au bout des coups maximum, le joueur perd
            elif Niveau.getNiveau() == 1:
                if coups == 10:
                    finPartie = fin(screen,code_secret,False )
            elif Niveau.getNiveau() == 2 or Niveau.getNiveau() == 3:
                if coups == 8:
                    finPartie = fin(screen,code_secret,False )

jeu()
