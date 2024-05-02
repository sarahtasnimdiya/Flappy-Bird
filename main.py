import pygame, sys, random,display

pygame.init()  # Initialize the pygame

class game(display.display):


    # Function to create the pipes
    def create_pipe(self):
        self.random_pipe_pos = random.choice(self.pipe_height)  # Random height of the pipe
        bottom_pipe = self.pipe_surface.get_rect(midtop=(600, self.random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(600, self.random_pipe_pos - 240))
        return bottom_pipe, top_pipe

    # Function to move the pipes
    def move_pipes(self,pipes):
        for pipe in pipes:
            pipe.centerx -= 4
        self.visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
        return self.visible_pipes

   # Function to draw the pipes
    def draw_pipes(self,pipes):
        for pipe in pipes:
            if pipe.bottom >= 800:
                self.screen.blit(self.pipe_surface, pipe)
            else:
                self.flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                self.screen.blit(self.flip_pipe, pipe)

    # Function to check the collision
    def check_collision(self,pipes):
        global can_score
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                self.death_sound.play()
                self.can_score = True
                return False
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 676:
            self.death_sound.play()
            self.can_score = True
            return False
        return True

    def rotate_bird(self,bird):
        new_bird = pygame.transform.rotozoom(bird, -self.bird_movement*2.7, 1)
        return new_bird

    def bird_animation(self):
        new_bird = self.bird_frames[self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    # Game Variables
    gravity = 0.20  # Gravity
    bird_movement = 0  # Bird movement
    game_active = True  # Game active
    score = 0  # Score
    high_score = 0  # High score
    can_score = True  # Can score
    restart = False  # Restart
    game_overed = 1

    # Font
    game_font = pygame.font.Font('04B_19.ttf', 40)  # Font

    # Bird
    bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()) # Load the bird image
    bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()) # Load the bird image
    bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()) # Load the bird image
    bird_frames = [bird_downflap, bird_midflap, bird_upflap]  # Bird frames
    bird_index = 0  # Bird index
    bird_surface = bird_frames[bird_index]  # Bird surface
    bird_rect = bird_surface.get_rect(center=(100, 400))  # Position of the bird

    BIRDFLAP = pygame.USEREVENT + 1  # Event to flap the bird
    pygame.time.set_timer(BIRDFLAP, 200)  # Timer for the event

    NIGHTTIME = pygame.USEREVENT + 2  # Event to change the background
    pygame.time.set_timer(NIGHTTIME, random.randint(10000,20000))  # Timer for the event

    DAYTIME = pygame.USEREVENT + 3  # Event to change the background


    # Pipes
    pipe_surface = pygame.image.load('assets/pipe-red.png').convert()  # Load the pipe image
    pipe_surface = pygame.transform.scale2x(pipe_surface)  # Double the size of the image
    pipe_list = []  # List to store the pipes

    SPAWNPIPE = pygame.USEREVENT  # Event to spawn the pipes
    pygame.time.set_timer(SPAWNPIPE, 1200)  # Timer for the event

    pipe_height = [250, 350, 400, 600, 650]  # Height of the pipes

    # Game over
    game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())  # Load the game over image
    game_over_rect = game_over_surface.get_rect(center=(288, 400))  # Position of the game over image

    game_over_message = pygame.transform.scale2x(pygame.image.load('assets/gameover.png').convert_alpha())  # Load the game over image
    game_over_message_rect = game_over_message.get_rect(center=(288, 180))  # Position of the game over image

    #sound
    flap_sound = pygame.mixer.Sound('assets/audio/sfx_wing.wav')  # Load the sound
    death_sound = pygame.mixer.Sound('assets/audio/sfx_hit.wav')  # Load the sound
    score_sound = pygame.mixer.Sound('assets/audio/sfx_point.wav')  # Load the sound
    score_sound_countdown = 100  # Score sound countdown
    game_over_sound = pygame.mixer.Sound('assets/audio/game_over.wav')  # Load the sound
    restart_sound = pygame.mixer.Sound('assets/audio/sfx_swooshing.wav')  # Load the sound



# Objects
play= game()
# Game loop
while True:
    for event in pygame.event.get():  # gets any   type of event from the user
        if event.type == pygame.QUIT:  # If the user clicks on the close button
             pygame.quit()  # Quit the game
             sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and play.game_active:
                 play.bird_movement = 0  # Reset the bird movement
                 play.bird_movement -= 7  # Move the bird up
                 play.flap_sound.play()  # Play the sound

            if event.key == pygame.K_RETURN and play.game_active == False:
                play.restart = True


            if event.key == pygame.K_SPACE and play.game_active == False and play.restart == True:
                play.game_active = True
                play.restart = False
                play.pipe_list.clear()
                play.bird_rect.center = (100, 400)
                play.bird_movement = 0
                play.score = 0


        if event.type == play.NIGHTTIME:
            play.bg_surface = pygame.image.load('assets/background-night.png').convert()
            play.bg_surface = pygame.transform.scale2x(play.bg_surface)
            play.pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
            play.pipe_surface = pygame.transform.scale2x(play.pipe_surface)
            play.bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
            play.bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
            play.bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
            play.bird_frames = [play.bird_downflap, play.bird_midflap, play.bird_upflap]
            play.bird_surface = play.bird_frames[play.bird_index]
            #back to daytime after a certain time

            pygame.time.set_timer(play.DAYTIME, random.randint(10000, 20000))

        if event.type == play.DAYTIME:
            play.bg_surface = pygame.image.load('assets/background-day.png').convert()
            play.bg_surface = pygame.transform.scale2x(play.bg_surface)
            play.pipe_surface = pygame.image.load('assets/pipe-red.png').convert()
            play.pipe_surface = pygame.transform.scale2x(play.pipe_surface)
            play.bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
            play.bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
            play.bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
            play.bird_frames = [play.bird_downflap, play.bird_midflap, play.bird_upflap]
            play.bird_surface = play.bird_frames[play.bird_index]
            #back to nighttime after a certain time
            pygame.time.set_timer(play.NIGHTTIME, random.randint(8000, 15000))



        if event.type == play.SPAWNPIPE:
            play.pipe_list.extend(play.create_pipe())  # Append the pipe to the pipe list


        if event.type == play.BIRDFLAP:
            if play.bird_index < 2:
                play.bird_index += 1
            else:
                play.bird_index = 0

            play.bird_surface, play.bird_rect = play.bird_animation()



    play.screen.blit(play.bg_surface, (0, 0))  # Draw the background


    if play.game_active:
        # Bird
        play.bird_movement += play.gravity  # Add gravity to the bird
        play.rotated_bird = play.rotate_bird(play.bird_surface)  # Rotate the bird
        play.bird_rect.centery += play.bird_movement  # Move the bird
        play.screen.blit(play.rotated_bird, play.bird_rect)  # Draw the bird
        play.game_active= play.check_collision(play.pipe_list)  # Check the collision

        # Pipes
        play.pipe_list = play.move_pipes(play.pipe_list)  # Move the pipes
        play.draw_pipes(play.pipe_list)  # Draw the pipes

        # Score
        play.pipe_score_check()
        play.score_display('main_game', 100,265)


    else:
        if play.restart == False:
            play.screen.blit(play.game_over_message, play.game_over_message_rect)  # Draw the game over image
            if play.game_overed==1:
                play.game_over_sound.play()
                play.game_overed=0

            play.high_score = play.update_high_score(play.score, play.high_score)
            play.score_display('game_over', 365, 280)
        else:
            if play.game_overed==0:
                play.game_over_sound.stop()
                play.restart_sound.play()
                play.game_overed=1
            play.screen.blit(play.game_over_surface, play.game_over_rect)  # Draw the game over image
            play.high_score = play.update_high_score(play.score, play.high_score)
            play.score_display('game_over', 100, 265)





    # Floor
    play.floor_x_pos -= 1  # Move the floor to the left
    play.draw_floor()  # Draw the floor
    if play.floor_x_pos <= -576:  # If the floor is out of the screen
        play.floor_x_pos = 0  # Reset the floor position

    pygame.display.update()  # Update the display
    play.clock.tick(120)  # Frame rate

