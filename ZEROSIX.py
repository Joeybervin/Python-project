
#@title
#______________________________________________________________________________ TOUS LES IMPORTATION DE MODULE ET DE FICHIER NECESSAIRE AU JEU_________________________________________________ 
import time
import locale
import csv
from random import randint

#_______________________________________________________________________________LANCEMENT DU JEU____________________________________________________________________________________________


def ZeroSix():
  Menu()
                                                                                                                
#_______________________________________________________________________________MENU____________________________________________________________________________________________

def Menu():
  espace()
  print("                                  -----------------         |  T’as pas un 06 ?  |         ------------------")
  print("   ")
  print("   ")
  print("   ")
  print("________________________________________   1: Nouvelle partie")
  print("________________________________________   2: Classement")
  print("________________________________________   3: About")
  print("________________________________________   4: Exit")
  print("   ")
  Choix = int(input())
  if Choix == 1:
    PlayGame()
  elif Choix == 2:
    classement()
  elif Choix == 3:
    About()
  elif Choix == 4:
    Exit()
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    Menu()

#_______________________________________________________________________________PLAY GAME____________________________________________________________________________________________



def PlayGame():
  synopsis()
  Deplacement = choixMouvementInGame()
  lieux = ""
  fin = 0
  while GameIsNotFinished():
    mouvementInGame(Deplacement)
    espace()
    if GameIsNotFinished():
      #time.sleep(5.5)
      for i in range(0,4,1) :
        print(Deplacement[i])
      if len(decompteRelous) > 2 : 
        print("5 : Rentrer chez soi")
    else :                                                                                                                                                                                                      
      print("Le jeu est fini...")
      if POINTS["patience"] < 1 :
        print("Tu as perdu patience avec tous ces relous...")
        print("Tu préfères rentrer chez toi directement et arrêter ta balade.")
        looser()
      elif POINTS["confiance"] < 1 : 
        print("Tu commences à vraiment avoir vraiment peur.")
        print("Tu préfères rentrer chez toi et arrêter ta balade.")
        looser()
      else : 
        print("Tu as réussi à rentrer chez soi !")
        print("Ça t'as fait du bien de prendre l'air mais tu aurais préféré éviter tous ces relous...")
        print("Prend soin de toi et n'hésite pas à en parler si tu en ressens le besoin.")
        print("Tu t'installes dans ton canapé sous ton plaid pour regarder Wonder Woman.")
        print("Tu te sens une âme de guerrière du quotidien !")
        winner()

def classement(): 
  fichier = open("jeu.csv" , "rt")
  lecteurCSV = csv.reader(fichier,delimiter=";", quoting=csv.QUOTE_NONE)
  for joueur in lecteurCSV :
    print(joueur)
  fichier.close()
  espace()
  print("Voulez vous retournez au menu ? oui / non")
  classementmenu = input()
  if classementmenu == str("oui") :
    Menu()
  else :
    classement()


#_______________________________________________________________________________FONCTION POUR L'ASPET____________________________________________________________________________________________


def espace():
  print("   ")
  print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
  print("   ")
#_______________________________________________________________________________ABOUT____________________________________________________________________________________________


def About():
  espace()
  print("Le jeu 'T’as pas un 06' ? a été pensé et développé par :")
  print("   ")
  print("Joey BERVIN")
  print("Chloé DOUSTALET")
  print("Kevin LACROIX")
  print("   ")
  print("Étudiants en première année à HETIC en Bachelor Concepteur développeur de solutions digitales.") 
  print("Le jeu a été réalisé dans le cadre du cours Fondamentaux de la programmation, enseigné par Loic JANIN.") 
  print("Pour le premier semestre, le projet était de développer un jeu RPG textuel en Python.")
  print("   ")
  print("1 : Retourner au menu")
  Retour = int(input())
  if Retour == 1 : 
    Menu()
  else : 
    Menu()

def Exit() :
  espace()
  quitter = input("Voulez-vous quitter le jeu ? yes/no : ")
  if quitter == str("no"):
    Menu()
  else :
    if quitter == str("yes") :
      print("   ")
      print("       ¯\_(ツ)_/¯ ")
      print("   ")
      exit()
#_______________________________________________________________________________LOOSER AND WINNER____________________________________________________________________________________________


def looser() :
  print("Tu finis par prendre un UBER pour rentrer plus vite")
  print("   ")
  print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("                                                                                                               PERDU !!")
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("   ")
  print("   ")
  print("SCORE :")
  print("   ")
  name = input("Un petit prénom qu'on te reconnaisse ? : ")
  print("Ton score est de ",POINTS["confiance"],"pts")
  pointsfinal = POINTS["confiance"]
  locale.setlocale(locale.LC_TIME,'')
  date = time.strftime('%d/%m %H:%M')
  fichier = open("jeu.csv" , "at")
  #fichier = open("jeu.csv", "at")
  ecrire = csv.writer(fichier,delimiter=";", quoting=csv.QUOTE_NONE)
  ecrire.writerow([date, name, pointsfinal])
  fichier.close()
  print("   ")
  print("   ")
  print("   ")
  lecture_score()

def winner() :
  print("AAAH !!! Qu'est ce qu'on est bien chez soi !!!!")
  print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("                                                                                                       (☞ﾟヮﾟ)☞  GAGNE !!  ☜(ﾟヮﾟ☜)")
  print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("   ")
  print("SCORE :")
  print("   ")
  name = input("Un petit prénom qu'on te reconnaisse ? : ")
  print("Ton score est de ",POINTS["confiance"],"pts")
  pointsfinal = POINTS["confiance"]
  locale.setlocale(locale.LC_TIME,'')
  date = time.strftime('%d/%m %H:%M')
  fichier = open("jeu.csv" , "at")
  #fichier = open("/content/drive/Shareddrives/PlusTrentesTrois/jeu.csv" , "at")
  ecrire = csv.writer(fichier,delimiter=";", quoting=csv.QUOTE_NONE)
  ecrire.writerow([date,name, pointsfinal])
  fichier.close()
  print("   ")
  print("   ")
  print("   ")
  lecture_score()

#_______________________________________________________________________________LECTURE DES SCORES____________________________________________________________________________________________

def lecture_score ():
  fichier = open("jeu.csv" , "rt")
  #fichier = open("/content/drive/Shareddrives/PlusTrentesTrois/jeu.csv" , "rt")
  lecteurCSV = csv.reader(fichier,delimiter=";", quoting=csv.QUOTE_NONE)
  for joueur in lecteurCSV :
    print(joueur)
  fichier.close()
  Menu()

#_______________________________________________________________________________PARAMETRES PAR DEFAUTS : JOUEUR + JEU_______________________________________________________________________


def lancement():
  #Va jusqu'à 4 pour que le jeu ne s'arrête pas quand les 3 relous sont passés
  Relous = [[1,2,3,4],[1,3,2,4],[2,1,3,4],[2,3,1,4],[3,1,2,4],[3,2,1,4]]
  i = randint(0,5)
  Relous = Relous[i]
  return Relous



OrdreR = lancement()

POINTS = {
        "confiance" : 30,
        "patience" : 10
}

INVENTAIRE = {
        "sac" : "sac",
        "tel" : "téléphone",
        #"sifflet" : "sifflet",
        #"alarme" : "alarme portable",
        #"spray" : "spray au poivre"
}

COMPETENCES = {
    #"Phrase insensée" : "La phrase insensée : 'Les dinosaures sont arc-en-ciels'",
    #"Self-défense" : "'Le pack': un ensemble de techniques de self-défense qui ferait fuir n'importe qui",
    #"Aide" : "Demander de l'aide : interpeler quelqu'un autour de vous, afin de vous sortir d'une situation pénible"
    
}
shopinventaire = {
        "1. article 1 :" : "sifflet",
        "2. article 2 :" : "alarme portable",
        "3. article 3 :" : "spray au poivre  (ಥ⌣ಥ) " 
    }

DOJO = {
    "1 :" : "ton rendez-vous avec l'une de tes amies au café 'ptit choux'",
    "2 :" : "ta séance d'initiation aux technique de self-defense (gratuite)",
    "3 :" : "Une conférence inédite sur le harcèlement de rue",
    "4 :" : "Si j'ai oublié, c'est que je ne voulais pas vraiment y allez, non ? tant pis une prochaine fois."
}

fin = 0
decompteDojo = []
decompteShop = []
decompteRelous = []

#_______________________________________________________________________________DEROULEMENT DU JEU________________________________________________________________________________________________


def GameIsNotFinished():
  if POINTS["confiance"] < 1 or POINTS["patience"] < 1 or fin == 1 : 
    return False 
  else : 
    return True 

def finish(reponse):
  if reponse == "oui" :
    fin = 1 
    return fin

#_______________________________________________________________________________SYNOPSIS____________________________________________________________________________________________



def synopsis() :
  espace()
  print("Dans ce jeu vous incarnez Lola, 26 ans, parisienne.")
  print("Vous incarnez aussi Aya, 34 ans, toulousaine.")
  print("Vous incarnez aussi Ines, 42 ans, bordelaise.")
  print("En fait, vous incarnez une femme qui souhaite profiter de la fin de journée avant de rentrer chez elle.")
  print("  ")
  lancer = input("Commencer ? oui/non : ")
  if lancer == str("oui") :  
    espace()
    print("Vous sortez du travail après une longue journée. C’est enfin le weekend !")
    print("Le soleil brille, il fait chaud. Ce serait dommage de rentrer directement chez vous sans en profiter.")
    print("Au lieu de prendre tout de suite le métro, vous décidez de vous balader en ville.")
    joueur()
  elif lancer == str("non"):
    Menu()
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    synopsis() 

#_______________________________________________________________________________PARAMETTRE DU JOUEUR AU DÉBUT____________________________________________________________________________________________


def joueur() :
    espace()
    print("Vous avez",POINTS["confiance"],"pts de confiance.")
    print("Vous avez",POINTS["patience"],"pts de patience.")
    print("Si les points tombent à 0 le jeu s'arrête !")
    print("  ")
    print("Pour l'instant, vous possédez :")
    for item in INVENTAIRE :
        print(INVENTAIRE[item])
    print("(Attention : chaque objet n'est utilisable qu'une fois)")
    debut()


#_______________________________________________________________________________ACTIONS DE DÉBUT DE JEU____________________________________________________________________________________________


def debut():
  espace()
  print("° Quel chemin souhaitez vous prendre ?")
  print("1 : Marcher le long de l'avenue Olympe de Goujes")
  print("2 : Prendre la rue Frida Kahlo")
  print("  ")
  debmouv = int(input())
  if debmouv == 1 :
    espace()
    print("Vous avez été tellement prise par le travail dernièrement que vous n'avez eu le temps de voir aucun de vos amis...")
    print("Il faut rattraper ça !")
    ChoixDeDebut()
  elif debmouv == 2:
    espace()
    print("Au programme de ce week-end : NO BRA, cheveux gras et tête à tête romantique avec votre lit.")
    ChoixDeDebut()
  else :
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    debut()

def ChoixDeDebut() :
  espace()
  print("En attendant, laissez vous guider par votre humeur")
  print("   ")
  print("° Quelle direction souhaites-tu prendre ? (on se tutoie dorénavant !)")
  print("1 : Prendre à gauche comme à ton habitude")
  print("2 : Prendre à droite, tous les chemins mènent à Rome")
  print("3 : Rentrer dans cette nouvelle petite boutique qui vient tout juste d'ouvrir")
  print("  ")
  Choixdebut2 = int(input())
  if Choixdebut2 == 1 :
    espace()
    print("Tu regardes les terrasses autour de toi. Il y a du monde aujourd'hui.")
  elif Choixdebut2 == 2 :
    espace()
    print("1km en talons ça brûle, ça brûle. 1km en talons ça donne envie pleurer")
    print("   ")
  elif Choixdebut2 == 3 :
    espace()
    print("OMG !!")
    debutshop = 1
    shop(debutshop)
  else :
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    ChoixDeDebut() 

#_______________________________________________________________________________DEPLACEMENT DANS LE JEU_____________________________________________________________________________________

def choixMouvementInGame(): #Il faudrait ne faire apparaitre les transports et retour qu'au bout d'un moment
  Possib = ["1 : Prendre la rue à droite","2 : Prendre la rue à gauche","3 : Prendre le metro","4 : Prendre le bus"]
  if len(OrdreR) < 3: 
    Possib.append("5 : Rentrer chez soi")
  if len(Possib) == 4 : 
    for i in range(0,4,1) :
      print(Possib[i])
  else : 
    for i in range(0,5,1) :
      print(Possib[i])
  return Possib 
  
def mouvementInGame(Possib):
  espace()
  Deplacement = int(input())
  if Deplacement == 1 or Deplacement == 2 :
    lieux ="rue"
    evenement(lieux)
  elif Deplacement == 3 :
    if Possib[2] == "3 : Prendre le metro": 
      lieux ="metro"
      Possib[2] = "3. Tu n'as plus de tickets de métro"
      evenement(lieux)
    else :
      espace()
      print("Tu n'as plus de tickets...")
      print("Tu ne peux donc pas prendre le métro. Il va falloir marcher !")
  elif Deplacement == 4 :
    if Possib[3] == "4 : Prendre le bus" :
      lieux ="bus"
      Possib[3] = "4. Tu n'as plus de ticket de bus"
      evenement(lieux)
    else :
      espace() 
      print("Tu n'as plus de tickets...")
      print("Tu ne peux donc pas prendre le bus. La marche, c'est bon pour la santé !")
  elif Deplacement == 5 and len(decompteRelous) > 2 :
    boss1()
  else :
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    

#_______________________________________________________________________________RUES__________________________________________________________________________________

def nomRues(): 
  NomDeRue = ["Simone de Beauvoir", "Hannah Arendt","Sévigné","Simone Weil","Marguerite Yourcenar",
              "Jeanne Moreau","Joséphine Baker","Peggy Guggenheim","Gisèle Halimi","Katia Krafft", "Thérèse Clerc", "Las Mariposas", "Agnodice","George Sand",
              "Sarah Bernhardt","Coco Chanel","Marie Curie","Colette","Aliénor d’Aquitaine","Catherine De Médicis"]
  return NomDeRue

N = nomRues()

def choixRues(NomDeRue):
  description = {
      "Simone de Beauvoir" : "Tu joues au ninja, en essayant d'éviter les crottes de chiens qui se trouvent sur le trotoir.",
      "Hannah Arendt" : "Une rue très passante, réunissant toute la condition de l'Homme moderne.",
      "Sévigné" : "Plein de petits restaurants cohabitent dans cette rue et une bonne odeur de crêpe vient chatouiller ton nez",
      "Simone Weil" : "Tu te demandes bien pourquoi tu as pris cette rue, tous les lampadaires sont cassés. Tu n'y vois rien du tout.",
      "Marguerite Yourcenar" : "Une jolie petite rue.",
      "Jeanne Moreau" : "Une petite ruelle déserte se présente devant toi, chacun de tes pas résonnent.",
      "Joséphine Baker" : "Tu reconnais ce petit restaurant 'Best B', qui fait les meilleurs burgers du monde.",
      "Peggy Guggenheim" : "Tu vois dans une vitrine un malheureux petit coussin à 500 euros !! ...  Nous n'avons pas les mêmes valeurs.",
      "Gisèle Halimi" : "Cela faisait longtemps que tu n'étais pas passée par là.",
      "Katia Krafft" : "Quelle statue bizarre, j'ai beau tourner la tête dans tous les sens, l'art abstrait reste un mystère pour moi.",
      "Thérèse Clerc" : "Cette rue semble interminable, elle est aussi longue que la muraille de Chine.",
      "Las Mariposas" : "Le trottoir est tellement étroit que tu n'arrêtes pas de te faire bousculer.",
      "Agnodice" : "Cette petite boutique te semble fort sympathique, jusqu'à ce que tu te rappelles du dernier appel de ton banquier.",
      "George Sand" : "SPLASH !! Et m*rcredi tu l'avais pas vue celle-là. Bon, j'ai entendu que ça porte chance ... Enfin, j'espère.",
      "Sarah Bernhardt" : "Un spectacle de rue commence devant toi, tu t'arrêtes 30 sec pour regarder.",
      "Coco Chanel" : "Cette rue monte .... Non, elle MOOOOOOOOOOOOOOONTE, tes mollets sont en feux.",
      "Marie Curie" : "Tu apperçois Marie au loin. Tu baisses la tête regarde ton téléphone et accélère la cadence. Faites qu'elle ne te vois pas !!",
      "Colette" : "Une voiture vient de rouler dans une flaque d'eau et devine qui est l'élue ?",
      "Aliénor d’Aquitaine" : "Un couple se dispute en plein milieu de la rue, le jeune homme ne semble pas content. Tu ralentis pour pouvoir écouter leur conversation.",
      "Catherine De Médicis" : "Tu n'étais jamais passée par là, mais cette rue est très mignonne."
  }
  iL = randint(0,len(NomDeRue) - 1)
  espace()
  print("Tu es dans la rue", NomDeRue[iL])
  print(description[NomDeRue[iL]])
  NomDeRue.pop(iL)
  event(OrdreR)

#_______________________________NE MARCHE PAS__________=====>_____________________ RUES 2 : pour ne pas que le joueur ce trouve à cours de mouvement si il décide de continuer de jouer_______________________________________________________

#def nomrues2() :
  #NomDeRue2 = ["Simone de Beauvoir", "Hannah Arendt","Sévigné","Simone Weil","Marguerite Yourcenar",
              #"Jeanne Moreau","Joséphine Baker","Peggy Guggenheim","Gisèle Halimi","Katia Krafft", "Thérèse Clerc", "Las Mariposas", "Agnodice","George Sand",
              #"Sarah Bernhardt","Coco Chanel","Marie Curie","Colette","Aliénor d’Aquitaine","Catherine De Médicis"]
  #return NomDeRue2

#M = nomrues2()

#def choixRues2(NomDeRue2):
  #description2 = {
      #"Simone de Beauvoir" : "Tu joues au ninja, en essayant d'éviter les crottes de chiens qui se trouvent sur le trotoir.",
      #"Hannah Arendt" : "Une rue très passante, réunissant toute la condition de l'Homme moderne.",
      #"Sévigné" : "Plein de petits restaurants cohabitent dans cette rue et une bonne odeur de crêpe vient chatouiller ton nez",
      #"Simone Weil" : "Tu te demandes bien pourquoi tu as pris cette rue, tous les lampadaires sont cassés. Tu n'y vois rien du tout.",
      #"Marguerite Yourcenar" : "Une jolie petite rue.",
      #"Jeanne Moreau" : "Une petite ruelle déserte se présente devant toi, chacun de tes pas résonnent.",
      #"Joséphine Baker" : "Tu reconnais ce petit restaurant 'Best B', qui fait les meilleurs burgers du monde.",
      #"Peggy Guggenheim" : "Tu vois dans une vitrine un malheureux petit coussin à 500 euros !! ...  Nous n'avons pas les mêmes valeurs.",
      #"Gisèle Halimi" : "Cela faisait longtemps que tu n'étais pas passée par là.",
      #"Katia Krafft" : "Quelle statue bizarre, j'ai beau tourner la tête dans tous les sens, l'art abstrait reste un mystère pour moi.",
      #"Thérèse Clerc" : "Cette rue semble interminable, elle est aussi longue que la muraille de Chine.",
      #"Las Mariposas" : "Le trottoir est tellement étroit que tu n'arrêtes pas de te faire bousculer.",
      #"Agnodice" : "Cette petite boutique te semble fort sympathique, jusqu'à ce que tu te rappelles du dernier appel de ton banquier.",
      #"George Sand" : "SPLASH !! Et m*rcredi tu l'avais pas vue celle-là. Bon, j'ai entendu que ça porte chance ... Enfin, j'espère.",
      #"Sarah Bernhardt" : "Un spectacle de rue commence devant toi, tu t'arrêtes 30 sec pour regarder.",
      #"Coco Chanel" : "Cette rue monte .... Non, elle MOOOOOOOOOOOOOOONTE, tes mollets sont en feux.",
      #"Marie Curie" : "Tu apperçois Marie au loin. Tu baisses la tête regarde ton téléphone et accélère la cadence. Faites qu'elle ne te vois pas !!",
      #"Colette" : "Une voiture vient de rouler dans une flaque d'eau et devine qui est l'élue ?",
      #"Aliénor d’Aquitaine" : "Un couple se dispute en plein milieu de la rue, le jeune homme ne semble pas content. Tu ralentis pour pouvoir écouter leur conversation.",
      #"Catherine De Médicis" : "Tu n'étais jamais passée par là, mais cette rue est très mignonne."
  #}
  #iL = randint(0,len(NomDeRue2) - 1)
  #espace()
  #print("Tu es dans la rue", NomDeRue2[iL])
  #print(description2[NomDeRue2[iL]])
  #NomDeRue2.pop(iL)
  #event(OrdreR)


#_______________________________________________________________________________EVENEMENT : Si choiRues2 avait marché____________________________________________________________________________

# LE SYSTEME NE FONCTIONNE PAS : POUS ALLONGER LE NOMBRE DE RUES QUI S'AFFICHE ET NE PAS FAIRE UN OUT OF RANGE
#def evenement(lieux):
  #i = 0
  #if lieux == "rue":
    #while i < 20 :
      #choixRues(N)
      #i += 1
    #if i == 20 :
      #j = 0
      #while j < 20 :
        #choixRues2(M)
        #j += 1

#_______________________________________________________________________________EVENEMENT___________________________________________________________________________________________


def evenement(lieux):
  if lieux == "rue":
    choixRues(N)
  elif lieux == "metro":
    espace()
    print("Tu arrives sur le quai de métro.")
    print("Le métro approche et il est bondé...") 
    print("Pas de places assises pour aujourd'hui...") 
    print("Tu te tiens à la barre. Plus que 5 stations.")
    relouMetro()
  else :
    espace()
    print("Tu es à l'arrêt de bus. Mince, tu viens de le louper...")
    print("Le prochain est dans 10 minutes.")
    print("L'attente semble interminable.")
    relouBus()

#_______________________________________________________________________________ACTION__________________________________________________________________________________

def event(OrdreR):
  rere = OrdreR[0]
  relouChance = randint(0,9)
  if relouChance == 2 or relouChance == 9:
    if len(decompteShop) < 3 :
      shop(0)
    else :
      rien()
  elif relouChance == 4 or relouChance == 5 :
    rien()
  elif relouChance == 6 or relouChance == 7 :
    if len(decompteDojo) < 3 :
      dojo()
    else :
      rien()
  else :
    relouRues(rere)

def rien(): #Peut-ëtre donner plus de chance à la fonction rien() d'apparaître
  rien = ["La vie est belle il ne se passe rien", "Tu continues ton chemin", "Il faut que tu penses à rappeler ta soeur", "Tu commences à avoir une petite faim", "Aujourd'hui, cheat day !! À toi le bon KEBAB  (っ˘ڡ˘ς)",
          "Ça fait longtime que tu n'as pas appelé teilleur ami.", "Ton téléphone vibre, tu regardes 'FÉLICITATIONS VOUS ÊTES L'HEURE...' ... courrier indésirable.","Tu as envie de faire pipi, mais aucun toilette dans les alentours, courage !!",
          "ATCHOUUUM !! D'un seul coup le trottoir se vide complètement. （　ﾟДﾟ）","Demain c'est l'anniversaire de MANON, tu programmes un messages à 11h50. Au cas où tu oublierais.", "Plus que 5on m jours avant le début de tes vacances. YOUHOUU!!!  “ヽ(´▽｀)ノ” ",
          "Du C.H.O.C.O.L.A.T, tu veux du chocolat. Il faut que tu ailles chercher ta dose hebdomadaire rapidement  (っ˘ڡ˘ς)", "Il fait froid aujourd'hui, tu sors une écharpe de ton sac et la met autour de ton coup.",
          "Tu mets tes écouteurs, le chemin est encore long jusqu'à la maison  ♪♪ ヽ(ˇ∀ˇ )ゞ ","Tu vois un chiot qui marche avec son propriétaire, tu as envie de l'attraper et de courrir avec...  ''⌐(ಠ۾ಠ)¬''' ","Tu te demandes pourquoi tu as mis ces chaussures aujourd'hui щ（ﾟДﾟщ）",
          "Si seulement tu étais Mimie Mathy, un claquement de doigts et HOP à la maison !","Il faut que tu regardes le cours du navet ce soir sur ton îles","Monsieur JANIN si vous tombé sur cette phrase vous devez rajouter 1 point à notre note globale. Parce que ... Vous nous aimez bien ? ^^",
          "Dans la ville, terrible ville, le roi est mort ce soir .... AYIIIIIIIII !  ヾ(´〇`)ﾉ♪♪♪"]
  n = randint(0,len(rien)-1)    
  print(rien[n])
  rien.pop(n)

#_______________________________________________________________________________SHOP______________________________________________________________________________________________

def shop(debutshop) :
  if debutshop == 0 :
    espace()
    print("Vous passez devant une boutique vendant des objets en tout genre et certains articles attirent votre regard")
    print("Voulez vous entrez dans la boutique ?")
    print("1 : Oui, je souhaite entrer.")
    print("2 : Non, je continue mon chemin")
    choixshop = int(input())
    shopON(choixshop)
  else :
    choixshop = 1
    shopON(choixshop)


def shopON(choixshop) :
  if choixshop == 1 :
    espace()
    print("Bienvenue dans notre magasin 'Je mords pas mais fais gaffe !!  ᕦ(ò_óˇ)ᕤ '")
    print("Nous proposons des objets en tout genre pour la défense.")
    print("   ")
    print("Le vendeur te propose alors plusieurs articles.")
    print("   ")
    print("Que souhaites-tu prendre ?")
    print("   ")
    for article in shopinventaire :
      print(article, shopinventaire[article])
    print("   ")
    choixarticle = int(input())
    if choixarticle == 1 :
        decompteShop.append(1)
        INVENTAIRE.update({"sifflet" : "sifflet"}) #SOLUTION A CHERCHER
        shopinventaire.pop("1. article 1 :")
        print("L'article a été placé dans ton Inventaire")
        print("   ")
        print("Le vendeur te remercie pour ton achat et espère te revoir bientôt.")
        print("À bientôt")
        print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    elif choixarticle == 2 :
        decompteShop.append(1)
        INVENTAIRE.update({"alarme" : "alarme portable"})
        shopinventaire.pop("2. article 2 :")
        print("L'article a été placé dans ton Inventaire")
        print("   ")
        print("Le vendeur te remercie pour ton achat et espère te revoir bientôt  ⊂(◉‿◉)つ .")
        print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    elif choixarticle == 3 :
      decompteShop.append(1)
      INVENTAIRE.update({"spray" : "spray au poivre"}) #SOLUTION A CHERCHER
      shopinventaire.pop("3. article 3 :")
      print("L'article a été placé dans ton Inventaire")
      print("   ")
      print("Le vendeur te remercie pour ton achat et espère te revoir bientôt.")
    else :
      print("À trop hésiter, le vendeur a dû fermer la boutique.")
      print("Tu n'as rien pu prendre malheureusement...")
  elif choixshop == 2 :
    print("Ce sera pour une autre fois, continuons notre chemin.")
  else :
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    shopON(1)


#_______________________________________________________________________________DOJO______________________________________________________________________________________________

def dojo() :
  decompteDojo = 0
  espace()
  print("BZZZ !!! BZZZZZ !!! BZZZZZZT !!")
  print("   ")
  print("Ton téléphone sonne !!!")
  print("C'est un rappel !!!")
  print("...")
  print("MIIINCE !! Tu as complètement oublié :")
  print("   ")
  for RDV in DOJO :
    print(RDV, DOJO[RDV])
  print("   ")
  dojochoix = int(input())
  print("   ")
  if dojochoix == 1:
    dojocafe()
  elif dojochoix == 2 :
    dojocours()
  elif dojochoix == 3 :
    dojoconference()
  elif dojochoix == 4 :
    ("Tu ranges ton téléphone dans ton sac et reprends ta route  ( ఠ ͟ʖ ఠ)")
  else :
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    dojo()
  

def dojocafe() :
  decompteDojo.append(1)
  print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("Après avoir pris à gauche rue Dulcie September, tu arrives enfin au café")
  print("   ")
  print("Après s'être moquées de la nouvelle coloration du chien de ta voisine ... ... cramoisi ..., vous en venez à un sujet plus sérieux.")
  print("Vous parlez de tous ces relous rencontrés. Vous ne manquez malheureusement pas d'anecdotes.")
  print("Il est temps de vous dire au revoir car le temps file.")
  print("Avant de vous séparer, ton amie te donne un conseil :")
  print("   ")
  print("'J'ai entendu que lorsque l'on se fait agresser, sortir une phrase n'ayant ni queue ni tête peut aider à destabiliser la personne en face.'")
  print("'Par exemple : Les dinosaures sont arc-en-ciels.'  乁( ◔ ౪◔)「      ┑(￣Д ￣)┍ ")
  print("   ")
  print("Merci du conseil, au revoir !!")
  espace()
  print("Une technique a été ajoutée dans tes COMPETENCES")
  print("Tu as gagné 5pts confiance")
  POINTS["confiance"] = POINTS["confiance"] + 5
  print("Il t'en reste",POINTS["confiance"])
  COMPETENCES.update({"Phrase insensée" : "La phrase insensée : 'Les dinosaures sont arc-en-ciels'"})
  DOJO.pop("1 :")

def dojocours() :
  decompteDojo.append(1)
  espace()
  print("Après un petit marathon pour arriver à l'heure, te voilà enfin arrivée devant la salle")
  print("Durant la séance tu apprends plusieurs techniques afin de pouvoir te défendre.")
  print("   ")
  print("Self-défense : 'le pack', un ensemble de techniques de self-défense qui ferait fuir n'importe qui   (ノಠ ∩ಠ)ノ彡( \o°o)\ ")
  print("    ")
  print("Après cette séance tu te sens plus confiante !!")
  espace()
  print("Une technique a été ajoutée dans tes COMPETENCES")
  print("Tu as gagné 5pts confiance")
  POINTS["confiance"] = POINTS["confiance"] + 5
  print("Il t'en reste",POINTS["confiance"])
  COMPETENCES.update({"Self-défense" : "'Le pack': un ensemble de techniques de self-défense qui ferait fuir n'importe qui"})
  DOJO.pop("2 :")

def dojoconference() :
  decompteDojo.append(1)
  espace()
  print("Tu arrives tout pile pour la conférence. Impatiente, tu de dépêches de trouver une place")
  print("   ")
  print("La conférence se termine après un petit meet-up avec les différents conférenciers")
  print("Tu as été marquée par l'un des conférenciers en particulier et par sa phrase :") 
  print("'N'ayez pas peur de demander de l'aide et d'interpeler les gens autour de vous!!'")
  espace()
  print("Une technique a été ajoutée dans tes COMPETENCES")
  POINTS["confiance"] = POINTS["confiance"] + 5
  print("Il t'en reste",POINTS["confiance"])
  COMPETENCES.update({"Aide" : "Demander de l'aide : interpeler quelqu'un autour de vous, afin de vous sortir d'une situation pénible"})
  # Voir si on ajouter des points de compétences
  DOJO.pop("3 :")



#_______________________________________________________________________________RELOUS____________________________________________________________________________________________

def relouRues(rere) :
  if rere == 1 :
    relou1()
  elif rere == 2 : 
    relou2()
  elif rere == 3 :
    relou3()
  else : 
    print("Tu as assez vu de relous pour aujourd'hui. Tu as mis tes écouteurs et tu n'entends plus rien.")

#_______________________________________________________________________________RELOUS1____________________________________________________________________________________________


def relou1(): 
  decompteRelous.append(1) 
  espace()
  print("Tout d’un coup, un relou sauvage apparaît...") 
  print("'Ton jean il te va trop bien franchement, ça te fait un de ces culs!'")
  print(" ")
  print("Tu as perdu 5 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 5
  print("Il t'en reste",POINTS["confiance"])
  print(" ") 
  print("Tu décides de :")
  print("1: Réagir") 
  print("2: Ne rien dire et descendre à la station suivante")
  print(" ")
  decision = int(input()) 
  if decision == 1 : 
    reagir("relou1")
  elif decision == 2 : 
    ignorer("relou3")
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    relou1()
  espace()
  print("Quand on dit aux filles de faire attention à la façon dont elles s'habillent, ça te fait bien rire !")
  print("Déjà c'est idiot mais avec ton jean tu prouves que l'harcèlement de rue existe quelle que soit la tenue.") 
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")
  OrdreR.pop(0)
  return OrdreR


#_______________________________________________________________________________RELOUS2____________________________________________________________________________________________

def relou2():
  decompteRelous.append(2) 
  espace()
  print("                           | CONFRONTATION (╬ ಠ益ಠ) |")
  print("   ")
  print("Tu marches tranquillement quand soudain, une bande de relous sauvage apparaît…")
  print("Une voix mélodieuse lance un :") 
  print("'Hé Mademoizelle'")
  print("Tu préfères ne rien répondre...")
  print("Mais voilà que tout d’un coup, une autre voix s’élève :")
  print("“T’entends pas quand on te parle ou quoi !”")
  print(" ")
  print("Tu as perdu 10 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 10
  print("Il t'en reste",POINTS["confiance"]) 
  print(" ")
  print("Tu décides de :")
  print("1: Réagir") 
  print("2: Ne rien dire et descendre à la station suivante")
  print(" ")
  decision = int(input()) 
  if decision == 1 : 
    reagir("relou2")
  elif decision == 2 : 
    ignorer("relou2")
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    relou2()
  espace()
  print("L'effet de groupe vraiment ça ne réussit pas à certains...")
  print("Ils sont bêtes x 2, se sentent puissants x2 et toi tu as peur x 2.")
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")
  OrdreR.pop(0)
  return OrdreR


#_______________________________________________________________________________RELOUS3____________________________________________________________________________________________


def relou3():
  decompteRelous.append(3) 
  espace()
  print("                           | CONFRONTATION (╬ ಠ益ಠ) |")
  print("   ")
  print("Tu passes devant un homme assis sur un banc.")
  print("Tu entends un sifflement.")
  print(" ")
  print("Tu as perdu 5 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 5
  print("Il t'en reste",POINTS["confiance"])
  print(" ") 
  print("Tu décides de :")
  print("1: Réagir") 
  print("2: Ne rien faire et continuer ton chemin")
  print(" ")
  decision = int(input()) 
  if decision == 1 : 
    reagir("relou3")
  elif decision == 2 : 
    ignorer("relou3")
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    relou3()
  espace()
  print("Tu n'es pas un chien franchement...")
  print("Qui peut croire que siffler quelqu'un est un compliment ?")
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")
  OrdreR.pop(0)
  return OrdreR

#_______________________________________________________________________________RELOUS METRO____________________________________________________________________________________________


def relouMetro() : 
  print("                           | CONFRONTATION (╬ ಠ益ಠ) |")
  print("   ")
  decompteRelous.append(4) 
  espace()
  print("D'un coup, tu sens une main qui touche tes fesses et une sensation bizarre dans ton dos.")
  print("Tu t’en doutes mais tu vérifies.") 
  print("Et oui, cette fois-ci tu as affaire à une espèce pire qu'un relou sauvage. Il s’agit d’un frotteur.")
  print(" ")
  print("Tu as perdu 5 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 5
  print("Il t'en reste",POINTS["confiance"])
  print(" ") 
  print("Tu décides de :")
  print("1: Réagir") 
  print("2: Ne rien dire, car tu te sens trop mal, et descendre à la station suivante")
  print(" ")
  decision = int(input()) 
  if decision == 1 : 
    reagir("relouMetro")
  elif decision == 2 : 
    ignorer("metro")
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    relouMetro()
  espace()
  print("Tu es mitigée entre le choc et l'énervement mais le trajet continue.")
  print("Tu gardes à l'esprit qu'il s'agit d'une agression sexuelle et que tu as la possibilité de porter plainte.")
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")


#_______________________________________________________________________________RELOUS BUS____________________________________________________________________________________________


def relouBus() : 
  print("                           | CONFRONTATION (╬ ಠ益ಠ) |")
  print("   ")
  decompteRelous.append(5) 
  espace()
  print("Sorti de nulle part, un relou sauvage apparait…") 
  print("Il vient s'asseoir à côté de toi et entame la conversation.")
  print("Après quelques échanges par politesse, tu lui fais comprendre que tu ne souhaites pas poursuivre la conversation.")
  print("Réponse immédiate du charmant interlocuteur : 'Tu te prends pour qui franchement à faire la meuf comme çà !'")
  print("'Ca va je t’agresse pas, je viens te parler tranquille.'")
  print(" ") 
  print("Tu as perdu 5 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 5
  print("Il t'en reste",POINTS["confiance"])
  print(" ") 
  print("Tu décides de :")
  print("1: Réagir") 
  print("2: Ne rien dire, partir de l'arrêt de bus et finir le trajet à pieds.")
  print(" ")
  decision = int(input()) 
  if decision == 1 : 
    reagir("relouBus")
    espace()
    print("Enfin débarassée de ce relou...")
    print("Tu te sens plus en sécurité dans le bus.")
  elif decision == 2 : 
    ignorer("bus")
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    relouBus() 
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")

#_______________________________________________________________________________BOSS______________________________________________________________________________________________

#Le boss est à battre en deux fois. 
#Quand on croit s'en être debarassé la première fois, en fait il nous a suivi

def boss1():
  print("                           |(╬ ಠ益ಠ) BOSS (╬ ಠ益ಠ) |")
  print("   ")
  espace()
  print("Tu marches dans la rue en profitant du soleil.")
  print("Tu sens les regards insistants d'un homme un peu plus haut dans la rue à droite.")
  print("Tu es fatiguée suite à tous ces relous rencontrés, et tu décides de ne pas y prêter attention.") 
  print("Tu arrives à sa hauteur, puis lorsque tu le dépasses il te met une main aux fesses.")
  print(" ")
  print("Tu as perdu 15 points de confiance.")
  POINTS["confiance"] = POINTS["confiance"] - 15
  print("Il te reste",POINTS["confiance"],"points de confiance.")
  print(" ") 
  print("Ça suffit maintenant ! Quand tu croyais avoir atteint tes limites, voilà qu'un nouvel incident arrive.")
  reagir("boss1")
  print("Tu te sens salis...")
  print("Tu n'oublies pas qu'il s'agit d'une agression sexuelle et donc d'un acte répréhensible par la loi.")
  print("Actuellement tu as",POINTS["confiance"],"points de confiance.")
  boss2()

def boss2():
  espace()
  print("                           | (╬ ಠ益ಠ) BOSS LE RETOUR (╬ ಠ益ಠ) |")
  print("   ") 
  espace()
  print("Tu commences à vraiment être à bout de nerfs.") 
  print("Heureusement que tu es bientôt arrivée chez toi.") 
  print("Tout d’un coup tu entends du bruit et tu te retournes.") 
  print("Le relou est toujours là, il t’a suivi.")
  print("Tu commences à avoir vraiment peur.") 
  print("En plus, vous n'êtes que tous les deux dans la rue...") 
  print("Il voit que tu l'as remarqué mais ça ne l’arrête pas.")
  reagir("boss2")
  finish("oui")




#_______________________________________________________________________________COMBAT REACTIONS____________________________________________________________________________________________



def ignorer(lieux):
  espace()
  if lieux == "metro":
    print("ε=ε=ε=┌(;*´Д`)ﾉ")
    print("Tu préfères finir le trajet à pieds car tu as peur de te faire agresser à nouveau.")
  elif lieux == "bus":
    print("ε=ε=ε=┌(;*´Д`)ﾉ")
    print("Finalement marcher c'est bien aussi.")
  elif lieux == "relou1":
    print("ε=ε=ε=┌(;*´Д`)ﾉ")
    print("Tu es tellement habituée à ce genre de relou que tu ne réagis même pas.")
  elif lieux == "relou2":
    print("ε=ε=ε=┌(;*´Д`)ﾉ")
    print("Ils sont quand même nombreux... Tu préfères ne pas prendre de risques.")
  else : 
    print("   ")
  print("Tu as perdu 5 points de patience.")
  POINTS["patience"] = POINTS["patience"] - 5
  print("Il t'en reste",POINTS["patience"])
  print(" ")
  print("Attention, tu ne peux ignorer qu'un relou.")
  print("La seconde fois, c'est retour à la maison.")
  OrdreR.pop(0)
  return OrdreR

def reagir(relou):
  espace() 
  print("Voici ce que tu as en ta possession pour te défendre : ")
  print("   ")
  print("Dans ton inventaire :")
  for item in INVENTAIRE :
    print(INVENTAIRE[item])
  print("   ")
  print("Dans tes compétences :")
  if len(COMPETENCES) > 0 : 
    for item in COMPETENCES :
      print(COMPETENCES[item])
  else : 
    print("Tu n'as pas encore de compétences")
  print(" ")
  print("Tu choisis de :")
  print("1. Utiliser un élément de l'inventaire")
  print("2. Utiliser une compétence")
  print("3. Parler")
  if relou == boss2 : 
    print("4. Rentrer dans un magasin que tu apperçois sur ta gauche.")
  print(" ")
  reaction = int(input())
  if reaction == 1 : 
    utilisationInventaire(relou)
  elif reaction == 2 : 
    utilisationCompetences(relou)
  elif reaction == 3 : 
    reponse(relou)
  elif reaction == 4 and relou == boss2 : 
    print("Tu remercies le ciel d'avoir mis ce magasin sur ton chemin.")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
    magasin()
  else : 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    reagir(relou)


#_______________________________________________________________________________OPTIONS DURANT LE COMBAT____________________________________________________________________________________________



def utilisationInventaire(relou):
  espace()
  print("Quel objet veux-tu utiliser ?")   
  if len(INVENTAIRE) > 0 :
    print("1: ", INVENTAIRE.get('sac', "Déjà utilisé"))
    print("2: ", INVENTAIRE.get('tel', "Déjà utilisé"))
    print("3: ", INVENTAIRE.get('sifflet', "A débloquer"))
    print("4: ", INVENTAIRE.get('alarme', "A débloquer"))
    print("5: ", INVENTAIRE.get('spray', "A débloquer"))  
    choixInventaire = int(input())
  #attention si l'on change les noms qui s'affichent pour les objets de l'inventaire, mettre à jour ici aussi
    if "sac" in INVENTAIRE.values() and choixInventaire == 1 :
      INVENTAIRE.pop("sac")
      sac(relou)
    elif "téléphone" in INVENTAIRE.values() and choixInventaire == 2:
      INVENTAIRE.pop("tel")
      telephone(relou)
    elif "sifflet" in INVENTAIRE.values() and choixInventaire == 3:
      INVENTAIRE.pop("sifflet")
      sifflet(relou)
    elif "alarme portable" in INVENTAIRE.values() and choixInventaire == 4:
      INVENTAIRE.pop("alarme")
      alarme(relou)
    elif "spray au poivre" in INVENTAIRE.values() and choixInventaire == 5:
      INVENTAIRE.pop("spray")
      spray(relou)
    else : 
      print("Objet non utilisable")
  else :
    print("Tu n'as pas d'objet à utiliser actuellement.")
    reagir(relou)

def utilisationCompetences(relou):
  espace() 
  print("Quelle compétence veux-tu utiliser ?") 
  if len(COMPETENCES) > 0 :
    print("1: ", COMPETENCES.get('Phrase insensée', "A débloquer"))
    print("2: ", COMPETENCES.get('Self-défense', "A débloquer"))
    print("3: ", COMPETENCES.get('Aide', "A débloquer"))  
    choixCompetence = int(input())
  #attention si l'on change les phrases qui s'affichent pour les compétences, mettre à jour ici aussi
    if "La phrase insensée : 'Les dinosaures sont arc-en-ciels'" in COMPETENCES.values() and choixCompetence == 1:
      COMPETENCES.pop("Phrase insensée")
      phrase(relou)
    elif "'Le pack': un ensemble de techniques de self-défense qui ferait fuir n'importe qui" in COMPETENCES.values() and choixCompetence == 2:
      COMPETENCES.pop("Self-défense")
      selfdefense(relou)
    elif "Demander de l'aide : interpeler quelqu'un autour de vous, afin de vous sortir d'une situation pénible" in COMPETENCES.values() and choixCompetence == 3:
      COMPETENCES.pop("Aide")
      aide(relou)
    else : 
      print("Tu n'as pas cette compétence.")
  else :
    print("Tu n'as pas de compétences à utiliser actuellement.")
    reagir(relou)


#_______________________________________________________________________________SAC____________________________________________________________________________________________


def sac(relou):
  espace()   
  if relou == "relouBus":
    #Action flop
    print("Le fait de fouiller dans ton sac, pour faire semblant d'être occupée, ne semble pas le décourager...")
    print("Il se rapproche et devient plus agressif. ")
    print("Heureusement tu vois le bus arriver. Il était temps! Tu commençais à avoir vraiment peur...")
  elif relou == "boss2" : 
    print("Tu as vraiment très peur...")
    print("Tu vois un autre magasin, et cette fois-ci, tu décides d'y aller chercher secours...")
    magasin()
  #Action top
  if relou == "relouMetro" or relou == "boss1" : 
    print("Tu donnes un coup de sac à ton agresseur.")
    print("Tu lui demandes s'il a besoin d'autres coups pour l'aider à ranger ses mains ou s'il va le faire tout seul.")
  else : 
    print("Tu fais semblant de ne pas entendre car tu es occupée à chercher quelque chose dans ton sac.")
    print("L'ignorance, une technique qui a fait ses preuves.")
    print("Heureusement, elle a suffit aujourd'hui. Ce n'est pas toujours le cas !")
  print("Tu as gagné 10 points confiance.")
  POINTS["confiance"] = POINTS["confiance"] + 10


#_______________________________________________________________________________TELEPHONE____________________________________________________________________________________________



def telephone(relou):
  espace()   
  if relou == "boss1":
    #Action flop
    print("Tu prends discrètement une photo de ton agresseur.")
    print("Tu sais que ça ne servira pas à grand chose mais au cas où tu l'as...")
  else : 
    #Action top
    if relou == "relouBus":
      print("Tu envoies discrètement 'SOS' par message à ta soeur.")
      print("Elle t'appelles et tu décroches.")
      print("Ouf, le relou s'en va! Tu restes avec ta soeur au téléphone pour te remettre de tes émotions.")
    if relou == "relouMetro":
      print("Tu filmes le frotteur en l'interpellant.")
      print("Il nie mais tu as une preuve vidéo.")
      print("Il s'enfuit mais tu as sa tête en vidéo pour porter plainte.")
    else : 
      print("Tu fais semblant d'être au téléphone et de rejoindre quelqu'un.")
      print("Tu entends les commentaires qui continuent mais tu poursuis ta route.")
      print("La technique a marché, on t'a laissé tranquille sans te suivre.")
      if relou == "boss2" : 
        winner()
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10

#_______________________________________________________________________________SIFFLET SHOP____________________________________________________________________________________________



def sifflet(relou):
  espace()
  print("Tu utilises le sifflet dans ton sac.")    
  if relou == "relouMetro" :
    #Action top
    print("Au son du sifflet, les gens autour sortent de leur stupeur et interviennent enfin.") 
    print("La sécurité du métro est appelée pour venir prendre en charge le frotteur.")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
  elif relou == "boss1" :
    #Action moyenne
    print("Au son du sifflet, les gens viennent voir ce qu'il se passe.") 
    print("Ton agresseur s'est enfui en courant, mais tu es entourée de gens bienveillants.")
    print("C'est déjà ça...") 
    print("Tu as gagné 5 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 5
  else : 
    #"Action flop
    print("On te demande ce que tu comptes faire avec ce sifflet. Tu te prends pour une arbitre ?")
    if relou == "relouBus" : 
      print("Le relou se rapproche et devient encore plus agressif.")
      print("Heureusement tu vois le bus arriver. Il était temps! Tu commençais à avoir vraiment peur...")
    if relou == "boss2" : 
      print("L'homme qui te suit commence à accélerer le pas.")
      print("Tu te rappelles de la boutique devant laquelle tu es passée.")
      print("Tu décides d'entrer dans la prochaine.")
      magasin()

#_______________________________________________________________________________ALARME SHOP____________________________________________________________________________________________


def alarme(relou):
  espace()  
  print("Tu déclences l'alarme sur ton téléphone.") 
  if relou == "relou1" or relou == "relou2" or relou == "relou3" :
    #Action flop
    print("Des gens autour interviennent au son de l'alarme.")
    print("Le relou se justifie en disant qu'il n'a rien fait. C'est de la drague gentilette, ça va !")
    print("Il se met à disserter avec les gens autour sur le droit à la galanterie.")
    print("Tu t'éclipses fatiguée par la bêtise humaine.")
  else : 
    #Action top
    print("L'alarme fait son effet. On te laisse tranquille !")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
#_______________________________________________________________________________SPRAY_ SHOP___________________________________________________________________________________________


def spray(relou):
  espace()  
  if relou == "relouMetro" or relou == "boss1" or relou == "boss2" :
    #Action top
    print("Hop, un petit coup de spray au poivre.")
    if relou == "relouMetro":
      print("En s'essuyant les yeux, au moins il enlève ses mains de toi et de son pantalon.")
      print(" ")
      print("Tu as gagné 10 points confiance.")
      POINTS["confiance"] = POINTS["confiance"] + 10     
    elif relou == "boss1": 
      print("En s'essuyant les yeux, au moins ses mains ne sont pas sur tes fesses.")
      print(" ")
      print("Tu as gagné 10 points confiance.")
      POINTS["confiance"] = POINTS["confiance"] + 10
    else : 
      print("Le temps qu'il s'essuie les yeux, tu pars en courant.")
      print("Tu rejoins une rue animée et te fonds au milieu des passants.")
      print("Tu as gagné 10 points confiance.")
      POINTS["confiance"] = POINTS["confiance"] + 10
      winner()
  else : 
    #Action flop
    print("Tu y es allée un peu fort... Il en a pris pour son grade.")
    print("Tu es sur les nerfs. Tant pis pour lui. Pas d'harcèlement de rue, pas de spray au poivre dans les yeux.")


#_______________________________________________________________________________PHRASE__DOJO__________________________________________________________________________________________


def phrase(relou):
  espace()  
  print("Tu te lances et dit la phrase préparée : 'Les dinosaures sont arc-en-ciels'")
  if relou == "relouMetro" :
    #Action flop
    print("Le frotteur te regarde mais la phrase ne semble pas avoir eu l'effet escompté.")
    print("En même temps, il s'agit d'une personne dérangée mentalement. Le non-sens ne fonctionne pas.")
    print("En parlant tu as attiré l'attention des autres passagers.")
    print("Il descend de la rame et change de métro pour pouvoir recommencer sans attirer l'attention.")
  elif relou == "boss2" : 
    #Action flop 
    print("Le relou ne t'entends pas et continues de te suivre.")
    print("Tu regrettes de ne pas être entrée dans la boutique devant laquelle tu es passée toute à l'heure.")
    print("Tu décides d'entrer dans la prochaine.")
    magasin()
  elif relou == "relou2": 
    #Action moyenne
    print("Les relous se regardent et explosent de rire.") 
    print("Ils te demandent de répéter. Voyant que tu ne réponds pas, ils abandonnent.")
    print("Tu continues ton chemin et tu les entends rigoler et disserter sur la folie féminine.")
    print("Tu as gagné 5 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 5
  else : 
    #Action top
    print("Le relou te regarde étonné. Il ne s'attendait pas cette réponse de ta part.")
    print("Il murmure 'Completement folle celle là' et continue son chemin.")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10

#_______________________________________________________________________________SELF DEFENSE_DOJO___________________________________________________________________________________________



def selfdefense(relou):
  espace()   
  if relou == "relouMetro" or relou == "boss1":
    #Action top
    if relou == "relouMetro" :
      print("Et hop, voilà qui devrait lui passer l'envie.")
    if relou == "boss1" :
      print("Et hop, voilà ce qui se passe quand on a les mains qui trainent.")
    print("Tout le monde te regarde étonné, mais tu te félicites d'avoir pris ces cours de self-defense!")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
  elif relou == "boss2": 
    #Action top 
    print("Quand il s'approche de toi tu appliques les techniques apprises en cour de self-defense.")
    print("Puis tu t'enfuies en courant.")
    print("Tu rejoins une rue animée et te fonds au milieu des passants.")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
    winner()
  else : 
    #Action flop
    print("Tu y es allée un peu fort... Il en a pris pour son grade.")
    print("Tu es sur les nerfs. Tant pis pour lui. Pas d'harcèlement de rue, pas de prises de self-defense ! ")

#_______________________________________________________________________________AIDE____________________________________________________________________________________________


def aide(relou):
  espace()   
  if relou == "relou1" or relou == "relou3":
    #Action moyenne
    print("Tu vas vers une personne à côté de toi et fait semblant de la connaître.")
    print("Le relou n'avait pas l'air agressif mais au moins tu te sens en sécurité.")
    print("Tu as gagné 5 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 5   
  else : 
    #Action top
    if relou == "relouMetro" or relou == "boss1":
      print("Tu interpelles les gens autour de toi. 'Personne ne compte réagir ?'")
      print("En comprenant ce qu'il vient de se passer, une personne intervient.")
      print("Effet de groupe oblige, les gens qui avaient fait semblant de ne rien voir réagissent aussi.")
      if relou == "relouMetro" : 
        print("La sécurité du métro est appelée pour venir prendre en charge le frotteur.")
    elif relou == "boss2" : 
      print("Il n'y a personne dans la rue.")
      print("Tu décides donc d'aller dans le magasin que tu as vu.")
      magasin()
    else :
      print("Tu vas vers une personne à côté de toi et fait semblant de la connaître.") 
      print("La personne comprend la situation et décides de faire un bout de chemin avec toi.")
      print("C'est bon, plus de relou à l'horizon ! Tu remercies vivement ton sauveur.")
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10

#_______________________________________________________________________________REPONSE____________________________________________________________________________________________


def reponse(relou):
  espace()   
  if relou == "relou1" or relou == "relou3" :
    #Action top
    if relou == "relou1" : 
      print("Tu réponds : 'Quoi ?'")
      print("Il répète 'Ton jean il te va trop bien franchement, ça te fait un de ces culs!'")
      print("Tu répètes : 'Quoi ?'")
      print("Cette fois le poète varie sa prose : 'Je te mangerai bien pour mon 4h'.") 
      print("Tu répètes : 'Quoi ?'")
      print("T'es sourde ou quoi ?") 
      print(" ")
      print("Tu réponds :") 
      print("1 : 'Quoi ?'") 
      print("2 : Je voulais être sûre que toi tu entendais bien les bêtises qui sortaient de ta bouche.")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("'Quoi ?'")
        print("Le relou s'énerve : 'Non mais laisse tomber, sale folle!'") 
        print("Il s'en va.")   
      elif dire == 2: 
        print("'Je voulais être sûre que toi tu entendais bien les bêtises qui sortaient de ta bouche.'")
        print("Le relou ne sait pas quoi répondre.")
        print("Il s'en va.")    
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou)  
    if relou == "relou3" : 
      print("Tu réponds : 'Tu sais que siffler quelqu'un ce n'est pas un compliment ce n'est pas un compliment.'")
      print("Le relou te rétorque qu'il fait ce qu'il veut.") 
      print(" ")
      print("Tu réponds :") 
      print("1 : Vas-y donne moi ton numéro") 
      print("2 : Ce que tu veux dans le respect en fait.")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("'Vas-y donne moi ton numéro'")
        print("Le relou te regarde surpris.") 
        print("Il ne répond rien et tu continues ton chemin.")   
      elif dire == 2: 
        print("'Ce que tu veux dans le respect en fait.'")
        print("Il s'énerve : 'De toute façon t'es dégueulasse, bouge.'")
        print("Tu continues ta balade.")    
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou)  
    print("Tu as gagné 10 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 10
  elif relou == "boss2" : 
    #Action flop
    print("Tu te retournes et tu t'adresses à l'homme qui te suit.")
    print("'Monsieur je vous demande d'arrêter de me suivre.'") 
    print("Il te fait part d'à quel point il te trouve charmante.") 
    print("Et rajoute : 'Si je te veux je t'aurais.'")
    print("Tu as encore plus peur...")
    print("Tu commences vraiment à te demander comment tu vas réussir à te débarasser de lui.")  
    print("Tu apperçois un magasin sur ta gauche. Voilà ta porte de sortie !")
    magasin()
  else : 
    #Action moyenne
    if relou == "relou2" :
      print("Un des relous ajoute : 'Tu pourrais sourire un peu'.")
      print(" ")
      print("Tu réponds :") 
      print("1 : par un sourire forcé exagéré") 
      print("2 : Tu pourrais me laisser tranquille un peu.")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("Tu souris du sourire le moins sincère possible.")
        print("Tu demandes : 'Content ?") 
        print("Ils explosent tous de rire, fiers d'eux.")
        print("Tu préfères ne pas les énerver, vu qu'ils sont nombreux.")      
      elif dire == 2: 
        print("'Tu pourrais me laisser tranquille un peu.'")
        print("Un des relous lance à ses potes : 'Elle est moche et elle fait trop la star.'")
        print("Mais tu es déjà loin, et les rageux ne t'atteignent pas.")    
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou) 
    elif relou == "relouMetro" :
      print("Tu réponds à cette agression :") 
      print("1 : en demandant haut et fort à qui est cette main baladeuse ?") 
      print("2 : en t'énervant")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("'A qui est cette main baladeuse ?'")
        print("Les autres passagers réagissent et viennent te défendre.")  
        print("Vous attendez ensemble la sécurité du métro.")    
      elif dire == 2: 
        print("Tu hurles sur le frotteur en lui demandant quel est son problème.")
        print("Tu ajoutes qu'il est dérangé mentalement et qu'il doit se faire soigner.")
        print("Les autres passagers ne réagissent pas mais il descend tout de même à la prochaine station.")     
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou) 
    elif relou == "relouBus" :
      print("Il renchérit : 'J'ai droit de te parler non ?'")
      print("Tu veux pas me donner ton 06 ?'")
      print(" ")
      print("Tu réponds :") 
      print("1 : 06 44 64 90 20. Il s'agit d'un numéro spécial.")
      print("S'il envoie un message à ce numéro, il recevra une mise au point sur le consentement.") 
      print("2 : Est-ce que ça marche vraiment cette technique ?")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("'06 44 64 90 20'")
        print("Le relou s'en va fier de lui.")
        print("Vivement qu'il reçoive le sms pour apprendre la notion de consentement.")     
      elif dire == 2: 
        print("'Est-ce que ça marche vraiment cette technique ?'")
        print("Il t'insulte en te disant que tu ferais mieux de moins faire la maligne.")
        print("Ouf, le bus arrive.")    
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou) 
    else :
      print("Tu affrontes le relou en lui demandant d'enlever sa main.")
      print("Tu lui expliques qu'il s'agit d'une agression.")
      print("Le relou te dit : 'T'es sûre que tu vas boire un verre au lieu de faire l'hystérique?'") 
      print(" ")
      print("Tu réponds :") 
      print("1 : Tu n'as qu'à offrir un verre à la voiture de police qui passe.")
      print("2 : Non. Au revoir, monsieur.")
      print(" ")
      dire=int(input())
      espace()
      if dire == 1 :
        print("'Tu n'as qu'à offrir un verre à la voiture de police qui passe.'")
        print("Le relou s'en va en marmonnant des insultes dans sa barbe.")  
      elif dire == 2: 
        print("'Non. Au revoir, monsieur.'")
        print("Tu continues d'avancer pendant que le relou; lui, continue de t'insulter.")  
      else : 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                    !! !! ERREUR, je n'ai pas compris ta commande. Merci de recommencer!! ¯\_(⊙︿⊙)_/¯")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        reponse(relou)  
    print("Tu as gagné 5 points confiance.")
    POINTS["confiance"] = POINTS["confiance"] + 5
   
  
#_______________________________________________________________________________MAGASIN____________________________________________________________________________________________


def magasin():
  espace()
  #Action top  
  print("Tu rentres dans le magasin pour demander de l'aide.")
  print("La gérante te prend en charge.")
  print("Elle t'offre un thé et demande à l'un de ses employés de te raccompagner.")
  winner()

#decompteRelous = [3,5,6,8]


ZeroSix()
