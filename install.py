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

toInstall = []
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

    if(mustIns == ""):
        return
    
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
        toInstall.append("wireless_tools")
        toInstall.append("linux-headers")
        toInstall.append("wpa_supplicant")
        toInstall.append("xf86-video-intel")
        toInstall.append("sof-firmware")
        toInstall.append("alsa-utils")
        toInstall.append("pulseaudio-alsa")
        toInstall.append("pulseaudio")
        toInstall.append("acpi")

def Display():
    askDownDis = str(input('Do you want to install Xorg on your system? [y/n]: '))
    if(askDownDis == "y" or askDownDis == "Y"):
        toInstall.append("xorg")

        def DM():
            askDownDm = str(input('Which display manager do you want to install? [1-gdm; 2-sddm]: '))
            insDm = askDownDm.replace("", " ")
            if(insDm.count != 1):
                print("Error! You can select only one!")
                DM()
            elif(insDm == "1"):
                toInstall.append("gdm")
                dm = "gdm"
            elif(insDm == "2"):
                toInstall.append("sddm")
                dm = "sddm"


def WM():
    askDownWm = str(input('Which WM/DEs do you want to install? [1-awesome 2-dwm 3-hyprland 4-plasma 5-gnome]: '))
    for v in askDownWm:
        if(v == "1"):
            # Aswesomewm configs will be added from github
            toInstall.append("awesome")
        elif(v == "2"):
            # This will change with dwm compalation
            toInstall.append("dwm")
        elif(v == "3"):
            toInstall.append("hyprland")
        elif(v == "4"):
            toInstall.append("plasma")
        elif(v == "5"):
            toInstall.append("gnome")


def Apps():
    print("Apps included: librewolf, vscodium, vlc, kitty, thunar, keepassxc, etcher, virtualbox, tutanota, qbittorrent, neovim, htop, gparted, nitrogen, android_tools ")
    askDownApp = str(input('Do you want to install your apps? [y/n]: '))
    if(askDownApp == "y" or askDownApp == "Y"):
        toInstall.append("librewolf-bin")
        toInstall.append("android-tools")
        toInstall.append("etcher-bin")
        toInstall.append("htop")
        toInstall.append("kitty")
        toInstall.append("neofetch")
        toInstall.append("unzip")
        toInstall.append("vim")
        toInstall.append("tutanota-desktop-bin")
        toInstall.append("virtualbox")
        toInstall.append("vlc")
        toInstall.append("vscodium-bin")
        toInstall.append("firefox")
        toInstall.append("android-tools")
        toInstall.append("brightnessctl")
        toInstall.append("dunst")
        toInstall.append("filelight")
        toInstall.append("light-git")
        toInstall.append("lxappearance")
        toInstall.append("neovim")
        toInstall.append("network-manager-applet")
        toInstall.append("pamixer")
        toInstall.append("pavucontrol")
        toInstall.append("picom-git")
        toInstall.append("pqiv")
        toInstall.append("pulseaudio-ctl")
        toInstall.append("qbittorrent")
        toInstall.append("shotgun")
        toInstall.append("swayidle")
        toInstall.append("virtualbox-guest-utils")
        toInstall.append("waybar-hyprland")
        toInstall.append("wlogout")
        toInstall.append("xautolock")
        toInstall.append("xss-lock")
        toInstall.append("gparted")
        toInstall.append("swaybg")



def FIT():
        askDownApp = str(input('Do you want to install your fonts, themes and icons? [y/n]: '))
        if(askDownApp == "y" or askDownApp == "Y"):
            toInstall.append("adobe-source-sans-fonts")
            toInstall.append("colloid-gtk-theme-git")
            toInstall.append("deepin-gtk-theme")
            toInstall.append("fluent-cursor-theme-git")
            toInstall.append("fonts-droid-fallback")
            toInstall.append("multicolor-sddm-theme")
            toInstall.append("nordic-polar-theme")
            toInstall.append("nordic-standard-buttons-theme")
            toInstall.append("nordic-theme")
            toInstall.append("otf-droid-nerd")
            toInstall.append("oxygen-icons")
            toInstall.append("oxygen")
            toInstall.append("pop-gtk-theme")
            toInstall.append("qogir-gtk-theme")
            toInstall.append("sddm-theme-astronaut")
            toInstall.append("spleen-font")
            toInstall.append("ttf-borg-sans-mono")
            toInstall.append("ttf-linux-libertine")
            toInstall.append("ttf-mononoki-nerd")
            toInstall.append("ttf-roboto")
            toInstall.append("ttf-ubuntu-font-family")
            toInstall.append("tela-icon-theme")
            toInstall.append("adwaita-dark")
            toInstall.append("qogir-icon-theme")
            toInstall.append("xcursor-oxygen")
            toInstall.append("archlinux-themes-sddm")




Yay()

Display()

WM()

Apps()

FIT()

def Install():
    installList = ""
    for c in toInstall:
        installList = installList + " " + c
    os.system('yay -S %s' % installList)

    os.system('sudo systemctl enable %s' % dm)



Install()

print("installation complate!")