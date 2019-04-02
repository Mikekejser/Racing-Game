import pygame, random, sys


def pause_screen():
    pause = True

    pause_text1 = largeFont.render('Pause', True, white)
    pause_text1_rect = pause_text1.get_rect()
    pause_text1_rect.center = width/2, height/2

    pause_text2 = smallFont.render('Press R to restart', True, white)
    pause_text2_rect = pause_text2.get_rect()
    pause_text2_rect.center = width/2, (height/2)+40

    while pause:
        pygame.display.set_caption('pause')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys. exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    pause = False
                elif event.key == pygame.K_r:
                    game_loop()

        ####
        window.fill(green)
        window.blit(pause_text1, pause_text1_rect)
        window.blit(pause_text2, pause_text2_rect)
        pygame.display.update()
        clock.tick(FPS)
        ####


def settings_screen():
    global block_speed
    global bomb_size
    settings = True

    settings_text1 = largeFont.render('Settings', True, white)
    settings_text1_rect = settings_text1.get_rect()
    settings_text1_rect.center = width/2, height/2

    settings_text2 = smallFont.render('Set level of difficulty: 1) Easy, 2) Normal 3) Hard', True, white)
    settings_text2_rect = settings_text2.get_rect()
    settings_text2_rect.center = width/2, (height/2)+40

    settings_text3 = smallFont.render('Start music: press Z, Stop music: press X', True, white)
    settings_text3_rect = settings_text3.get_rect()
    settings_text3_rect.center = width/2, (height/2)+60

    while settings:
        pygame.display.set_caption('settings')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_s:
                    settings = False
                elif event.key == pygame.K_1:
                    block_speed = 2
                    #bomb_size = 30
                elif event.key == pygame.K_2:
                    block_speed = 4
                    #bomb_size = 40
                elif event.key == pygame.K_3:
                    block_speed = 8
                    #bomb_size = 50
                elif event.key == pygame.K_z:
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_x:
                    pygame.mixer.music.stop()
        ####
        window.fill(green)
        window.blit(settings_text1, settings_text1_rect)
        window.blit(settings_text2, settings_text2_rect)
        window.blit(settings_text3, settings_text3_rect)
        pygame.display.update()
        clock.tick(FPS)
        ####

start = True

def start_screen():
    global start
    start_text = largeFont.render('Welcome', True, green)
    start_text_rect = start_text.get_rect()
    start_text_rect.center = width/2, height/2

    game_rules = smallFont.render('Game-objective: Collect the blocks.', True, black)
    game_rules_rect = game_rules.get_rect()
    game_rules_rect.center = width/2, height/2+40

    info = smallFont.render('Hit SPACE to start the game, P to pause or Q to quit.', True, black)
    info_rect = info.get_rect()
    info_rect.center = width/2, height/2+60

    while start:
        pygame.display.set_caption('welcome to race')
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
        ####
                    pygame.mouse.set_visible(False)
                    point_sound.play()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        ####
        window.fill(white)
        button_start(green, (width/2)-button_length, height/2+80, light_green, 'Start')
        button_exit(red, (width/2), height/2+80, lightred, 'Exit')
        window.blit(start_text, start_text_rect)
        window.blit(game_rules, game_rules_rect)
        window.blit(info, info_rect)
        pygame.display.update()
        clock.tick(10)


def quit_game():
    pygame.quit()
    sys.exit()


def coin(x, y):
    window.blit(coinObject, (x, y))


def coin_score(x, y):
    window.blit(coin_to_score, (x, y))


def car(mouse):
    window.blit(carObject, mouse)


def bomb(x, y):
    window.blit(bombObject, (x, y))


def background(x, y):
    window.blit(bgImage, (x, y))


def background_start(x, y):
    window.blit(bgImageStart, (x, y))

# button starts game
def button_start(color, x, y, hover_color, text):
    global start
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+button_length > mouse_x > x and y+button_height > mouse_y > y:
        pygame.draw.rect(window, hover_color, (x, y, button_length, button_height))
        if click[0] == 1:
            print('clicked')
            pygame.draw.rect(window, grey, (x, y, button_length+6, button_height+6))
            pygame.draw.rect(window, hover_color, (x-2, y-2, button_length+4, button_height+4))
            start = False

    else:
        pygame.draw.rect(window, grey, (x, y, button_length + 3, button_height + 3))
        pygame.draw.rect(window, color, (x, y, button_length, button_height))

    button_text = smallFont.render(text, True, white)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = x+button_length/2, y+button_height/2

    window.blit(button_text, button_text_rect)


# button exits game
def button_exit(color, x, y, hover_color, text):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+button_length > mouse_x > x and y+button_height > mouse_y > y:
        pygame.draw.rect(window, hover_color, (x, y, button_length, button_height))
        if click[0] == 1:
            print('clicked')
            pygame.draw.rect(window, grey, (x, y, button_length+6, button_height+6))
            pygame.draw.rect(window, hover_color, (x-2, y-2, button_length+4, button_height+4))
            quit_game()

    else:
        pygame.draw.rect(window, grey, (x, y, button_length + 3, button_height + 3))
        pygame.draw.rect(window, color, (x, y, button_length, button_height))

    button_text = smallFont.render(text, True, white)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = x+button_length/2, y+button_height/2

    window.blit(button_text, button_text_rect)





####
pygame.init()
block_size = 15
bomb_size = 30
circle_size = 15
coin_size = 15
car_length, car_height = 73, 82
button_length, button_height = 80, 40
size = width, height = 800, 600
window = pygame.display.set_mode(size)
FPS = 25
block_speed = 4
clock = pygame.time.Clock()
# COLORS #
white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
light_green = (0,255,0)
grey = (100,100,100)
red = (200,0,0)
lightred = (255,0,0)
# FONTS #
smallFont = pygame.font.SysFont('Arial', 15, False, False)
largeFont = pygame.font.SysFont('Palatino Linotype', 40, False, False)
# SOUNDS #
point_sound = pygame.mixer.Sound('collect_point.wav')
point_sound.set_volume(.1)
slap_sound = pygame.mixer.Sound('slap_sound.ogg')
metal_tap = pygame.mixer.Sound('metal_tap.wav')
intro_music = pygame.mixer.music.load('intro_music.wav')
off_the_road = pygame.mixer.Sound('skateboard.wav')
off_the_road.set_volume(0.5)
# IMAGES #
coinImg = pygame.image.load('goldcoin1.png').convert_alpha()
coinObject = pygame.transform.scale(coinImg, (coin_size*2, coin_size*2))
coin_to_score = pygame.transform.scale(coinImg, (coin_size*2, coin_size*2))
carObject = pygame.image.load('racecar.png').convert_alpha()
bombImg = pygame.image.load('bomb.png').convert_alpha()
bombObject = pygame.transform.scale(bombImg, (bomb_size, bomb_size))
bgImage = pygame.image.load('track.png').convert()
bgImageStart = pygame.image.load('track_start.png').convert()

#with open('Highscore.txt', 'r') as highscoreFile:
    #print(highscoreFile.read())
####
newList = []

def game_loop():
    score_count = 0

    highscoreFile = open('Highscore.csv', 'a')

    pygame.display.set_caption('playing')
    text = smallFont.render('Score:', True, black)
    done = False
    x1 = random.randint(0, width - block_size)
    y1 = 0
    block_x = random.randint(0, width - block_size)
    block_y = 0
    bg_x = 0
    bg_y = -1200
    bg_x_start = 0
    bg_y_start = 0
    coin_to_score_x = -coin_size*3
    coin_to_score_y = -coin_size*3
    ####
    while not done:
        pygame.display.set_caption('race')
        score = smallFont.render(str(score_count), True, black)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
                elif event.key == pygame.K_p:
                    pause_screen()

                elif event.key == pygame.K_s:
                    settings_screen()

        #### CHANGE BLOCK SPEED
        if score_count <= 5:
            y1 += block_speed
            block_y += block_speed
        if 6 <= score_count <= 25:
            y1 += block_speed * 2
            block_y += block_speed * 2
        if 26 <= score_count:
            y1 += block_speed * 3
            block_y += block_speed * 3

        #### RESET BLOCK IF IT REACHES BOTTOM OF SCREEN
        if y1 >= height:
            x1 = random.randint(0, width - block_size)
            y1 = 0

        if block_y >= height:
            block_x = random.randint(0, width - block_size)
            block_y = 0


        #### RESETS THE BACKGROUND IMAGE WHEN THE TOP REACHES 0
        bg_y += 3
        if bg_y >= 0:
            bg_y = -600

        bg_y_start += 3
        if bg_y_start >= 600:
            bg_y_start = 600


        #### RESET OBJECT AND ADD 1 TO SCORE IF OBJECT HITS PLAYER OBJECT
        if mouse[0] < x1+coin_size/2 < mouse[0]+car_length and mouse[1] <= y1+coin_size <= mouse[1]+car_height:
            x1 = random.randint(0, width - coin_size)
            y1 = 0
            score_count += 1
            # adds score_count to file each time it increments
            # if score_count >= 1:
            #     highscoreFile.write(str(score_count) + ',')
            metal_tap.play()
            # sets the coin_to_score position from off the screen to mouse position:
            coin_to_score_x = mouse[0]
            coin_to_score_y = mouse[1]

        if mouse[0] < block_x+block_size/2 < mouse[0]+car_length and mouse[1] <= block_y+block_size <= mouse[1]+car_height:
            block_x = random.randint(0, width - block_size)
            block_y = 0
            score_count -= 1
            slap_sound.play()

        #### PLAY SOUND IF CAR GOES OFF ROAD
        if 50 > mouse[0] or mouse[0]+car_length > 750:
            off_the_road.play()
        else:
            off_the_road.stop()

        #### MAKE THE COIN FLY OFF THE SCREEN ONCE HIT
        # if 0 <= coin_to_score_y <= 200:
        #     coin_to_score_x -= 10
        #     coin_to_score_y -= 10
        # if 200 < coin_to_score_y <= 400:
        #     coin_to_score_x -= 10
        #     coin_to_score_y -= 10
        # if 400 < coin_to_score_y <= 600:
        coin_to_score_x -= 10
        coin_to_score_y -= 10

        if coin_to_score_x <= -coin_size*2:
            coin_to_score_x = -coin_size*3
            coin_to_score_y = -coin_size*3

        ####
        window.fill(white)
        background_start(bg_x_start, bg_y_start)
        background(bg_x, bg_y)
        window.blit(text, (10, 10))
        window.blit(score, (70, 10))
        coin(x1, y1)
        car(mouse)
        bomb(block_x, block_y)
        coin_score(coin_to_score_x, coin_to_score_y)
        pygame.display.update()
        clock.tick(FPS)


    #### WRITING SCORE TO FILE, THEN READ IT
    if score_count >= 1:
        highscoreFile.write(str(score_count) + ',')
    highscoreFile.close()

    outputFile = open('Highscore.csv')
    print(outputFile.read())
    #newList.append(outputFile.read())
    outputFile.close()

    #print(newList)



start_screen()
game_loop()
pygame.quit()
