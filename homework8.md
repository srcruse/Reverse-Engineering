# Homework 8
## What is njRAT?
njRAT, as its name implies, is a RAT - Remote Access Tool/Trojan. Once infected, it allows an attacker to take control of a victim's machine. 
This can include making changes to the victim machine's registry, logging keystrokes, and stealing credentials stored in browsers, per [Eran 
Yosef](https://www.cynet.com/attack-techniques-hands-on/njrat-report-bladabindi/). It often persists on the system by making copies of itself in 
different locations on the machine, and sometimes deletes the original copy of itself, as was found by 
[JustAnother-Engineer](https://infosecwriteups.com/part1-static-code-analysis-of-the-rat-njrat-2f273408df43). It was notably one of several 
RATs used to target Discord servers in 2016, according to
[Catalin Cimpanu](https://news.softpedia.com/news/gaming-voip-servers-abused-to-spread-remote-access-trojans-rats-509496.shtml)

## Registry
I noticed that a registry key was added to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`, which causes the specified
processes to be run on startup. The value added was a call to run `windows.exe`, located in `C:\Users\User\AppData\Local\Temp`. Suspicious, I
looked in that directory and noticed that "windows.exe" had been created shortly after my most recent run of njRAT. This obviously an attempt
to persist on the system and allow the process to run on startup every time the computer is turned on. Network administrators could check the
registry for what processes are called to run on startup, and investigate even ones who appear benign.
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw8-reg-4.png "Registry Key")
![Image](https://github.com/srcruse/Reverse-Engineering/blob/main/Pictures/hw8-windows.png "njRAT copy")

## Files Affected
Most obviously, I noticed that a copy of `njRAT.exe` was copied onto the C: drive of my virtual machine. As previously mentioned, I also found 
a copy of "windows.exe" which was surely another copy of the malware, renamed in hopes of not being discovered. This is clearly an effort to 
persist beyond a user's attempt to delete the trojan. After much reading about this RAT, it's hard to make a recommendation on how to look at 
the filesystem to determine if a computer has been infected; different sources often had different accounts of ways and locations that njRAT would 
duplicate itself and attempt to hide. Disguising one of its copies as `windows.exe` seemed to be a common theme, and copies were reported to be 
hidden in the user's `Temp` folder, but it seems difficult to make universal recommendations when different iterations of the malware often behave 
differently.

## Network Behavior
Shortly after starting to run the program, FakeNet received a DNS request for `zaaptoo.zapto.org`. Using a [Whois lookup for zapto.org](https://www.whois.com/whois/zapto.org) 
reveals a seemingly legitimate domain; it was first registered in 2001 and was most recently updated in 2022. The registrar of the domain, a 
company named Vitalwerks Internet Solutions, also owns `noip.com`, which was first registered in 2000, and is also maintained to this day. To 
me, it seems most likely that the creator of njRAT was abusing a legitimate domain. Network administrators could obviously look for requests 
for `zaaptoo.zapto.org` to diagnose a machine infected with a copy of this same version of njRAT; however, because this version appears to be 
using a what otherwise appears to be a legitimate domain, this isn't a good universal recommendation. I would rather suggest to monitor for 
unusual network activity in conjunction with other symptoms as discussed earlier in this report for determining if a machine has been infected.
