# CS 579 - Reverse Engineering at NMSU | Shannon Cruse

## Summary
This repository is where I will keep all of my reports on reverse engineering malware using the book "Learning Malware Analysis" by K A Monnappa. for CS 579 - Reverse Engineering course at NMSU, taught by Joshua Reynolds

## System Setup
Using Ubuntu, I set up my environment for reverse engineering first by using VMware Workstation to install a Windows 11 virtual machine from [Microsoft Developer](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/); using a Linux distribution on my home machine should hopefully limit the ability for malware to infect my main machine were it to escape the environment of the virtual machine. After all necessary installations were complete, I also isolated the virtual machine from any network connections to prevent any malware from having access to the internet, lest it find a way to replicate. These steps to isolate my virtual machine are to prevent any malware I'll be analyzing from spreading any further than my virtual machine.

Disabling Windows Defender took multiple attempts; first, I booted into safe mode and ran the provided commands to edit the registry, which should have prevented Windows Defender from starting, and then I booted into normal mode to open the task scheduler and disable Windows Defender tasks from running. At this point, Defender appeared to be disabled. However, rebooting revealed that it had turned itself back on. After following the instructions [here](https://woshub.com/disable-windows-defender-antivirus/) for both manually toggling settings to disable Defender and editing the register manually using `regedit.exe` while in minimal safe mode, I was finally successful.

Tools that I installed in my reverse engineering system include:
- Visual Studio with a C/C++ development environment: code editor
- IDA Education: a binary reverse engineering tool
- Flare VM: a large collection of tools for analyzing Windows malware
