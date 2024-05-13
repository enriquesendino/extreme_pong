import pygame, sys
from random import randint,choices, choice

#Variables
screen_width = 1000
screen_height= 700
ball_size = 30 
cursor_width = 10
cursor_height = 140
jugador_score = 0
opponent_score = 0
counter =0
lista_pelotas = []
list_choices = [-7,-6,-5,-4,-3,3,4,5,6,7]

#General setup
pygame.init()
game_font= pygame.font.Font("freesansbold.ttf", 50)
game_font_big = pygame.font.Font("freesansbold.ttf", 100)
game_font_giant = pygame.font.Font("freesansbold.ttf", 120)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
sonido_punto = pygame.mixer.Sound("punto.wav")
sonido_golpe = pygame.mixer.Sound("golpe.wav")
click_golpe = pygame.mixer.Sound("click.mp3")

class Block:
    def __init__(self,pos_x,pos_y,tam_x,tam_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tam_x = tam_x
        self.tam_y = tam_y    
        self.block = pygame.Rect(self.pos_x,self.pos_y,self.tam_x,self.tam_y)        
    
class Moviles(Block):
    def __init__(self,pos_x,pos_y,tam_x,tam_y,speed_x,speed_y):
        super().__init__(pos_x,pos_y,tam_x,tam_y)
        self.speed_x =speed_x
        self.speed_y= speed_y
        self.timer= 0
        self.momento_muerte = 0
        self.pausa = False
        
        
        
                
    def salir_pantalla(self):        
        if self.pos_y <= 0:
            self.speed_y *=-1            
        if self.pos_y >= screen_height-self.tam_y:
            self.speed_y *=-1
        pygame.draw.ellipse(screen,(255,255,255),self.block)
        
        self.timer =pygame.time.get_ticks()
        #print("timer", self.timer - self.momento_muerte)

        
        
        self.mover()

    def salir_pantalla_jugadores(self):
        if self.pos_y <= 0:
            self.pos_y = 0
        if self.pos_y >= screen_height-self.tam_y:
            self.pos_y = screen_height-self.tam_y
        pygame.draw.rect(screen,(255,255,255),self.block)
        self.timer=3000         
        self.mover()
       
    def mover(self):
        if self.timer - self.momento_muerte < 3000 or self.pausa == True:
            pygame.draw.ellipse(screen,(170,170,170),self.block)
            pygame.draw.rect(screen,(255,255,255),jugador.block)
            pygame.draw.rect(screen,(255,255,255),oponente.block)
        else:
            for x in range(game_manager.pelotas_max):
                if  not lista_pelotas[x].block.colliderect(oponente.block):
                    if self.speed_x <= -12:
                        self.speed_x = -12
                    if self.speed_x >= 12:
                        self.speed_x = 12
                if  not lista_pelotas[x].block.colliderect(oponente.block):
                    if self.speed_x <= -12:
                        self.speed_x = -12
                    if self.speed_x >= 12:
                        self.speed_x = 12
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
        self.block= pygame.Rect(self.pos_x,self.pos_y,self.tam_x,self.tam_y)

class Menuitems(Block):
    def __init__ (self,pos_x,pos_y,tam_x,tam_y,texto,tipo_texto):
        super().__init__(pos_x,pos_y,tam_x,tam_y)
        self.tipo_texto =tipo_texto
        self.texto = texto
        self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))
        self.rectangulo = self.textito.get_rect(topleft =(self.pos_x,self.pos_y))
        screen.blit(self.textito,(self.pos_x,self.pos_y))
    
    def mostrar_opciones(self):
        if event.type== pygame.MOUSEMOTION:
            if self.rectangulo.collidepoint(event.pos):
                pygame.draw.ellipse(screen,(163,151,234),self.rectangulo)
                self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))                
                
            else:
                self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))
        else:
            self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))
        screen.blit(self.textito,(self.pos_x,self.pos_y))
        
    
    
    def mostrar_pulsables(self):
        
                     
                        
        if event.type== pygame.MOUSEMOTION:
            
            if self.rectangulo.collidepoint(event.pos):
                self.textito = self.tipo_texto.render(f"{self.texto}",True,(170,170,170))
                
                
            else:
                self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))
        else:
            self.textito = self.tipo_texto.render(f"{self.texto}",True,(255,255,255))

            
        screen.blit(self.textito,(self.pos_x,self.pos_y))
            
class Manager():
    def __init__(self,jugador_score = 0,opponent_score = 0,counter = 0) -> None:
          self.jugador_score =jugador_score
          self.opponent_score =opponent_score
          self.game_active = False
          self.settings_active =False
          self.uno_dos_jugador = True
          self.pelotas_max = 3
          self.score_max = 5            

    def colision(self):
        for x in range(game_manager.pelotas_max):
            inc_vel_max = 1.3
            inc_vel_min = 0.9
            inc_vel_maxy = 5
            inc_vel_miny= 0          
                
            if lista_pelotas[x].block.colliderect(jugador.block):
                sonido_golpe.play()    
                if lista_pelotas[x].block.y >= screen_height or lista_pelotas[x].block.y <=0:
                    lista_pelotas[x].speed_y *= -1
                if lista_pelotas[x].block.colliderect(jugador.block)and lista_pelotas[x].speed_x>0:                                            
                    if abs(lista_pelotas[x].block.bottom-jugador.block.top) < 10 and lista_pelotas[x].speed_y > 0:
                        lista_pelotas[x].speed_x *= -2
                    elif abs(lista_pelotas[x].block.top-jugador.block.bottom) < 10 and lista_pelotas[x].speed_y < 10:
                        lista_pelotas[x].speed_x *= -2
                    elif abs(lista_pelotas[x].block.right-jugador.block.left)<10:
                        pos_choque = lista_pelotas[x].pos_y + (ball_size/2)-jugador.pos_y              
                        dis_c =abs(pos_choque-(cursor_height/2))
                        dis_c_prop = dis_c/(cursor_height/2) 
                        variacion = dis_c_prop * (inc_vel_max-inc_vel_min)
                        variacion_y= dis_c_prop *(inc_vel_maxy - inc_vel_miny)
                        inc_vel_dosy = inc_vel_miny + variacion_y
                        inc_vel_dos = inc_vel_min + variacion
                        inc_vel = inc_vel_min + ((abs(pos_choque-(cursor_height/2))/(cursor_height/2)) * (inc_vel_max-inc_vel_min))
                        inc_vel_y =inc_vel_miny +((abs(pos_choque-(cursor_height/2))/(cursor_height/2)) *(inc_vel_maxy-inc_vel_miny))
                        lista_pelotas[x].speed_x *= - inc_vel
                        if pos_choque > 70:  
                            lista_pelotas[x].speed_y = inc_vel_y
                        else:
                            lista_pelotas[x].speed_y = -inc_vel_y    
                        
            if self.uno_dos_jugador == True:

                if lista_pelotas[x].block.colliderect(oponente.block)and lista_pelotas[x].speed_x<0:
                    sonido_golpe.play()
                    if abs(lista_pelotas[x].block.bottom-jugador.block.top) > 10 and lista_pelotas[x].speed_y < 0:
                            lista_pelotas[x].speed_x *= -1
                    elif abs(lista_pelotas[x].block.top-jugador.block.bottom) > 10 and lista_pelotas[x].speed_y > 1:
                        lista_pelotas[x].speed_x *= -1
                    elif abs(lista_pelotas[x].block.right - jugador.block.left)>10:
                        lista_pelotas[x].speed_x *= -1
            else:
                if lista_pelotas[x].block.colliderect(oponente.block):
                    sonido_golpe.play()                                                        
                    if lista_pelotas[x].block.y >= screen_height or lista_pelotas[x].block.y <=0:
                        lista_pelotas[x].speed_y *= -1
                    if lista_pelotas[x].block.colliderect(oponente.block)and lista_pelotas[x].speed_x<0:                                            
                        if abs(lista_pelotas[x].block.bottom-oponente.block.top) < 10 and lista_pelotas[x].speed_y > 0:
                            lista_pelotas[x].speed_x *= -2                      
                        elif abs(lista_pelotas[x].block.top-oponente.block.bottom) < 10 and lista_pelotas[x].speed_y < 10:
                            lista_pelotas[x].speed_x *= -2                           
                        elif abs(lista_pelotas[x].block.left-oponente.block.right)<10:
                            pos_choque = lista_pelotas[x].pos_y + (ball_size/2)-oponente.pos_y
                            dis_c =abs(pos_choque-(cursor_height/2))
                            dis_c_prop = dis_c/(cursor_height/2) 
                            variacion = dis_c_prop * (inc_vel_max-inc_vel_min)
                            variacion_y= dis_c_prop *(inc_vel_maxy - inc_vel_miny)
                            inc_vel_dosy = inc_vel_miny + variacion_y
                            inc_vel_dos = inc_vel_min + variacion
                            inc_vel = inc_vel_min + ((abs(pos_choque-(cursor_height/2))/(cursor_height/2)) * (inc_vel_max-inc_vel_min))
                            inc_vel_y =inc_vel_miny +((abs(pos_choque-(cursor_height/2))/(cursor_height/2)) *(inc_vel_maxy-inc_vel_miny))
                            lista_pelotas[x].speed_x *= - inc_vel
                            if pos_choque > 70:  
                                lista_pelotas[x].speed_y = inc_vel_y
                            else:
                                lista_pelotas[x].speed_y = -inc_vel_y                                
        self.calcular_speed_oponente()
                              
    def calcular_speed_oponente(self):
        if self.uno_dos_jugador== True:
            for x in range(game_manager.pelotas_max):
                if x == 0:
                    pos_min = lista_pelotas[0].pos_x
                    pel_min = x
                else:
                    if lista_pelotas[x].pos_x <=  pos_min and lista_pelotas[x].speed_x < 0:
                        pos_min = lista_pelotas[x].pos_x
                        pel_min = x                          
                if lista_pelotas[pel_min].pos_y < oponente.pos_y+((cursor_height/2)-(ball_size/2)):
                    oponente.speed_y = - abs(oponente.speed_y)
                else:
                    oponente.speed_y =abs(oponente.speed_y)

    def score(self):
        for x in range(game_manager.pelotas_max):
            print(lista_pelotas[x],lista_pelotas[x].speed_x)
                
            if lista_pelotas[x].pos_x <= 0:
                lista_pelotas[x].pos_x= screen_width/2-ball_size/2
                lista_pelotas[x].pos_y= screen_height/2
                lista_pelotas[x].speed_x = choice(list_choices)
                lista_pelotas[x].speed_y = choice(list_choices)
                sonido_punto.play()
                self.jugador_score += 1
                lista_pelotas[x].momento_muerte = pygame.time.get_ticks()
            if lista_pelotas[x].pos_x >= screen_width-lista_pelotas[x].tam_x:
                lista_pelotas[x].pos_x= screen_width/2-ball_size/2
                lista_pelotas[x].pos_y= screen_height/2
                lista_pelotas[x].speed_x = choice(list_choices)
                lista_pelotas[x].speed_y = choice(list_choices)
                sonido_punto.play()
                self.opponent_score += 1
                lista_pelotas[x].momento_muerte = pygame.time.get_ticks()
            if self.jugador_score == self.score_max or self.opponent_score == self.score_max:                
                for x in range(game_manager.pelotas_max):
                    lista_pelotas[x].momento_muerte = pygame.time.get_ticks()
                    lista_pelotas[x].pos_x =screen_width/2-(lista_pelotas[x].tam_x/2)
                    lista_pelotas[x].pos_y= screen_height/2
                self.game_active = False                    
        if self.settings_active== False:     
            player_text = game_font_big.render(f"{self.jugador_score}",True,(170,170,170))
            screen.blit(player_text,((screen_width/2)+200,screen_height/2-50))
            opponent_text = game_font_big.render(f"{self.opponent_score}",True,(170,170,170))
            screen.blit(opponent_text,((screen_width/2)-250,screen_height/2-50))

    def correr_juego(self):   
                
        if self.game_active== True:
            pygame.draw.aaline(screen,(170,170,170),(screen_width/2,0),(screen_width/2,screen_height))            
            jugador.salir_pantalla_jugadores()
            oponente.salir_pantalla_jugadores()
            self.colision()
            self.score()
            if jugador.pausa == False:
                pause_boton.mostrar_pulsables()
            else:
                resume_boton.mostrar_pulsables()          
            for x in range(game_manager.pelotas_max):            
                lista_pelotas[x].salir_pantalla()
        if self.game_active == False and self.settings_active == False:
            start_boton.mostrar_pulsables()   
            settings_boton.mostrar_pulsables()
            titulo.__init__(0, 200,0,0,"EXTREME PONG",game_font_giant)
            if self.uno_dos_jugador == True:
                if self.jugador_score == self.score_max:
                    you_win.__init__(365,340,0,0,"YOU WIN!",game_font)
                if self.opponent_score == self.score_max:
                    you_lose.__init__(365,340,0,0,"YOU LOSE!",game_font)
            if self.uno_dos_jugador == False:
                if self.jugador_score == self.score_max:
                    you_win.__init__(650,340,0,0,"YOU WIN!",game_font)
                    you_lose.__init__(100,340,0,0,"YOU LOSE!",game_font)
                if self.opponent_score == self.score_max:
                    you_win.__init__(100,340,0,0,"YOU WIN!",game_font)
                    you_lose.__init__(650,340,0,0,"YOU LOSE!",game_font)
            for x in range(game_manager.pelotas_max):
                    lista_pelotas.insert(x,Moviles((screen_width - ball_size)/2,(screen_height - ball_size)/2,ball_size,ball_size,choice(list_choices),choice(list_choices)))           
        
        if self.settings_active == True:
            self.jugador_score = 0
            self.opponent_score = 0
            if event.type== pygame.MOUSEBUTTONDOWN:
                if uno.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=1
                if dos.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=2
                if tres.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=3
                if cuatro.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=4
                if cinco.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=5
                if seis.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=6
                if siete.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    lista_pelotas.clear()
                    self.pelotas_max=7
                if score_cinco.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    self.score_max = 5
                if score_diez.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    self.score_max = 10
                if score_veinticinco.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    self.score_max = 25
                if score_cincuenta.rectangulo.collidepoint(event.pos):
                    click_golpe.play()
                    self.score_max = 50
                for x in range(game_manager.pelotas_max):
                    lista_pelotas.insert(x,Moviles((screen_width - ball_size)/2,(screen_height - ball_size)/2,ball_size,ball_size,choice(list_choices),choice(list_choices)))

            num_jugadores.__init__(0,100,0,0,"1/2 Players:",game_font)
            num_pelotas.__init__(0,200,0,0,"Balls:",game_font)
            num_score_max.__init__(0,300,0,0,"Max Score:",game_font)
            if self.uno_dos_jugador == True:
                pygame.draw.ellipse(screen,(200,101,244),un_jugador.rectangulo)
            elif self.uno_dos_jugador == False:
                pygame.draw.ellipse(screen,(200,101,244),dos_jugadores.rectangulo)
            if self.pelotas_max == 1:
                pygame.draw.ellipse(screen,(200,101,244),uno.rectangulo)
            elif self.pelotas_max == 2:
                pygame.draw.ellipse(screen,(200,101,244),dos.rectangulo)
            elif self.pelotas_max == 3:
                pygame.draw.ellipse(screen,(200,101,244),tres.rectangulo)
            elif self.pelotas_max == 4:
                pygame.draw.ellipse(screen,(200,101,244),cuatro.rectangulo)
            elif self.pelotas_max == 5:
                pygame.draw.ellipse(screen,(200,101,244),cinco.rectangulo)
            elif self.pelotas_max == 6:
                pygame.draw.ellipse(screen,(200,101,244),seis.rectangulo)
            elif self.pelotas_max == 7:
                pygame.draw.ellipse(screen,(200,101,244),siete.rectangulo)
            if self.score_max == 5:
                pygame.draw.ellipse(screen,(200,101,244),score_cinco.rectangulo)
            if self.score_max == 10:
                pygame.draw.ellipse(screen,(200,101,244),score_diez.rectangulo)
            if self.score_max == 25:
                pygame.draw.ellipse(screen,(200,101,244),score_veinticinco.rectangulo)
            if self.score_max == 50:
                pygame.draw.ellipse(screen,(200,101,244),score_cincuenta.rectangulo)
            un_jugador.mostrar_opciones()
            dos_jugadores.mostrar_opciones()
            back_boton.mostrar_pulsables()
            uno.mostrar_opciones()
            dos.mostrar_opciones()
            tres.mostrar_opciones()
            cuatro.mostrar_opciones()
            cinco.mostrar_opciones()
            seis.mostrar_opciones()
            siete.mostrar_opciones()
            score_cinco.mostrar_opciones()
            score_diez.mostrar_opciones()
            score_veinticinco.mostrar_opciones()
            score_cincuenta.mostrar_opciones()
            
        
        if event.type== pygame.MOUSEBUTTONDOWN:
            if start_boton.rectangulo.collidepoint(event.pos):
                click_golpe.play()
                self.game_active= True
                self.jugador_score = 0
                self.opponent_score = 0       
            if pause_boton.rectangulo.collidepoint(event.pos):
                click_golpe.play()                
                for x in range(game_manager.pelotas_max):                                               
                    lista_pelotas[x].pausa = True
                    oponente.pausa= True
                    jugador.pausa = True                
            if resume_boton.rectangulo.collidepoint(event.pos):
                click_golpe.play()
                for x in range(game_manager.pelotas_max):
                    lista_pelotas[x].momento_muerte = (pygame.time.get_ticks()-2000)
                    lista_pelotas[x].pausa= False
                    oponente.pausa= False
                    jugador.pausa = False
            if settings_boton.rectangulo.collidepoint(event.pos) and self.settings_active== False:
                click_golpe.play()
                self.settings_active =True
            if un_jugador.rectangulo.collidepoint(event.pos):
                click_golpe.play()
                self.uno_dos_jugador= True
                oponente.speed_y = 7
            if dos_jugadores.rectangulo.collidepoint(event.pos):
                click_golpe.play()
                self.uno_dos_jugador= False
                oponente.speed_y=0
            if back_boton.rectangulo.collidepoint(event.pos) and self.settings_active== True:
                click_golpe.play()
                self.settings_active= False
            
#Creacion de objetos 
game_manager = Manager()         
oponente = Moviles(0,(screen_height-cursor_height)/2,cursor_width,cursor_height,0,7)
jugador=  Moviles(screen_width-cursor_width,(screen_height-cursor_height)/2,cursor_width,cursor_height,0,0)
start_boton = Menuitems(418,400,0,0, "START",game_font)
settings_boton = Menuitems(373,500,0,0, "SETTINGS",game_font)
pause_boton = Menuitems(0,0,50,50, "ll",game_font)
resume_boton = Menuitems(370,screen_height/2,0,0, "PLAY",game_font_big)
titulo = Menuitems(screen_width/2, 200,0,0,"EXTREME PONG",game_font_giant)
num_jugadores = Menuitems(0,100,0,0,"1/2 Players:",game_font)
un_jugador = Menuitems(300,100,0,0,"1P",game_font)
dos_jugadores = Menuitems(375,100,0,0,"2P",game_font)
num_pelotas = Menuitems(0,100,0,0,"BALLS:",game_font)
back_boton = Menuitems(650,500,0,0, "BACK",game_font)
uno= Menuitems(180,200,0,0,"1",game_font)
dos= Menuitems(230,200,0,0,"2",game_font)
tres= Menuitems(280,200,0,0,"3",game_font)
cuatro= Menuitems(330,200,0,0,"4",game_font)
cinco= Menuitems(380,200,0,0,"5",game_font)
seis= Menuitems(430,200,0,0,"6",game_font)
siete= Menuitems(480,200,0,0,"7",game_font)
num_score_max = Menuitems(0,300,0,0,"Max Score:",game_font)
score_cinco= Menuitems(310,300,0,0,"5",game_font)
score_diez= Menuitems(380,300,0,0,"10",game_font)
score_veinticinco= Menuitems(480,300,0,0,"25",game_font)
score_cincuenta= Menuitems(580,300,0,0,"50",game_font)
you_win= Menuitems(580,300,0,0,"YOU WIN!",game_font)
you_lose= Menuitems(580,300,0,0,"YOU LOSE!",game_font)

while True:        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
            #KEYBOARD INPUT       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:                
                jugador.speed_y+=7
            if event.key == pygame.K_UP:               
                jugador.speed_y-=7
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_DOWN:                
                jugador.speed_y-=7
            if event.key == pygame.K_UP:                
                jugador.speed_y+=7
        if game_manager.uno_dos_jugador == False:            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    oponente.speed_y+=7
                if event.key == pygame.K_w:
                    oponente.speed_y-=7                    
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_s:                    
                    oponente.speed_y-=7
                if event.key == pygame.K_w:                    
                    oponente.speed_y+=7

    screen.fill((123,111,194))    
    game_manager.correr_juego()      
    pygame.display.flip()
    clock.tick(60)