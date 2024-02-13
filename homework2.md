# Homework 2
## Summary
Win32.KeyPass.bin is a ransomware virus targeting Windows systems which encrypts user files, giving them the .KEYPASS file extension. It then leaves a .txt file with instructions on 
the victim computer's desktop and deletes itself. The attackers are likely looking to receive their payment in Bitcoin.

## Type of Malware
KeyPass targets Windows operating systems; aside from the filename beginning with 'Win32,' analyzing the binary in Common File Format Explorer (CFF) under the Address Explorer 
section shows that the file begins with "MZ," which is followed shortly by "This program cannot be run in DOS mode."

Because KeyPass requires human intervention to be run, it is a virus rather than a worm. It is an example of ransomware, which encrypts the users' personal files and leaves a 
ransom note behind with instructions on paying the creators in order to get their data back. Icons of the Bitcoin logo can be found using CFF, so this is very likely the manner 
in which the attackers are looking to be paid. The file does contact a Ukrainian site and likely downloads a file called `get.php`, but I could find no information about what that 
might do; however, there is enough to learn from the KeyPass file that it is malicious itself, and not just a loader or dropper for further malware.

## Signatures
Under CFF's Dependency Walker, the MD5 hash for this file is `6999C944D1C98B2739D015448C99A291`, and the SHA-1 hash is `D9BEB50B51C30C02326EA761B5F1AB158C73B12C`. Searching for 
the MD5 hash on VirusTotal yields a lot of incredibly helpful information, some of which I didn't find on my own investigation. 

## Indicators of Compromise
A system compromised by KeyPass will be easy to spot -- personal files like documents and images will be encrypted, with their extensions changed to .KEYPASS. A text file, 
`!!!DECRYPTION__KEYPASS__INFO!!!.txt`, will be generated on the desktop with instructions for the victim.

Based on the information found on the TotalVirus results for this file, KeyPass will contact `kronus.pp.ua`, a domain based in Ukraine.

## Clues about Origin
First, typos in the explanation text suggest a non-native English speaker is potentially behind the malware. Although the .ch domain in the text originates from Switzerland, 
the attackers may not necessarily be Swiss. According to the [WikiPedia Entry](https://en.wikipedia.org/wiki/.ch) for the domain, 
>.ch has been of a rising interest to Chinese domain investors for several reasons. According to EuropeID.com, the domain .ch still has many valuable English keywords and
>short letter and number combinations left. A contributing factor may be because the majority of .ch registrations are in German, leaving many English words available.

According to the [VirusTotal analysis](https://www.virustotal.com/gui/file/35b067642173874bd2766da0d108401b4cf45d6e2a8b3971d95bf474be4f6282/details) of the file, and confirmed 
when I looked into it on CFF, a majority of the resources are considered to be in the Russian language. While most of these are icons, this could be a significant clue about the origin of this malware.

## YARA Rule
Because we know from the FLOSS output and our trial during lecture that KeyPass generates a file titled `!!!DECRYPTION__KEYPASS__INFO!!!.txt,` I thought a good starting point 
would be to search for that title or variations thereof, and possibly some notable lines from that text. I made the rule inclusive of variations using regular expressions, in 
case this title is changed in a future iteration of KeyPass. Rather than include a particular section of the ransom note file or the the email referenced within, I realized that either of those would be too 
easy to change in future iterations of the malware to avoid detection. Instead, I decided to also search for the PHP file referenced.

```
rule keypass {
	strings:
		$title = /!*DECRYPTION_*KEYPASS_*INFO!*/ nocase
		$url = "kronus.pp.ua/upwinload/get.php"
		
	condition:
		$title or $url
}
```
I think that this method has a low chance of generating false positives, and a moderate chance of false negatives if the authors of KeyPass change the wording of the title or stop 
referencing the given URL. False positives are unlikely in my opinion, since my rule is looking for two fairly specific strings, even if it is inclusive of variations to punctuation. 
Rules generated using a tool like YARA-Signator would be much more reliable in detecting KeyPass, as they will pull several examples from disassembly of memory dumps, rather than 
few specific examples when the authors might change this kind of easily-searchable information frequently.
	
