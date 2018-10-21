import random
import winsound
import sys
from colorama import Fore
from colorama import Style
from colorama import init
from colorama import Back


t = []
pos = 0
data2 = []
mtn = ""
gmo = False
i = 0
moves = 0
dif = 0
FLAG = ""
PLYR = ""
LOW = ""
MED = ""
HIGH = ""
TXT = ""

def main():
    setup()
    clrScheme()
    global moves
    while True:
        printWorld()
        player(data2)
        moves += 1
        winsound.PlaySound('move.wav', winsound.SND_FILENAME)
        if data2[pos] == "⚑":
            printWorld()
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)
            print("You found the flag in " + str(moves) + " moves!" + Fore.RESET)

            break

def clrScheme():
    global i
    init()
    print("What color scheme do you want?")
    print("Type 1 for Black and White Scheme:")
    print("    Sample: ▓ ▒ ░ " + Fore.YELLOW +"P " + Fore.RED +"⚑ " + Fore.WHITE + "Text")
    print("Type 2 for Blue & Green:")
    print("    Sample: " + Fore.GREEN + "▓ " + Fore.CYAN + "▒ "+ Fore.BLUE +"░ " + Fore.YELLOW +"P " + Fore.RED +"⚑ " + Fore.CYAN + "Text")
    print("Type 3 for Red and Purple:")
    print("    Sample: " + Fore.RED+ "▓ " + Fore.BLUE + "▒ "+ Fore.MAGENTA +"░ " + Fore.YELLOW +"P " + Fore.WHITE+"⚑ " + Fore.RED+ "Text")
    print("Type 4 for Inverted Red and Green:")
    print("    Sample: " + Fore.RED+Back.WHITE +"▓ " + Fore.BLUE + "▒ "+ Fore.GREEN+"░ " + Fore.YELLOW +"P " + Fore.WHITE+"⚑ " +Back.BLACK+ Fore.RED+ "Text")
    print(Fore.RESET, end="")
    while True:
        i = input()
        try:
            d = int(i)
            if d > 0 and d <= 4:
                winsound.PlaySound('move.wav', winsound.SND_FILENAME)
                break
        except:
            winsound.PlaySound('error.wav', winsound.SND_FILENAME)
            pass
    global FLAG
    global PLYR
    global LOW
    global MED
    global HIGH
    global TXT
    if d == 1:
        FLAG = Fore.RED
        PLYR = Fore.YELLOW
        LOW = Fore.WHITE
        MED = Fore.WHITE
        HIGH = Fore.WHITE
        TXT = Fore.WHITE
    elif d == 2:
        FLAG = Fore.RED
        PLYR = Fore.YELLOW
        LOW = Fore.BLUE
        MED = Fore.CYAN
        HIGH = Fore.GREEN
        TXT = Fore.CYAN
    elif d == 3:
        FLAG = Fore.BLACK
        PLYR = Fore.YELLOW
        LOW = Fore.MAGENTA
        MED = Fore.BLUE
        HIGH = Fore.RED
        TXT = Fore.RED
    elif d == 4:
        FLAG = Fore.BLACK + Back.WHITE
        PLYR = Fore.YELLOW + Back.WHITE
        LOW = Fore.GREEN + Back.WHITE
        MED = Fore.BLUE + Back.WHITE
        HIGH = Fore.RED + Back.WHITE
        TXT = Fore.RED + Back.BLACK

def setup():
    winsound.PlaySound('open.wav', winsound.SND_FILENAME)
    global dif
    while True:
        dif = input("Please set the difficulty from 1-10. (10 is easiest) ")
        try:
            int(dif)
            if int(dif) >= 1 and int(dif) <= 10:
                break
            else:
                print("Please provide a valid number.")
                winsound.PlaySound('error.wav', winsound.SND_FILENAME)
        except:
            print("Please provide a valid number.")
            winsound.PlaySound('error.wav', winsound.SND_FILENAME)
    winsound.PlaySound('move.wav', winsound.SND_FILENAME)
    global t
    s = [" ", "░", "▒", "▓"]
    v = 0
    while 400 != v:
        t.append(s[random.randint(0, 3)])
        v += 1
    global data2
    data2 = t[:]
    t[0] = "P"
    c = 0
    while int(dif) != c:
        ran = random.randint(5,399)
        data2[ran] = "⚑"
        t[ran] = "⚑"
        c += 1
    global mtn
    file = open("mountainnames.txt", "r")
    r = file.read().split(",   ")
    mtn = r[random.randint(0, len(r))]


def printWorld():
    print(TXT, end="")
    if gmo == True:
        print("Game Over!!")
        winsound.PlaySound('error.wav', winsound.SND_FILENAME)
        sys.exit()
    print("~|[Mountain Climbing Simulator v2]|~")
    print("""Rules:
----You have to climb a mountain. The goal of the game is to reach
----one of the flags. There are four elevation types.
----No elevation, Low, Medium, and High.
----You cannot go too steep down because you will fall and
----die (like High Elevation to Low for example).
----You can only go onto the same elevation or onto
----the next ones. (At low elevation, you can go
----to Low (░), None( ), Or Medium(▒)) Good Luck!
""")
    print(HIGH + "High Elevation: ▓ " + MED + "Medium Elevation: ▒ "+ LOW +"Low Elevation: ░ ")
    print(TXT + "██████████████████████████████████████████")
    r = 0
    m = 0
    while r != 10:
        d = 0
        print(TXT + "█", end="")
        while d != 40:
            if t[m] == "░":
                print(LOW, end="")
            elif t[m] == "▒":
                print(MED, end="")
            elif t[m] == "▓":
                print(HIGH, end="")
            elif t[m] == "P":
                print(PLYR, end="")
            else:
                print(FLAG, end="")
            print(t[m], end="")
            m += 1
            d += 1
        print(TXT + "█", end="")
        r += 1
        print(" ")
    print(TXT + "██████████████████████████████████████████")
    print("||Info:||")
    print("||You are climbing: " + mtn.upper() + "!||")
    print("||Current Block On: " + data2[pos], end="")
    if data2[pos] == " ":
        print(" (No Elevation)||")
    elif data2[pos] == "░":
        print(" (Low Elevation)||")
    elif data2[pos] == "▒":
        print(" (Medium Elevation)||")
    elif data2[pos] == "⚑":
        print(" (Flag {You Win!})||")
    else:
        print(" (High Elevation)||")
    print("||Moves: "+ str(moves) +"||")


def player(data):
    global pos
    while True:
        p = input("What direction? W, A, S, or D ")
        p = p.lower()
        if p == "w":
            if (pos - 40) >= 0:
                if(check(pos - 40) == True):
                    t[pos] = data[pos]
                    pos -= 40
                    t[pos] = "P"
            break
        elif p == "a":
            if (pos - 1) >= 0 and (((pos) % 40) != 0):
                if(check(pos - 1) == True):
                    t[pos] = data[pos]
                    pos -= 1
                    t[pos] = "P"
            break
        elif p == "s":
            if (pos + 40) < 400:
                if(check(pos + 40) == True):
                    t[pos] = data[pos]
                    check(pos + 40)
                    pos += 40
                    t[pos] = "P"
            break
        elif p == "d":
            if (pos + 1) < 400 and (((pos + 1) % 40) != 0):
                if(check(pos + 1) == True):
                    t[pos] = data[pos]
                    check(pos + 1)
                    pos += 1
                    t[pos] = "P"
            break
        print("Please provide a valid direction.")
        winsound.PlaySound('error.wav', winsound.SND_FILENAME)


def check(go):
    cb = data2[pos]
    gb = data2[go]
    global gmo
    if gb == "⚑":
        return True
    elif cb == " ":
        if gb == "░" or gb == " ":
            return True
        gmo = True
        return False
    elif cb == "░":
        if gb == "░" or gb == "▒" or gb == " ":
            return True
        gmo = True
        return False
    elif cb == "▒":
        if gb == "░" or gb == "▒" or gb == "▓":
            return True
        gmo = True
        return False
    else:
        if gb == "▓" or gb == "▒":
            return True
        gmo = True
        return False

main()
