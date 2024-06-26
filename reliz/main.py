﻿import pygame
import random
pygame.init()
class Card:
    def __init__(self,x,y,width,height,back_color,pered_color,text):
        self.back_rect = pygame.Rect(x,y,width,height)
        self.back_color = back_color
        vidstup_width = width*0.1
        vidstup_height = width*0.1
        new_x = x + vidstup_width
        new_y = y + vidstup_height
        new_width = width - 2*vidstup_width
        new_height =height - 2*vidstup_height
    
        self.pered_rect = pygame.Rect(new_x, new_y, new_width, new_height)
        self.pered_color = pered_color
        self.text = pygame.font.SysFont(None,24).render(text,True, (0,0,0))
    def draw(self,window):
        pygame.draw.rect(window,self.back_color,self.back_rect)
        pygame.draw.rect(window,self.pered_color,self.pered_rect)
        window.blit(self.text,(self.pered_rect.x +0,self.pered_rect.y +0))
    
    def change_text(self,text):
        self.t = text
        self.text = pygame.font.SysFont(None,24).render(text,True,(0,0,0))
country1 = "скіки є фруктів в блоксфрут"
country2 = "скіки є мечів в блоксфрут"
country3 = "скіки є пушок в блоксфрут" 
country4 = "скіки є костюмів в блоксфрут"
country5 = "з якого левела можна йти на 2 світ в блоксфрут"
country6 = "з якого левела можна йти на 3 світ в блоксфрут"
country7 = "який максимальний левел в блоксфрут"
country8 = "скільки коштує фрукт Flame в блоксфрут"
country9 = "скільки коштує фрукт ice в блоксфрут"
country10 = "скільки коштує фрукт Roket в блоксфрут"
country11 = "скільки коштує фрукт Spin в блоксфрут"
country12 = "скільки коштує фрукт Light в блоксфрут"
country13 = "скільки коштує фрукт Rubber в блоксфрут"
country14 = "скільки коштує фрукт Chop в блоксфрут"
country15 = "скільки коштує фрукт Spring в блоксфрут"
country16 = "скільки коштує фрукт Bomb в блоксфрут"
country17 = "скільки коштує фрукт Buddha в блоксфрут"
country18 = "скільки коштує фрукт Portal в блоксфрут"
country19 = "скільки коштує фрукт T-Rex в блоксфрут"
country20 = "скільки коштує фрукт leopard в блоксфрут"
country21 = "скільки коштує фрукт kitsune в блоксфрут"
country22 = "скільки коштує фрукт Love в блоксфрут"
country23 = "скільки коштує фрукт spider в блоксфрут"

capital1 = "39"
capital2 = "37"
capital3 = "13"
capital4 = "38"
capital5 = "700"
capital6 = "1500"
capital7 = "2550"
capital8 = "550"
capital9 = "750"
capital10 = "50"
capital11 = "75"
capital12 = "1100"
capital13 = "1200"
capital14 = "100"
capital15 = "180"
capital16 = "220"
capital17 = "1650"
capital18 = "2000"
capital19 = "2350"
capital20 = "3000"
capital21 = "4000"
capital22 = "1700"
capital23 = "1800"


window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()
pygame.font.init()
card1 = Card(10,200,100,100,(255,0,0),(255,255,255),"клікай")
card2 = Card(130,200,100,100,(255,0,0),(255,255,255),"клікай")
card3 = Card(260,200,100,100,(255,0,0),(255,255,255),"клікай")
card4 = Card(390,200,100,100,(255,0,0),(255,255,255),"клікай")
cards = [card1,card2,card3,card4]

countries=[country1,country2,country3,country4,country5,country6,country7,country8,country9,country10,country11,country12,country13,country14,country15,country16,country17,country18,country19,country20,country21,country22,country23]
capitals =[capital1,capital2,capital3,capital4,capital5,capital6,capital7,capital8,capital9,capital10,capital11,capital12,capital13,capital14,capital15,capital16,capital17,capital18,capital19,capital20,capital21,capital22,capital23]

scoro = 0
scoro_text = pygame.font.SysFont(None,49).render("Rahunok :" + str(scoro),True,(255,255,255))

loose_text = pygame.font.SysFont(None,40).render("Ти програв",True,(0,0,0))
win_text = pygame.font.SysFont(None,40).render("Ти виграв і набрав потрібну кількість балів",True,(0,0,0))

a = 0
unique_numbers = set()
unique_numbers.add(a)
while len(unique_numbers) < 4:
    unique_numbers.add(random.randint(0, 22))

num1, num2, num3, num4 = unique_numbers
cards[0].change_text(capitals[num1])
cards[1].change_text(capitals[num2])
cards[2].change_text(capitals[num3])
cards[3].change_text(capitals[num4])

game = True
while game:
    #оновлення

    if scoro <= -1:
        window.fill((0,0,255))
        window.blit(loose_text, ([200,200]))
        pygame.display.flip()
        break
    if scoro >= 23:
        window.fill([0,0,255])
        window.blit(win_text, (200,200))
        pygame.display.flip()
        break       
    #відмалювання
    window.fill((0,255,0))
    window.blit(scoro_text,(300,100))
    window.blit(pygame.font.SysFont(None, 24).render(countries[a], True, (0, 0, 0)), (150, 50))
    for card in cards:
        card.draw(window)
     
            

    pygame.display.flip()
       #обробка подій
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(len(cards)):
                if cards[i].pered_rect.collidepoint(x,y):
                    if cards[i].t == capitals[a]:
                        scoro += 1
                        print(scoro)
                    else:
                        scoro -= 1
                    a +=1
                    if a == len(capitals):
                        if scoro >20:
                            print("дякую за гру ")
                            game = False
                            break
                    unique_numbers = set()
                    unique_numbers.add(a)
                    while len(unique_numbers) < 4:
                        unique_numbers.add(random.randint(0, 22))

                    num1, num2, num3, num4 = unique_numbers
                    print(unique_numbers)
                    cards[0].change_text(capitals[num1])
                    cards[1].change_text(capitals[num2])
                    cards[2].change_text(capitals[num3])
                    cards[3].change_text(capitals[num4])
                    random.shuffle(cards)
                    scoro_text = pygame.font.SysFont(None, 49).render("Rahunok: " + str(scoro), True, (255, 255, 255))
                    break   

                  
    
    fps.tick(60)
    