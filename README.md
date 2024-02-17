# README
Voo2dir is a sophisticated and efficient Python script that allows users to perform HTTP GET requests to enumerate hidden directories on a website. It employs a user-defined wordlist and, if desired, extensions. Voo2dir is designed for educational usage and offers a simple usage. When using the script, notice you are using the correct http/https format.

![1](https://user-images.githubusercontent.com/90532971/230961052-5012c0d3-99c4-4a8e-adab-306defb4c093.PNG)


![2](https://user-images.githubusercontent.com/90532971/230961062-e8aec162-f63e-4efe-b9a5-cc880bf38894.PNG)

# Optional Args
<pre>
optional arguments:
  -h, --help -> <b>Show this help message and exit.</b>
  -u URL, --url URL -> <b>HOST/TARGET to scan.</b>
  -w WORDLIST, --wordlist WORDLIST -> <b>Path to wqordlist to be loaded.</b>
  -e EXTENSIONS -> <b>Select extension to look for using space. example: -e php rar txt.</b>
  -v, --verbose -> <b>Enable verbose mode to see more.</b>
  -t TIME, --time TIME ->  <b>Set the timing for each request.</b>
  -b BATCH, --batch BATCH -> <b>How many directory paths are sent for enumeration at once.</b>
</pre>
  
  # Install
 <pre>
 1. git clone https://github.com/Adkali/Voo2Dir.git
 2. cd [Directory-Name]
 3. pip install -r requirements.txt
 4. Run python3 voo2dir.py
 </pre>

# Updates 
Voo2dir has been rebuilt from ZERO with a more user-friendly interface and additional options that give users greater control over the directory brute-forcing process. The new version 2.0 includes a batch-size option that lets users limit the number of requests sent in each batch, as well as a delay time option that controls the time interval between each request. The wordlist and extensions options have also been enhanced, providing users with greater flexibility and customization. Additionally, a 'verbose' mode has been added which shows users the error messages including status codes and server reactions. In the future, I intend to further upgrade this tool to identify more vulnerabilities and interact with web interfaces, such as detecting vulnerable user inputs. It took me time to modify this tool, i think it is very handy and useful.
