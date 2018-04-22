import pygame.ftfont
from pygame.sprite import  Sprite

class Button(Sprite):

    def __init__(self, screen, x_pos, y_pos, settings, msg):

        Sprite.__init__(self)
        self.screen =screen
        self.settings =settings

        # set dimensions and properties of the button to be used
        self.width, self.height= settings.button_width, settings.button_height
        self.x_position, self.y_position= x_pos, y_pos
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(settings.button_font, settings.button_font_size)
        self.msg =msg

        #Button message
        self.prep_msg()

    def prep_msg(self):
        self.msg_image =self.font.render(self.msg, True, self.settings.button_text_color)
        self.msg_x = self.x_position+ (self.width - self.msg_image.get_width()) /2
        self.msg_y = self.y_position + (self.height - self.msg_image.get_height()) / 2

    def blitme(self):
        # Draw blank button, and draw message
        self.screen.fill(self.settings.button_bg, self.rect)
        self.screen.blit(self.msg_image, (self.msg_x, self.msg_y))
