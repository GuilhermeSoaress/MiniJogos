import pyxel
from random import randint

#Declaravariáveisglobais

#Posiçãoevelocidade
x = 10
y = 40
vy = -30

#Gravidade
g = 200

#Duraçãodoframe
fps = 75
dt = 1 / fps #duraçãodecadaframe

#Guardascoreeseojogoestáperdidoounão
game_over = False
score = 0

#Posições(x,h)docantoinferioresquerdodecada
#pardecanos.
#Usaocanosuperiorcomoreferência
canos_xs = [50, 90, 130, 170]
canos_hs = [10, 25, 15, 5]


def update():
    global x, y, vy, game_over, canos_xs, score

#Nãoatualizamosafísicadeumjogoperdido.
#Podemosfazerissosimplesmenteretornandoa
#funçãoprematuramente
    if game_over and pyxel.btnp(pyxel.KEY_SPACE):
    #Reiniciaojogo
        y = 40
        vy = -20
        game_over = False
        canos_xs = [50 ,90, 130, 170]
        score = 0
    elif game_over:
        #Mantêmojogopausado
        return

    #Atualizaaposiçãoevelocidadedopassarinho
    #deacordocomasleisdafísicademovimento
    #acelerado
    #s=s0+v0*t+a*t**2/2
    #v=v0+a*t
    y = y + vy * dt + g * dt ** 2 / 2
    vy = vy + g * dt

    #Verificaseojogadorapertouespaço
    #paracausarumpulo
    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) or pyxel.btnp(pyxel.KEY_SPACE):#pulacomomouse
        vy = -75

    #Atualizaaposiçãoxdoscanos
    for i in range(len(canos_xs)):
        canos_xs[i] -= 0.6

    #Reciclaoscanos,senecessário
    if canos_xs[0] < -10:#(10=L,larguradocano)
        del canos_xs[0]
        del canos_hs[0]
        canos_xs.append(canos_xs[-1] + 40)#criaumnovocano40pxapósoúltimocano
        canos_hs.append(randint(5, 30))#sorteiaumaalturaaleatóriaparaele
        score += 1

    #Verificacolisões
    for i in range(int(x), int(x + 5)):
        for j in range(int(y), int(y + 4)):
            if pyxel.pget(i, j) == pyxel.COLOR_LIME:
                game_over = True


def draw():
     #Limpaatela
    pyxel.cls(pyxel.COLOR_BLACK)

        #Desenhaopassarinho
    pyxel.rect(x + 1, y, 4, 4, pyxel.COLOR_YELLOW)
    if vy < 0:
        pyxel.rect(x - 1, y+2, 2, 2, pyxel.COLOR_YELLOW)
    else:
        pyxel.rect(x - 1, y, 2, 2, pyxel.COLOR_YELLOW)

    pyxel.rect(x + 4, y + 2, 2, 1, pyxel.COLOR_ORANGE)
    pyxel.rect(x + 3, y + 1, 1, 1, pyxel.COLOR_BLACK)

#Desenharoscanos
    for x_cano, h_cano in zip(canos_xs, canos_hs):
        desenha_cano(x_cano, h_cano)

    #Desenhao"gameover"
    if game_over:
        pyxel.text(38, 40, "PERDEUPATO", pyxel.COLOR_WHITE)

    #Desenhaoscore
        pyxel.text(100, 5, f"n:{score}", pyxel.COLOR_WHITE)


def desenha_cano(x, h):
    cor = pyxel.COLOR_LIME
    L = 10
    B = 40

    #Canodecima
    pyxel.rect(x, 0, L, h, cor)

    #Canodebaixo
    pyxel.rect(x, h + B, L, pyxel.height-(h + B), cor)

    #Testedecírculo
    pyxel.circ(x, 5, 10, pyxel.COLOR_PINK)


pyxel.init(150, 100, fps = 75)
pyxel.mouse(True)
pyxel.run(update, draw)
