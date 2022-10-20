> **Please note** this is just me documenting stuff. Not a serious readme, but will be updated. Steps described here are definitely gonna change to make it easier for users to implement and install themselves. This file as of right now is to just dump my thoughts and sync it over all my developer envs. Thank you okay bye bye now.

- Install raspberry pi OS lite on an SD-card with RPimager, enable ssh, wifi, all the cool stuff
- Put SD-card in pi 0, power the pi using the 5V rail.
- Disable bluetooth
> `sudo nano /boot/config.txt`, and add `dtoverlay=disable-bt` to bottom of file. After run `sudo systemctl disable bluetooth.service`. After that, reboot.
- Install python3 and nodeJS
