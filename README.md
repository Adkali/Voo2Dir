# VOO2DIR
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f"> <img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet">
# Readme
![צילום מסך 2022-11-28 232140](https://user-images.githubusercontent.com/90532971/204383589-15191364-1131-47c0-8e8a-8ede9d686488.png)
A light tool for enumerate hidden path/directories within a website.
# Operating System Tested On
~ Kali Linux, Windows 10<br>Windows 10
please let me know if you have experienced any problems when using it.<br>

When using the script, notice you are using the correct http URL.
Example: http://10.0.0.0 - Bad while http://10.0.0.0/ - Good.
The '/' at the end matters, so if you have problems, notice to the URL.

# Usage
<pre> 
1. git clone [ Repository name ]
2. cd Voo2dir
3. python3 voo2dir.py -Url [Host] -Word [Path/To/Dir/</pre]

# Optional Args
<pre>
optional arguments:
  -h, --help  show this help message and exit
  -Url URL    Host URL, Make Sure You Insert It Properly.
  -Word WORD  Wordlist Path.
  -v V        voo2dir, Version 1.0 Made By Adkali With Love.
  -ex EX      Extension flag for use (php,txt,rar,zip,html)
</pre>
  
  # Install
 <pre>
 1. git clone https://github.com/Adkali/Voo2Dir.git
 2. cd [Directory-Name]
 3. pip install -r requirements.txt
 4. python3 voo2dir.py
 </pre>
 # Updates 
 Fixed some bugs while trying to show the results on Windows.<br>
 Also, the flag '-ex' can now help you specified which extension do you want to search for.<br>
 Example of use: Python3 Voo2dir.py -Url http://site.com -Word wordlist.txt -ex php 
 # Problems
 if from any reason, the tool seems not responding, or showing errors, try to see if you filled the correct URL. Sometimes it happens, and could fix the issue you have. for exapmle : "http://", https://, slash(/) at the end of the URL. it might and could be the problem you have when enumerate/scan for directories. Remember to Use it only on CTF's/education only.
