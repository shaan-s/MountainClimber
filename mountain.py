import random
import sys
#for sound
import winsound

#For text colour
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
sflag = "⚑"

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
    global FLAG, PLYR, LOW, MED, HIGH, TXT, sflag
    #Setting colours
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
    global sflag
    #asking difficulty
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
    #Changing flag symbol
    fla = input("Would you like to change the flag symbol to 'F' instead of '⚑'? (Y/N) ")
    winsound.PlaySound('move.wav', winsound.SND_FILENAME)
    if fla == "Y":
        sflag = "F"
    #One list, t, is used to store what shows up on the screen
    #Data 2 stores the actual data so once you step on a square, you can get the height again.
    global t, data2
    #S is the possible tiles
    s = [" ", "░", "▒", "▓"]
    #This generates 400 of those tiles
    for x in range(400):
        t.append(s[random.randint(0, 3)])
    #These add a flag 2x3 area in the start so you cant get locked
    t[0], t[1], t[2] = " ", " ", " "
    t[39], t[40], t[41] = " ", " ", " "
    #This copies t over to data2
    data2 = t[:]
    #Displays the starting pos of the player
    t[0] = "P"
    #Generates flag(s)
    for x in range(int(dif)):
        ran = random.randint(5,399)
        data2[ran] = sflag
        t[ran] = sflag
    #Generates mountain names
    global mtn
    file = open("mountainnames.txt", "r")
    r = file.read().split(",   ")
    mtn = r[random.randint(0, len(r))]

def printWorld():
    #Sets txt colour
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
    #Prints the top border of the screen
    print(TXT + "█" * 42)
    m = 0
    #This prints the screen by first checking which tile it is, then setting the color. At the end, it is printed.
    for r in range(10):
        print(TXT + "█", end="")
        for d in range(40):
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
        print(TXT + "█", end="")
        print(" ")
    #Bottom screen border
    print(TXT + "█" * 42)
    #Bottom info screen
    print("||Info:||")
    print("||You are climbing: " + mtn.upper() + "!||")
    print("||Current Block On: " + data2[pos], end="")
    #Tells what height you are on
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
    #Moves
    print("||Moves: "+ str(moves) +"||")


def player(data):
    #This function asks for the direction, and checks if it's possible in the screen boundaries.
    #This does not check if the height is correct because that is the check's function job.
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
    #This returns true or false depending on if the surrounding squares can be moved on.
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
