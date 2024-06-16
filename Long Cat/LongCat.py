import pygame, sys, random, os
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

       # Get the directory of the current script
        current_dir = os.path.dirname(__file__)
        graphics_dir = os.path.join(current_dir, 'Graphics')
        sounds_dir = os.path.join(current_dir, 'Sound')

    #This is Snake Graphics ------
    #Cat Head
        self.head_up = pygame.image.load(os.path.join(graphics_dir,'cath_up.png')).convert_alpha()
        self.head_down = pygame.image.load(os.path.join(graphics_dir,'cath_down.png')).convert_alpha()
        self.head_right = pygame.image.load(os.path.join(graphics_dir,'cath_right.png')).convert_alpha()
        self.head_left = pygame.image.load(os.path.join(graphics_dir,'cath_left.png')).convert_alpha()
    #Cat Tail
        self.tail_up = pygame.image.load(os.path.join(graphics_dir,'tail_up.png')).convert_alpha()
        self.tail_down = pygame.image.load(os.path.join(graphics_dir,'tail_down.png')).convert_alpha()
        self.tail_right = pygame.image.load(os.path.join(graphics_dir,'tail_right.png')).convert_alpha()
        self.tail_left = pygame.image.load(os.path.join(graphics_dir,'tail_left.png')).convert_alpha()
    #Cat Body V/H
        self.body_vertical = pygame.image.load(os.path.join(graphics_dir,'body_vertical.png')).convert_alpha()
        self.body_horizontal = pygame.image.load(os.path.join(graphics_dir,'body_horizontal.png')).convert_alpha()
    #Cat Body
        self.body_tr = pygame.image.load(os.path.join(graphics_dir,'body_tr.png')).convert_alpha()
        self.body_tl = pygame.image.load(os.path.join(graphics_dir,'body_tl.png')).convert_alpha()
        self.body_br = pygame.image.load(os.path.join(graphics_dir,'body_br.png')).convert_alpha()
        self.body_bl = pygame.image.load(os.path.join(graphics_dir,'body_bl.png')).convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(os.path.join(sounds_dir, '8bit-pickup2.wav'))
        self.meow_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'meow.wav'))  # Load the meow sound
        self.meow_sound.set_volume(0.1)  # Set volume for meow sound (0.0 to 1.0)

    def draw_snake(self):
       self.update_head_graphics()
       self.update_tail_graphics()

       for index,block in enumerate (self.body):
        x_pos = int(block.x * cell_size)
        y_pos = int(block.y * cell_size)
        block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

        if index == 0:
            screen.blit(self.head,block_rect)
        elif index == len(self.body) - 1:
            screen.blit(self.tail,block_rect)
        else:
            previous_block = self.body[index + 1] - block
            next_block = self.body[index - 1] - block
            if previous_block.x == next_block.x:
                screen.blit(self.body_vertical,block_rect)
            elif previous_block.y == next_block.y:
                screen.blit(self.body_horizontal,block_rect)
            else:
                if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    screen.blit(self.body_tl,block_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    screen.blit(self.body_bl,block_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    screen.blit(self.body_tr,block_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    screen.blit(self.body_br,block_rect)
         
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    #snake reappear around the screen
        if self.body[0].x >= cell_number:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = cell_number - 1
        if self.body[0].y >= cell_number:
            self.body[0].y = 0
        elif self.body[0].y < 0:
            self.body[0].y =  cell_number -1

    def add_block(self):
        self.new_block = True
    
    def play_crunch_sound(self):
        self.crunch_sound.play()
        self.crunch_sound.set_volume(0.2)

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        scaled_fish = pygame.transform.scale(fish, (cell_size, cell_size))
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(scaled_fish, fruit_rect)
        #pygame.draw.rect(screen,(100,150,100),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score_last_checked = 0 # Keep track last score checked
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_meow_sound()  # Check and play meow sound if needed

    def check_meow_sound(self):
        current_score = len(self.snake.body) - 3
        if current_score % 10 == 0 and current_score != self.score_last_checked:
            self.snake.meow_sound.play()
            self.score_last_checked = current_score

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
    
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self):
        grass_color = (215,213,168)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(215,213,168))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        fish_rect = fish.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(fish_rect.left,fish_rect.top,fish_rect.width + score_rect.width,fish_rect.height)

        pygame.draw.rect(screen,(82,75,36),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(fish,fish_rect)
        pygame.draw.rect(screen,(175,184,123),bg_rect,2)

#Creates a display screen
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
image_path = os.path.join(current_dir, 'Graphics', 'fish.png')  # Construct the absolute path
fish = pygame.image.load(image_path).convert_alpha()
font_path = os.path.join(current_dir, 'Font', 'Early GameBoy.ttf')  # Construct the correct path for the font file
game_font = pygame.font.Font(font_path, 25)

#Music & Sound
sounds_dir = os.path.join(current_dir, 'Sound')  # Directory for sound files
music_path = os.path.join(sounds_dir, 'wyver9_Funny Chase (8-bit).wav')  # Path to background music file
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1 means the music will loop
pygame.mixer.music.set_volume(0.2)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            #Snake goes UP
            if event.key == pygame.K_w:
               if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            #Snake goes DOWN
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            #Snake goes LEFT
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            #Snake goes RIGHT
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
    
    screen.fill((175,184,123))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)