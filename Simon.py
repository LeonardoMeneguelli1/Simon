import pygame
from random import randrange
import time

#musicas
pygame.init()
pygame.mixer.music.load(r"c:\Users\leona\Desktop\Simon\jogo\botao.mp3")
pygame.mixer.music.set_volume(0.5)


#Cores do Nosso Jogo
branco = (255,255,255)
cinza = (100,100,100)
branco = (255,255,255)
vermelho = (255,100,100)
vermelho_escuro = (255,0,0)
amarelo = (255,255,150)
amarelo_escuro = (255,255,0)
verde = (100,255,100)
verde_escuro =(0,200,0)
azul = (150,150,255)
azul_escuro = (0,0,255)
preto = (0,0,0)

window = pygame.display.set_mode((600,600))
window.fill(branco)

pygame.font.init()
fonte = pygame.font.SysFont("Comic Sans MS", 30)

#formar Geométricas do jogo
def start(window):
    
    #Quadrados
    pygame.draw.rect(window,verde_escuro, (100,100,200,200))
    pygame.draw.rect(window,vermelho_escuro, (300,100,200,200))
    pygame.draw.rect(window,amarelo_escuro, (100,300,200,200))
    pygame.draw.rect(window,azul_escuro, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
    #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()

def b_centro(window):
    
    #Quadrados
    pygame.draw.rect(window,verde_escuro, (100,100,200,200))
    pygame.draw.rect(window,vermelho_escuro, (300,100,200,200))
    pygame.draw.rect(window,amarelo_escuro, (100,300,200,200))
    pygame.draw.rect(window,azul_escuro, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
    #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    pygame.draw.circle(window,cinza,(300,300),80)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()

def h_verde(window):
    #Quadrados
    pygame.draw.rect(window,verde, (100,100,200,200))
    pygame.draw.rect(window,vermelho_escuro, (300,100,200,200))
    pygame.draw.rect(window,amarelo_escuro, (100,300,200,200))
    pygame.draw.rect(window,azul_escuro, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
     #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()
    

def h_vermelho(window):
    pygame.draw.rect(window,verde_escuro, (100,100,200,200))
    pygame.draw.rect(window,vermelho, (300,100,200,200))
    pygame.draw.rect(window,amarelo_escuro, (100,300,200,200))
    pygame.draw.rect(window,azul_escuro, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
    #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()

def h_amarelo(window):

    pygame.draw.rect(window,verde_escuro, (100,100,200,200))
    pygame.draw.rect(window,vermelho_escuro, (300,100,200,200))
    pygame.draw.rect(window,amarelo, (100,300,200,200))
    pygame.draw.rect(window,azul_escuro, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
    #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()

def h_azul(window):

    pygame.draw.rect(window,verde_escuro, (100,100,200,200))
    pygame.draw.rect(window,vermelho_escuro, (300,100,200,200))
    pygame.draw.rect(window,amarelo_escuro, (100,300,200,200))
    pygame.draw.rect(window,azul, (300,300,200,200))
    pygame.draw.rect(window,preto, (100,300,400,10))
    pygame.draw.rect(window,preto, (300,100,10,400))
    #Circulos
    pygame.draw.circle(window,branco,(300,300,),300,100)
    pygame.draw.circle(window,preto,(300,300,),90)
    pygame.draw.circle(window,preto,(300,300),210,10)
    #Texto
    texto = fonte.render("Simon",1,branco )
    window.blit(texto,(260,275))
    pygame.display.update()

#Variaveis
click_on_off = 0
sequencia = []
repeticao = 0
resposta = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Declarando cursor
    cursor = pygame.mouse.get_pos()
    # print(cursor)

    #Click do Cursor
    click = pygame.mouse.get_pressed()
    # print(click)

    #Repeticao
    if repeticao == 1:
        start(window)
        time.sleep(1)
        for i in range(len(sequencia)):
            pygame.draw.rect(window, branco, (0,0,500,50))
            texto = fonte.render(str(i + 1) + ' / ' + str(len(sequencia)), 1, preto)
            window.blit(texto, (10, 10))
            pygame.display.update()
            if sequencia[i] == 0:
                h_verde(window)
            if sequencia[i] == 1:
                h_vermelho(window)
            if sequencia[i] == 2:
                h_amarelo(window),
            if sequencia[i] == 3:
                h_azul(window)

            print(sequencia[i])
            time.sleep(1)
            start(window)
            time.sleep(0.5)
        repeticao = 0

    #logica de error
    if resposta == sequencia and sequencia != []:
        repeticao = 1
        sequencia.append(randrange(4))
        resposta = []
    if len (resposta) > 0 and \
    len(sequencia) > 0 and \
    resposta[len(resposta)-1] != sequencia[len(resposta)-1] and \
    sequencia !=[]:
        pygame.draw.rect(window, branco, (0, 0, 500, 50))
        texto = fonte.render('Game Over - Você fez ' + str(len(sequencia) -1) + ' pontos', 1, vermelho_escuro)
        window.blit(texto, (10,10))
        pygame.display.update()
        time.sleep(5)
        sequencia = []
        resposta = []

    #Holde dos botões
    if(cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 <= 40000 and  \
    (cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 >= 8100 and \
    100 <= cursor[0] <= 300 and \
    100 <= cursor[1] <= 300: 
        h_verde(window)
        if click[0] == 0 and click_on_off == 1:
            resposta.append(0)
            pygame.mixer.music.play()
            print(resposta)

    elif(cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 <= 40000 and  \
    (cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 >= 8100 and \
    300 <= cursor[0] <= 500 and \
    100 <= cursor[1] <= 300: 
        h_vermelho(window)
        if click[0] == 0 and click_on_off == 1:
            resposta.append(1)
            pygame.mixer.music.play()
            print(resposta)

    elif(cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 <= 40000 and  \
    (cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 >= 8100 and \
    100 <= cursor[0] <= 300 and \
    300 <= cursor[1] <= 500: 
        h_amarelo(window),
        if click[0] == 0 and click_on_off == 1:
            resposta.append(2)
            pygame.mixer.music.play()
            print(resposta)
            
    elif(cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 <= 40000 and  \
    (cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 >= 8100 and \
    300 <= cursor[0] <= 500 and \
    300 <= cursor[1] <= 500: 
        h_azul(window),
        if click[0] == 0 and click_on_off == 1:
            resposta.append(3)
            pygame.mixer.music.play()
            print(resposta)

    elif(cursor[0] -300) ** 2 + (cursor[1] - 300) ** 2 <= 6400:
        b_centro(window),
        if click[0] == 0 and click_on_off == 1:
            repeticao = 1
            sequencia.append(randrange(4))
            pygame.mixer.music.play()
            resposta = []
        
    else:start(window)
    pygame.draw.rect(window, branco, (0, 0, 500, 50))
    texto = fonte.render(str(len(sequencia)), 1, preto)
    window.blit(texto,(10, 10))

    click_on_off = click[0]

    pygame.display.update()
    

    
