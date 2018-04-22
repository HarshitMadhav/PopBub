import pygame
import sys

from Balloon import Balloon
from Settings import Settings
from Sword import Sword
from Scoreboard import Scoreboard
from Button import Button
from Engine import Engine
from Instructions import Instructions

def run_game():
    # access to settings
    #width,height=800,600
    settings =Settings()
    #initialize game
    pygame.init()
    sound= 'resources/back_sound.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)
    pygame.event.wait()
    screen=pygame.display.set_mode((settings.width,settings.height),0,32)

    pygame.display.set_caption("PopBob")
    clock =pygame.time.Clock()
    scoreboard = Scoreboard(screen, settings)
    play_button = Button(screen, settings.width/2-settings.button_width/2,
                            settings.height/2-settings.button_height/2, settings, "Play")
    game_over_button = Button(screen,play_button.x_position, play_button.y_position-2*settings.button_height,
                            settings, "Game Over")
    #balloons=[Balloon(screen, settings.balloon_speed)]
    # scoreboard_height=50
    # game play params
    #balloon_speed= 0.1
    #points_per_hit=10
    instructions = Instructions(screen, settings)
    #scoreboard=Scoreboard(screen, settings.scoreboard_height)
    balloons =  []
    fish = []
    #spawn_balloon(screen, settings, balloons)
    # balloons=[Balloon(screen, settings.balloon_speed)]

    sword=Sword(screen, settings.scoreboard_height)
    #new_balloon=Balloon(screen)
    #bg_image=pygame.image.load('resources/back_pop_ga.jpg')

    engine = Engine(screen, settings, scoreboard, balloons, fish, sword)

    while 1:
        time_passed =  clock.tick(50)
        mouse_x,mouse_y  = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
        engine.check_events(play_button,  mouse_x,  mouse_y)
        print (pygame.mouse.get_pos())

        screen.blit(settings.bg_image,(0,0))

        if settings.game_active:
            engine.update_sword(mouse_x, mouse_y)
            engine.check_balloons(time_passed)
            engine.check_fishes(time_passed)

            if len(balloons)==0:
                if scoreboard.balloons_popped >0:
                    settings.balloon_speed *= settings.speed_increase_factor
                    settings.fish_ratio *= settings.speed_increase_factor
                    settings.points_per_hit = int(round(settings.points_per_hit * settings.speed_increase_factor))
                    scoreboard.batches_finished +=1

                if scoreboard.batches_finished % settings.batches_needed == 0 and scoreboard.batches_finished>0:
                    settings.batch_size+=1
                engine.release_batch()
        else :
            play_button.blitme()
            if settings.games_played < 3 :
                instructions.blitme()
            if settings.games_played >0:
                game_over_button.blitme()
        #displaying the scoreboard
        scoreboard.blitme()

        pygame.display.flip()


run_game()

