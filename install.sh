#!/bin/bash

# This is my post installation script for Arch Linux
# This script is written for my device and may not work for you

echo "Hi! This is post installation script for Luka287"
echo "Script works on Arch Linux only!"

echo " "

echo "This script assumes that you have installed sudo and networkmanager and you are logged in as user that is in wheel user group"

adf=$(pwd)

sd=0
down_arr_yay=() 

# array for packages

echo $ich
function Yay {
    echo -n "::Installing yay and git is neccecery to continue [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Necceccery programs will be installed!"
           
	    sudo pacman -S make git
	    sleep 0.2
	    git clone https://aur.archlinux.org/yay.git;
            cd yay;
            makepkg -si
        $adf
    else
        echo "Yay download cancelled!"
    fi;
}

function Wifi {
    echo -n "::Do you want wifi and other drivers set up on your system? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Neccecery programs will be installed!"

            down_arr_yay[${#down_arr_yay[@]}]="wireless_tools"
            down_arr_yay[${#down_arr_yay[@]}]="linux-headers"
            down_arr_yay[${#down_arr_yay[@]}]="wpa_supplicant"
            down_arr_yay[${#down_arr_yay[@]}]="xf86-video-intel"
            down_arr_yay[${#down_arr_yay[@]}]="xf86-video-vesa"
            down_arr_yay[${#down_arr_yay[@]}]="sof-firmware"
            down_arr_yay[${#down_arr_yay[@]}]="alsa-utils"
   
    else 
	    echo "Wifi set up cancelled!"
    fi;
}


function Xorg {
    echo -n "::Do you want to install xorg and sddm? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Neccecery programs will be installed!"

            down_arr_yay[${#down_arr_yay[@]}]="xorg"
            down_arr_yay[${#down_arr_yay[@]}]="sddm"
        # sudo systemctl enable sddm
	    set_arr[${set_arr[@]}]="sddm"
	    sd=${sd + 1}
    else 
	    echo "Xorg set up cancelled!"
    fi;
}


function Awesomewm {
    echo -n "::Do you want to install custom awesomewm? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Neccecery programs will be added"

            down_arr_yay[${#down_arr_yay[@]}]="awesome"
            down_arr_yay[${#down_arr_yay[@]}]="brightnessctl"
            down_arr_yay[${#down_arr_yay[@]}]="light-git"
            down_arr_yay[${#down_arr_yay[@]}]="acpi"
            down_arr_yay[${#down_arr_yay[@]}]="lxappearance"
            down_arr_yay[${#down_arr_yay[@]}]="shotgun"
            down_arr_yay[${#down_arr_yay[@]}]="pavucontrol"
            down_arr_yay[${#down_arr_yay[@]}]="network-manager-applet"
            down_arr_yay[${#down_arr_yay[@]}]="xss-lock"

	    #configs
	    git clone https://github.com/Luka287/awesome.git;
	    mv awesome ~/.config/
	    git clone https://github.com/Luka287/dmenu.git
	    mv dmenu ~/.config/
	    cd ~/.config/dmenu/
	    sudo make install
        cd $adf

        echo "setting up picom!"
        sleep 1;

        down_arr_yay[${#down_arr_yay[@]}]="picom-git"

        git clone https://github.com/Luka287/picom.git
        cd picom
        chmod +x setup
        ./setup
        cd $adf
    else
	    echo "Awesomewm downdoad cancelled!"
    fi;

}	 


function Apps {
    echo -n "::Do you want to install your apps? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Necceccery programs will be installed"
             down_arr_yay[${#down_arr_yay[@]}]="librewolf-bin"
	     down_arr_yay[${#down_arr_yay[@]}]="android-tools"
             down_arr_yay[${#down_arr_yay[@]}]="codeblocks"
             down_arr_yay[${#down_arr_yay[@]}]="etcher-bin"
             down_arr_yay[${#down_arr_yay[@]}]="gedit"
             down_arr_yay[${#down_arr_yay[@]}]="htop"
             down_arr_yay[${#down_arr_yay[@]}]="kitty"
             down_arr_yay[${#down_arr_yay[@]}]="neofetch"
             down_arr_yay[${#down_arr_yay[@]}]="unzip"
             down_arr_yay[${#down_arr_yay[@]}]="vim"
             down_arr_yay[${#down_arr_yay[@]}]="tutanota-desktop-bin"
             down_arr_yay[${#down_arr_yay[@]}]="virtualbox"
             down_arr_yay[${#down_arr_yay[@]}]="vlc"
             down_arr_yay[${#down_arr_yay[@]}]="vscodium-bin"
             down_arr_yay[${#down_arr_yay[@]}]="librewolf-bin"

    else
	    echo "Apps download cancelled!"
    
    fi;
}

# PICOM GAQ SASAKETEBELI


function Fonts {
    echo -n "::Do you want to install your fonts? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Necceccery programs will be installed"
            down_arr_yay[${#down_arr_yay[@]}]="spleen-font"
            down_arr_yay[${#down_arr_yay[@]}]="cantarell-fonts"
            down_arr_yay[${#down_arr_yay[@]}]="adobe-source-code-pro-fonts"
            down_arr_yay[${#down_arr_yay[@]}]="gnu-free-fonts"
            down_arr_yay[${#down_arr_yay[@]}]="xorg-fonts-100dpi"
            down_arr_yay[${#down_arr_yay[@]}]="xorg-fonts-75dpi"
            down_arr_yay[${#down_arr_yay[@]}]="xorg-fonts-alias-100dpi"
            down_arr_yay[${#down_arr_yay[@]}]="xorg-fonts-alias-75dpi"
            down_arr_yay[${#down_arr_yay[@]}]="ttf-linux-libertine"
            down_arr_yay[${#down_arr_yay[@]}]="nerd-fonts-droid-sans-mono"
            down_arr_yay[${#down_arr_yay[@]}]="fonts-droid-fallback"
            down_arr_yay[${#down_arr_yay[@]}]="ttf-borg-sans-mono"
    
    else
	    echo "Font install cancelled!"


    fi;
}


function Themes {
    echo -n "::Do you want to install your sddm and system themes and icons? [y/n]: ";
    read;
    if [ ${REPLY} = "y" ]; then
	    echo "Necceccery programs will be installed"
            down_arr_yay[${#down_arr_yay[@]}]="archlinux-themes-sddm"
            down_arr_yay[${#down_arr_yay[@]}]="deepin-gtk-theme"
            down_arr_yay[${#down_arr_yay[@]}]="multicolor-sddm-theme"
            down_arr_yay[${#down_arr_yay[@]}]="nordic-polar-theme"
            down_arr_yay[${#down_arr_yay[@]}]="oxygen-icons"
            down_arr_yay[${#down_arr_yay[@]}]="pop-gtk-theme"
            down_arr_yay[${#down_arr_yay[@]}]="pop-gtk-theme"
            down_arr_yay[${#down_arr_yay[@]}]="sddm-theme-astronaut"
            down_arr_yay[${#down_arr_yay[@]}]="xcursor-oxygen"
            down_arr_yay[${#down_arr_yay[@]}]="qogir-icon-theme"
            down_arr_yay[${#down_arr_yay[@]}]="qogir-gtk-theme"
            down_arr_yay[${#down_arr_yay[@]}]="fluent-cursor-theme-git"
            down_arr_yay[${#down_arr_yay[@]}]="nordic-standard-buttons-theme"
            down_arr_yay[${#down_arr_yay[@]}]="nordic-theme"
            down_arr_yay[${#down_arr_yay[@]}]="fluent-cursor-theme-git"
            down_arr_yay[${#down_arr_yay[@]}]="adwaita-dark"
            down_arr_yay[${#down_arr_yay[@]}]="nordic-theme"
            down_arr_yay[${#down_arr_yay[@]}]="tela-icon-theme"

    
    else
	    echo "Themes/icons install cancelled!"
    fi;
}

Yay

sleep 0.3

Wifi

sleep 0.3

Xorg

sleep 0.3

Awesomewm

sleep 0.3

Fonts

sleep 0.3

Themes

sleep 0.3

Apps

sleep 0.3

if [ ${#down_arr_yay[@]} != 0 ]; then
	yay -S ${down_arr_yay[@]}
fi;

sleep 0.1

if [ sd==1 ]; then 
	sudo systemctl enable sddm
fi;
