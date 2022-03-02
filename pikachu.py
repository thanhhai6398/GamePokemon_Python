
from typing import no_type_check, no_type_check_decorator
import pygame,sys
from pygame.display import update
from pygame.locals import *
import pygame.sprite
from pygame.version import PygameVersion
import random
from random import *
from pygame import mixer

mixer.init()
pygame.font.init()
pygame.init()

form = pygame.display.set_mode((800,600))
pygame.display.set_caption("PIKACHU")
music = pygame.mixer.music.load("./music_1.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.queue("./tinhyeumauhong.mp3")

white = (255,255,255,128)
black = (0,0,0)
navyxanh = (0 , 50 , 65)
xanh_blue = (47,79,79)
timer = pygame.time.Clock()
diem = 0

#thiết kế form tạo form chào mừng.
class form_welcom:
    def __init__(self):
        
        self.background_welcom = pygame.image.load("./background_welcom2.jpeg")
        self.background_welcom = pygame.transform.scale(self.background_welcom , (800,600))
        form.blit(self.background_welcom,(0,0))

        self.khung = pygame.Surface((800,200))
        self.khung.set_alpha(200)
        self.khung.fill((255,255,255))
        form.blit(self.khung,(0,200))

        self.text_form = pygame.font.SysFont("Times New Roman" , 70)
        welcom_text = self.text_form.render("Welcom to our project" , True , (0,50,65))
        form.blit(welcom_text , [70,260])

        pygame.draw.line(form , (54,54,54) , (0,200) , (800,200) , 10)
        pygame.draw.line(form , (54,54,54) , (0,400) , (800,400) , 10)

        self.logo_hcmute = pygame.image.load("./logo.png")
        self.logo_hcmute = pygame.transform.scale(self.logo_hcmute , (100,128))
        form.blit(self.logo_hcmute , [10,10])

        pygame.draw.line(form , (152,208,185) , (150,80) , (780,80) , 5)

        self.text_logo = pygame.font.SysFont("Times New Roman" , 20)
        self.text_logo_ = pygame.font.SysFont("Times New Roman" , 28)
        self.text_logo1 = self.text_logo.render("TRƯỜNG ĐẠI HỌC" , True , (175,215,136))
        self.text_logo2 = self.text_logo_.render("SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH" , True , (0,50,65))
        self.text_logo3 = self.text_logo.render("HCMC University of Technology and Education" , True , (0,0,0) )

        form.blit(self.text_logo1 , [150,25])
        form.blit(self.text_logo2 , [150,50])
        form.blit(self.text_logo3 , [150,90])

        pygame.draw.rect(form , (100,0,22) , (0 , 490 , 800 , 60) )

        self.text_thongbao = pygame.font.SysFont("Comic Sans MS" , 30)
        text_start = self.text_thongbao.render("ENTER to Start - ESC to exit" , True , (255,255,255))
        self.surface = pygame.Surface(text_start.get_size())
        self.surface.fill((100,0,22))
        self.surface.set_colorkey((100,0,22))
        self.surface.blit(text_start , (0,0))
        self.thoigian_thaydoi = 0
        self.alpha = 0
        

    def chinhthoigian_nhapnhay(self):
        pygame.display.set_caption("Welcom Team 7's Project Python")
        self.alpha = abs(int(255 - self.thoigian_thaydoi))
        if self.thoigian_thaydoi > 255*2:
            self.thoigian_thaydoi = 0
        self.thoigian_thaydoi += 5

    def ve_text(self):
        self.surface.set_alpha(self.alpha)
        form.blit(self.surface , (200,500))
        
    


#thiết kế form giới thiệu nhóm:
class form_nhom:

    def __init__(self):

        

        self.background_nhom = pygame.image.load("./background2.jpg")
        self.background_nhom = pygame.transform.scale(self.background_nhom,(1210,690))
        self.text_form = pygame.font.SysFont("Arial" , 35)
        self.text_form1 = pygame.font.SysFont("Comic Sans MS" , 30)
        self.text_form2 = pygame.font.SysFont("Comic Sans MS" , 40)
        self.avatar = pygame.image.load("./avatar.jpg")
        self.avatar = pygame.transform.scale(self.avatar , (190,300))
        self.hai_avatar = pygame.image.load("./hai_avartar.jpg")
        self.hai_avatar = pygame.transform.scale(self.hai_avatar , (190,300))
        self.nhi_avatar = pygame.image.load("./nhi_avartar.jpg")
        self.nhi_avatar = pygame.transform.scale(self.nhi_avatar , (190,300))
        self.loc_avatar = pygame.image.load("./loc_avartar.jpg")
        self.loc_avatar = pygame.transform.scale(self.loc_avatar , (190,300))
        self.thao_avatar = pygame.image.load("./thao_avartar.jpg")
        self.thao_avatar = pygame.transform.scale(self.thao_avatar , (190,300))
        self.nhan_avatar = pygame.image.load("./nhan_avartar.jpg")
        self.nhan_avatar = pygame.transform.scale(self.nhan_avatar , (190,300))
        self.linh_avatar = pygame.image.load("./linh_avatar.jpg")
        self.linh_avatar = pygame.transform.scale(self.linh_avatar , (190,300))

        self.text_ten = pygame.font.SysFont("Times New Roman" , 17)
        
        self.text_thongbao = pygame.font.SysFont("Comic Sans MS" , 30)
        text_start = self.text_thongbao.render("ENTER to Play - ESC to exit" , True , (255,255,255))
        self.surface = pygame.Surface(text_start.get_size())
        self.surface.fill((10,70,65))
        self.surface.set_colorkey((10,70,65))
        self.surface.blit(text_start , (0,0))
        self.thoigian_thaydoi = 0
        self.alpha = 0

    def ve(self):

        pygame.display.set_caption("INTRODUCION TEAM 7")
        form = pygame.display.set_mode((1210,690))
        form.blit(self.background_nhom , (0,0))
        tenmonhoc = self.text_form.render("Introduction to Python Programming Course for Analysis" , True , (200,191,127))
        tendetai = self.text_form1.render("Project Winform Application - Game Pikachu" , True , (255,255,255))
        tennhom = self.text_form2.render("Team 7" , True , (54,117,23))

        s = pygame.Surface((1210,690))
        s.set_alpha(200)
        s.fill((0,0,0))

        form.blit(s,(0,0))
        
        form.blit(tenmonhoc , (240,5))
        form.blit(tendetai , (280 , 50))
        form.blit(tennhom , (540,530))

        form.blit(self.hai_avatar , (10,150))
        form.blit(self.linh_avatar , (210,150))
        form.blit(self.loc_avatar , (410,150))
        form.blit(self.nhan_avatar , (610,150))
        form.blit(self.nhi_avatar , (810,150))
        form.blit(self.thao_avatar , (1010,150))

        hai = self.text_ten.render("Nguyễn Huỳnh Thanh Hải" , True , (255,255,255))
        hai_mssv = self.text_ten.render("19110355" , True , (255,255,255))
        
        linh = self.text_ten.render("Lê Nguyễn Thế Linh" , True , (255,255,255))
        linh_mssv = self.text_ten.render("19110389" , True , (255,255,255))

        loc = self.text_ten.render("Phạm Nguyễn Quang Lộc" , True , (255,255,255))
        loc_mssv = self.text_ten.render("19110393" , True , (255,255,255))

        nhan = self.text_ten.render("Nguyễn Hữu Thiện Nhân" , True , (255,255,255))
        nhan_mssv = self.text_ten.render("19110415" , True , (255,255,255))

        nhi = self.text_ten.render("Lê Thị Thanh Nhi" , True , (255,255,255))
        nhi_mssv = self.text_ten.render("19110420" , True , (255,255,255))

        thao = self.text_ten.render("Nguyễn Thị Thu Thảo" , True , (255,255,255))
        thao_mssv = self.text_ten.render("19110460" , True , (255,255,255))

        ngaybd = self.text_ten.render("Date Start Project: 26/3/2021" , True , ((255,255,255)))
        form.blit(ngaybd , (0,670))
        ngayht = self.text_ten.render("Date Complete Project: 12/5/2021" , True , ((255,255,255)))
        form.blit(ngayht , (970,670))

        form.blit(hai,(10,460))
        form.blit(hai_mssv , (10,480))
        form.blit(linh,(210,460))
        form.blit(linh_mssv , (210,480))
        form.blit(loc,(410,460))
        form.blit(loc_mssv , (410,480))
        form.blit(nhan,(610,460))
        form.blit(nhan_mssv , (610,480))

        form.blit(nhi,(810,460))
        form.blit(nhi_mssv , (810,480))

        form.blit(thao,(1010,460))
        form.blit(thao_mssv , (1010,480))

        pygame.draw.rect(form , (0,70,65) , (0,600 , 1210 , 50))
        

    def chinhthoigian_nhapnhay(self):
        self.alpha = abs(int(255 - self.thoigian_thaydoi))
        if self.thoigian_thaydoi > 255*2:
            self.thoigian_thaydoi = 0
        self.thoigian_thaydoi += 5

    def ve_text(self):
        
        self.surface.set_alpha(self.alpha)
        form.blit(self.surface , (400,600))


class form_trangchu():
    def __init__(self):

        self.background_trangchu = pygame.image.load("background_trangchu.png")
        self.background_trangchu = pygame.transform.scale(self.background_trangchu , (800,600))
        self.text_tieude = pygame.font.SysFont("Comic Sans MS" , 30)
        self.logo_tieude = pygame.image.load("./logo_trangchu.png")
        self.logo_tieude = pygame.transform.scale(self.logo_tieude , (200 , 70))
        self.text_menu = pygame.image.load("./text_menu.png")
        self.music = pygame.image.load("./music.png")
        self.music = pygame.transform.scale(self.music , (50,50))
        self.play_game = pygame.image.load("./play_game.png")
        self.play_game = pygame.transform.scale(self.play_game , (50,50))
        self.direct = pygame.image.load("./direct.png")
        self.direct = pygame.transform.scale(self.direct , (50,50))
        self.exit = pygame.image.load("./exit.png")
        self.exit = pygame.transform.scale(self.exit , (50,50))

        self.pikachu = pygame.image.load("./pikachu.png")
        self.pikachu = pygame.transform.scale(self.pikachu , (200,300))
        self.pikachu1 = pygame.image.load("./pikachu1.png")
        self.pikachu1 = pygame.transform.scale(self.pikachu1 , (200,300))



        text_play = self.text_tieude.render("Play Game" , (True) , (139,0,22))
        #form.blit(text_play , (350 , 300))
        text_music = self.text_tieude.render("Play Music" , (True) , (139,0,22))
        #form.blit(text_music , (350 , 360))
        text_direction = self.text_tieude.render("Show Direction" , (True) , (139,0,22))
        #form.blit(text_direction , (310 , 420))
        text_exit = self.text_tieude.render("Exit Game" , (True) , (139,0,22))
        #form.blit(text_exit , (350 , 480))

        self.surface_play = pygame.Surface(text_play.get_size())
        self.surface_play.fill((255,255,255))
        self.surface_play.set_colorkey((10,70,65))
        self.surface_play.blit(text_play , (0,0))

        self.surface_music = pygame.Surface(text_music.get_size())
        self.surface_music.fill((255,255,255))
        self.surface_music.set_colorkey((10,70,65))
        self.surface_music.blit(text_music , (0,0))

        self.surface_direction = pygame.Surface(text_direction.get_size())
        self.surface_direction.fill((255,255,255))
        self.surface_direction.set_colorkey((10,70,65))
        self.surface_direction.blit(text_direction , (0,0))
        
        self.surface_exit = pygame.Surface(text_exit.get_size())
        self.surface_exit.fill((255,255,255))
        self.surface_exit.set_colorkey((10,70,65))
        self.surface_exit.blit(text_exit , (0,0))

        self.thoigian_thaydoi = 0
        self.alpha = 0

        self.background_music = pygame.image.load("./background_music.jpg")
        self.background_music = pygame.transform.scale(self.background_music , (400,400))


        
    def ve(self):
        form = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Menu")
        
        s = pygame.Surface((400,50))
        s.set_alpha(255)
        s.fill((255,255,255))

        form.blit(self.background_trangchu , (0,0))
        form.blit(self.logo_tieude , (0,10))
        form.blit(self.text_menu , (250,100))
        form.blit(s,(200,300))
        form.blit(self.play_game , (200 , 300))
        form.blit(s,(200,360))
        form.blit(self.music , (200,360))
        form.blit(s,(200,420))
        form.blit(self.direct , (200,420))
        form.blit(s,(200,480))
        form.blit(self.exit , (200,480))

        form.blit(self.pikachu , (590 , 10))
        form.blit(self.pikachu1 , (10 , 300))

    def chinhthoigian_nhapnhay(self):
        self.alpha = abs(int(255 - self.thoigian_thaydoi))
        if self.thoigian_thaydoi > 255*2:
            self.thoigian_thaydoi = 0
        self.thoigian_thaydoi += 10

    def ve_text(self):
        
        self.surface_play.set_alpha(self.alpha)
        self.surface_music.set_alpha(self.alpha)
        self.surface_direction.set_alpha(self.alpha)
        self.surface_exit.set_alpha(self.alpha)

        form.blit(self.surface_play , (350,300))
        form.blit(self.surface_music ,(350,360))
        form.blit(self.surface_direction ,(310,420))
        form.blit(self.surface_exit ,(350,480))
    
    
#form music
class form_music:
    def __init__(self):
        self.background_music = pygame.image.load("./background_music.jpg")
        self.background_music = pygame.transform.scale(self.background_music , (600,400))
        self.logo_music = pygame.image.load("./logo_music.png")
        self.change_music = pygame.image.load("./doi_music.png")
        self.change_music = pygame.transform.scale(self.change_music , (100,100))
        self.power_music = pygame.image.load("./power_music.png")
        self.power_music = pygame.transform.scale(self.power_music , (70,70))
        self.text = pygame.font.SysFont("Comic Sans MS" , 20)
        
        

    def ve(self):

        pygame.display.set_caption("Music")
        form.blit(self.background_music , (100,100))
        form.blit(self.logo_music  , (210 , 80))
        pygame.draw.rect(form,(100,0,0),(150,240,400,50))
        form.blit(self.change_music , (100 , 220))
        pygame.draw.rect(form,(100,0,0),(150,340,400,50))
        form.blit(self.power_music , (130,330))

        text_change_music = self.text.render("Change Play Music" , True , (255,255,255))
        text_power_music = self.text.render("Power Off Music" , True , (255,255,255))

        form.blit(text_change_music , (250,250))
        form.blit(text_power_music , (250,350))
        

class form_list_music:
    def __init__(self):
        self.background_list_music = pygame.image.load("./background_list_music.jpg")
        self.background_list_music = pygame.transform.scale(self.background_list_music , (600,400))
        self.music_hinh = pygame.image.load("./music_list_hinh.png")
        self.music_hinh = pygame.transform.scale(self.music_hinh , (100,100))
        self.music_list = pygame.Surface((400,50))
        self.music_list.set_alpha(128)
        self.music_list.fill((255,255,255))
        self.text = pygame.font.SysFont("Times New Roman" , 30)

    def ve(self):
        pygame.display.set_caption("Choose Music To List")
        form.blit(self.background_list_music,(100,100))
        self.background_list_music.blit(self.music_hinh , (0,0))
        text_1 = self.text.render("1" , True , (255,255,255))
        self.background_list_music.blit(text_1 , (40,30))
        text_music_1 = self.text.render("Chỉ là không cùng nhau" , True , (255,255,255))
        self.background_list_music.blit(text_music_1,(100,40))

        self.background_list_music.blit(self.music_hinh ,(0,100))
        text_2 = self.text.render("2" , True , (255,255,255))
        self.background_list_music.blit(text_2 , (40,130))
        text_music_1 = self.text.render("Khác biệt to lớn" , True , (255,255,255))
        self.background_list_music.blit(text_music_1,(100,140))

        self.background_list_music.blit(self.music_hinh ,(0,200))
        text_2 = self.text.render("3" , True , (255,255,255))
        self.background_list_music.blit(text_2 , (40,230))
        text_music_1 = self.text.render("Phải chăng em đã yêu" , True , (255,255,255))
        self.background_list_music.blit(text_music_1,(100,240))

        self.background_list_music.blit(self.music_hinh ,(0,300))
        text_2 = self.text.render("4" , True , (255,255,255))
        self.background_list_music.blit(text_2 , (40,330))
        text_music_1 = self.text.render("Sài Gòn đau lòng quá" , True , (255,255,255))
        self.background_list_music.blit(text_music_1,(100,340))


#form hướng dẫn
class form_direction:
    def __init__(self):
        self.back_ground = pygame.image.load("./direction_background.png")
    def ve(self):
        
        form = pygame.display.set_mode((900,600))
        pygame.display.set_caption("Direction our game")
        form.blit(self.back_ground,(0,0))



class form_exit:
    def __init__(self):
        self.background_text = pygame.image.load("./exit_form.png")
        self.text = pygame.font.SysFont("Comic Sans MS" , 50)
        self.exit_background = pygame.image.load("./exit_background.png")
        self.exit_background = pygame.transform.scale(self.exit_background , (900,300))
        

    def ve(self):
        pygame.display.set_caption("Exit")
        form = pygame.display.set_mode((900,300))
        form.blit(self.exit_background ,(0,0))
        form.blit(self.background_text,(50,50))
        pygame.draw.rect(form,(77,25,53) , (200,150,200,70))
        pygame.draw.rect(form,(255,255,255) , (200,150,200,70),5)
        yes = self.text.render("YES"  , True , (255,255,255))
        no = self.text.render("NO"  , True , (255,255,255))
        form.blit(yes,(250,150))

        pygame.draw.rect(form,(77,25,53) , (450,150,200,70))
        pygame.draw.rect(form,(255,255,255) , (450,150,200,70),5)
        form.blit(no,(500,150))
        
list_background_play_game = []
background_play_game1 = pygame.image.load("./beutiful1.jpg")
background_play_game1 = pygame.transform.scale(background_play_game1,(900,600))
list_background_play_game.append(background_play_game1)
background_play_game2 = pygame.image.load("./beutiful2.jpg")
background_play_game2= pygame.transform.scale(background_play_game2,(900,600))
list_background_play_game.append(background_play_game2)
background_play_game3 = pygame.image.load("./beutiful3.jpg")
background_play_game3 = pygame.transform.scale(background_play_game3,(900,600))
list_background_play_game.append(background_play_game3)
background_play_game5 = pygame.image.load("./beutiful5.jpg")
background_play_game5 = pygame.transform.scale(background_play_game5,(900,600))
list_background_play_game.append(background_play_game5)
background_play_game6 = pygame.image.load("./beutiful6.jpg")
background_play_game6 = pygame.transform.scale(background_play_game6,(900,600))
list_background_play_game.append(background_play_game6)
background_play_game = choice(list_background_play_game)

po1 = pygame.image.load("./1.jpg")
po2 = pygame.image.load("./2.jpg")
po3 = pygame.image.load("./3.jpg")
po4 = pygame.image.load("./4.jpg")
po5 = pygame.image.load("./5.jpg")
po6 = pygame.image.load("./6.jpg")
po7 = pygame.image.load("./7.jpg")
po8 = pygame.image.load("./8.jpg")
po9 = pygame.image.load("./9.jpg")
po10 = pygame.image.load("./10.jpg")

po0 = pygame.Surface((50,50))
po0.set_alpha(0)
po0.fill((255,255,255))


list_pokemon = (po1,po2,po3,po4,po5,po6,po7,po8,po9,po10)

background_1 = pygame.image.load("./form_4_1.jpg")
background_2 = pygame.image.load("./form_4_2.jpg")
background_3 = pygame.image.load("./form_4_3.jpg")
background_4 = pygame.image.load("./form_4_4.jpg")
background_5 = pygame.image.load("./form_4_5.jpg")
background_6 = pygame.image.load("./form_4_6.jpg")
background_7 = pygame.image.load("./form_4_7.jpg")
background_8 = pygame.image.load("./form_4_8.jpg")
background_9 = pygame.image.load("./form_4_9.jpg")
background_10 = pygame.image.load("./form_4_10.jpg")    

background_1 = pygame.transform.scale(background_1,(800,400))
background_2 = pygame.transform.scale(background_2,(800,400))
background_3 = pygame.transform.scale(background_3,(800,400))
background_4 = pygame.transform.scale(background_4,(800,400))
background_5 = pygame.transform.scale(background_5,(800,400))
background_6 = pygame.transform.scale(background_6,(800,400))
background_7 = pygame.transform.scale(background_7,(800,400))
background_8 = pygame.transform.scale(background_8,(800,400))
background_9 = pygame.transform.scale(background_9,(800,400))
background_10 = pygame.transform.scale(background_10,(800,400))

list_background = [background_1,background_2,background_3,background_4,background_5,background_6,background_7,background_8,background_9,background_10]
background_play = choice(list_background)

diem_hinh = pygame.image.load("./diem.png")


list_1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6] ; shuffle(list_1)
list_2 = [7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2]; shuffle(list_2)
list_3 = [3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8] ; shuffle(list_3)
list_4 = [9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4] ; shuffle(list_4)
list_5 = [5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10] ; shuffle(list_5)
list_6 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6] ; shuffle(list_6)
list_7 = [7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2] ; shuffle(list_7)
list_8 = [3,4,5,6,7,8,9,10,1,1,2,2,3,3,4,4] ; shuffle(list_8)

list_giatri_hinh = [list_1,list_2,list_3 , list_4 , list_5 , list_6 , list_7 , list_8]
L = [list_1,list_2,list_3 , list_4 , list_5 , list_6 , list_7 , list_8]
shuffle(list_giatri_hinh)

def doichieu_hinh(vitri):
            if vitri == 1:
                return po1
            elif vitri == 2:
                return po2
            elif vitri == 3:
                return po3
            elif vitri == 4:
                return po4
            elif vitri == 5:
                return po5
            elif vitri == 6:
                return po6
            elif vitri == 7:
                return po7
            elif vitri == 8:
                return po8
            elif vitri == 9:
                return po9
            elif vitri == 10:
                return po10
            elif vitri == 0:
                return po0

list_toado_hinh1 = []
list_toado_hinh2 = []
list_toado_hinh3 = []
list_toado_hinh4 = []
list_toado_hinh5 = []
list_toado_hinh6 = []
list_toado_hinh7 = []
list_toado_hinh8 = []

loai = 0
def ve_hinh():

    toado1 = 50 
    for cot in list_giatri_hinh[0]:
        form.blit(doichieu_hinh(cot) , (toado1,150))
        list_toado_hinh1.append((toado1,150))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[1]:
        form.blit(doichieu_hinh(cot) , (toado1,200))
        list_toado_hinh2.append((toado1,200))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[2]:
        form.blit(doichieu_hinh(cot) , (toado1,250))
        list_toado_hinh3.append((toado1,250))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[3]:
        form.blit(doichieu_hinh(cot) , (toado1,300))
        list_toado_hinh4.append((toado1,300))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[4]:
        form.blit(doichieu_hinh(cot) , (toado1,350))
        list_toado_hinh5.append((toado1,350))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[5]:
        form.blit(doichieu_hinh(cot) , (toado1,400))
        list_toado_hinh6.append((toado1,400))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[6]:
        form.blit(doichieu_hinh(cot) , (toado1,450))
        list_toado_hinh7.append((toado1,450))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[7]:
        form.blit(doichieu_hinh(cot) , (toado1,500))
        list_toado_hinh8.append((toado1,500))
        toado1 += 50
    
list_toado_hinh = [list_toado_hinh1 , list_toado_hinh2 , list_toado_hinh3 , list_toado_hinh4, list_toado_hinh5, list_toado_hinh6, list_toado_hinh7, list_toado_hinh8]

def toa_do_anh_mo(pos):

    i = 50
    dem = 0
    while i <= 800:
        if pos[0] >= i and pos[1] >= 150 and pos[0] <= i+50 and pos[1] <= 200:
            dem += 1
            return (i,150)
        elif pos[0] >= i and pos[1] >= 200 and pos[0] <= i+50 and pos[1] <= 250:
            dem += 1
            return (i,200)
        elif pos[0] >= i and pos[1] >= 250 and pos[0] <= i+50 and pos[1] <= 300:
            dem += 1
            return (i,250)
        elif pos[0] >= i and pos[1] >= 300 and pos[0] <= i+50 and pos[1] <= 350:
            dem += 1
            return (i,300)
        elif pos[0] >= i and pos[1] >= 350 and pos[0] <= i+50 and pos[1] <= 400:
            dem += 1
            return (i,350)
        elif pos[0] >= i and pos[1] >= 400 and pos[0] <= i+50 and pos[1] <= 450:
            dem += 1
            return (i,400)
        elif pos[0] >= i and pos[1] >= 450 and pos[0] <= i+50 and pos[1] <= 500:
            dem += 1
            return (i,450)
        elif pos[0] >= i and pos[1] >= 500 and pos[0] <= i+50 and pos[1] <= 550:
            dem += 1
            return (i,500)
        else:
            i += 50
    if dem == 0:
        return (-100,-100)

def ve_anh_mo(pos):
        s = pygame.Surface((50,50))
        s.set_alpha(128)
        s.fill((255,255,255))

        form.blit(s,toa_do_anh_mo(pos))
    
def laygiatri_hinh(pos):
    dem = 0
    toado1 = toa_do_anh_mo(pos)
    for hang in range(0,8):
        for cot in range(0,16):
            if list_toado_hinh[hang][cot] == toado1:
                dem += 1
                return list_giatri_hinh[hang][cot]
                break
    if dem == 0:
        return -1

def kiemtra_thongnhau(chon_1 , chon_2):
    if toa_do_anh_mo(chon_1) != toa_do_anh_mo(chon_2):
        if laygiatri_hinh(chon_1) == laygiatri_hinh(chon_2):
            return True
    else:
        return False

def kiemtra_namtronglist(pos):
    if toa_do_anh_mo(pos) in list_toado_hinh:
        return True
    else:
        return False

def kiem_tra_la_duong_vien(point_1):

    giatri_trave = False
    kiemtra_dung = 0
    for hang in range(0,8):
        dem = 0
        if list_toado_hinh[hang][15] == point_1 or list_toado_hinh[hang][0] == point_1:
            giatri_trave = True
            kiemtra_dung += 1
            break
        
    if kiemtra_dung == 0:
        giatri_trave = False
    
    return giatri_trave

def kiem_tra_la_duong_vien2(point_1):
    dem = 0
    giatri_trave = False
    for cot in range(0,16):
        if list_toado_hinh[0][cot] == point_1 or list_toado_hinh[7][cot] == point_1:
            dem += 1
            giatri_trave = True
            break
    if dem == 0:
       giatri_trave = False 
    
    return giatri_trave

def cungnam_hangngang(chon_1 , chon_2):

    giatri_trave = False

    if toa_do_anh_mo(chon_1)[1] == toa_do_anh_mo(chon_2)[1] and toa_do_anh_mo(chon_1)[0] != toa_do_anh_mo(chon_2)[0]:
        point_trai = toa_do_anh_mo(chon_1)
        point_phai = toa_do_anh_mo(chon_2)

        if toa_do_anh_mo(chon_1)[0] > toa_do_anh_mo(chon_2)[0]:
            point_trai = toa_do_anh_mo(chon_2)
            point_phai = toa_do_anh_mo(chon_1)

        for hang in range(0,8):
            for cot in range(0,16):
                if list_toado_hinh[hang][cot] == point_trai:
                    vitri_trai = (hang,cot)
                if list_toado_hinh[hang][cot] == point_phai:
                    vitri_phai = (hang,cot)
        #nó nằm ngoài bìa
        if kiem_tra_la_duong_vien2(point_trai) == True and kiem_tra_la_duong_vien2(point_phai) == True:
            giatri_trave = True

        #nó nằm kế bên nhau
        elif point_trai[0] + 50 == point_phai[0]:
            giatri_trave = True
        else:
            kiemtra_dung = 0

            #đường ở giữa
            if list_giatri_hinh[vitri_trai[0]][vitri_trai[1]+1] == 0:

                dem = 0
                for cot in range(vitri_trai[1]+1 , vitri_phai[1],1):
                    hang = vitri_trai[0]
                    if list_giatri_hinh[hang][cot] != 0:
                        dem += 1
                        break
                    
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1

            #đường ở dưới
            if vitri_trai[0]+1 <= 7 and list_giatri_hinh[vitri_trai[0]+1][vitri_trai[1]] == 0:
                
                dem = 0
                for cot in range(vitri_trai[1] , vitri_phai[1],1):
                    hang = vitri_trai[0]+1
                    if list_giatri_hinh[hang][cot] != 0:
                        dem += 1
                        break
                    
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
                    
            #đường ở trên
            if vitri_trai[0]-1 >= 0 and list_giatri_hinh[vitri_trai[0]-1][vitri_trai[1]] == 0:
                
                dem = 0
                for cot in range(vitri_trai[1] , vitri_phai[1],1):
                    hang = vitri_trai[0]-1
                    if list_giatri_hinh[hang][cot] != 0:
                        dem += 1
                        break
                    
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
            
            if kiemtra_dung == 0:
                giatri_trave = False
            
    else:
        giatri_trave = False
    
    return giatri_trave

def cungnam_hangdoc(chon_1 , chon_2):
    giatri_trave = False
    if toa_do_anh_mo(chon_1)[0] == toa_do_anh_mo(chon_2)[0] and toa_do_anh_mo(chon_1)[1] != toa_do_anh_mo(chon_2)[1]:
        point_tren = toa_do_anh_mo(chon_1)
        point_duoi = toa_do_anh_mo(chon_2)

        if toa_do_anh_mo(chon_1)[1] > toa_do_anh_mo(chon_2)[1]:
            point_tren = toa_do_anh_mo(chon_2)
            point_duoi = toa_do_anh_mo(chon_1)

        for hang in range(0,8):
            for cot in range(0,16):
                if list_toado_hinh[hang][cot] == point_tren:
                    vitri_tren = (hang,cot)
                if list_toado_hinh[hang][cot] == point_duoi:
                    vitri_duoi = (hang,cot)

        hang_tren = vitri_tren[0]
        cot_tren = vitri_tren[1]
        hang_duoi = vitri_duoi[0]
        cot_duoi = vitri_duoi[1]
            
        if kiem_tra_la_duong_vien(point_tren) == True and kiem_tra_la_duong_vien(point_duoi) == True:
            giatri_trave = True
        elif point_tren[1] + 50 == point_duoi[1]:
            giatri_trave = True
        else:
            dem = 0
            kiemtra_dung = 0

            #ở giữa
            if list_giatri_hinh[hang_tren+1][cot_tren] == 0:
                hang = hang_tren+1
                while hang <= hang_duoi-1:
                    if list_giatri_hinh[hang][cot_tren] != 0:
                        dem += 0
                        break
                    hang += 1
            
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
        
            #bên phải
            if cot_tren < 15 and list_giatri_hinh[hang_tren][cot_tren+1] == 0:
                hang = hang_tren
                while hang <= hang_duoi:
                    if list_giatri_hinh[hang][cot_tren+1] != 0:
                        dem += 1
                        break
                    hang += 1
                
                
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
            
            #bên trái
            if cot_tren > 0 and list_giatri_hinh[hang_tren][cot_tren-1] == 0:
                hang = hang_tren
                while hang <= hang_duoi:
                    if list_giatri_hinh[hang][cot_tren-1] != 0:
                        dem += 1
                        break
                    hang += 1

                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
            
            if kiemtra_dung == 0:
                giatri_trave = False

    else:
        giatri_trave = False
    
    return giatri_trave

#trên dưới
def nam_xeo_trai(chon_1,chon_2):

    giatri_trave = False
    kiemtra_dung = 0
    if (toa_do_anh_mo(chon_1)[0] < toa_do_anh_mo(chon_2)[0] and toa_do_anh_mo(chon_1)[1] < toa_do_anh_mo(chon_2)[1]) or (toa_do_anh_mo(chon_2)[0] < toa_do_anh_mo(chon_1)[0] and toa_do_anh_mo(chon_2)[1] < toa_do_anh_mo(chon_1)[1]): 

        point_tren_trai = toa_do_anh_mo(chon_1)
        point_duoi_phai = toa_do_anh_mo(chon_2)

        if toa_do_anh_mo(chon_2)[0] < toa_do_anh_mo(chon_1)[0] and toa_do_anh_mo(chon_2)[1] < toa_do_anh_mo(chon_1)[1]: 
            point_tren_trai = toa_do_anh_mo(chon_2)
            point_duoi_phai = toa_do_anh_mo(chon_1)
            
        for hang in range(0,8):
                for cot in range(0,16):
                    if list_toado_hinh[hang][cot] == point_tren_trai:
                        vitri_tren_trai = (hang,cot)
                    if list_toado_hinh[hang][cot] == point_duoi_phai:
                        vitri_duoi_phai = (hang,cot)

        hang_tren = vitri_tren_trai[0]
        cot_tren = vitri_tren_trai[1]
        hang_duoi = vitri_duoi_phai[0]
        cot_duoi = vitri_duoi_phai[1]

        if list_giatri_hinh[hang_tren][cot_duoi] == 0:
            dem = 0
            cot = cot_tren+1
            while cot <= cot_duoi:
                if list_giatri_hinh[hang_tren][cot] != 0:
                    dem += 1
                    break
                cot += 1
            hang = hang_tren + 1
            while hang <= hang_duoi-1:
                if list_giatri_hinh[hang][cot_duoi] != 0:
                    dem += 1
                    break
                hang += 1

            
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
            print (1)
        if list_giatri_hinh[hang_duoi][cot_tren] == 0:
            dem = 0
            hang = hang_tren+1
            while hang <= hang_duoi:
                if list_giatri_hinh[hang][cot_tren] != 0:
                    dem += 1
                    break
                hang += 1
            cot = cot_tren
            while cot <= cot_duoi-1:
                if list_giatri_hinh[hang_duoi][cot] != 0:
                    dem += 1
                    break
                cot += 1
                
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1

            print(2)
        
        if hang_tren == 0:
            dem = 0
            hang = hang_duoi-1
            while hang >= 0:
                if list_giatri_hinh[hang][cot_duoi] != 0:
                    dem += 1
                    break
                hang -= 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1

        if hang_duoi == 7:
            dem = 0
            hang = hang_tren-1
            while hang <= 7:
                if list_giatri_hinh[hang][cot_tren] != 0:
                    dem += 1
                    break
                hang += 1
            
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        
        if cot_tren == 0:
            dem = 0
            cot = cot_duoi-1
            while cot >= 0:
                if list_giatri_hinh[hang_duoi][cot] != 0:
                    dem += 1
                    break
                cot -= 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        
        if cot_duoi == 15:
            dem = 0
            cot = cot_tren+1
            while cot <= 15:
                if list_giatri_hinh[hang_tren][cot] != 0:
                    dem +=1
                    break
                cot += 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        if hang_tren > 0 and list_giatri_hinh[hang_tren-1][cot_tren] == 0:
            if list_giatri_hinh[hang_tren-1][cot_duoi] == 0:
                dem = 0
                cot = cot_tren
                while cot <= cot_duoi:
                    if list_giatri_hinh[hang_tren-1][cot] != 0:
                        dem += 1
                        break
                    cot += 1
                hang = hang_duoi-1
                while hang >= hang_tren-1:
                    if list_giatri_hinh[hang][cot_duoi] != 0:
                        dem += 1
                        break
                    hang -= 1
                
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
        
        if cot_tren > 0 and list_giatri_hinh[hang_tren][cot_tren-1] == 0:
            if list_giatri_hinh[hang_duoi][cot_tren-1] == 0:
                dem = 0
                hang = hang_tren
                while hang <= hang_duoi:
                    if list_giatri_hinh[hang][cot_tren-1] != 0:
                        dem += 1
                        break
                    hang += 1
                cot = cot_duoi-1
                while cot <= cot_tren-1:
                    if list_giatri_hinh[hang_duoi][cot] != 0:
                        dem += 1
                        break
                    cot -= 1
                
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1

        if hang_duoi < 7 and list_giatri_hinh[hang_tren+1][cot_tren] == 0:
            if list_giatri_hinh[hang_duoi+1][cot_tren] == 0:
                dem = 0
                hang = hang_tren+1
                while hang <= hang_duoi+1:
                    if list_giatri_hinh[hang][cot_tren] != 0:
                        dem += 0
                        break
                    hang += 1
                cot = cot_duoi-1
                while cot <= cot_tren:
                    if list_giatri_hinh[hang_duoi+1][cot] != 0:
                        break
                    cot += 1
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
        if cot_duoi < 15 and list_giatri_hinh[hang_tren][cot_tren+1] == 0:
            if list_giatri_hinh[hang_tren][cot_duoi+1] == 0:
                dem += 0
                cot = cot_tren+1
                while cot <= cot_duoi + 1:
                    if list_giatri_hinh[hang_tren][cot] != 0:
                        dem += 0
                        break
                    cot += 1
                hang = hang_duoi
                while hang >= hang_tren:
                    if list_giatri_hinh[hang][cot_duoi+1] != 0:
                        dem += 1
                        break
                    hang -= 1
                
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1

                
        if kiemtra_dung == 0:
            giatri_trave = False
        else:
            giatri_trave = True
        
    else:
        giatri_trave = False
    
    return giatri_trave

def nam_xeo_phai(chon_1 , chon_2):

    giatri_trave = False
    kiemtra_dung = 0
    if (toa_do_anh_mo(chon_1)[0] < toa_do_anh_mo(chon_2)[0] and toa_do_anh_mo(chon_1)[1] > toa_do_anh_mo(chon_2)[1]) or (toa_do_anh_mo(chon_2)[0] < toa_do_anh_mo(chon_1)[0] and toa_do_anh_mo(chon_2)[1] > toa_do_anh_mo(chon_1)[1]): 

        point_tren_phai = toa_do_anh_mo(chon_2)
        point_duoi_trai = toa_do_anh_mo(chon_1)

        if toa_do_anh_mo(chon_2)[0] < toa_do_anh_mo(chon_1)[0] and toa_do_anh_mo(chon_2)[1] > toa_do_anh_mo(chon_1)[1]: 
            point_tren_phai = toa_do_anh_mo(chon_1)
            point_duoi_trai = toa_do_anh_mo(chon_2)
            
        for hang in range(0,8):
                for cot in range(0,16):
                    if list_toado_hinh[hang][cot] == point_tren_phai:
                        vitri_tren_phai = (hang,cot)
                    if list_toado_hinh[hang][cot] == point_duoi_trai:
                        vitri_duoi_trai = (hang,cot)

        hang_tren = vitri_tren_phai[0]
        cot_tren = vitri_tren_phai[1]
        hang_duoi = vitri_duoi_trai[0]
        cot_duoi = vitri_duoi_trai[1]

        if list_giatri_hinh[hang_tren][cot_duoi] == 0:
            dem = 0
            hang = hang_duoi-1
            while hang >= hang_tren:
                if list_giatri_hinh[hang][cot_duoi] != 0:
                    dem += 1
                    break
                hang -= 1
            cot = cot_tren-1
            while cot >= cot_duoi:
                if list_giatri_hinh[hang_tren][cot] != 0:
                    dem += 1
                    break
                cot -= 1

            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
            
            
        
        if list_giatri_hinh[hang_duoi][cot_tren] == 0:
            dem = 0
            cot = cot_duoi+1
            while cot <= cot_tren:
                if list_giatri_hinh[hang_duoi][cot] != 0:
                    dem += 1
                    break
                cot += 1
            hang = hang_tren+1
            while hang <= hang_duoi:
                if list_giatri_hinh[hang][cot_tren] != 0:
                    dem += 1
                    break
                hang += 1
            
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
            
            
        
        if hang_duoi < 7 and list_giatri_hinh[hang_duoi+1][cot_duoi] == 0:
            if list_giatri_hinh[hang_duoi+1][cot_tren] == 0:
                dem = 0
                cot = cot_duoi
                while cot <= cot_tren:
                    if list_giatri_hinh[hang_duoi+1][cot] != 0:
                        dem += 1
                        break
                    cot += 1
                hang = hang_tren-1
                while hang <= hang_duoi+1:
                    if list_giatri_hinh[hang][cot_tren] != 0:
                        dem += 1
                        break
                    hang += 1
                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
                
        if cot_duoi > 0 and list_giatri_hinh[hang_duoi][cot_duoi-1] == 0:
            if list_giatri_hinh[hang_tren][cot_duoi-1] == 0:
                dem = 0
                hang = hang_duoi
                while hang >= hang_tren:
                    if list_giatri_hinh[hang][cot_duoi-1] != 0:
                        dem += 1
                        break
                    hang -= 1
                cot = cot_tren-1
                while cot >= cot_duoi-1:
                    if list_giatri_hinh[hang_tren][cot] != 0:
                        dem += 1
                        break
                    cot -= 1

                if dem == 0:
                    giatri_trave = True
                    kiemtra_dung += 1
        

        
        if hang_duoi == 7:
            dem = 0
            hang = hang_tren-1
            while hang <= 7:
                if list_giatri_hinh[hang][cot_tren] != 0:
                    dem += 1
                    break
                hang += 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        
        if cot_duoi == 0:
            dem = 0
            cot = cot_tren-1
            while cot >= 0:
                if list_giatri_hinh[hang_tren][cot] != 0:
                    dem += 1
                    break
                cot -= 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        if hang_tren == 0:
            dem = 0
            hang = hang_duoi-1
            while hang >= 0:
                if list_giatri_hinh[hang][cot_duoi] != 0:
                    dem += 1
                    break
                hang -= 1
            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        if cot_tren == 15:
            dem = 0
            cot = cot_duoi + 1
            while cot <= 15:
                if list_giatri_hinh[hang_duoi][cot] != 0:
                    dem += 1
                    break
                cot += 1

            if dem == 0:
                giatri_trave = True
                kiemtra_dung += 1
        
        if kiemtra_dung == 0:
            giatri_trave = False
        else:
            giatri_trave = True
    else:
        giatri_trave = False
    return giatri_trave

def ve_lai_hinhanh():

    form.blit(background_play , (50,150))

    toado1 = 50 
    for cot in list_giatri_hinh[0]:
        form.blit(doichieu_hinh(cot) , (toado1,150))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[1]:
        form.blit(doichieu_hinh(cot) , (toado1,200))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[2]:
        form.blit(doichieu_hinh(cot) , (toado1,250))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[3]:
        form.blit(doichieu_hinh(cot) , (toado1,300))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[4]:
        form.blit(doichieu_hinh(cot) , (toado1,350))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[5]:
        form.blit(doichieu_hinh(cot) , (toado1,400))
        toado1 += 50
    toado1 = 50 

    for cot in list_giatri_hinh[6]:
        form.blit(doichieu_hinh(cot) , (toado1,450))
        toado1 += 50
    toado1 = 50 
    for cot in list_giatri_hinh[7]:
        form.blit(doichieu_hinh(cot) , (toado1,500))
        toado1 += 50
    
def thaythegiatri_hinh(chon_1 , chon_2):
    point1 = toa_do_anh_mo(chon_1)
    point2 = toa_do_anh_mo(chon_2)

    for hang in range(0,8):
        for cot in range(0,16):
            if list_toado_hinh[hang][cot] == point1:
                list_giatri_hinh[hang][cot] = 0
            if list_toado_hinh[hang][cot] == point2:
                list_giatri_hinh[hang][cot] = 0

def demso0():
    s0 = list_giatri_hinh[0].count(0)
    s1 = list_giatri_hinh[1].count(0)
    s2 = list_giatri_hinh[2].count(0)
    s3 = list_giatri_hinh[3].count(0)
    s4 = list_giatri_hinh[4].count(0)
    s5 = list_giatri_hinh[5].count(0)
    s6 = list_giatri_hinh[6].count(0)
    s7 = list_giatri_hinh[7].count(0)

    tong = s0+s1+s2+s3+s4+s5+s6+s7
    return tong
def kiemtraxem_hople(chon_1 , chon_2):
    
    global loai
    global diem
    if kiemtra_thongnhau(chon_1 , chon_2) == True:
        if cungnam_hangdoc(chon_1,chon_2) == True:
            thaythegiatri_hinh(chon_1,chon_2)
            if demso0() <= 126 and (demso0()  == loai+2):
                diem += 5
                loai = demso0()

        if cungnam_hangngang(chon_1 , chon_2) == True:
            thaythegiatri_hinh(chon_1,chon_2)
            if demso0() <= 126 and (demso0()  == loai+2):
                diem += 5
                loai = demso0()
            
        if nam_xeo_trai(chon_1 , chon_2) == True:
            thaythegiatri_hinh(chon_1,chon_2)
            if demso0() < 126 and (demso0()  == loai+2):
                diem += 5
                loai = demso0()

            
        if nam_xeo_phai(chon_1 , chon_2) == True:
            thaythegiatri_hinh(chon_1,chon_2)
            if demso0() < 126 and (demso0()  == loai+2):
                diem += 5
                loai = demso0()

        
            
    else:
        ve_lai_hinhanh()
#click chuột đầu tiên
chon_1 = None
#độ dài thanh thởi gian
time_x = 550
#chiều rộng của thanh thời gian
time_y = 20

def ve_thoigian(time_x,time_y):
    pygame.draw.rect(form,navyxanh,(20,50,550,20))
    time = pygame.image.load("time.png")
    time = pygame.transform.scale(time,(100,100))
    time_clock = pygame.draw.rect(form,(12,255,12),(20,50,time_x,time_y))
    form.blit(time,(10,10))

def tinh_diem(diem):

    score_text = pygame.image.load("./score.png")
    text_score = pygame.font.SysFont("Comic Sans MS" , 70)
    score = text_score.render(str(diem) , True , (255,255,255))
    form.blit(score_text,(550,10))
    form.blit(score,(780,5))
def ve_tinh_nang():
    trangchu = pygame.image.load("./trangchu.png")
    trangchu = pygame.transform.scale(trangchu,(50,50))
    form.blit(trangchu,(100,80))
    text = pygame.font.SysFont("Comic Sans MS" , 40)
    trangchu_text = text.render("Menu" , True , (255,255,255))
    form.blit(trangchu_text,(150,80))

    thoat = pygame.image.load("./thoat.png")
    thoat = pygame.transform.scale(thoat,(50,50))
    form.blit(thoat , (300,80))
    text_thoat = text.render("Exit" , True , (255,255,255))
    form.blit(text_thoat,(350,80))

    lammoi = pygame.image.load("./refresh.png")
    lammoi = pygame.transform.scale(lammoi,(50,50))
    form.blit(lammoi,(450,80))
    text_lammoi = text.render("Refresh" , True , (255,255,255))
    form.blit(text_lammoi,(500,80))

def kiem_tra_thang(time_x):

    #global list_giatri_hinh

    s0 = list_giatri_hinh[0].count(0)
    s1 = list_giatri_hinh[1].count(0)
    s2 = list_giatri_hinh[2].count(0)
    s3 = list_giatri_hinh[3].count(0)
    s4 = list_giatri_hinh[4].count(0)
    s5 = list_giatri_hinh[5].count(0)
    s6 = list_giatri_hinh[6].count(0)
    s7 = list_giatri_hinh[7].count(0)

    tong = s0+s1+s2+s3+s4+s5+s6+s7
    if tong == 128 and time_x > 0:
        win = pygame.image.load("./win.png")
        form.blit(win,(90,100))
        
        return True
    else:
        return False
def kiem_tra_thua(time_x):

    #global list_giatri_hinh

    s0 = list_giatri_hinh[0].count(0)
    s1 = list_giatri_hinh[1].count(0)
    s2 = list_giatri_hinh[2].count(0)
    s3 = list_giatri_hinh[3].count(0)
    s4 = list_giatri_hinh[4].count(0)
    s5 = list_giatri_hinh[5].count(0)
    s6 = list_giatri_hinh[6].count(0)
    s7 = list_giatri_hinh[7].count(0)

    tong = s0+s1+s2+s3+s4+s5+s6+s7
    
    if tong < 128 and time_x < 0:
        fail = pygame.image.load("./fail.png")
        form.blit(fail,(90,100))
        
        return True
    else:
        return False
def form5_play():
    form = pygame.display.set_mode((900,600))
    form.fill(navyxanh)        
    trangchu = pygame.image.load("./trangchu.png")
    trangchu = pygame.transform.scale(trangchu,(200,200))
    form.blit(trangchu,(150,250))
    text = pygame.font.SysFont("Comic Sans MS" , 50)
    trangchu_text = text.render("Menu" , True , (255,255,255))
    form.blit(trangchu_text,(180,440))

    thoat = pygame.image.load("./thoat.png")
    thoat = pygame.transform.scale(thoat,(200,200))
    form.blit(thoat , (540,250))
    text_thoat = text.render("Exit" , True , (255,255,255))
    form.blit(text_thoat,(580,440))



class form_play_game:
    def __init__(self):
        self.logo_play = pygame.image.load("./logo_play.png")
        self.logo_play = pygame.transform.scale(self.logo_play,(400,400))

    def ve_background(self):
        form = pygame.display.set_mode((900,600))
        form.blit(background_play_game , (0,0))
        form.blit(self.logo_play , (240,100))
    def ve_background_play(self):
        form.fill(navyxanh)
    

#tình trạng của form
class Form:
    def __init__(self):
        self.form1 = True #form chào mừng - form 1
        self.form2 = False #form giới thiệu nhóm - form 2
        self.form3 = False #Form trang chủ - form 3
        self.form4 = False #Form chính play -  trò chơi - form 4
        self.music_form = False #Form chọn âm nhạc
        self.list_music_form = False
        self.direction_form = False  #Form xem hướng dẫn
        self.exit_form = False
        self.form5 = False

        self.text_start_  = form_welcom()
        self.text_start_play = form_nhom()
        self.trangchu = form_trangchu()
        self.music = form_music()
        self.list_music = form_list_music()
        self.direction = form_direction()
        self.exit = form_exit()
        self.form_play = form_play_game()
        
def run_game():

    
    play = False
    cuaso = Form()

    #vòng lặp form chào mừng

    while cuaso.form1 == True:

        pygame.draw.rect(form , (100,0,22) , (0 , 490 , 800 , 60))
        cuaso.text_start_.chinhthoigian_nhapnhay()
        cuaso.text_start_.ve_text()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #nhấn enter để sang trang mới
            if event.type == KEYDOWN and event.key in (13,271):
                cuaso.form1 = False
                cuaso.form2 = True
            
            elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                #code thêm có chắc muốn thoát
        
    
        timer.tick(60)
        pygame.display.update()

    while cuaso.form2 == True and cuaso.form1 == False:

        cuaso.text_start_play.ve()
        cuaso.text_start_play.chinhthoigian_nhapnhay()
        cuaso.text_start_play.ve_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #nhấn enter để sang trang mới
            if event.type == KEYDOWN and event.key in (13,271):
                condition = True
                cuaso.form2 = False
                cuaso.form3 = True
            
            elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                #code thêm có chắc muốn thoát
        
        timer.tick(60)
        pygame.display.update()
    
    while True:

        
        while cuaso.form3 == True:
                
                cuaso.trangchu.ve()
                cuaso.trangchu.chinhthoigian_nhapnhay()
                cuaso.trangchu.ve_text()
                mouse_x = 0
                mouse_y = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x  , mouse_y = pygame.mouse.get_pos()
                
                #sang chế độ play - game
                if mouse_x >= 200 and mouse_y >= 300 and mouse_x <= 600 and mouse_y <= 350:
                    play = True
                   
                    condition = True
                    cuaso.form3 = False

                #chế độ music
                elif mouse_x >= 200 and mouse_y >= 360 and mouse_x <= 600 and mouse_y <= 410:

                    s = pygame.Surface((800,600))
                    s.set_alpha(128)
                    s.fill((107,142,35))

                    form.blit(s,(0,0))

                    cuaso.form3 = False
                    cuaso.music_form = True

                #chế độ hướng dẫn
                elif mouse_x >= 200 and mouse_y >= 420 and mouse_x <= 600 and mouse_y <= 470:
                    cuaso.form3 = False
                    cuaso.direction_form = True
                
                #chế độ thoát
                elif mouse_x >= 200 and mouse_y >= 480 and mouse_x <= 600 and mouse_y <= 530:
                    cuaso.form3 = False
                    cuaso.exit_form = True
                    
                
                timer.tick(60)
                pygame.display.update()

        
        while cuaso.music_form == True:
            
                cuaso.music.ve()
                mouse_x = 0
                mouse_y = 0

                first_2 = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x  , mouse_y = pygame.mouse.get_pos()
                
                    
                if mouse_x >= 150 and mouse_y >= 240 and mouse_x <= 550 and mouse_y <= 290:
                        cuaso.list_music_form =True
                        cuaso.music_form = False
                elif mouse_x >= 150 and mouse_y >= 340 and mouse_x <= 550 and mouse_y <= 390:
                        pygame.mixer.music.stop()
                        cuaso.music_form = False
                        cuaso.form3 = True
               

                timer.tick(60)
                pygame.display.update()
            
        while cuaso.list_music_form == True:

                cuaso.list_music.ve()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x  , mouse_y = pygame.mouse.get_pos()

                if mouse_x >= 100 and mouse_y >=100 and mouse_x <= 200 and mouse_y <= 200:
                    pygame.draw.rect(form,(255,255,255) , (100,100,100,100))
                    music = pygame.mixer.music.load("./chilakhongcungnhau.mp3")
                    pygame.mixer.music.play(-1)
                    cuaso.form3 = True
                    cuaso.list_music_form = False
                elif mouse_x >= 100 and mouse_y >= 200 and mouse_x <= 200 and mouse_y <= 300:
                    music = pygame.mixer.music.load("./khacbiettolon.mp3")
                    pygame.draw.rect(form,(255,255,255) , (100,100,100,100))
                    pygame.mixer.music.play(-1)
                    cuaso.form3 = True
                    cuaso.list_music_form = False
                elif mouse_x >= 100 and mouse_y >= 300 and mouse_x <= 200 and mouse_y <= 400:
                    pygame.mixer.music.load("./phaichangemdayeu.mp3")
                    pygame.mixer.music.play(-1)
                    cuaso.form3 = True
                    cuaso.list_music_form = False
                elif mouse_x >= 100 and mouse_y >= 400 and mouse_x <= 200 and mouse_y <= 500:
                    pygame.mixer.music.load("./saigondaulongqua.mp3")
                    pygame.mixer.music.play(-1)
                    cuaso.form3 = True
                    cuaso.list_music_form = False

                

                timer.tick(60)
                pygame.display.update()

        while cuaso.direction_form == True:
                cuaso.direction.ve()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x  , mouse_y = pygame.mouse.get_pos()

                if mouse_x >= 700 and mouse_y >= 500 and mouse_x <= 900 and mouse_y <= 600:
                    cuaso.form3 = True
                    cuaso.direction_form = False 
                
                timer.tick(60)
                pygame.display.update()
            
        while cuaso.exit_form == True:

                cuaso.exit.ve()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x  , mouse_y = pygame.mouse.get_pos()
                
                if mouse_x >= 200 and mouse_y >= 150 and mouse_x <= 400 and mouse_y <= 220:
                    pygame.quit()
                    sys.exit()
                    
                elif mouse_x >= 450 and mouse_y >= 150 and mouse_x <= 650 and mouse_y <= 220:
                    cuaso.form3 = True
                    cuaso.exit_form = False
                
                timer.tick(60)
                pygame.display.update()

        thanh_bar_x = 800
        thanh_bar_y = 10

        while play == True:
            cuaso.form_play.ve_background()
            pygame.draw.rect(form,(247,255,0),(50,500,thanh_bar_x,thanh_bar_y))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_click = True
                        pos = pygame.mouse.get_pos()
            thanh_bar_x-=1

            if thanh_bar_x < 0:
                play = False
                cuaso.form4 = True
            
            timer.tick(60)
            pygame.display.update()
            



        if cuaso.form4 == True:
                cuaso.form_play.ve_background()
                cuaso.form_play.ve_background_play()
                ve_hinh()

        chon_1 = None
        time_x = 550
        time_y = 20

        
        while cuaso.form4 == True:
                global diem
                global list_giatri_hinh
                ve_thoigian(time_x,time_y)
                pygame.draw.rect(form,navyxanh,(750,20,200,70))
                tinh_diem(diem)
                ve_tinh_nang()
                mouse_click = False
                pos = None

                chon_2 = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_click = True
                        pos = pygame.mouse.get_pos()
                if pos != None:
                    #button menu
                    if pos[0] >= 100 and pos[1] >= 80 and pos[0] <= 150 and pos[1] <= 130 and mouse_click == True:
                        
                        cuaso.form3 = True
                        cuaso.form4 = False
                    #button Exit
                    elif pos[0] >= 300 and pos[1] >= 80 and pos[0] <= 350 and pos[1] <= 130 and mouse_click == True:
                        
                        pygame.quit()
                        sys.exit()
                        condition = False
                    #button Làm mới
                    elif pos[0] >= 450 and pos[1] >= 80 and pos[0] <= 550 and pos[1] <= 130 and mouse_click == True:
                        
                        shuffle(list_giatri_hinh)
                        ve_lai_hinhanh()
                
            
                if chon_1 == None and mouse_click == True:
            
                    
                        chon_1 = pos
                        s = pygame.Surface((50,50))
                        s.set_alpha(128)
                        s.fill((255,255,255))

                        form.blit(s,toa_do_anh_mo(chon_1))
                elif chon_1 != None and mouse_click == True:
                    
                        chon_2 = pos
                        s = pygame.Surface((50,50))
                        s.set_alpha(128)
                        s.fill((255,255,255))

                        form.blit(s,toa_do_anh_mo(chon_2))

                if chon_1 != None and chon_2!=None:
                    kiemtraxem_hople(chon_1 , chon_2)
                    ve_lai_hinhanh()
                    
                    chon_1 = None
                    chon_2 = None
                

                    
                time_x -= 0.1
                time_y = 20
                
                if kiem_tra_thang(time_x) == True:
                    cuaso.form4 = False
                    cuaso.form5 = True
                if kiem_tra_thua(time_x) == True:
                    cuaso.form4 = False
                    cuaso.form5 = True
                    
                timer.tick(60)
                pygame.display.update()

        while cuaso.form5 == True:
            
            form5_play()
            a = kiem_tra_thang(time_x)
            b = kiem_tra_thua(time_x)

            pos = None

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_click = True
                        pos = pygame.mouse.get_pos()
            if pos != None:
                if pos[0] >= 150 and pos[1] >= 250 and pos[0] <= 350 and pos[1] <= 450:
                    pygame.draw.rect(form,(255,255,255) , (150,250,200,200) , 4 )
                    cuaso.form3 = True
                    
                    cuaso.form5 = False

                elif pos[0] >= 540 and pos[1] >= 250 and pos[0] <= 740 and pos[1] <= 450:
                    pygame.draw.rect(form,(255,255,255) , (550,250,200,200) , 4)
                    cuaso.form5 =False
                    cuaso.exit_form = True
                    
            list_giatri_hinh = L
            timer.tick(60)
            pygame.display.update()

            
        pygame.display.update()
            
run_game()
