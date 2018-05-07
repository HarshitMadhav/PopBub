import pygame

class Settings():
    def __init__(self):
        # screen parameters
        self.width=800
        self.height=600
        self.bg_image = pygame.image.load('resources/backk.jpg')
        self.scoreboard_height=50
        # game status
        self.game_active=False

        self.min_popped_ratio =0.9

        # some specific settings to the start button

        self.button_width,self.button_height = 250,50
        self.button_bg = (0,153,153)
        self.button_text_color = (235,235,235)
        self.button_font, self.button_font_size = 'Arial', 24

        #game over conditions
        self.misses_allowed =3
        self.games_played= 0
        self. initialize_game_parameters()

    def initialize_game_parameters(self):

        #game play parameeters

        self.balloon_speed =0.1
        # use 1.05 while testing and 1.01 for playing
        self.speed_increase_factor= 1.05
        self.points_per_hit =10
        self.batch_size= 1

        #  hit needed  to difficult the game at initial stage
        # play use 10 and while testing use 3
        #self.hits_needed=3
        self.batches_needed=3
        self.fish_ratio = 0.10
        self.fish_score_factor = 3