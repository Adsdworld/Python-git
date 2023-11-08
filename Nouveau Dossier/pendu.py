import os

# clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# A faire : import nécessaire pour le bonus choix aléatoire


# A faire - Bonus : Création d'une liste qui contient (au moins) 10 mots
import randommodule as rdm
ListeDe10Mots=["chaussettes", "bois", "feuille", "eseo", "code", "popcorn", "ds", "ange", "aigle", "oeil"]

def afficherPendu() :
      liste=["============ "," ||/   |  "," ||    0  "," ||   /|\ "," ||   / \  ","/||       ","============\n"]
      """
      # A faire : gérer l'affichage du pendu en fonction du nombre d'erreurs
      print("============ ")
      print(" ||/   |  ")
      print(" ||    0  ")
      print(" ||   /|\ ")
      print(" ||   / \  ")
      print("/||       ")             
      print("============\n")  # ligne à afficher en premier : première erreur
      """
      for i in range(nb_tentative):#la ligne du bas en premier n'est pas respecté :/
        print(liste[i])

def affichage_joueur(): #foncionnel
  affichage=[]
  for i in solution.lower():
    affichage.append(" _ ")
  for j in LettreListe:
    if j in solution.lower():
      for i in range(len(solution)):
        if solution[i].lower()==j:
          del affichage[i]
          affichage.insert(i,j)
  String=""
  for i in affichage:
    String+=" "+i
  return String.upper()


def vérifier_lettre(lettre, affichage):#Inutilisé ici, remplace par affichagejoueur()
  compteur = 0
  new_affichage = ""
  if lettre in solution:
    for lettre_affichage in affichage:
      print(solution[compteur], compteur)
      if lettre_affichage == solution[compteur]:
        new_affichage += solution[compteur]
      else:
        if lettre == solution[compteur]:
          new_affichage += lettre
        else:
          new_affichage += "_"
      compteur += 1
    print(new_affichage)
    return new_affichage
  else:
    return affichage

while True:
  # A faire - Bonus : Choix aléatoire d'un mot de la liste
  #solution = "motTest" # mot "en dur" pour vos tests
  print(len(ListeDe10Mots))
  solution = rdm.random(ListeDe10Mots)
  LettreListe=[]

  # A faire : Déclarer les variables nécessaires au programme
  affichage = ""
  # A faire : variable contenant les 7 tentatives
  nb_tentative = 0

  # A faire : fonction à modifier pour afficher
  # au fur et à mesure le pendu

  # Solution pour afficher les "_" en fonction du nombre de lettres du mots
  for x in solution:
    affichage = affichage + "_ "


  print(">> Bienvenue dans le jeu du pendu <<")

  print("\nMot à deviner : ", affichage)


  # A faire : Mettre en place la boucle pour proposer des lettres
  # tant que le mot n'est pas trouvé ou que le joueur n'a pas perdu

  # A faire : Mettre en place les exceptions/erreurs nécessaires
  # il ne faut saisir qu'une lettre (pas plusieurs, et pas de chiffre)
  # permettre de saisir en minuscule OU majuscule
  win = False
  while not win and nb_tentative < 7:
    if not "_" in affichage_joueur().lower():
      win=True
      continue
    try:
      lettre = str(input("\nChoisissez une lettre : ")).lower()
      compteur_lettre = 0
      for letter in lettre:
        compteur_lettre += 1
        if lettre == "0" or lettre == "1" or lettre == "2" or lettre == "3" or lettre == "4" or lettre == "5" or lettre == "6" or lettre == "7" or lettre == "8" or lettre == "8" or lettre == "9":
          raise Exception("Veuillez entrer une lettre!")
      if compteur_lettre>1:
        raise Exception("Veuillez entrer une seule lettre!")
    except Exception as e:
      print(e)
    else:
      LettreListe.append(lettre)
      if lettre not in solution:
        nb_tentative += 1
      afficherPendu()
      print("Il vous reste {} tentatives".format(7-nb_tentative))
      #affichage = vérifier_lettre(lettre, affichage)
      print(affichage_joueur())

  # A faire : tester si la lettre est dans le mot ou non
  ListeSolution=[]


  # A faire : Afficher la nouvelle chaine "_" + lettres trouvées
  # A faire : Sinon, afficher le pendu (en fonction du nombre de tentatives restantes)


  # A faire : Tester s'il reste des "_". Si non, c'est que le joueur à gagné

  # A faire - Bonus : proposer de rejouer

      
  print("\n **** Fin de la partie ****  ")
  while True:
      try:
          choice=input("Souhaiter vous quitter le programme 'o' ou 'n': ")
          if choice=='o':
              print("Fermeture du programme")
              quit()
          elif(choice=='n'):
              break
          else:
              raise Exception("Vous devez choisir entre 'o' ou 'n'")
      except Exception as err:
          print(err)
