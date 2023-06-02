#Edward Grau
#gr.401

import arcade
from game_state import GameState
from attack_animation import AttackType
from attack_animation import AttackAnimation
import random
class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2

class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0



#from attack_animation import AttackType, AttackAnimation
#from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = None

   def setup(self):
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {1: AttackType.ROCK, 2: AttackType.PAPER, 3: AttackType.SCISSORS}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_win_round = 0
       self.draw_round = None
       self.game_state = GameState.ROUND_ACTIVE
       self.player = arcade.Sprite('asset/faceBeard.png', 0.5, center_x=self.PLAYER_IMAGE_X, center_y=self.PLAYER_IMAGE_Y)
       self.computer = arcade.Sprite('asset/compy.png', 2.5, center_x=self.COMPUTER_IMAGE_X, center_y=self.COMPUTER_IMAGE_Y)
       self.players = None
       self.rock = arcade.Sprite('asset/srock.png', 0.5, center_x=SCREEN_WIDTH / 4, center_y=SCREEN_HEIGHT / 5)
       self.paper = arcade.Sprite('asset/spaper.png', 0.5, center_x=SCREEN_WIDTH / 3, center_y=SCREEN_HEIGHT / 5)
       self.scissors = arcade.Sprite('asset/scissors.png', 0.5, center_x=SCREEN_WIDTH / 6, center_y=SCREEN_HEIGHT / 5)




   def validate_victory(self):
       if self.player_win:
           arcade.draw_text("Partie gagnée!", 280, 530, arcade.color.RED, 30)
       elif self.player_lose:
           arcade.draw_text("Partie perdue!", 280, 530, arcade.color.RED, 30)
       elif self.nul_game:
           arcade.draw_text("Partie nulle!", 300, 530, arcade.color.RED, 30)

   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.draw_instructions()
       self.players.draw()
       self.draw_possible_attack()
       self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)


   def on_update(self, delta_time):

        self.rock.on_update()
        self.scissors.on_update()
        self.paper.on_update()
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.atack_choix:
                bot_attaque = random.randint(0, 2)
                if bot_attaque == 0:
                    self.robot_attack = AttaqueType.ROCK
                elif bot_attaque == 1:
                    self.robot_attack = AttaqueType.PAPER
                else:
                    self.robot_attack = AttaqueType.SCISSOR

                if self.robot_attack == AttaqueType.ROCK:
                    if self.joueur_atack == AttaqueType.ROCK:
                        self.nul_game = True
                    elif self.joueur_atack == AttaqueType.PAPER:
                        self.player_win = True
                    else:
                        self.player_lose = True
                elif self.robot_attack == AttaqueType.PAPER:
                    if self.joueur_atack == AttaqueType.ROCK:
                        self.player_lose = True
                    elif self.joueur_atack == AttaqueType.PAPER:
                        self.nul_game = True
                    else:
                        self.player_win = True
                elif self.robot_attack == AttaqueType.SCISSOR:
                    if self.joueur_atack == AttaqueType.ROCK:
                        self.player_win = True
                    elif self.joueur_atack == AttaqueType.PAPER:
                        self.player_lose = True
                    else:
                        self.nul_game = True

                if self.player_win:
                    self.points_joueurs += 1
                    self.game_state = GameState.ROUND_DONE
                elif self.player_lose:
                    self.point_botssss += 1
                    self.game_state = GameState.ROUND_DONE
                elif self.nul_game:
                    self.point_botssss += 0
                    self.points_joueurs += 0
                    self.game_state = GameState.ROUND_DONE

        elif self.game_state == GameState.ROUND_DONE:
            if self.points_joueurs == 3:
                self.round_won = True
                self.game_state = GameState.ROUND_OVER
            elif self.point_botssss == 3:
                self.round_won = False
                self.game_state = GameState.ROUND_OVER

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.player_win = self.player_lose = self.nul_game = False
                self.atack_choix = False
                self.joueur_atack = AttaqueType.NOT_STARTED

        elif key == arcade.key.R:
            if self.game_state == GameState.ROUND_OVER:
                self.game_state = GameState.NOT_STARTED
                self.player_win = self.player_lose = self.nul_game = False
                self.points_joueurs = self.point_botssss = 0
                self.atack_choix = False
                self.joueur_atack = AttaqueType.NOT_STARTED



   def on_key_press(self, key, key_modifiers):

       if key == arcade.key.SPACE:
           if self.game_state == GameState.NOT_STARTED:
               self.game_state = GameState.ROUND_ACTIVE
           elif self.game_state == GameState.ROUND_DONE:
               self.game_state = GameState.ROUND_ACTIVE
               self.player_win = self.player_lose = self.nul_game = False
               self.atack_choix = False
               self.joueur_atack = AttackType.NOT_STARTED
       pass

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):

       if self.game_state == GameState.ROUND_ACTIVE:
           if self.scissors.collides_with_point((x, y)):
               self.joueur_atack = AttaqueType.SCISSOR
               self.atack_choix = True

           if self.rock.collides_with_point((x, y)):
               self.joueur_atack = AttaqueType.ROCK
               self.atack_choix = True

           if self.paper.collides_with_point((x, y)):
               self.joueur_atack = AttaqueType.PAPER
               self.atack_choix = True

       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
       pass


def main():
   """ Main method """
   game = My
   Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()
