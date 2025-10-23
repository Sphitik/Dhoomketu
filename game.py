import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.game_state = "start_menu"

        self.start_menu = Menu(self.screen, "Dhoomketu", ["Start", "Quit"])
        self.pause_menu = Menu(self.screen, "Paused", ["Resume", "New Game", "Quit"])
        self.game_over_menu = Menu(self.screen, "Game Over", ["New Game", "Quit"])

        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        self.asteroid_field = AsteroidField()
        Shot.containers = (self.shots, self.updatable, self.drawable)

        Player.containers = (self.updatable, self.drawable)

        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def run(self):
        while True:
            if self.game_state == "start_menu":
                if not self.handle_start_menu():
                    return "Quit"
            elif self.game_state == "playing":
                self.handle_playing()
            elif self.game_state == "paused":
                selected_option = self.handle_paused()
                if selected_option in ["New Game", "Quit"]:
                    return selected_option
            elif self.game_state == "game_over":
                selected_option = self.handle_game_over()
                if selected_option in ["New Game", "Quit"]:
                    return selected_option

    def handle_start_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            selected_option = self.start_menu.handle_input(event)
            if selected_option == "Start":
                self.game_state = "playing"
            elif selected_option == "Quit":
                return False

        self.start_menu.draw()
        return True

    def handle_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_state = "paused"

        self.updatable.update(self.dt)

        for asteroid in self.asteroids:
            for bullet in self.shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()

            if self.player.collision(asteroid):
                self.game_state = "game_over"

        self.screen.fill("black")

        for obj in self.drawable:
            obj.draw(self.screen)

        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000

    def handle_paused(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Quit"
                selected_option = self.pause_menu.handle_input(event)
                if selected_option == "Resume":
                    self.game_state = "playing"
                    return None
                elif selected_option in ["New Game", "Quit"]:
                    return selected_option

            self.pause_menu.draw()

    def handle_game_over(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Quit"
                selected_option = self.game_over_menu.handle_input(event)
                if selected_option in ["New Game", "Quit"]:
                    return selected_option

            self.game_over_menu.draw()
