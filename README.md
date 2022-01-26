# SavedWiFiPasswords
This program shows passwords on every wifi saved on your device by accessing some simple terminal commands.

<h2>How it works?</h2>

1\) First we run a command in your **PowerShell** that show names of the wifi connections that are saved on your device and save them to a list.
```cmd
netsh wlan show profiles
```
2\) Then we iterate through that list and run a command that shows up the **password**.
```cmd
netsh wlan show profile wifi-name key=clear
```
<br>

| Known Networks | Program in work |
| -------------- | ------------- |
| <img src="https://github.com/MrGrizz11/SavedWiFiPasswords/blob/main/saved%20networks.png"> | <img src="https://github.com/MrGrizz11/SavedWiFiPasswords/blob/main/wifi%20demonstration.gif"> |


<img src="https://github.com/MrGrizz11/SavedWiFiPasswords/blob/main/saved%20networks.png">
