from random import randint
import pygame
import random
pygame.init()
from pygame.image import load
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide

fundo = load('cozinhajogo2.png')

musica_fundo = pygame.mixer.music.load('BoxCat Games - Young Love (1).mp3')
pygame.mixer.music.play(-1)
x = 320
y = 440

q = random.randint(1,32) * 20
e = 0

class Cebola(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('cebolajogo.png')
        self.rect = self.image.get_rect(
            center = (randint( 50, 640) , 0)
        )
        self.y = self.rect.y

    def update(self):
        self.rect.y += 4
        self.y = self.rect.y

        if self.rect.y == 480:
            self.kill()
            perdidas += 1
            print(f"perdidas - {perdidas}")

cebola = Cebola()

class Cesta(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('cestajogo.png')
        self.rect = self.image.get_rect()
        self.velocidade = 5
        self.rect = self.image.get_rect(
            center = (x, y)
        )
            
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
cesta = Cesta()

class Retangulo(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('retangulojogo.png')
        self.rect = self.image.get_rect(
            center = (320,720)
        )
'''
    def update(self):
        '''
retangulo = Retangulo()

grupo_comida = Group()
grupo_retangulo = GroupSingle(retangulo)
grupo_cesta = GroupSingle(cesta)

grupo_comida.add(Cebola())
grupo_retangulo.add(Retangulo())
grupo_cesta.add(Cesta())


tela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Joguinho")

tempo = pygame.time.Clock()
flag = True
cont = 0

pontos = 0
fonte = pygame.font.SysFont("comicsans", 20, False, True)
round = 0


perdidas = 0
morreu = False

def reiniciar_jogo():
    global pontos, morreu, perdidas
    pontos = 0 
    x = 320
    y = 420
    q = random.randint(1,32) * 20
    e = 0
    perdidas = 0
    morreu = False


while True:
    tempo.tick(360)
    PONTUAÇÃO = f'Pontos: {pontos}'
    Texto = fonte.render(PONTUAÇÃO, False, (0, 0, 0))
    tela.blit(fundo, (0, 0))
    tela.blit(Texto, (450, 65))

  
    grupo_cesta.draw(tela)
    grupo_cesta.update()

    grupo_retangulo.draw(tela)
    grupo_retangulo.update()
    
    grupo_comida.draw(tela)
    grupo_comida.update()

    if round % 120 == 0:
        if pontos < 10:
            grupo_comida.add(Cebola())
        for _ in range(int(pontos / 10)):
            grupo_comida.add(Cebola())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    if groupcollide(grupo_comida, grupo_cesta, True, False):
        pontos += 1
    if groupcollide(grupo_comida, grupo_retangulo, True, False):
        perdidas += 1

    print(cebola.y)
    if cebola.y >= 480:
        perdidas += 1
        print(f"perdidas = {perdidas}")

    if perdidas == 3:
        morreu = True
        while morreu:
                    tela.fill((224, 203, 99))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                reiniciar_jogo()
                    fonte2 = pygame.font.SysFont('arial', 20, True, True)
                    mensagem = "Game over! Pressione a tecla R para jogar novamente"
                    texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
                    ret_texto = texto_formatado.get_rect()
                    ret_texto.center = (320, 240)
                    tela.blit(texto_formatado, (ret_texto))
                    pygame.display.update ()


    pygame.display.update()
    round += 1
    




