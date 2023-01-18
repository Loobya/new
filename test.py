import re
import random
import requests
from multiprocessing import Pool
from termcolor import colored
from fake_useragent import UserAgent

def revsip10(url):
    try:
        # Generate a random user-agent
        ua = UserAgent()
        random_user_agent = ua.random
        # Read the proxy list from a file
        with open(input("Enter the proxy file name : "), "r") as f:
            proxy_list = f.readlines()
        # Select a random proxy from the list
        proxy = {"http": random.choice(proxy_list), "https": random.choice(proxy_list)}
        head = {'User-Agent': random_user_agent,'proxies':proxy}
        ress = requests.post("https://osint.sh/reverseip/", data={"domain": url}, timeout=10, headers=head).text
        if 'Domain' in ress:
            ajg = re.findall('<td data-th="Domain">\n(.*?)<', ress)
            for asu in ajg:
                mek = asu.replace(" ", "")
                print(colored("[+] " + mek + " [!] GRABED . .",'green'))
                open('Results_domain.txt', 'a').write(mek + '\n')
        else:
                print(colored('ERROR!!!', 'red'))
    except:
        pass

def Main():
    try:
        list = input(colored("\n Give Me List :~# ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'])))
        crownes = input(colored("thread :~# ", random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'])))
        rev10 = open(list, 'r').read().splitlines()
        pp = Pool(int(crownes))
        pr = pp.map(revsip10, rev10)

    except :
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    Main()