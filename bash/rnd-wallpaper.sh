#!/usr/bin/env bash


## Description:
## This file was created for a user on the CachyOS discord #Lounge channel
## This file is meant to be used with KDE
##
## This file, when {dir} is pointed to the correct directory will scan and
## select a random desktop background wallpaper and apply it.
## add to the CachyOS/KDE Autostart in settings for it to randomly change
## wallpaper on login


dir='/path/to/desktop_background/wallapers/'

rndfile=$(find "${dir}" -type f -print0 | shuf -z -n 1 | tr -d '\0')

[[ -n $rndfile ]] || { echo "No files found in $dir" >&2; exit 1; }

/usr/bin/kwriteconfig6 --file kscreenlockerrc --group Greeter --group Wallpaper --group org.kde.image --group General --key Image "${rndfile}" && echo "Lockscreen wallpaper set to ${rndfile}" || echo "File not found: ${rndfile}"
/usr/bin/kwriteconfig6 --file kscreenlockerrc --group Greeter --group Wallpaper --group org.kde.image --group General --key PreviewImage "${rndfile}"
/usr/bin/plasma-apply-wallpaperimage "${rndfile}"