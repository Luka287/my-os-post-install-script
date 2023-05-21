import subprocess
import os

from distutils.spawn import find_executable
import shutil 


hi = subprocess.run(["echo", "Hi! This is post installation script for Luka287"])

hi = subprocess.run(["echo", "Script works on Arch Linux only!"])

space = subprocess.run("echo")

hi = subprocess.run(["echo", "This script assumes that you have installed sudo and networkmanager and you are logged in as user that is in wheel user group"
])


location = subprocess.run("pwd", capture_output=True)

crux = str(location.stdout)

curdir = crux[2:-3]

toInstall_Pacman = []
toInstall_Yay = []
dm = ""

def checkApp(app):
    if(find_executable(app) == None):
        return 0
    else:
        return 1



def Yay():
    
    yayIns = 0
    askList = []
    if(checkApp("/bin/yay") == 0):
        askList.append("yay")
    
    if(checkApp("/bin/git") == 0):
        askList.append("git")

    if(checkApp("/bin/make") == 0):
        askList.append("make")


    mustIns = ""
    for r in askList:
        if(r != "yay"):
            mustIns = mustIns + " " + r
        else:
            yayIns = 1

    if(mustIns == "" and yayIns != 1):
        return
    elif(mustIns == "" and yayIns == 1):
        mustIns = "yay"
    
    askDown = str(input('To continue installation you must install "' + mustIns + '" [y/n]: '))

    if(askDown == "y" or askDown == "Y"):
        os.system('sudo pacman -S %s' % mustIns)
    else:
        exit

    

    if(yayIns == 1):
       insYay = subprocess.run(["bash", "install-yay.sh"])

    
    print("Installation setup complate!")



def Drivers():
    askDownDr = str(input('Do you want wifi and other drivers set up on your system? [y/n]: '))
    if(askDownDr == "y" or askDownDr == "Y"):
        toInstall_Pacman.append("wireless_tools")
        toInstall_Pacman.append("linux-headers")
        toInstall_Pacman.append("wpa_supplicant")
        toInstall_Pacman.append("xf86-video-intel")
        toInstall_Pacman.append("sof-firmware")
        toInstall_Pacman.append("alsa-utils")
        toInstall_Pacman.append("pulseaudio-alsa")
        toInstall_Pacman.append("pulseaudio")
        toInstall_Pacman.append("acpi")


def Display():
    askDownDis = str(input('Do you want to install Xorg on your system? [y/n]: '))
    if(askDownDis == "y" or askDownDis == "Y"):
        toInstall_Pacman.append("xorg")

        def DM():
            askDownDm = str(input('Which display manager do you want to install? [1-gdm; 2-sddm]: '))
            insDm = askDownDm.replace("", " ")
            if(insDm.count != 1):
                print("Error! You can select only one!")
                DM()
            elif(insDm == "1"):
                toInstall_Pacman.append("gdm")
                dm = "gdm"
            elif(insDm == "2"):
                toInstall_Pacman.append("sddm")
                dm = "sddm"


def WM():
    askDownWm = str(input('Which WM/DEs do you want to install? [1-awesome 2-dwm 3-hyprland 4-plasma 5-gnome]: '))
    for v in askDownWm:
        if(v == "1"):
            # Aswesomewm configs will be added from github
            toInstall_Pacman.append("awesome")
        elif(v == "2"):
            # This will change with dwm compalation
            toInstall_Yay.append("dwm")
        elif(v == "3"):
            toInstall_Pacman.append("hyprland")
        elif(v == "4"):
            toInstall_Pacman.append("plasma")
        elif(v == "5"):
            toInstall_Pacman.append("gnome")


def Apps():
    print("Apps included: librewolf, vscodium, vlc, kitty, thunar, keepassxc, etcher, virtualbox, tutanota, qbittorrent, neovim, htop, gparted, nitrogen, android_tools ")
    askDownApp = str(input('Do you want to install your apps? [y/n]: '))
    if(askDownApp == "y" or askDownApp == "Y"):
        toInstall_Yay.append("librewolf-bin")
        toInstall_Pacman.append("android-tools")
        toInstall_Yay.append("etcher-bin")
        toInstall_Pacman.append("htop")
        toInstall_Pacman.append("kitty")
        toInstall_Pacman.append("neofetch")
        toInstall_Pacman.append("unzip")
        toInstall_Pacman.append("vim")
        toInstall_Yay.append("tutanota-desktop-bin")
        toInstall_Pacman.append("virtualbox")
        toInstall_Pacman.append("vlc")
        toInstall_Yay.append("vscodium-bin")
        toInstall_Pacman.append("firefox")
        toInstall_Pacman.append("brightnessctl")
        toInstall_Pacman.append("dunst")
        toInstall_Pacman.append("filelight")
        toInstall_Yay.append("light-git")
        toInstall_Pacman.append("lxappearance")
        toInstall_Pacman.append("neovim")
        toInstall_Pacman.append("network-manager-applet")
        toInstall_Pacman.append("pamixer")
        toInstall_Pacman.append("pavucontrol")
        toInstall_Yay.append("picom-git")
        toInstall_Pacman.append("pqiv")
        toInstall_Yay.append("pulseaudio-ctl")
        toInstall_Pacman.append("qbittorrent")
        toInstall_Pacman.append("shotgun")
        toInstall_Pacman.append("swayidle")
        toInstall_Pacman.append("virtualbox-guest-utils")
#        toInstall_Yay.append("waybar-hyprland")
        toInstall_Yay.append("wlogout")
        toInstall_Pacman.append("xautolock")
        toInstall_Pacman.append("xss-lock")
        toInstall_Pacman.append("gparted")
        toInstall_Pacman.append("swaybg")



def FIT():
        askDownApp = str(input('Do you want to install your fonts, themes and icons? [y/n]: '))
        if(askDownApp == "y" or askDownApp == "Y"):
            toInstall_Pacman.append("adobe-source-sans-fonts")
            toInstall_Yay.append("colloid-gtk-theme-git")
            toInstall_Pacman.append("deepin-gtk-theme")
            toInstall_Yay.append("fluent-cursor-theme-git")
            toInstall_Yay.append("fonts-droid-fallback")
            toInstall_Yay.append("multicolor-sddm-theme")
            toInstall_Yay.append("nordic-polar-theme")
            toInstall_Yay.append("nordic-standard-buttons-theme")
            toInstall_Yay.append("nordic-theme")
            toInstall_Pacman.append("otf-droid-nerd")
            toInstall_Pacman.append("oxygen-icons")
            toInstall_Pacman.append("oxygen")
            toInstall_Pacman.append("pop-gtk-theme")
            toInstall_Yay.append("qogir-gtk-theme")
            toInstall_Yay.append("sddm-theme-astronaut")
            toInstall_Yay.append("spleen-font")
            toInstall_Yay.append("ttf-borg-sans-mono")
            toInstall_Pacman.append("ttf-linux-libertine")
            toInstall_Pacman.append("ttf-mononoki-nerd")
            toInstall_Pacman.append("ttf-roboto")
            toInstall_Pacman.append("ttf-ubuntu-font-family")
            toInstall_Yay.append("tela-icon-theme")
            toInstall_Yay.append("adwaita-dark")
            toInstall_Yay.append("qogir-icon-theme")
            toInstall_Yay.append("archlinux-themes-sddm")



Yay()

Display()

WM()

Apps()

FIT()


def Install_Pacman():
    installList_Pacman = ""
    
    for p in toInstall_Pacman:
        installList_Pacman = installList_Pacman + " " + p
    os.system('yay -S %s' % installList_Pacman)


def Install_Yay():
    installList_Yay = ""

    for y in toInstall_Yay:
        installList_Yay = installList_Yay + " " + y
    os.system('yay -S %s' % installList_Yay)


Install_Pacman()
Install_Yay()

print("Installation complate!")