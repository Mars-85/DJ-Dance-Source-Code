import pgzrun
import random
# Width of the window
WIDTH = 840
# Height of the window
HEIGHT = 630
# Title of the game
TITLE = "DJ Dance by ! LemoLev"
# Frames per second
FPS = 30

# Actors
bg_djk = Actor("bg_djk")
lnna = Actor("lnna", (250, 60))
rnna = Actor("rnna", (593, 60))
dnna = Actor("dnna", (365, 60))
unna = Actor("unna", (470, 60))
lbd = Actor("lbd", (250, 60))
rbd = Actor("rbd", (593, 60))
dbd = Actor("nbd", (365, 60))
ubd = Actor("ubd", (470, 60))
miny = Actor("menu_screen")
gos = Actor('gos')
ws = Actor("ws")
bs = Actor("bs")
tys = Actor("try_again")
batan0 = Actor("button", (410, 130))
batan1 = Actor("button", (410, 200))
batan2 = Actor("button", (410, 270))
batan3 = Actor("button", (410, 340))
batan4 = Actor("bata", (40, 597))
hardr = Actor("harddifr", (410, 130))
medr = Actor("meddifr", (410, 200))
easr = Actor("easydifr", (410, 270))
hard = Actor("harddif", (410, 130))
med = Actor("meddif", (410, 200))
easy = Actor("easydif", (410, 270))
LangSel = Actor("rl", (420, 130))
button_sprites = ["button", "button_2"]
notes = [Actor("ln", (250, 690)), Actor("rn", (593, 690)), Actor("un", (470, 690)), Actor("dn", (365, 690))]
bg_l2 = Actor("bg_l2")
bg_l3 = Actor("bg_l3")
nr = random.randint(0, 3)
count = 0
bf = Actor("bflose")
djk = Actor("djk1", (420, 315))
djkanim = ["djk1", "djk-4", "djk-3", "djk2", "djk3", "djk-2", "djk4", "djk-1"]
djkcanim = ["djk1c", "djk-4c", "djk-3c", "djk2c", "djk3c", "djk-2c", "djk4c", "djk-1c"]
djkwanim = ["djk1w", "djk-4w", "djk-3w", "djk2w", "djk3w", "djk-2w", "djk4w", "djk-1w"]
tfp = Actor('tfp')
mode = 5
hitted = 0
lang = "americ"
level = 1
speed = 6 * level + 7
bonus = 0
i = 0
cs = 0
k = 200
n = 0

# Music
music.play_once('breakfast.ogg')

# Drawing
def draw():
    global nr, mode, hitted, level, bonus, i, cs, k, n
    # Win Check
    if not music.is_playing("o|oo|o") and count > 0 and mode == 1:
        mode = 2
        ws.draw()
    # TA(Try Again) Check
    if not music.is_playing("o|oo|o") and count < 0 and mode == 1:
        tys.draw()
        mode = 3

    # **********************************************
    if music.is_playing("0m0gus"):
        if mode == 1:
            # Drawing personage and background of the level
            if level == 1:
                djk.image = djkanim[i]
                bg_djk.draw()
            elif level == 2:
                djk.image = djkwanim[i]
                bg_l2.draw()
            elif level == 3:
                djk.image = djkcanim[i]
                bg_l3.draw()
            djk.draw()
            cs += 1
            # cs - Speed of DJK (1 - fast, 9 - slow)
            if level == 3:
                if cs > 4:
                    i += 1
                    cs = 0
                    if level == 3:
                        if n==0:
                            k += 1
                        if n==1:
                            k -= 1
                        if k==260:
                            n = 0
                        if k==320:
                            n = 1
                        djk.y = k
                    
            else:
                if cs > 3:
                    i += 1
                    cs = 0
            if i > 7:
                i = 0
            # *******************************************************

            batan0.y = 1010101
            batan1.y = 736198653921
            batan2.y = 21376819723613981236
            batan3.y = 786587453649823640923069264027364982764872364
# *************************************************
            if lang == "americ" and mode == 1:
                screen.draw.text('Score: ' + str(count),
                                 center=(420, 12), color='white', fontsize=36)
                screen.draw.text('LEVEL: ' + str(level),
                                 center=(420, 512), color='white', fontsize=36)
                if bonus > 0:
                    screen.draw.text('BONUS: ' + str(bonus),
                                     center=(720, 512), color='white', fontsize=36)
                screen.draw.text('ESC -> MENU', (20, 582), color='white', fontsize=36)
            if lang == "rus" and mode == 1:
                screen.draw.text("Счёт: " + str(count),
                                 center=(420, 12), color='white', fontsize=36)
                screen.draw.text('Уровень: ' + str(level),
                                 center=(420, 512), color='white', fontsize=36)
                if bonus > 0:
                    screen.draw.text('БОНУС: ' + str(bonus),
                                     center=(720, 512), color='white', fontsize=36)
                screen.draw.text('ESC -> Выход в меню', (20, 582),
                                 color='white', fontsize=36)
# ************************************************
            lnna.draw()
            rnna.draw()
            dnna.draw()
            unna.draw()
            notes[nr].draw()
            if hitted == 1:
                lbd.draw()
                if notes[nr].y < 600:
                    hitted = 0
            if hitted == 2:
                rbd.draw()
                if notes[nr].y < 600:
                    hitted = 0
            if hitted == 3:
                ubd.draw()
                if notes[nr].y < 600:
                    hitted = 0
            if hitted == 4:
                dbd.draw()
                if notes[nr].y < 600:
                    hitted = 0
# *******************************************

    # If mode is four
    if mode == 4:
        gos.draw()

    # If mode is five
    if mode == 5:
        miny.draw()

        batan0.y = 130
        batan1.y = 200
        batan2.y = 270
        batan3.y = 340
        batan4.y = 597

        batan0.draw()
        batan1.draw()
        batan2.draw()
        batan3.draw()
        batan4.draw()

    if mode == 6:
        miny.draw()
        batan4.draw()
        LangSel.draw()

    # If mode is seven
    if mode == 7:
        bs.draw()
        tfp.draw()
        for i in range(40):
            tfp.y -= 0.01

    if lang == "americ" and mode == 5:
        screen.draw.text('RESUME/', pos=(370, 114), color="black", fontsize=30)
        screen.draw.text('    START', pos=(355, 128), color="black", fontsize=25)
        screen.draw.text('RESTART SONG', pos=(340, 190), color="black", fontsize=27)
        screen.draw.text('QUIT', pos=(380, 260), color="black", fontsize=36)
        screen.draw.text('OPTIONS', pos=(353, 330), color="black", fontsize=36)

    if lang == "americ":
        gos.image = "gos"
    if lang == "rus":
        gos.image = "gosr"

    if lang == "americ":
        tys.image = "try_again"
    if lang == "rus":
        tys.image = "tasr"

    if lang == "americ":
        ws.image = "ws"
    if lang == "rus":
        ws.image = "wsr"

    if lang == "rus" and mode == 5:
        screen.draw.text('ПРОДОЛЖИТЬ/', pos=(345, 114), color="black", fontsize=25)
        screen.draw.text('    СТАРТ', pos=(355, 128), color="black", fontsize=25)
        screen.draw.text('РЕСТАРТ', pos=(360, 190), color="black", fontsize=34)
        screen.draw.text('ВЫЙТИ', pos=(360, 259), color="black", fontsize=36)
        screen.draw.text('НАСТРОЙКИ', pos=(346, 330), color="black", fontsize=30)

# Moving
def muf():
    # Globals
    global nr, count
    if mode == 1:
        if notes[nr].y < 0:
            notes[nr].y = 690
            nr = random.randint(0, 3)
            sounds.hah.play()
            count -= 3
        else:
            notes[nr].y -= speed

# Update DT
def update(dt):
    # Globals
    global nr, count, mode, level, speed, bonus

    # Other
    muf()
    if count > 50 and level == 1:
        count = 50
        bonus += 1

    if count > 80 and level == 2:
        count = 80
        bonus += 1

    if count > 110 and level == 3:
        count = 110
        bonus += 1

    if count < -50:
        if mode != 5:
            mode = 4
            music.stop()

    if mode == 4 and keyboard.r and level == 1:
        mode = 1
        count = 0
        level = 1
        music.play_once("kpytoi_ihct.wav")
    if mode == 4 and keyboard.r and level == 2:
        mode = 1
        count = 0
        level = 2
        music.play_once("making_tracks.mp3")

    if mode == 4 and keyboard.r and level == 3:
        mode = 1
        count = 0
        level = 3
        music.play_once("efm.mp3")

    if mode == 3 and keyboard.r and level == 1:
        mode = 1
        count = 0
        level = 1
        music.play_once("kpytoi_ihct.wav")
    if mode == 3 and keyboard.r and level == 2:
        mode = 1
        count = 0
        level = 2
        music.play_once("making tracks....mp3")

    if mode == 3 and keyboard.r and level == 3:
        mode = 1
        count = 0
        level = 3
        music.play_once("escape from monster! (remake).mp3")
    if mode == 2 and keyboard.r and level == 1:
        mode = 1
        count = 0
        level = 31
        music.play_once("kpytoi_ihct.wav")
    if mode == 2 and keyboard.r and level == 2:
        mode = 1
        count = 0
        level = 2
        music.play_once("making tracks....mp3")
    if mode == 2 and keyboard.r and level == 3:
        mode = 1
        count = 0
        level = 3
        music.play_once("escape from monster! (remake).mp3")

    if mode == 2 and keyboard.space and level == 1:
        mode = 1
        count = bonus
        bonus = 0
        level += 1
        speed = 6 * level + 7
        music.play_once("making tracks....mp3")
    if mode == 2 and keyboard.space and level == 2:
        mode = 1
        count = bonus
        bonus = 0
        level += 1
        speed = 6 * level + 7
        music.play_once("escape from monster! (remake).mp3")
    if mode == 2 and keyboard.space and level == 3:
        mode = 7
        music.play_once("tfp.wav")
        if not music.is_playing('tfp.wav'):
            music.play_once("amogus.wav")

# Definder of menu
def menu():
    global mode, count
    count = 0
    mode = 5
    music.play_once("breakfast.ogg")

# If mouse on menu button
def on_mouse_move(pos):
    # If mouse on the one of the buttons
    if batan0.collidepoint(pos):
        batan0.image = button_sprites[1]
    else:
        batan0.image = button_sprites[0]
    if batan1.collidepoint(pos):
        batan1.image = button_sprites[1]
    else:
        batan1.image = button_sprites[0]
    if batan2.collidepoint(pos):
        batan2.image = button_sprites[1]
    else:
        batan2.image = button_sprites[0]
    if batan3.collidepoint(pos):
        batan3.image = button_sprites[1]
    else:
        batan3.image = button_sprites[0]

# Pressing on the button
def on_mouse_down(pos, button):
    # Globals
    global mode, count, lang

    # If buttons is pressed
    if batan0.collidepoint(pos) and mode != 6 and mode != 7 and level == 1:
        mode = 1
        music.play_once("kpytoi_ihct.wav")
    if batan0.collidepoint(pos) and mode != 6 and mode != 7 and level == 2:
        mode = 1
        music.play_once("making tracks....mp3")
    if batan0.collidepoint(pos) and mode != 6 and mode != 7 and level == 3:
        mode = 1
        music.play_once("escape from monster! (remake).mp3")

    if batan1.collidepoint(pos) and mode != 6 and mode != 7 and level == 1:
        music.play_once("kpytoi_ihct.wav")
        mode = 1
        count = 0
    if batan1.collidepoint(pos) and mode != 6 and mode != 7 and level == 2:
        music.play_once("making tracks....mp3")
        mode = 1
        count = 0
    if batan1.collidepoint(pos) and mode != 6 and mode != 7 and level == 3:
        music.play_once("escape from monster! (remake).mp3")
        mode = 1
        count = 0

    if button == mouse.LEFT and batan2.collidepoint(pos) and mode != 7 and mode != 6:
        exit()

    if batan3.collidepoint(pos) and mode != 7 and mode != 6:
        mode = 6

    if LangSel.collidepoint(pos) and LangSel.image == "rl" and mode == 6:
        lang = "rus"
        LangSel.image = "al"
        miny.image = "msr"
        tfp.image = "tfpr"
    elif LangSel.collidepoint(pos) and LangSel.image == "al" and mode == 6:
        lang = "americ"
        LangSel.image = "rl"
        miny.image = "menu_screen"
        tfp.image = "tfp"
    if batan4.collidepoint(pos):
        print("https://form.jotform.com/213090427439051")


# Arrow Check
def on_key_down(key):
    # Globals
    global nr, count, hitted, mode, level, speed
    # Menu Check
    if key == keys.ESCAPE:
        menu()
    # Keys Check
    if ((key == keys.LEFT and nr == 0) or (key == keys.RIGHT and nr == 1)
            or (key == keys.UP and nr == 2)
            or (key == keys.DOWN and nr == 3)) and notes[nr].y < 100:
        # ***** суммируем очки в зависимости от уровня ****
        if level == 1:
            count += 3
        if level == 2:
            count += 5
        if level == 3:
            count += 10
# *********************************************************
        nr = random.randint(0, 3)
        notes[nr].y = 690
        if key == keys.LEFT or keyboard.a:
            hitted = 1
        if key == keys.RIGHT or keyboard.d:
            hitted = 2
            rbd.draw()
        if key == keys.UP or keyboard.w:
            hitted = 3
            ubd.draw()
        if key == keys.DOWN or keyboard.s:
            hitted = 4
            dbd.draw()
pgzrun.go()
