import pygame 
import time
import random
from random import randint
pygame.init() # lấy toàn bộ thư viện trong pygame

# Size
x = 80
unit = 3
win_width = 1280
win_height = 720
Width_Finish = win_width - x
Player_width = 80
Player_height = 80
Buff_width = 40
Buff_height = 40
Finish_position = [Width_Finish ,2*x+unit]


# Display
GameDisplay = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('The Fastest Pig')

#color mode:
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
Orange = (255,165,0)
Yellow = (255,255,0)
White = (255,255,255)

# Character
Player_position1 = [x-40,2*x+unit]
Player_position2 = [x-40,3*x+unit]
Player_position3 = [x-40,4*x+unit]
Player_position4 = [x-40,5*x+unit]
Player_position5 = [x-40,6*x+unit]
Player_position6 = [x-40,7*x+unit]

Player_position = []
Player_position.append(Player_position1)
Player_position.append(Player_position2)
Player_position.append(Player_position3)
Player_position.append(Player_position4)
Player_position.append(Player_position5)
Player_position.append(Player_position6)
# BLock
Buff_position1 = [random.randint(200,700),2*x+unit]
Buff_position2 = [random.randint(200,700),3*x+unit] 
Buff_position3 = [random.randint(200,700),4*x+unit]
Buff_position4 = [random.randint(200,700),5*x+unit]
Buff_position5 = [random.randint(200,700),6*x+unit]
Buff_position6 = [random.randint(200,700),7*x+unit]

Buff_position = []
Buff_position.append(Buff_position1)
Buff_position.append(Buff_position2)
Buff_position.append(Buff_position3)
Buff_position.append(Buff_position4)
Buff_position.append(Buff_position5)
Buff_position.append(Buff_position6)


# Speed
Speed1 = random.randint(3,6)
Speed2 = random.randint(3,6)
Speed3 = random.randint(3,6)
Speed4 = random.randint(3,6)
Speed5 = random.randint(3,6)
Speed6 = random.randint(3,6)
Speedbuff = 2
Speednerf = 2

# Load Image
back_ground1 = pygame.image.load("cover1.PNG")

Pig1= pygame.image.load("pig1_1.PNG")
Pig2= pygame.image.load("pig2_2.PNG")
Pig3= pygame.image.load("pig3_1.PNG")
Pig4= pygame.image.load("pig4_1.PNG")
Pig5= pygame.image.load("pig5_1.PNG")
Pig6= pygame.image.load("pig6_1.PNG")
Pig = []
Pig.append(Pig1)
Pig.append(Pig2)
Pig.append(Pig3)
Pig.append(Pig4)
Pig.append(Pig5)
Pig.append(Pig6)

a= pygame.image.load("vang.PNG")
b= pygame.image.load("vang 1.PNG")
c= pygame.image.load("vang 2.PNG")
d= pygame.image.load("vang 3.PNG")

Buff1= pygame.image.load("buff.PNG")
Buff2= pygame.image.load("buff.PNG")
Buff3= pygame.image.load("buff.PNG")
Buff4= pygame.image.load("buff.PNG")
Buff5= pygame.image.load("buff.PNG")
Buff6= pygame.image.load("buff.PNG")
Buff = []
Buff.append(Buff1)
Buff.append(Buff2)
Buff.append(Buff3)
Buff.append(Buff4)
Buff.append(Buff5)
Buff.append(Buff6)

# Draw
def draw_background(back_ground):
    GameDisplay.blit(back_ground, (0,0))
def draw_pig(Player_position, number):
    for idx in range(0, number, 1):
        GameDisplay.blit(Pig[idx],(Player_position[idx][0],Player_position[idx][1]))
def draw_buff(Buff_position, number):
    for idx in range(0, number, 1):
        GameDisplay.blit(Buff[idx],(Buff_position[idx][0],Buff_position[idx][1]))
# Clock and FPS
FPS = 30
Clock = pygame.time.Clock()

#Function: text, messenger:
fontsize = 50
font = pygame.font.SysFont("comicsansms", fontsize)

def Text_Object(msg, color):
    text_surf = font.render(msg, True, color)
    return text_surf, text_surf.get_rect()

def print_text_in_center(msg, color):
    textsurf, textrect = Text_Object(msg, color)
    textrect.center = (win_width / 2), (win_height / 2)
    GameDisplay.blit(textsurf, textrect)

# Biến phụ
Repeat = ["False"]
Timebuff = 150
Timenerf = 100
Same1= [0,0]
Same1[0] = Buff_position5[0]
Khong = 0
num=5

smallfont = pygame.font.SysFont("comicsansms", 25)

def score(score):
    text = smallfont.render("Scores: "+str(score),True,Red)
    GameDisplay.blit(text,[0,0])

def Tangtoc(Player,Buff,Khong1,Khong2) :
	if (Player[0]+Player_width) < Buff[0] : 
		B1 = pygame.draw.rect(GameDisplay,Red,(Buff[0],Buff[1],Buff_width,Buff_height)) # xuất hiện block
	if (Player[0]+Player_width) >= Buff[0] and (Player[0] + Player_width) < (Buff[0] + Timebuff) : 
		Player[0] += Speedbuff # bùa tăng tốc trong 1 khoảng thời gian

def Vedich(Player,Buff,Khong1,Khong2) : 
	if (Player[0]+Player_width) < Buff[0] : 
		B2 = pygame.draw.rect(GameDisplay,Blue,(Buff[0],Buff[1],Buff_width,Buff_height)) # xuất hiện block
	if (Player[0]+Player_width) >= Buff[0] : 
		Player[0] = Width_Finish

def Vevachxuatphat(Player,Buff,Repeat,Khong1) : 
	if (Player[0] + Player_width) < Buff[0] and Repeat[0] == "False" : 
		B3 = pygame.draw.rect(GameDisplay,Green,(Buff[0],Buff[1],Buff_width,Buff_height)) # xuất hiện block
	elif (Player[0]+Player_width) >= Buff[0] and Repeat[0] == "False" : 
		Player[0] = 0 # bùa về lại vạch xuất phát
		Repeat[0] = "True"

def Quaydau(Player,Buff,Khong,Khong1) : 
	if (Player[0]+Player_width) < Buff[0] : 
		B4 = pygame.draw.rect(GameDisplay,Orange,(Buff[0],Buff[1],Buff_width,Buff_height)) # xuất hiện block
	if (Player[0]+Player_width) >= Buff[0] and (Player[0] + Player_width) < (Buff[0] + Timenerf) : 
		Player[0] -= Speednerf # bùa tăng tốc trong 1 khoảng thời gian

def Dung1luc(Player,Buff,Same,Speed) : 
	if (Player[0] + Player_width) < Buff[0] : 
		B5 = pygame.draw.rect(GameDisplay,Yellow,(Buff[0],Buff[1],Buff_width,Buff_height)) # xuất hiện block 
	elif (Player[0] + Player_width) >= Buff[0] and (Buff[0] - Same[0]) != 10: 
		Same1[0] -=1  # bùa dừng trong 1 khoảng thời gian
		Player[0] -= Speed

def Dichuyen(Player,Buff,Ham,Thembien,Speed) :

        if Player[0] >= 0 and Player[0] < Width_Finish:
                Player[0] += Speed
                Ham(Player,Buff,Thembien,Speed)
        else :
                Player[0] = Width_Finish
#Start                
set_scores=200 #tiền đặt 
scores=100     #tiền khởi đầu
PlayerChoice = 1 #chọn nhân vật (0->5)

def GameLoop():
    ExitGame = False
    StartRun = False
    GameOver = False
    End = False
    FindTheWinner = False
    YouWon = False

    tram =0
    while not ExitGame:
        while GameOver:
            global scores
            GameDisplay.fill(White)
            if YouWon == True:
                print_text_in_center("Congratulation!! You Won", Red)
            else:
                print_text_in_center("HAHA LOSER!! Press C to Continue or Q to Quit", Red)
            score(scores)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOver = False
                    ExitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        GameLoop()
                    if event.key == pygame.K_q:
                        ExitGame = True
                        GameOver = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitGame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    StartRun = True
                    
        draw_background(back_ground1)
        GameDisplay.blit(Pig[0],(Player_position[0][0],Player_position[0][1]))
        GameDisplay.blit(Pig[1],(Player_position[1][0],Player_position[1][1]))
        GameDisplay.blit(Pig[2],(Player_position[2][0],Player_position[2][1]))
        GameDisplay.blit(Pig[3],(Player_position[3][0],Player_position[3][1]))
        GameDisplay.blit(Pig[4],(Player_position[4][0],Player_position[4][1]))
        if StartRun:
                if tram <20:
                    tram+=1
                if tram>=20 and tram <40:
                    GameDisplay.blit(a,(600,300))
                    tram+=2

                if tram >=40 and tram <60:
                    GameDisplay.blit(b,(600,300))
                    tram+=2

                if tram >=60 and tram <80:
                    GameDisplay.blit(c,(600,300))
                    tram+=2
                if tram >=80 and tram <100:
                    GameDisplay.blit(d,(600,300))
                    tram+=2
                    
                T1 = Dichuyen(Player_position[0],Buff_position[0],Tangtoc,Khong,Speed1)

                T2=Dichuyen(Player_position[1],Buff_position[1],Vedich,Khong,Speed2)

                T3=Dichuyen(Player_position[2],Buff_position[2],Vevachxuatphat,Repeat,Speed3)

                T4=Dichuyen(Player_position[3],Buff_position[3],Quaydau,Khong,Speed4)
                
                T5=Dichuyen(Player_position[4],Buff_position[4],Dung1luc,Same1,Speed5)
                
                
                if FindTheWinner == False:
                        for i in range(num):
                            if (Player_position[i][0] == Width_Finish ):
                                FindTheWinner = True
                                if i == PlayerChoice:
                                    YouWon = True
                                    scores = scores + set_scores*2
                                else:
                                    YouWon = False
                                    scores = scores - set_scores*0.5
                                break
                
        pygame.display.update()
        i = 0
        cnt = 0

        while i < num:
            if (Player_position[i][0] == Width_Finish):
                cnt = cnt + 1   #Đếm số lượng Player về đích
            i += 1
        if cnt == num: # Nếu số lượng Player về đích bằng số người chơi thì Game Over
            StartRun = False
            GameOver = True        
        
        Clock.tick(FPS) # Giảm tốc độ trò chơi xuống 

    pygame.quit()
    quit()

GameLoop()
	    

