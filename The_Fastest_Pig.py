import pygame 
import time
import random 
import math
from random import randint
from datetime import datetime
pygame.init() # lấy toàn bộ thư viện trong pygame
pygame.mixer.init()

#color mode:
Red = (200,0,0)
light_red = (255,0,0)

Green = (0,200,0)
light_green = (0,255,0)

Yellow = (200,200,0)
light_yellow = (255,255,0)

Blue = (0,0,190)
light_blue = (0,0,255)

Orange = (255,165,0)
White = (255,255,255)
Black = (0,0,0)

Speedbuff = 4
Speednerf = 4

Width_Start=0
isShort=1

# Load Image
# Background
back_ground1 = pygame.image.load("cover1.PNG")
back_ground2 = pygame.image.load("cover2.PNG")
line_start = pygame.image.load("line_start.PNG")
line_finish = pygame.image.load("line_finish.PNG")
startgame= pygame.image.load("startgame.PNG")
information = pygame.image.load("information.JPG")
instruction = pygame.image.load("instruction.JPG")
play = pygame.image.load("play.JPG")
buttonquit = pygame.image.load("quit.PNG")
guide= pygame.image.load("guide.PNG")
amulet= pygame.image.load("amulet.PNG")
bg_rank= pygame.image.load("rank.PNG")
bg_history= pygame.image.load("history.PNG")
gameover = pygame.image.load("GameOver.PNG")
buttonMute = pygame.image.load("mute.PNG")
buttonUnMute = pygame.image.load("unmute.PNG")
shop = pygame.image.load("shop.PNG")
store = pygame.image.load("store.PNG")
backgroundA = pygame.image.load("bgA.PNG")
backgroundB = pygame.image.load("bgB.PNG")
backgroundC = pygame.image.load("bgC.PNG")
backgroundD = pygame.image.load("bgD.PNG")
setbua = pygame.image.load("setbua.PNG")
setskin = pygame.image.load("setskin.PNG")
Fill = pygame.image.load("Fill.PNG")



Pig1_1= pygame.image.load("pig1_1.PNG")
Pig1_2= pygame.image.load("pig1_2.PNG")
Pig1_3= pygame.image.load("pig1_3.PNG")
Pig1 = []
Pig1.append(Pig1_1)
Pig1.append(Pig1_2)
Pig1.append(Pig1_3)
Pig2_1= pygame.image.load("pig2_1.PNG")
Pig2_2= pygame.image.load("pig2_2.PNG")
Pig2_3= pygame.image.load("pig2_3.PNG")
Pig2 = []
Pig2.append(Pig2_1)
Pig2.append(Pig2_2)
Pig2.append(Pig2_3)
Pig3_1= pygame.image.load("pig3_1.PNG")
Pig3_2= pygame.image.load("pig3_2.PNG")
Pig3_3= pygame.image.load("pig3_3.PNG")
Pig3 = []
Pig3.append(Pig3_1)
Pig3.append(Pig3_2)
Pig3.append(Pig3_3)
Pig4_1= pygame.image.load("pig4_1.PNG")
Pig4_2= pygame.image.load("pig4_2.PNG")
Pig4_3= pygame.image.load("pig4_3.PNG")
Pig4 = []
Pig4.append(Pig4_1)
Pig4.append(Pig4_2)
Pig4.append(Pig4_3)
Pig5_1= pygame.image.load("pig5_1.PNG")
Pig5_2= pygame.image.load("pig5_2.PNG")
Pig5_3= pygame.image.load("pig5_3.PNG")
Pig5= []
Pig5.append(Pig5_1)
Pig5.append(Pig5_2)
Pig5.append(Pig5_3)
Pig6_1= pygame.image.load("pig6_1.PNG")
Pig6_2= pygame.image.load("pig6_2.PNG")
Pig6_3= pygame.image.load("pig6_3.PNG")
Pig6= []
Pig6.append(Pig6_1)
Pig6.append(Pig6_2)
Pig6.append(Pig6_3)
Pig = []
Pig.append(Pig1)
Pig.append(Pig2)
Pig.append(Pig3)
Pig.append(Pig4)
Pig.append(Pig5)
Pig.append(Pig6)

Pig1_1s= pygame.image.load("pig1_1s.PNG")
Pig1_2s= pygame.image.load("pig1_2s.PNG")
Pig1_3s= pygame.image.load("pig1_3s.PNG")
Pig1s = []
Pig1s.append(Pig1_1s)
Pig1s.append(Pig1_2s)
Pig1s.append(Pig1_3s)
Pig2_1s= pygame.image.load("pig2_1s.PNG")
Pig2_2s= pygame.image.load("pig2_2s.PNG")
Pig2_3s= pygame.image.load("pig2_3s.PNG")
Pig2s = []
Pig2s.append(Pig2_1s)
Pig2s.append(Pig2_2s)
Pig2s.append(Pig2_3s)
Pig3_1s= pygame.image.load("pig3_1s.PNG")
Pig3_2s= pygame.image.load("pig3_2s.PNG")
Pig3_3s= pygame.image.load("pig3_3s.PNG")
Pig3s = []
Pig3s.append(Pig3_1s)
Pig3s.append(Pig3_2s)
Pig3s.append(Pig3_3s)
Pig4_1s= pygame.image.load("pig4_1s.PNG")
Pig4_2s= pygame.image.load("pig4_2s.PNG")
Pig4_3s= pygame.image.load("pig4_3s.PNG")
Pig4s = []
Pig4.append(Pig4_1s)
Pig4.append(Pig4_2s)
Pig4.append(Pig4_3s)
Pig5_1s= pygame.image.load("pig5_1s.PNG")
Pig5_2s= pygame.image.load("pig5_2s.PNG")
Pig5_3s= pygame.image.load("pig5_3s.PNG")
Pig5s= []
Pig5s.append(Pig5_1s)
Pig5s.append(Pig5_2s)
Pig5s.append(Pig5_3s)
Pig6_1s= pygame.image.load("pig6_1s.PNG")
Pig6_2s= pygame.image.load("pig6_2s.PNG")
Pig6_3s= pygame.image.load("pig6_3s.PNG")
Pig6s= []
Pig6s.append(Pig6_1s)
Pig6s.append(Pig6_2s)
Pig6s.append(Pig6_3s)
Pigs = []
Pigs.append(Pig1s)
Pigs.append(Pig2s)
Pigs.append(Pig3s)
Pigs.append(Pig4s)
Pigs.append(Pig5s)
Pigs.append(Pig6s)


hao= pygame.image.load("hao.PNG")
chao= pygame.image.load("chao.PNG")
hieu1= pygame.image.load("hieu1.PNG")
hieu2= pygame.image.load("hieu2.PNG")
hoa= pygame.image.load("hoa.PNG")
hien= pygame.image.load("hien.PNG")
CTT3= []
CTT3.append(hao)
CTT3.append(chao)
CTT3.append(hieu1)
CTT3.append(hieu2)
CTT3.append(hoa)
CTT3.append(hien)

player_pig=[Pig1_1,Pig2_1,Pig3_1,Pig4_1,Pig5_1,Pig6_1]
player_ctt3=[hao,chao,hieu1,hieu2,hoa,hien]

player_set=[player_pig,player_ctt3]

Buff= pygame.image.load("buff.PNG")

vang= pygame.image.load("vang.PNG")
vang1= pygame.image.load("vang 1.PNG")
vang2= pygame.image.load("vang 2.PNG")
vang3= pygame.image.load("vang 3.PNG")
xanh= pygame.image.load("xanh.PNG")
xanh1= pygame.image.load("xanh 1.PNG")
xanh2= pygame.image.load("xanh 2.PNG")
xanh3= pygame.image.load("xanh 3.PNG")
do= pygame.image.load("do.PNG")
do1= pygame.image.load("do 1.PNG")
do2= pygame.image.load("do 2.PNG")
do3= pygame.image.load("do 3.PNG")
# Display
win_width = 1280    
win_height = 720
GameDisplay = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('The Fastest Pig')
pygame.display.set_icon(Pig1_1)

# Clock
Clock = pygame.time.Clock()

# Biến phụ
Timebuff = 150
Timenerf = 100
Dau =5 #speed set 
Cuoi = 7    
Dista = 100
Money = 1000
Back = ["False","False","False","False","False","False"]
start_time = None
a=[Width_Start,Width_Start,Width_Start,Width_Start,Width_Start,Width_Start]
b=[90,90,90,90,90,90]
start_firework=0
count=0
list_history=[]
count_play_time=-1

#Input: PHAN NHAP O DAU NE:
input_infor = [] # cai nay nhap 1 lan thoi
input_choice = [] # cai nay nhap lai moi lan nguoi choi choi lai
text1 = 'Player Name'
text2 = 'Bet Money'
input_infor.append(text1)
input_choice.append(text2)
#Output: MANG LUU TRU THONG TIN NHAP O TREN
Info_user = []
Choice_user = []

#font
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms",75)

def Size(x,xsize,xfont):
    # Size
    global win_width, win_height,Player_width, Player_height, Buff_width, Buff_height, Finish_position, Player_position, GameDisplay, smallfont, medfont, largefont,Width_Finish,Width_Start, xtemp, unit, xsizetemp
    unit=x/6
    xtemp=x
    xsizetemp=xsize
    win_width = 16*x    
    win_height = 9*x
    Player_width = 4*unit
    Player_height = 4*unit
    Width_Finish = win_width - Player_width
    Buff_width = 2*unit
    Buff_height = 2*unit
    Finish_position = [Width_Finish ,2*x+unit]

    # Character
    Player_position1 = [x/3,2*x+unit]
    Player_position2 = [x/3,3*x+unit]
    Player_position3 = [x/3,4*x+unit]
    Player_position4 = [x/3,5*x+unit]
    Player_position5 = [x/3,6*x+unit]
    Player_position6 = [x/3,7*x+unit]

    Player_position = []
    Player_position.append(Player_position1)
    Player_position.append(Player_position2)
    Player_position.append(Player_position3)
    Player_position.append(Player_position4)
    Player_position.append(Player_position5)
    Player_position.append(Player_position6)

    # Display
    GameDisplay = pygame.display.set_mode((win_width, win_height))

    #Function: text, messenge
    smallfont = pygame.font.SysFont("comicsansms", xfont)
    medfont = pygame.font.SysFont("comicsansms", 2*xfont)
    largefont = pygame.font.SysFont("comicsansms",3*xfont)


# Draw
def draw_background(back_ground,start,finish):                                     
    GameDisplay.blit(back_ground, (0,0))
    GameDisplay.blit(line_start, (start+Player_width,162/720*win_height))
    GameDisplay.blit(line_finish, (finish-2*unit,162/720*win_height))

def draw_player(Player_position, number,setplayer):
    global a,b
    if setplayer == Pig:
        for idx in range(0, number):
            if Player_position[idx][0]>=b[idx]:
                a[idx]=b[idx]
                b[idx]=b[idx]+90  
            if Back[idx]==False:
                if Player_position[idx][0]<30+a[idx]:
                    GameDisplay.blit(Pig[idx][0],(Player_position[idx][0],Player_position[idx][1]))
                if Player_position[idx][0]>=30+a[idx] and Player_position[idx][0]<60+a[idx]:
                    GameDisplay.blit(Pig[idx][1],(Player_position[idx][0],Player_position[idx][1]))
                if Player_position[idx][0]>=60+a[idx] and Player_position[idx][0]<90+a[idx]:
                    GameDisplay.blit(Pig[idx][2],(Player_position[idx][0],Player_position[idx][1]))         
            else:
                PigBack1 = pygame.transform.flip(Pig[idx][0],1,0)
                PigBack2 = pygame.transform.flip(Pig[idx][1],1,0)
                PigBack3 = pygame.transform.flip(Pig[idx][2],1,0)
                if Player_position[idx][0]<30+a[idx]:
                    GameDisplay.blit(PigBack3,(Player_position[idx][0],Player_position[idx][1]))
                if Player_position[idx][0]>=30+a[idx] and Player_position[idx][0]<60+a[idx]:
                    GameDisplay.blit(PigBack2,(Player_position[idx][0],Player_position[idx][1]))
                if Player_position[idx][0]>=60+a[idx] and Player_position[idx][0]<90+a[idx]:
                    GameDisplay.blit(PigBack1,(Player_position[idx][0],Player_position[idx][1])) 
                Back[idx]=False
    if setplayer == CTT3:
        for idx in range(0,number):
            if Back[idx]==False:
                GameDisplay.blit(CTT3[idx],(Player_position[idx][0],Player_position[idx][1]))
            else:
                CTT3Back = pygame.transform.flip(CTT3[idx],1,0)
                GameDisplay.blit(CTT3Back,(Player_position[idx][0],Player_position[idx][1]))
                Back[idx]=False
def draw_firework(Player_position):
    global count, start_firework, unit
    count = pygame.time.get_ticks()
    if count <start_firework+500:
        GameDisplay.blit(vang,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count>=start_firework+500 and count <start_firework+1000:
        GameDisplay.blit(xanh,(Width_Finish-Player_width/4,Player_position[1]-Player_width-unit))
        GameDisplay.blit(vang1,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count >=start_firework+1000 and count <start_firework+1500:
        GameDisplay.blit(xanh1,(Width_Finish-Player_width/4,Player_position[1]-Player_width-unit))
        GameDisplay.blit(vang2,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        GameDisplay.blit(do,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
    if count >=start_firework+1500 and count <start_firework+2000:
        GameDisplay.blit(xanh2,(Width_Finish-Player_width/4,Player_position[1]-Player_width-unit))
        GameDisplay.blit(vang3,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        GameDisplay.blit(vang,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        GameDisplay.blit(do1,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
    if count >=start_firework+2000 and count <start_firework+3500:
        GameDisplay.blit(xanh3,(Width_Finish-Player_width/4,Player_position[1]-Player_width-unit))
        GameDisplay.blit(vang1,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        GameDisplay.blit(do2,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
    if count >=start_firework+3500 and count <start_firework+4000:
        GameDisplay.blit(vang2,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        GameDisplay.blit(do3,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
    if count >=start_firework+4000 and count <start_firework+4300:
        GameDisplay.blit(do,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
        GameDisplay.blit(vang3,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count >=start_firework+4200 and count <start_firework+4500:    
        GameDisplay.blit(do1,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
        GameDisplay.blit(vang,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count >=start_firework+4500 and count <start_firework+5000:
        GameDisplay.blit(do2,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
        GameDisplay.blit(vang1,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count >=start_firework+5000 and count <start_firework+5500:
        GameDisplay.blit(do3,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit-unit/2))
        GameDisplay.blit(vang2,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
    if count >=start_firework+5500 and count <start_firework+5800:
        GameDisplay.blit(vang3,(Width_Finish-Player_width*3/4,Player_position[1]-Player_width-unit+unit/2))
        
 # Function: Message
def Text_Object(msg, color, size):
    if size == "small":
        text_surf = smallfont.render(msg, True, color)
    if size == "medium":
        text_surf = medfont.render(msg, True, color)
    if size == "large":
        text_surf = largefont.render(msg, True, color)

    return text_surf, text_surf.get_rect()

def Message_to_screen(msg, color, y_displace=0, size = "small"):
    textsurf, textrect = Text_Object(msg, color, size)
    textrect.center = (win_width / 2), (win_height / 2) + y_displace
    GameDisplay.blit(textsurf, textrect)

def Text_to_screen(msg, color, x,y, size = "small"):
    textsurf, textrect = Text_Object(msg, color, size)
    textrect.center = x, y
    GameDisplay.blit(textsurf, textrect)

def Text_to_button(msg,color,buttonx, buttony, buttonwidth, buttonheight, size ="small"):
    textsurf, textrect = Text_Object(msg, color, size)
    textrect.center = ((buttonx + (buttonwidth/2)), buttony + (buttonheight/2))
    GameDisplay.blit(textsurf, textrect)

# Function: Buff
def Tangtoc(Player,Block) :
    if (Player[0]+Player_width) < Block[0] : 
        GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block
    if (Player[0]+Player_width) >= Block[0] and (Player[0] + Player_width) <= (Block[0] + Timebuff)  : 
        Player[0] += Speedbuff # bùa tăng tốc trong 1 khoảng thời gian

def Vedich(Player,Block) : 
    if (Player[0]+Player_width) < Block[0] : 
         GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block
    if (Player[0]+Player_width) >= Block[0] : 
        Player[0] = Width_Finish

def Vevachxuatphat(Player,Block,Condition) : 
    if (Player[0] + Player_width) < Block[0] and Condition[0] == "False" : 
        GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block
    elif (Player[0]+Player_width) >= Block[0] and Condition[0] == "False" : 
        Player[0] = Width_Start # bùa về lại vạch xuất phát
        Condition[0] = "True"   

def Quaydau(Player,Block):
    if (Player[0]+Player_width) < Block[0] : 
         GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block
    if (Player[0]+Player_width) >= Block[0] and( Player[0] + Player_width) < (Block[0] + Timenerf) : 
        Player[0] -= Speednerf # bùa tăng tốc trong 1 khoảng thời gian
        for i in range(NumOfPlayer):
            if Player_position[i][0] == Player[0]:
                Back[i]=True

def Dung1luc(Player,Block,Timestop,Speed): 
    if (Player[0] + Player_width) < Block[0] : 
         GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block 
    elif (Player[0] + Player_width) >= Block[0] and Timestop[0] <=60 : 
        Timestop[0] +=1
        Player[0] -= Speed

def Flash(Player,Block,Distance):
    if (Player[0]+Player_width) < Block[0] : 
        GameDisplay.blit(MainBuff,(Block[0],Block[1])) # xuất hiện block 
    elif (Player[0]+Player_width) >= Block[0] and Distance[0] == "False" :
        Player[0] = Player[0] + Dista 
        Distance[0] = "True"

def Dichuyen(Player,Block1,Block2,Condition,Distance,Timestop,SL,a,b):
    if Player[0] >= 0 and Player[0] < Width_Finish :
        Speed = random.randint(Dau,Cuoi)
        Player[0] += Speed
        Tile(Player,Block1,Block2,Condition,Distance,Timestop,Speed,SL,a,b) 
    else : Player[0] = Width_Finish

def Tile(Player,Block1,Block2,Condition,Distance,Timestop,Speed,SL,a,b) :
    x = 0 
    if 21 <= SL and SL <= 60 :
        if 1<= a and a <= 10 :
            Vevachxuatphat(Player,Block1,Condition) 
        if 11 <= a and a <= 15 :
            Vedich(Player,Block1)
        if 16 <= a and a <= 35 :
            Tangtoc(Player,Block1)
        if 36 <= a and a <= 60 :
            Quaydau(Player,Block1)
        if 61 <= a and a <= 80 :
            Dung1luc(Player,Block1,Timestop,Speed)
        if 81 <= a and a <= 100 :
            Flash(Player,Block1,Distance)

    if 61 <= SL and SL <= 100 :
        if 1<= a and a <= 10 :
            Vevachxuatphat(Player,Block1,Condition) 
            x = 2
        if 11 <= a and a <= 15 :
            Vedich(Player,Block1)
        if 16 <= a and a <= 35 :
            Tangtoc(Player,Block1)
            x = 3
        if 36 <= a and a <= 60 :
            Quaydau(Player,Block1)
            x = 4
        if 61 <= a and a <= 80 :
            Dung1luc(Player,Block1,Timestop,Speed)
            x = 5
        if 81 <= a and a <= 100 :
            Flash(Player,Block1,Distance)
            x = 6

        if x == 2 :
            if 1<= b and b <= 20 :
                Quaydau(Player,Block2) 
            if 21 <= b and b <= 30 :
                Vedich(Player,Block2)
            if 31 <= b and b <= 75 :
                Flash(Player,Block2,Distance)
            if 76 <= b and b <= 100 :
                Dung1luc(Player,Block2,Timestop,Speed)
        if x == 3 : 
            if 1 <= b and b <= 20 :
                Flash(Player,Block2,Distance)
            if 21 <= b and b <= 25 :
                Vedich(Player,Block2)
            if 26 <= b and b <= 65 :
                Quaydau(Player,Block2)
            if 66 <= b and b <= 100 :
                Dung1luc(Player,Block2,Timestop,Speed)
        if x == 4 :
            if 1 <= b and b <= 30 :
                Flash(Player,Block2,Distance)
            if 31 <= b and b <= 60 :
                Tangtoc(Player,Block2)
            if 61 <= b and b <= 70 :
                Vedich(Player,Block2)
            if 71 <= b and b <= 100 :
                Dung1luc(Player,Block2,Timestop,Speed)
        if x == 5 :
            if 1 <= b and b <= 30 :
                Flash(Player,Block2,Distance)
            if 31 <= b and b <= 40 :
                Vedich(Player,Block2)
            if 41 <= b and b <= 70 :
                Tangtoc(Player,Block2)
            if 71 <= b and b <= 100 :
                Quaydau(Player,Block2)
        if  x == 6 :
            if 1 <= b and b <= 25 :
                Tangtoc(Player,Block2)
            if 26 <= b and b <= 35 :
                Vedich(Player,Block2)
            if 36 <= b and b <= 65 :
                Quaydau(Player,Block2)
            if 66 <= b and b <= 100 : 
                Dung1luc(Player,Block2,Timestop,Speed) 

def money(money):
    text = smallfont.render("Money: $ "+str(int(money)),True,Red)
    GameDisplay.blit(text,[0,0])

# Biến Hàm
screen = True
intro = True
mute = False

#Function Input Information:	
def signin(text, archive):
    val = ''
    active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = True
                color = color_active if active else color_inactive
                if active:
                    if event.key == pygame.K_RETURN:
                        archive.append(val)
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        val = val[:-1]
                    else:
                        val += event.unicode
                
        GameDisplay.fill(light_yellow)
        Message_to_screen("Press Space to enter from the keyboard, press enter to continue",Red,-4*xtemp,"small")
        Message_to_screen(text, color, -50,"small")
        Message_to_screen(val, Black, 0,"small")
        pygame.display.update()
    

def signin_all(Texts , archive):
    for val in Texts:
        signin(val, archive)  

#Function: button image
def buttonImage (x,y,width,height,image, action = None):
    global SetImage, back_ground, back_ground1, back_ground2, PlayerChoose, mute
    global intro, prepare, Choose_Player,Choose_Background, Choose_Length, in_struct1,in_struct2, infor, Choose_Set, Choose_number, ExitGame
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0]==1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "instruction":
                in_struct1 = True
                in_struct2 = True
                instruct()
            if action == "information":
                infor = True
                buttonInfor()
            if action == "play":
                intro = False
                prepare = True
                Choose_Set = True
                Choose_number = True
                Choose_Player = True
                Choose_Background = True
                Choose_Length = True
                PrepareGameLoop()
            if action == "shop":
                pass
            if action == "background1":
                back_ground1= pygame.transform.scale(back_ground1,(win_width,win_height))
                back_ground2= pygame.transform.scale(back_ground1,(win_width,win_height))
                back_ground = back_ground1
                Choose_Background = False
            if action == "background2":
                back_ground1= pygame.transform.scale(back_ground1,(win_width,win_height))
                back_ground2= pygame.transform.scale(back_ground1,(win_width,win_height))
                back_ground = back_ground2
                Choose_Background = False
            if action == "player1":
                PlayerChoose = 1
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "player2":
                PlayerChoose = 2
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "player3":
                PlayerChoose = 3
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "player4":
                PlayerChoose = 4
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "player5":
                PlayerChoose = 5
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "player6":
                PlayerChoose = 6
                Choose_Player = False
                prepare = False
                ExitGame = False
                GameLoop()
            if action == "mute":
                pygame.mixer_music.pause()
                mute=True
            if action == "unmute":
                pygame.mixer_music.unpause()
                mute=False
            
            

    else:
        GameDisplay.blit(image,(x,y))

#Function: Button
def button(text, x,y,width,height,inactive_color, active_color, action = None):
    global xbutton1,ybutton1, xbutton2,ybutton2, FPS, line_finish, line_start, MainPlayer, MainBuff,NumOfPlayer
    global screen, infor, intro, prepare, Choose_Set,Choose_number,Choose_Length,Width_Finish,Width_Start,isShort,in_struct1,in_struct2, menu,ExitGame
    global Choose_Background, Choose_Set, Choose_number, Choose_Player, Choose_Length, show_rank, show_history, buff1
    global val_buy1,val_buy2,val_buy3,val_buy4,val_buy5,val_buy6, val_use1,val_use2,val_use3,val_use4,val_use5,val_use6,val_shop, backgroundA, back_ground,backgroundB,backgroundC,backgroundD, Pigs, Pig
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(GameDisplay, active_color, (x,y,width,height))
        if click[0]==1 and action != None:
            if action == "smallscreen":
                screen = False
                intro = True
                FPS=20
                Size(60,30,15)
                xbutton1=193
                ybutton1=34
                xbutton2=116
                ybutton2=33
                line_finish = pygame.transform.scale(line_finish,(60,355))
                line_start = pygame.transform.scale(line_start,(4,355))
                Game_intro()
            if action == "mediumscreen":
                screen = False
                FPS=25
                Size(70,40,20)
                xbutton1=213
                ybutton1=54
                xbutton2=136
                ybutton2=43
                line_finish = pygame.transform.scale(line_finish,(75,414))              
                line_start = pygame.transform.scale(line_start,(4,414))
                Game_intro()
            if action == "largescreen":
                screen = False
                FPS=30
                xbutton1= 233
                ybutton1=74
                xbutton2=156
                ybutton2=53
                Size(80,50,25)
                Game_intro()
            if action == "play":
                in_struct2= False
                intro = False
                prepare = True
                Choose_Set = True
                Choose_number = True
                Choose_Player = True
                Choose_Background = True
                Choose_Length = True
                PrepareGameLoop()
            if action == "shop":
                pass
            if action == "intro":
                in_struct1 = True
                Game_intro()
            if action == "intro1":
                menu = False
                in_struct1 = True
                ExitGame = True
                intro = True
                Game_intro()
            if action == "next":
                in_struct1= False
            if action == "set1":
               Choose_Set = False
               NumOfPlayer=6
               MainPlayer = CTT3
               MainBuff = Buff
            if action == "set2":
               Choose_Set = False
               MainPlayer = Pig
               MainBuff = Buff
            if action == "4":
                Choose_number = False
                NumOfPlayer = 4
            if action == "5":
                Choose_number = False
                NumOfPlayer = 5
            if action == "6":
                Choose_number = False
                NumOfPlayer = 6
            if action == "short":
                Choose_Length = False
                isShort=3/5 #bỏ qua tỉ lệ xuất hiện 2 bùa
                Width_Start = (win_width - Player_width)/4
                Width_Finish = (win_width - Player_width)*2/3
                signin_all(input_choice, Choice_user)
            if action == "medium":
                Choose_Length = False
                Width_Start= (win_width - Player_width)/6
                Width_Finish =(win_width - Player_width)*5/6
                signin_all(input_choice, Choice_user)
            if action == "long":
                Width_Finish = win_width - Player_width
                Width_Start=0
                Choose_Length = False
                signin_all(input_choice, Choice_user)
            if action == "menu":
                Menu()  
            if action == "continue":
                menu = False
                val_use1 = False
                val_buy1 = False
                val_use2 = False
                val_buy2 = False
                val_use3 = False
                val_buy3 = False
                val_use4 = False
                val_buy4 = False
                val_use5 = False
                val_buy5 = False
                val_use6 = False
                val_buy6 = False
                val_shop= False
            if action == "next_rank":
                show_rank = False
            if action == "next_history":
                show_history = False
            if action == "quit":
                pygame.quit()
                quit()
            if action == "shop":
                val_shop = True
                #menu=False
                Shop()
            if action == "buy1":
                val_buy1 = True
                buy1()
            if action == "buy2":
                val_buy2 = True
                buy2()
            if action == "buy3":
                val_buy3 = True
                buy3()
            if action == "buy4":
                val_buy4 = True
                buy4()
            if action == "buy5":
                val_buy5 = True
                buy5()
            if action == "buy6":
                val_buy6 = True
                buy6()
            if action == "use1":
                val_use1= True
                val_buy1=False
                backgroundA= pygame.image.load("bgA.PNG")
                backgroundA=pygame.transform.scale(backgroundA,(win_width,win_height))
                back_ground = backgroundA
                use1()
            if action == "use2":
                val_use2= True
                val_buy2=False
                backgroundB= pygame.image.load("bgB.PNG")
                backgroundB=pygame.transform.scale(backgroundB,(win_width,win_height))
                back_ground = backgroundB
                use2()
            if action == "use3":
                val_use3= True
                val_buy3=False
                backgroundC= pygame.image.load("bgC.PNG")
                backgroundC=pygame.transform.scale(backgroundC,(win_width,win_height))
                back_ground = backgroundC
                use3()
            if action == "use4":
                val_use4= True
                val_buy4=False
                backgroundD= pygame.image.load("bgD.PNG")
                backgroundD=pygame.transform.scale(backgroundD,(win_width,win_height))
                back_ground = backgroundD
                use4()
            if action == "use5":
                val_use5= True
                val_buy5=False
                buff1=pygame.image.load("buff1.PNG")
                buff1=pygame.transform.scale(buff1,(math.floor(Buff_width),math.floor(Buff_height)))
                MainBuff=buff1
                use5()
            if action == "use6":
                val_use6= True
                val_buy6=False
                Pig=Pigs
                MainPlayer = Pigs
                use6()
    else:
        pygame.draw.rect(GameDisplay, inactive_color, (x,y,width,height))
    Text_to_button(text,Black,x,y,width,height)
# Function Game pause
def pause():
    paused = True
    while paused:
        Message_to_screen("Pause",Black,-xtemp,"large")
        Message_to_screen("Press C to continue or Q to quit.",Black,0,"medium")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()  
        pygame.display.update()
        Clock.tick(20)

# Function Menu
def Menu():
    while menu:
        GameDisplay.fill(White)
        Message_to_screen("Menu",Red,-4*xtemp,"large")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if mute == False:  
            buttonImage(0,0,xtemp,xtemp,buttonMute,"mute")
        else:
            buttonImage(xtemp,0,xtemp,xtemp,buttonUnMute,"unmute")
        button("Main Menu", win_width/2-1.5*xtemp,win_height/2-3*xtemp,3*xtemp,xtemp,Red,light_red,"intro1")
        button("Shop",win_width/2-1.5*xtemp,win_height/2-xtemp,3*xtemp,xtemp,Yellow,light_yellow,"shop")
        button("Continue",win_width/2-1.5*xtemp,win_height/2+xtemp,3*xtemp,xtemp,Blue,light_blue,"continue")
        button("Quit",win_width/2-1.5*xtemp,win_height/2 + 3*xtemp,3*xtemp,xtemp,Green,light_green,"quit")
        pygame.display.update()
        Clock.tick(20)

# Function shop
def Shop():
    global  shop, backgroundA,backgroundB,backgroundC,backgroundD, setbua, setskin,Money
    shop = pygame.transform.scale(shop,(win_width,win_height))
    backgroundA = pygame.transform.scale(backgroundA,(4*xtemp,2*xtemp))
    backgroundB = pygame.transform.scale(backgroundB,(4*xtemp,2*xtemp))
    backgroundC = pygame.transform.scale(backgroundC,(4*xtemp,2*xtemp))
    backgroundD = pygame.transform.scale(backgroundD,(4*xtemp,2*xtemp))
    setbua = pygame.transform.scale(setbua,(4*xtemp,2*xtemp))
    setskin = pygame.transform.scale(setskin,(4*xtemp,2*xtemp))
    GameDisplay.blit(shop,(0,0))
    pygame.display.update()
    while val_shop:
        #GameDisplay.blit(shop,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #money(Money)
        buttonImage((53/1280)*win_width,(17/80)*win_height+0.3*xtemp,4*xtemp,2*xtemp,backgroundA,"bgA")
        buttonImage((479/1280)*win_width,(17/80)*win_height+0.3*xtemp,4*xtemp,2*xtemp,backgroundB,"bgB")
        buttonImage((453/640)*win_width,(17/80)*win_height+0.3*xtemp,4*xtemp,2*xtemp,backgroundC,"bgC")
        buttonImage((53/1280)*win_width,(17/80)*win_height+3.8*xtemp,4*xtemp,2*xtemp,backgroundD,"bgD")
        buttonImage((479/1280)*win_width,(17/80)*win_height+3.8*xtemp,4*xtemp,2*xtemp,setbua,"setbua")
        buttonImage((453/640)*win_width,(17/80)*win_height+3.8*xtemp,4*xtemp,2*xtemp,setskin,"setskin")
        Text_to_screen("2000$",Black,(53/1280)*win_width+2*xtemp,(17/80)*win_height+1.5*xtemp,"medium")
        Text_to_screen("2000$",Black,(479/1280)*win_width+2*xtemp,(17/80)*win_height+1.5*xtemp,"medium")
        Text_to_screen("2000$",Black,(453/640)*win_width+2*xtemp,(17/80)*win_height+1.5*xtemp,"medium")
        Text_to_screen("2000$",Black,(53/1280)*win_width+2*xtemp,(17/80)*win_height+4.7*xtemp,"medium")
        Text_to_screen("1500$",Black,(479/1280)*win_width+2*xtemp,(17/80)*win_height+4.7*xtemp,"medium")
        Text_to_screen("1500$",Black,(453/640)*win_width+2*xtemp,(17/80)*win_height+4.7*xtemp,"medium")
        button("Buy",(53/1280)*win_width+1.8*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy1")
        button("Buy",(53/1280)*win_width+6.5*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy2")
        button("Buy",(53/1280)*win_width+12*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy3")
        button("Buy",(53/1280)*win_width+1.8*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy4")
        button("Buy",(53/1280)*win_width+6.5*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy5")
        button("Buy",(53/1280)*win_width+12*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Yellow,light_yellow,"buy6")
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)

def buy1():
    global back_ground, Money
    Money = Money - 2000
    while val_buy1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Bought",(53/1280)*win_width+1.8*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Use",(53/1280)*win_width+2.8*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use1")
        money(Money)
        pygame.display.update()
        Clock.tick(15)

def buy2():
    global back_ground, Money
    Money = Money - 2000
    while val_buy2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Bought",(53/1280)*win_width+6.5*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Use",(53/1280)*win_width+7.5*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use2")
        money(Money)
        pygame.display.update()
        Clock.tick(15)
def buy3():
    global back_ground, Money
    Money = Money - 2000
    while val_buy3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Bought",(53/1280)*win_width+12*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Use",(53/1280)*win_width+13*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use3")
        money(Money)
        pygame.display.update()
        Clock.tick(15)
def buy4():
    global back_ground, Money
    Money = Money - 2000
    while val_buy4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Use",(53/1280)*win_width+2.8*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use4")
        button("Bought",(53/1280)*win_width+1.8*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        
        money(Money)
        pygame.display.update()
        Clock.tick(15)
def buy5():
    global back_ground, Money
    Money = Money - 1500
    while val_buy5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Bought",(53/1280)*win_width+6.5*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Use",(53/1280)*win_width+7.5*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use5")
        money(Money)
        pygame.display.update()
        Clock.tick(15)
def buy6():
    global back_ground, Money
    Money = Money - 1500
    while val_buy6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Bought",(53/1280)*win_width+12*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Use",(53/1280)*win_width+13*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Blue,light_blue,"use6")
        money(Money)
        pygame.display.update()
        Clock.tick(15)

def use1():
    while val_use1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Used",(53/1280)*win_width+2.8*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)
def use2():
    while val_use2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Used",(53/1280)*win_width+7.5*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)
def use3():
    while val_use3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Used",(53/1280)*win_width+13*xtemp,(17/80)*win_height-0.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)
def use4():
    while val_use4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Used",(53/1280)*win_width+2.8*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)

def use5():
    while val_use5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Used",(53/1280)*win_width+7.5*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)

def use6():
    while val_use6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Used",(53/1280)*win_width+13*xtemp,(17/80)*win_height+3.2*xtemp,xtemp,0.5*xtemp,Red,Red)
        button("Continue",win_width-2*xtemp,win_height/2-4*xtemp,1.5*xtemp,xtemp/2,Yellow,light_yellow,"continue")
        pygame.display.update()
        Clock.tick(15)


# Function choose Screen
def ChooseScreen():
    while screen:
        GameDisplay.fill(White)
        Message_to_screen("Choose the size of window", Green,-100,"large")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Small",80,360,240,160,Blue,light_blue,"smallscreen")
        button("Medium",480,360,240,160,Red,light_red,"mediumscreen")
        button("Large",880,360,240,160,Yellow,light_yellow,"largescreen")

        pygame.display.update()
        Clock.tick(15)

# Function: Game intro
def Game_intro():
    global startgame, play, information, instruction, buttonquit, bg_rank, bg_history, store,Fill
    startgame= pygame.transform.scale(startgame,(win_width,win_height))
    play= pygame.transform.scale(play,(xbutton1,ybutton1))
    information= pygame.transform.scale(information,(xbutton1,ybutton1))
    instruction= pygame.transform.scale(instruction,(xbutton1,ybutton1))
    buttonquit= pygame.transform.scale(buttonquit,(xbutton2,ybutton2))
    bg_rank = pygame.transform.scale(bg_rank,(win_width,win_height))
    bg_history = pygame.transform.scale(bg_history,(win_width,win_height))
    Fill = pygame.transform.scale(Fill,(win_width,win_height))
    store = pygame.transform.scale(store,(xtemp,xtemp))
    GameDisplay.blit(startgame,(0,0))
    pygame.display.update()
    pygame.mixer_music.load("start_end.mp3")
    pygame.mixer_music.play(-1)

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        if mute == False:  
                buttonImage(0,0,xtemp,xtemp,buttonMute,"mute")
        else:
                buttonImage(xtemp,0,xtemp,xtemp,buttonUnMute,"unmute")

        buttonImage(win_width/2-ybutton1/2-xtemp/2,win_height/2,xbutton1,ybutton1,play,"play")
        buttonImage(win_width/2-ybutton1/2-xtemp/2,win_height/2+1.5*xtemp,xbutton1,ybutton1,instruction,"instruction")
        buttonImage(win_width/2-ybutton1/2-xtemp/2,win_height/2+3*xtemp,xbutton1,ybutton1,information,"information")
        buttonImage(win_width-3*xtemp,win_height/2+2*xtemp,xbutton2,ybutton2,buttonquit,"quit")
        pygame.display.update()
        Clock.tick(15)

# Ham intruction
def instruct():
    global guide, amulet
    guide= pygame.transform.scale(guide,(win_width,win_height))
    amulet= pygame.transform.scale(amulet,(win_width,win_height))
    while in_struct1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(guide,(0,0))
        button("Next",win_width-2*xtemp,win_height/2+2*xtemp,xtemp,xtemp/2,Yellow,light_yellow,"next")
        pygame.display.update()
        Clock.tick(15)
    while in_struct2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(amulet,(0,0))
        button("Play",win_width-4*xtemp,win_height/2+xtemp,xtemp,xtemp/2,Yellow,light_yellow,"play")
        button("Back",win_width-4*xtemp,win_height/2+3*xtemp,xtemp,xtemp/2,Red,light_red,"intro")
        pygame.display.update()
        Clock.tick(15)

# Ham button information
def buttonInfor():
    while infor:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        GameDisplay.fill(Orange)
        Message_to_screen("Copyrighted products of team 23 - HCMUS",Red,0,"medium")
        button("Back",xtemp,win_height/2+3*xtemp,xtemp,xtemp/2,Red,light_red,"intro")
        pygame.display.update()
        Clock.tick(15)

def PrepareGameLoop():
    global input_infor
    while prepare:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        signin_all(input_infor, Info_user)
        ChooseSet()
        ChooseBackground()
        ChooseLength()
        ChoosePlayer()
        pygame.display.update()
        Clock.tick(15)

def ChooseBackground():
    GameDisplay.fill(White)
    Message_to_screen("Choose the background", Blue,-1.5*xtemp,"large")
    pygame.display.update()
    background1=pygame.transform.scale(back_ground1,(5*xsizetemp,3*xsizetemp))
    background2= pygame.transform.scale(back_ground2,(5*xsizetemp,3*xsizetemp))
    while Choose_Background:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        buttonImage(win_width/2 + 1.5*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,background1,"background1")
        buttonImage(win_width/2 - 4*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,background2,"background2")

        pygame.display.update()
        Clock.tick(15)

def ChooseSet():
    global Pig, Buff, Pig1, Pig2, Pig3, Pig4, Pig5, Pig6
    global CTT3, hao, chao, hieu1, hieu2, hoa, hien
    while Choose_Set:
        Buff= pygame.transform.scale(Buff,(math.floor(Buff_width),math.floor(Buff_height)))
        for idx in range(0,6,1):
            CTT3[idx]= pygame.transform.scale(CTT3[idx],(math.floor(Player_width),math.floor(Player_height)))
        GameDisplay.fill(light_red)
        Message_to_screen("Choose the type of set", Blue,-1.5*xtemp,"large")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Set member in group",win_width/2- 4*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Green,light_green,"set1")
        button("Set normal - Pig",win_width/2 + 1.5*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Yellow,light_yellow,"set2")

        pygame.display.update()
        Clock.tick(15)
    if MainPlayer == Pig:
        for i in range (6):
            for j in range (3):
                Pig[i][j] = pygame.transform.scale(Pig[i][j],(math.floor(Player_width),math.floor(Player_height)))
        while Choose_number:
            GameDisplay.fill(Orange)
            Message_to_screen("Choose the number of Pig", Blue,-1.5*xtemp,"large")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            button("4",win_width/2 - 6*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Green,light_green,"4")
            button("5",win_width/2 - 1.5*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Yellow,light_yellow,"5")
            button("6",win_width/2 + 3*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Red,light_red,"6")
            pygame.display.update()
            Clock.tick(15)
            
def ChooseLength():
    GameDisplay.fill(White)
    Message_to_screen("Choose the length of road", Blue,-1.5*xtemp,"large")
    pygame.display.update()
    while Choose_Length:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("short",win_width/2 - 6*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Green,light_green,"short")
        button("medium",win_width/2 - 1.5*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Yellow,light_yellow,"medium")
        button("long",win_width/2 + 3*xtemp,win_height/2,5*xsizetemp,3*xsizetemp,Red,light_red,"long")

        pygame.display.update()
        Clock.tick(15)
        
def ChoosePlayer():
    GameDisplay.fill(White)
    Message_to_screen("Choose the player", Blue,-1.5*xtemp,"large")
    pygame.display.update()
    while Choose_Player:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if NumOfPlayer == 4 and MainPlayer == Pig:
            buttonImage(5*xtemp,win_height/2,Player_width,Player_height,Pig1[0],"player1")
            buttonImage(7*xtemp,win_height/2,Player_width,Player_height,Pig2[0],"player2")
            buttonImage(9*xtemp,win_height/2,Player_width,Player_height,Pig3[0],"player3")
            buttonImage(11*xtemp,win_height/2,Player_width,Player_height,Pig4[0],"player4")
        if NumOfPlayer == 5 and MainPlayer == Pig:
            buttonImage(3.5*xtemp,win_height/2,Player_width,Player_height,Pig1[0],"player1")
            buttonImage(5.5*xtemp,win_height/2,Player_width,Player_height,Pig2[0],"player2")
            buttonImage(7.5*xtemp,win_height/2,Player_width,Player_height,Pig3[0],"player3")
            buttonImage(9.5*xtemp,win_height/2,Player_width,Player_height,Pig4[0],"player4")
            buttonImage(11.5*xtemp,win_height/2,Player_width,Player_height,Pig5[0],"player5")
        if NumOfPlayer == 6 and MainPlayer == Pig:
            buttonImage(3*xtemp,win_height/2,Player_width,Player_height,Pig1[0],"player1")
            buttonImage(5*xtemp,win_height/2,Player_width,Player_height,Pig2[0],"player2")
            buttonImage(7*xtemp,win_height/2,Player_width,Player_height,Pig3[0],"player3")
            buttonImage(9*xtemp,win_height/2,Player_width,Player_height,Pig4[0],"player4")
            buttonImage(11*xtemp,win_height/2,Player_width,Player_height,Pig5[0],"player5")
            buttonImage(13*xtemp,win_height/2,Player_width,Player_height,Pig6[0],"player6")
        if MainPlayer == CTT3:
            buttonImage(3*xtemp,win_height/2,Player_width,Player_height,hao,"player1")
            buttonImage(5*xtemp,win_height/2,Player_width,Player_height,chao,"player2")
            buttonImage(7*xtemp,win_height/2,Player_width,Player_height,hieu1,"player3")
            buttonImage(9*xtemp,win_height/2,Player_width,Player_height,hieu2,"player4")
            buttonImage(11*xtemp,win_height/2,Player_width,Player_height,hoa,"player5")
            buttonImage(13*xtemp,win_height/2,Player_width,Player_height,hien,"player6")
        pygame.display.update()
        Clock.tick(15)
def ShowRank():
    while show_rank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(bg_rank,(0,0))
        if MainPlayer == Pig:
            i=0
        if MainPlayer == CTT3:
            i=1 
        if len(rank)==4:
            GameDisplay.blit(player_set[i][rank[0]],(win_width/2.8,xtemp*2))
            GameDisplay.blit(player_set[i][rank[1]],(win_width/2.8,xtemp*3.1))
            GameDisplay.blit(player_set[i][rank[2]],(win_width/2.8,xtemp*4.3))
            GameDisplay.blit(player_set[i][rank[3]],(win_width/2.8,xtemp*5.5))
            Text_to_screen(str(round(time_list[0],3))+"s",Red,win_width/2+xtemp,xtemp*2.3,"medium")
            Text_to_screen(str(round(time_list[1],3))+"s",Red,win_width/2+xtemp,xtemp*3.45,"medium")
            Text_to_screen(str(round(time_list[2],3))+"s",Red,win_width/2+xtemp,xtemp*4.55,"medium")
            Text_to_screen(str(round(time_list[3],3))+"s",Red,win_width/2+xtemp,xtemp*5.73,"medium")
        if len(rank)==5:
            GameDisplay.blit(player_set[i][rank[0]],(win_width/2.8,xtemp*2))
            GameDisplay.blit(player_set[i][rank[1]],(win_width/2.8,xtemp*3.1))
            GameDisplay.blit(player_set[i][rank[2]],(win_width/2.8,xtemp*4.3))
            GameDisplay.blit(player_set[i][rank[3]],(win_width/2.8,xtemp*5.5))
            GameDisplay.blit(player_set[i][rank[4]],(win_width/2.8,xtemp*6.7))
            Text_to_screen(str(round(time_list[0],3))+"s",Red,win_width/2+xtemp,xtemp*2.3,"medium")
            Text_to_screen(str(round(time_list[1],3))+"s",Red,win_width/2+xtemp,xtemp*3.45,"medium")
            Text_to_screen(str(round(time_list[2],3))+"s",Red,win_width/2+xtemp,xtemp*4.55,"medium")
            Text_to_screen(str(round(time_list[3],3))+"s",Red,win_width/2+xtemp,xtemp*5.73,"medium")
            Text_to_screen(str(round(time_list[4],3))+"s",Red,win_width/2+xtemp,xtemp*7,"medium")
        if len(rank)==6:
            GameDisplay.blit(player_set[i][rank[0]],(win_width/2.8,xtemp*2))
            GameDisplay.blit(player_set[i][rank[1]],(win_width/2.8,xtemp*3.1))
            GameDisplay.blit(player_set[i][rank[2]],(win_width/2.8,xtemp*4.3))
            GameDisplay.blit(player_set[i][rank[3]],(win_width/2.8,xtemp*5.5))
            GameDisplay.blit(player_set[i][rank[4]],(win_width/2.8,xtemp*6.7))
            GameDisplay.blit(player_set[i][rank[5]],(win_width/2.8,xtemp*7.85))
            Text_to_screen(str(round(time_list[0],3))+"s",Red,win_width/2+xtemp,xtemp*2.3,"medium")
            Text_to_screen(str(round(time_list[1],3))+"s",Red,win_width/2+xtemp,xtemp*3.45,"medium")
            Text_to_screen(str(round(time_list[2],3))+"s",Red,win_width/2+xtemp,xtemp*4.55,"medium")
            Text_to_screen(str(round(time_list[3],3))+"s",Red,win_width/2+xtemp,xtemp*5.73,"medium")
            Text_to_screen(str(round(time_list[4],3))+"s",Red,win_width/2+xtemp,xtemp*7,"medium")
            Text_to_screen(str(round(time_list[5],3))+"s",Red,win_width/2+xtemp,xtemp*8,"medium")
        button("Next",win_width-2*xtemp,win_height/2+2*xtemp,xtemp,xtemp/2,Yellow,light_yellow,"next_rank")    
        pygame.display.update()
        Clock.tick(15)
def ShowHistory():
    while show_history:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        GameDisplay.blit(bg_history,(0,0))
        for i in range(len(list_history)-1):
            pigscale=pygame.transform.scale(list_history[i][0],(math.floor(60/960*win_height),math.floor(60/960*win_height)))
            GameDisplay.blit(pigscale,(300/960*win_width, 90/540*win_height+53*count_play_time))
            Text_to_screen("Rank: "+str(list_history[i][1]+1),Red,400/960*win_width,104/540*win_height+53*count_play_time,"small")
            Text_to_screen("Time: "+str(list_history[i][2])+"s",Red,510/960*win_width,104/540*win_height+53*count_play_time,"small")
            Text_to_screen("Money: "+str(list_history[i][3])+"$",Red,650/960*win_width,104/540*win_height+53*count_play_time,"small")

        button("Next",win_width-2*xtemp,win_height/2+2*xtemp,xtemp,xtemp/2,Yellow,light_yellow,"next_history")    
        pygame.display.update()
        Clock.tick(15)      
# Function: GameLoop
def GameLoop():
    global Money, itemp, menu, ExitGame, Choose_Length, intro, Choose_Player, a,b,count, start_firework,xtemp,rank,show_rank,show_history, time_list,count_play_time,haha, gameover
    for i in range(6):
        Player_position[i][0]=Width_Start
    Buff_position1_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,2*xtemp+unit]
    Buff_position1_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,2*xtemp+unit] 
    Buff_position2_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,3*xtemp+unit]
    Buff_position2_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,3*xtemp+unit]
    Buff_position3_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,4*xtemp+unit]
    Buff_position3_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,4*xtemp+unit]
    Buff_position4_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,5*xtemp+unit]
    Buff_position4_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,5*xtemp+unit]
    Buff_position5_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,6*xtemp+unit]
    Buff_position5_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,6*xtemp+unit]
    Buff_position6_a = [random.randint(4*xsizetemp,7*xsizetemp)+Width_Start,7*xtemp+unit]
    Buff_position6_b = [random.randint(10*xsizetemp,14*xsizetemp)+Width_Start,7*xtemp+unit]

    SL1 = random.randint(1,100*isShort)
    SL2 = random.randint(1,100*isShort)
    SL3 = random.randint(1,100*isShort)
    SL4 = random.randint(1,100*isShort)
    SL5 = random.randint(1,100*isShort)
    SL6 = random.randint(1,100*isShort)

    a1 = random.randint(1,100)
    a2 = random.randint(1,100)
    a3 = random.randint(1,100)
    a4 = random.randint(1,100)
    a5 = random.randint(1,100)
    a6 = random.randint(1,100)
    b1 = random.randint(1,100)
    b2 = random.randint(1,100)
    b3 = random.randint(1,100) 
    b4 = random.randint(1,100)
    b5 = random.randint(1,100)
    b6 = random.randint(1,100)

    Condition1 = ["False"]
    Condition2 = ["False"]
    Condition3 = ["False"]
    Condition4 = ["False"]
    Condition5 = ["False"]
    Condition6 = ["False"]

    Distance1 = ["False"]
    Distance2 = ["False"]
    Distance3 = ["False"]
    Distance4 = ["False"]
    Distance5 = ["False"]
    Distance6 = ["False"]

    Timestop1 = [0]
    Timestop2 = [0]
    Timestop3 = [0]
    Timestop4 = [0]
    Timestop5 = [0]
    Timestop6 = [0]
    
    random.seed(datetime.now())
    StartRun = False
    GameOver = False
    FindTheWinner = False
    FindTheWinner_ = False
    YouWon = False

    pygame.mixer_music.stop()
    pygame.mixer_music.load("midgame.mp3")
    pygame.mixer_music.play(-1)

    a=[Width_Start,Width_Start,Width_Start,Width_Start,Width_Start,Width_Start]
    b=[90,90,90,90,90,90]
    toFinish =["False","False","False","False","False","False"]
    rank=[]
    time=[]
    history=[]
    start_firework=0
    start_time=0
    time_list=[]
    show_rank=True
    show_history=True
    count_play_time+=1

    while not ExitGame:
        # Vong lap kiem tra Game Over
        while GameOver :
            pygame.mixer_music.stop()
            pygame.mixer_music.load("start_end.mp3")
            pygame.mixer_music.play(-1)
            ShowRank()
            ShowHistory()           
            if YouWon == True:
                GameDisplay.blit(Fill,(0,0))
                Message_to_screen("Congratulation" +str(Info_user[0])+"!! You Won", White, - xtemp, "large")
                Message_to_screen("Press C to Continue or Q to Quit", White, 0, "medium")
            elif Money != 0 and Money >= int(Choice_user[0]):
                GameDisplay.blit(Fill,(0,0))
                Message_to_screen("Better Luck Next Time "+str(Info_user[0])+"!!", White, - xtemp, "large")
                Message_to_screen("Press C to Continue or Q to Quit", White,0, "medium")
            if Money <= 0 or Money< int(Choice_user[0]):
                gameover= pygame.transform.scale(gameover,(win_width,win_height))
                GameDisplay.blit(gameover,(0,0))
                Message_to_screen("Game over", Black, -2*xtemp, "large")
                Message_to_screen("Press R to Restart game or Q to Quit", Black,-xtemp, "medium")             
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOver = False
                    ExitGame = True
                if event.type == pygame.KEYDOWN and Money >= int(Choice_user[0]):
                    if event.key == pygame.K_c:
                        ExitGame = True
                        GameOver = False
                        Choose_Length = True
                        Choose_Player= True
                        ChooseLength()
                        ChoosePlayer()
                    if event.key == pygame.K_q:
                        ExitGame = True
                        GameOver = False
                if event.type == pygame.KEYDOWN and (Money == 0 or Money< int(Choice_user[0])):
                    if event.key == pygame.K_r:
                        ExitGame = True
                        GameOver = False
                        Money = 1000
                        intro=True
                        Game_intro()
                    if event.key == pygame.K_q:
                        ExitGame = True
                        GameOver = False
        # Cac phim tuong tac trong game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitGame = True
            # Nhan phim Space de bat dau choi
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_time = pygame.time.get_ticks()
                    StartRun = True
                # Nhan p de pause game
                if event.key == pygame.K_p:
                    pause()
        
        # Hien thi bua, background, hinh anh player va tien
        draw_background(back_ground,Width_Start,Width_Finish) 
        draw_player(Player_position,NumOfPlayer,MainPlayer)
        money(Money)
        # Hien thi nut menu tren man hinh
        button("Menu",win_width-xtemp,0,xtemp,0.5*xtemp,Red,light_red,"menu")
        menu = True

        # Dieu kien chuyen dong cua player
        if StartRun:
           if NumOfPlayer == 4:
                Dichuyen(Player_position[0],Buff_position1_a,Buff_position1_b,Condition1,Distance1,Timestop1,SL1,a1,b1)
                Dichuyen(Player_position[1],Buff_position2_a,Buff_position2_b,Condition2,Distance2,Timestop2,SL2,a2,b2)
                Dichuyen(Player_position[2],Buff_position3_a,Buff_position3_b,Condition3,Distance3,Timestop3,SL3,a3,b3)
                Dichuyen(Player_position[3],Buff_position4_a,Buff_position4_b,Condition4,Distance4,Timestop4,SL4,a4,b4)
           if NumOfPlayer == 5:
                Dichuyen(Player_position[0],Buff_position1_a,Buff_position1_b,Condition1,Distance1,Timestop1,SL1,a1,b1)
                Dichuyen(Player_position[1],Buff_position2_a,Buff_position2_b,Condition2,Distance2,Timestop2,SL2,a2,b2)
                Dichuyen(Player_position[2],Buff_position3_a,Buff_position3_b,Condition3,Distance3,Timestop3,SL3,a3,b3)
                Dichuyen(Player_position[3],Buff_position4_a,Buff_position4_b,Condition4,Distance4,Timestop4,SL4,a4,b4)
                Dichuyen(Player_position[4],Buff_position5_a,Buff_position5_b,Condition5,Distance5,Timestop5,SL5,a5,b5)
           if NumOfPlayer == 6:
                Dichuyen(Player_position[0],Buff_position1_a,Buff_position1_b,Condition1,Distance1,Timestop1,SL1,a1,b1)
                Dichuyen(Player_position[1],Buff_position2_a,Buff_position2_b,Condition2,Distance2,Timestop2,SL2,a2,b2)
                Dichuyen(Player_position[2],Buff_position3_a,Buff_position3_b,Condition3,Distance3,Timestop3,SL3,a3,b3)
                Dichuyen(Player_position[3],Buff_position4_a,Buff_position4_b,Condition4,Distance4,Timestop4,SL4,a4,b4)
                Dichuyen(Player_position[4],Buff_position5_a,Buff_position5_b,Condition5,Distance5,Timestop5,SL5,a5,b5)
                Dichuyen(Player_position[5],Buff_position6_a,Buff_position6_b,Condition6,Distance6,Timestop6,SL6,a6,b6)
        else: 
            Message_to_screen("Press Space to start game!",Red,0,"large")
        if FindTheWinner_ == True:
            draw_firework(Player_position[itemp])
        pygame.display.update()

        # Thay doi hinh anh dong ve dich cua bot ve dich dau tien
        if FindTheWinner_ == False:  
            for i in range(NumOfPlayer):
                if (Player_position[i][0] == Width_Finish ):
                    start_firework = pygame.time.get_ticks()
                    FindTheWinner_ = True
                    itemp = i
                    pygame.display.update()
        #Kiểm tra người thắng và xử lý scores
        if FindTheWinner == False: 
            for i in range(NumOfPlayer):
                if (Player_position[i][0] == Width_Finish ):
                    FindTheWinner = True
                    time_list.append((pygame.time.get_ticks() - start_time)/1000)
                    rank.append(i)
                break
        # Kiem tra dieu kien dung cua game
        i=1
        for idx in range(1,NumOfPlayer,1):
                if(Player_position[idx][0]== Width_Finish):
                    if toFinish[idx]=='False':
                        time_list.append((pygame.time.get_ticks() - start_time)/1000)
                        rank.append(idx)
                        toFinish[idx]=True
                    i+=1        
        # Nếu số lượng Player về đích bằng số người chơi thì game ket thuc   
        if i == NumOfPlayer and count-start_firework>5000:
            if rank[0] == PlayerChoose - 1:
                YouWon = True
                Money = Money + int(Choice_user[0])                                
            else:
                YouWon = False 
                Money = Money - int(Choice_user[0])
                
            if count_play_time == 9:
                count_play_time= 0
                
            for i in range (0,NumOfPlayer,1):
                if MainPlayer == Pig:
                    a=0
                if MainPlayer == CTT3:
                    a=1
                if rank[i]== (PlayerChoose-1):
                    history.append(player_set[a][PlayerChoose-1])
                    history.append(i)
                    history.append(time_list[i])
                    history.append(Money)
            list_history.append(history)
            StartRun = False
            GameOver = True
            for idx in range(0,NumOfPlayer,1):
                Player_position[idx][0] = xtemp/3
        pygame.display.update()
        # Tuy chinh toc do tro choi
        Clock.tick(FPS)

    pygame.quit()
    quit()

ChooseScreen()
	    



