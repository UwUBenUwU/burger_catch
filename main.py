import pygame
import os
import random
import time

pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

left = [pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "L1.png")), (50, 112.5)),
        pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "L2.png")), (50, 112.5)),
        pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "L3.png")), (50, 112.5))
        ]                                                                         
right =[pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "R1.png")), (50, 112.5)),
        pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "R2.png")), (50, 112.5)),
        pygame.transform.scale(pygame.image.load(os.path.join("Images", "Hero", "R3.png")), (50, 112.5))
        ]

background = pygame.transform.scale(pygame.image.load(os.path.join("Images", "bg.png")), (win_width, win_height))

food = pygame.transform.scale(pygame.image.load(os.path.join("Images", "burger.png")), (75, 75))

class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 6
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.hitboxPlayer = pygame.Rect(self.x, self.y, 50, 112.5)
        # Jump
        self.jump = False
       

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, win):
        self.hitboxPlayer = pygame.Rect(self.x, self.y, 50, 112.5)
        #pygame.draw.rect(win, (0, 0, 0), self.hitboxPlayer, 1)
        if self.stepIndex >= 3:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        collide = self.hitboxPlayer.colliderect(snacks.hitboxFood)


    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely * 4
            self.vely -= 1
        if self.vely < -6:
            self.jump = False
            self.vely = 6

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1


class Food:
    def __init__(self, lx, hx):
        self.y = 0
        self.speed = 5
        self.highestx = win_width
        self.x = random.randint(0,self.highestx)
        self.sprite = str(1)
        self.FoodCount = []
        self.hitboxFood = pygame.Rect(self.x, self.y, 50, 50)
        self.hitCheck = True
        self.hitCount = 0 
       

    def draw(self):
        self.hitboxFood = pygame.Rect(self.x + 15, self.y + 15, 50, 50)
        #pygame.draw.rect(win, (0, 0, 0), self.hitboxFood, 1)
        win.blit(food, (self.x,self.y))
        self.sprite = win.blit(food, (self.x,self.y))
        if self.y == win_height-200:
            print("Ground ")
        collide = self.hitboxFood.colliderect(player.hitboxPlayer)
        hitCount = 0
        if self.hitCheck:
            if collide: 
                print('hit')

                hitCount += 1
                print(hitCount)
                self.hitCheck = False


    def spawn(self):
        snack = Food(0, win_width)
        snack.draw()
        self.FoodCount.append(snack)
        for snack in snack.FoodCount:
            snack.move()

        
    def move(self):
        self.y += self.speed


def draw_game():
    global tower_health, speed
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    
    player.draw(win)

    for snack in snacks.FoodCount:
        snack.draw()
        snack.move()
                

    pygame.time.delay(30)
    pygame.display.update()



pygame.time.set_timer(pygame.USEREVENT, 1000)

snacks = Food(0, win_width)
player = Hero(250, 290)
hitCount = 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.USEREVENT:
            snacks.spawn()
           
        collide = snacks.hitboxFood.colliderect(player.hitboxPlayer)
        
        if collide: 

            hitCount += 1
            print(hitCount)

    userInput = pygame.key.get_pressed()

    player.move_hero(userInput)
    player.jump_motion(userInput)

    draw_game()