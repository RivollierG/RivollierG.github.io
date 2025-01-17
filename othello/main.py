from utils.board import Board
from utils.player import Player
from utils.ia import Ia


def othello(j1="Player", j2="IA", lv=4):
    #joueur1 = Player("noir")
    if j1 == "Player":

        joueur1 = Player("noir")

    elif j1 == "IA":
        joueur1 = Ia("noir", lv)

    else:
        return("unrecognize player1")

    if j2 == "Player":

        joueur2 = Player("blanc")

    elif j2 == "IA":
        joueur2 = Ia("blanc", lv)

    else:
        return("unrecognize player2")

    plateau = Board()

    # Joueur 1 sera le 1er joueur (le script commence par "next_joueur")
    joueur2.is_actif = True
    print("")
    print("\nBienvenue dans Othello, le jeu qui vous retourne le cervO !")
    print("Les pions du joueur Noir sont des X.\n")
    print("Les pions du joueur Blanc sont des O.\n")

    plateau.afficher_board()

    # Debut du jeu
    # Le jeu se continue tant qu'un des deux joueurs peut jouer

    while plateau.trigger < 2:
        joueur_actif, joueur_inactif = plateau.next_joueur(joueur1, joueur2)
        print("C'est au joueur", joueur_actif.couleur, "de jouer.")
        # calcul le poids de chaque cells
        plateau.calcul_poids(joueur_actif)
        # si pas de coup possible, si trig = Warning => Fin else trig= "Warning"
        # soit le joueur effectue ses actions, soit nouveau tour
        # plateau.afficher_board_debug()
        if not plateau.joueur_actif_peut_jouer(joueur_actif):
            continue
        coup = plateau.choix_joueur(joueur_actif)
        plateau.maj_board(coup, joueur_actif, joueur_inactif)
        plateau.afficher_board()
    plateau.fin_du_jeu(joueur1, joueur2)


othello()
