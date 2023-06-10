#Edward Grau
#gr.401

import arcade
from game_state import GameState
from attack_animation import AttackType
from attack_animation import AttackAnimation
import random


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rock, Paper,, Scissors"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
    #define the parameters before the game starts
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}

   def setup(self):
       #define the parameters before the first roud after the game starts
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

   def draw_possible_attack(self):
       #Draw the attacks that the player can chose from (Ui element)
       if self.game_state == GameState.ROUND_ACTIVE:
           self.type_choice.draw()
       elif self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER:
           if self.player_attack_type == AttackType.ROCK:
               self.rock_player.draw()
           elif self.player_attack_type == AttackType.PAPER:
               self.paper_player.draw()
           elif self.player_attack_type == AttackType.SCISSORS:
               self.scissors_player.draw()

   def draw_computer_attack(self):
       #Draw the attacks that the computer can chose (Ui element)
       if self.computer_attack_type == AttackType.ROCK:
           self.rock_computer.draw()
       elif self.computer_attack_type == AttackType.PAPER:
           self.paper_computer.draw()
       elif self.computer_attack_type == AttackType.SCISSORS:
           self.scissors_computer.draw()


   def draw_scores(self):
       #Draw the score of the computer so the player can see it
       arcade.draw_text("Computer score: {self.computer_score}", SCREEN_WIDTH / 4.1, SCREEN_HEIGHT / 12,
       arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
       arcade.draw_text("Your score: {self.player_score}", SCREEN_WIDTH / -4, SCREEN_HEIGHT / 12,
       arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")


   def draw_instructions(self):
       #Draw the instructions for the player and if they won or lost the current round
       if self.game_state == GameState.NOT_STARTED:
           arcade.draw_text("Press space bar to reset", 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                            arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")

       elif self.game_state == GameState.ROUND_ACTIVE:
           arcade.draw_text("Click to attack", 0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                            arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
       elif self.game_state == GameState.ROUND_DONE and self.player_won_round == True:
           arcade.draw_text("You won. Congratulations. Press space bar to reset.", 0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                            arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
       elif self.game_state == GameState.ROUND_DONE and self.player_won_round == False:
           arcade.draw_text("You lost. Better luck next time. Press space bar to reset.", 0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                            arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
       elif self.game_state == GameState.ROUND_DONE and self.player_won_round == None:
           arcade.draw_text("You tied. So close! Press space bar to reset.", 0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                            arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
       elif self.game_state == GameState.GAME_OVER:
           if self.player_score > self.computer_score:
               arcade.draw_text("You won the game. Congratulations. Press space bar to reset.", 0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                                arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")
           elif self.player_score < self.computer_score:
               arcade.draw_text("You lost the game. Better luck next time. Press space bar to reset.", 0,
                                SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                                arcade.color.ALMOND, 20, width=SCREEN_WIDTH, align="center")


   def on_draw(self):
       #Draw all the ui elements so the end user can see them
       arcade.start_render()
       arcade.draw_text(SCREEN_TITLE, 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2, arcade.color.ALMOND, 50,
                        width=SCREEN_WIDTH, align="center")

       arcade.draw_rectangle_outline(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.AERO_BLUE, 5)
       arcade.draw_rectangle_outline(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.AERO_BLUE, 5)
       arcade.draw_rectangle_outline(SCREEN_WIDTH / 6, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.AERO_BLUE, 5)
       arcade.draw_rectangle_outline(SCREEN_WIDTH / 1.35, SCREEN_HEIGHT / 5, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.AERO_BLUE, 5)

       self.draw_scores()
       self.draw_computer_attack()
       self.draw_instructions()
       self.player.draw()
       self.computer.draw()
       self.draw_possible_attack()


   def on_update(self, delta_time):
       self.rock.on_update()
       self.scissors.on_update()
       self.paper.on_update()

       if self.game_state == GameState.ROUND_ACTIVE:
           if self.game_state == GameState.ROUND_ACTIVE:
               if self.player_attack_chosen:
                   npc_attack = random.randint(0, 2)
                   if npc_attack == 0:
                       self.computer_attack_type = AttaqueType.ROCK
                   elif npc_attack == 1:
                       self.computer_attack_type = AttaqueType.PAPER
                   else:
                       self.computer_attack_type = AttaqueType.SCISSOR

           if self.robot_attack == AttackType.ROCK:
                   if self.player_attack_type == AttackType.ROCK:
                       self.nul_game = True
                   elif self.player_attack_type == AttackType.PAPER:
                       self.player_win = True
                   else:
                       self.player_lose = True
               elif self.player_attack_type == AttackType.PAPER:
                   if self.player_attack_type == AttackType.ROCK:
                       self.player_lose = True
                   elif self.player_attack_type == AttackType.PAPER:
                       self.nul_game = True
                   else:
                       self.player_win = True
               elif self.computer_attack_type == AttackType.SCISSOR:
                   if self.player_attack_type == AttackType.ROCK:
                       self.player_win = True
                   elif self.player_attack_type == AttackType.PAPER:
                       self.player_lose = True
                   else:
                       self.nul_game = True

               if self.player_win:
                   self.player_score += 1
                   self.game_state = GameState.ROUND_DONE
               elif self.player_lose:
                   self.computer_score += 1
                   self.game_state = GameState.ROUND_DONE
               elif self.nul_game:
                   self.computer_score += 0
                   self.player_score += 0
                   self.game_state = GameState.ROUND_DONE

       elif self.game_state == GameState.ROUND_DONE:
           if self.player_score == 3:
               self.round_won = True
               self.game_state = GameState.ROUND_OVER
           elif self.computer_score == 3:
               self.round_won = False
               self.game_state = GameState.ROUND_OVER

   def on_key_press(self, key, key_modifiers):

       if key == arcade.key.SPACE:

           if self.game_state == GameState.NOT_STARTED:
               self.game_state = GameState.ROUND_ACTIVE
           elif self.game_state == GameState.ROUND_DONE:
               self.game_state = GameState.ROUND_ACTIVE
               self.player_win = self.player_lose = self.nul_game = False
               self.player_attack_chosen = False
               self.player_attack_type = AttackType.NOT_STARTED
       elif key == arcade.key.R:
           if self.game_state == GameState.ROUND_OVER:
               self.game_state = GameState.NOT_STARTED
               self.player_win = self.player_lose = self.nul_game = False
               self.player_score = self.computer_score = 0
               self.player_attack_chosen = False
               self.player_attack_type = AttaqueType.NOT_STARTED



   def reset_round(self):
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_win = False
       self.draw_round = False

   def on_mouse_press(self, x, y, button, key_modifiers):

       if self.game_state == GameState.ROUND_ACTIVE:
           if self.scissors.collides_with_point((x, y)):
               self.player_attack_type = AttackType.SCISSOR
               self.player_attack_chosen = True

           if self.rock.collides_with_point((x, y)):
               self.player_attack_type = AttackType.ROCK
               self.player_attack_chosen = True

           if self.paper.collides_with_point((x, y)):
               self.player_attack_type = AttackType.PAPER
               self.player_attack_chosen = True

       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True


def main():
   """ Main method """
   game = My
   Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()
