import pygame, sys, random

class display:
    # Function to draw the floor
    def draw_floor(self):
        self.screen.blit(self.floor_surface, (self.floor_x_pos, 676))
        self.screen.blit(self.floor_surface, (self.floor_x_pos + 576, 676))

    # Function to display the score
    def score_display(self, game_state,score_height,highscore_height):
        if game_state == 'main_game':
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, score_height))
            self.screen.blit(score_surface, score_rect)

        if game_state == 'game_over':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, score_height))
            self.screen.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(f'High score: {int(self.high_score)}', True, (255, 195, 0))
            high_score_rect = high_score_surface.get_rect(center=(288, highscore_height))
            self.screen.blit(high_score_surface, high_score_rect)
            if self.restart == False:
                self.game_font_1 = pygame.font.Font('SuperPixel.ttf', 18)  # Font
                restart_menu_surface = self.game_font_1.render('Press "Enter" for restart menu', True, (200, 255, 200))
                restart_menu_rect = restart_menu_surface.get_rect(center=(288, 555))
                self.screen.blit(restart_menu_surface, restart_menu_rect)


    # Function to check the score
    def pipe_score_check(self):
        global score, can_score
        if self.pipe_list:
            for pipe in self.pipe_list:
                if 95 < pipe.centerx < 105 and self.can_score:
                    self.score += 1
                    self.score_sound.play()
                    self.can_score = False

                if pipe.centerx < 0:
                    self.can_score = True





    # Function to update the high score
    def update_high_score(self,score,high_score):
        if score > high_score:
            high_score = score
        return high_score



    screen = pygame.display.set_mode((576, 800))  # Display
    clock = pygame.time.Clock()  # Clock


    bg_surface = pygame.image.load('assets/background-day.png').convert()  # Load the background image
    bg_surface = pygame.transform.scale2x(bg_surface)  # Double the size of the image

    floor_surface = pygame.image.load('assets/base.png').convert()  # Load the floor image
    floor_surface = pygame.transform.scale2x(floor_surface)  # Double the size of the image
    floor_x_pos = 0  # Position of the floor



