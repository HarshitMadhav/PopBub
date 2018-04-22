import pygame , sys
from Balloon import Balloon
from Button import Button
from Fish import Fish
from random import random

class Engine():
    def __init__(self, screen, settings, scoreboard, balloons, fish, sword):
        self.screen = screen
        self.settings = settings
        self.scoreboard = scoreboard
        self.balloons = balloons
        self.fish = fish
        self.sword =sword

    def release_batch(self):
        for x in range (0, self.settings.batch_size):
            self.spawn_balloon()

    def check_balloons(self, time_passed):
        for balloon in self.balloons:
            balloon.update(time_passed)

            if balloon.rect.colliderect(self.sword.rect):
                self.pop_balloon(balloon)
                continue

                # settings.balloon_speed *= 1.05
                #spawn_balloon(screen, settings, balloons)
                # balloons.append(Balloon(screen, settings.balloon_speed))
                #continue

            print("y_position: ", balloon.y_position)

            if balloon.y_position < -balloon.image_h / 2 + self.settings.scoreboard_height:
                self.miss_balloon(balloon)
                # for x in range(0,2):
                # balloons.append(Balloon(screen, settings.balloon_speed))
                self.spawn_balloon()
                continue
            balloon.blitme()

        if self.scoreboard.balloons_popped > 0 or self.scoreboard.balloons_missed >0:
            self.scoreboard.popped_ratio = float(self.scoreboard.balloons_popped) / (self.scoreboard.balloons_popped + self.scoreboard.balloons_missed)
            if self.scoreboard.popped_ratio < self.settings.min_popped_ratio:

                self.settings.game_active = False
                self.settings.games_played +=1

    def check_fishes(self, time_passed):
        for fishes in self.fish:
            fishes.update(time_passed)

            if fishes.rect.colliderect(self.sword.rect):
                self.kill_fish(fishes)
                continue

            if fishes.y_position < -fishes.image_h / 2 + self.settings.scoreboard_height:
                self.spare_fish(fishes)
                continue

            fishes.blitme()

    def update_sword(self,mouse_x, mouse_y):
        self.sword.x_position = mouse_x
        if self.sword.grabbed:
            self.sword.y_position = mouse_y
        else:
            self.sword.y_position = self.sword.image_h / 2 + self.settings.scoreboard_height

        self.sword.update_rect()
        self.sword.blitme()


    def check_events(self,play_button, mouse_x,mouse_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.sword.rect.collidepoint(mouse_x, mouse_y):
                    self.sword.grabbed = True
                if play_button.rect.collidepoint(mouse_x,mouse_y):
                    del self.balloons[:]
                    self.scoreboard.initialize_stats()
                    self.settings.initialize_game_parameters()

                    self.settings.game_active =True
            if event.type == pygame.MOUSEBUTTONUP:
                self.sword.grabbed = False

    def spawn_balloon(self):
        self.balloons.append(Balloon(self.screen, self.settings))
        if random() < self.settings.fish_ratio:
            self.spawn_fishes()

    def spawn_fishes(self):
        self.fish.append(Fish(self.screen, self.settings))


    def miss_balloon(self, balloon):
        self.scoreboard.balloons_missed +=1
        self.balloons.remove(balloon)

    def spare_fish(self, fishes):
        self.scoreboard.fish_spared+=1
        self.scoreboard.score += self.settings.fish_score_factor * self.settings.points_per_hit
        self.fish.remove(fishes)

    def kill_fish(self, fishes):
        self.scoreboard.fish_killed +=1
        self.scoreboard.score -= self.settings.fish_score_factor * self.settings.points_per_hit
        self.fish.remove(fishes)

    def pop_balloon(self, balloon):
        self.scoreboard.balloons_popped += 1
        self.scoreboard.score += self.settings.points_per_hit
        self.balloons.remove(balloon)
        # speedd up the game everytime a hit is made
        # use 1.05 while testing and 1.01 for play
        #settings.balloon_speed *= settings.speed_increase_factor

        #if scoreboard.balloons_popped % settings.hits_needed ==0:
            #settings.batch_size +=1
