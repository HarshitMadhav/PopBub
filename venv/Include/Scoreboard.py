import pygame,pygame.ftfont
from pygame.sprite import Sprite

class Scoreboard(Sprite):

    def __init__(self,screen, settings):

        Sprite.__init__(self)
        self.screen = screen

        self.settings = settings
        self.initialize_stats()

        #attribute to track scoring

        self.sb_height = settings.scoreboard_height
        self.sb_width = self.screen.get_width()
        self.rect = pygame.Rect(0,0,self.sb_width, self.sb_height)
        self.bg_color=(51,153,255)
        self.text_color=(225,225,225)
        self.font = pygame.font.SysFont('Serif',20)


        self.x_popped_pos, self.y_popped_pos=20.0, 10.0
        #self.x_missed_pos, self.y_missed_pos=150.0, 10.0
        self.x_points_pos, self.y_points_pos = 350, 10.0
        self.x_score_pos, self.y_score_pos = self.screen.get_width() - 200, 10.0
        self.x_ratio_pos, self.y_ratio_pos = 150, 10.0

    def initialize_stats(self):
        self.balloons_popped = 0
        self.balloons_missed = 0
        self.score = 0
        self.popped_ratio =1.0
        self.batches_finished= 0
        self.fish_spared = 0
        self.fish_killed =  0

    def prep_scores(self):
        self.popped_string="Popped: "+str (self.balloons_popped)
        self.popped_image = self.font.render(self.popped_string, True, self.text_color)

        #self.missed_string="Missed: "+str(self.balloons_missed)
        #self.missed_image = self.font. render (self.missed_string, True, self.text_color)

        self.score_string ="Score: " +str(self.score)
        self.score_image = self.font.render(self.score_string, True, self.text_color)
        self.score_image = self.font.render(self.score_string, True, self.text_color)

        self.set_ratio_string()
        self.popped_ratio_image = self.font.render(self.popped_ratio_string, True, self.ratio_text_color)

        self.points_string = "Points per Bubble: " +str (self.settings.points_per_hit)
        self.points_image = self.font.render(self.points_string, True, self.text_color)

    def set_ratio_string(self):
        if self.popped_ratio == 1.0:
            self.popped_ratio_string = "Pop Rate: 100%"
        else:
            self.popped_ratio_string = "Pop Rate : "+ "{0:.3}%".format(self.popped_ratio*100.0)
        if self.popped_ratio<0.95:
            self.ratio_text_color =(255,51,51)
        else:
            self.ratio_text_color =self.text_color

    def blitme(self):
        # change the score into images related to the digits
        self.prep_scores()
        #draw a blank scoreboard
        self.screen.fill(self.bg_color,self.rect)
        #draw individual scoring elements
        self.screen.blit(self.popped_image,(self.x_popped_pos, self.y_popped_pos))
        self.screen.blit(self.points_image,(self.x_points_pos, self.y_points_pos))
        #self.screen.blit(self.missed_image, (self.x_missed_pos, self.y_missed_pos))
        self.screen.blit(self.score_image,(self.x_score_pos, self.y_score_pos))
        self.screen.blit(self.popped_ratio_image, (self.x_ratio_pos, self.y_ratio_pos))
        #eof
