import pyfiglet
from colorama import init, Fore, Style
import requests
import random

# Initialize colorama
init()

# Function to print ASCII art with rainbow colors
def print_ascii_art(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    result = pyfiglet.figlet_format(text)
    rainbow_result = ""
    for char in result:
        color = random.choice(colors)
        rainbow_result += f"{color}{char}"
    print(rainbow_result + Style.RESET_ALL)

# Function for scanning subdomains
def subdomain_scanner(domain_name, subdomain_list, use_tor=False):
    print('----URLs after scanning----')

    for subdomain in subdomain_list:
        if use_tor:
            url = f"http://{subdomain}.{domain_name}"
        else:
            url = f"https://{subdomain}.{domain_name}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'[+] {Fore.GREEN}{url} - Live (Status Code: {response.status_code}){Style.RESET_ALL}')
            else:
                print(f'[-] {Fore.RED}{url} - Dead (Status Code: {response.status_code} - {response.reason}){Style.RESET_ALL}')
        except requests.ConnectionError:
            print(f'[-] {Fore.RED}{url} - Connection Error{Style.RESET_ALL}')

# Function for scanning directories
def directory_scanner(domain_name, directory_list, use_tor=False):
    print('----URLs after scanning----')

    for directory in directory_list:
        if use_tor:
            url = f"http://{domain_name}/{directory}"
        else:
            url = f"https://{domain_name}/{directory}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'[+] {Fore.GREEN}{url} - Live (Status Code: {response.status_code}){Style.RESET_ALL}')
            else:
                print(f'[-] {Fore.RED}{url} - Dead (Status Code: {response.status_code} - {response.reason}){Style.RESET_ALL}')
        except requests.ConnectionError:
            print(f'[-] {Fore.RED}{url} - Connection Error{Style.RESET_ALL}')

# Main function
if __name__ == '__main__':
    # Generate random rainbow colors for the tool
    random_colors = [random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]) for _ in range(5)]

    # Print ASCII art for the program name with random rainbow colors
    print_ascii_art("Floki")

    # Print options with random rainbow colors
    print(f"{random_colors[0]}Made By V1k1ng138{Style.RESET_ALL}")

    # Randomly select initial colors
    random_color_1 = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
    random_color_2 = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

    # Input option for Tor scanning
    tor_scan_option = input("Do you want to scan using Tor network? (y/n): ")

    if tor_scan_option.lower() == 'y':
        use_tor = True

        print("Attention: Enabling Tor network scanning requires VPN to be enabled.")
        vpn_enabled = input("Is your VPN enabled? (y/n): ")
        if vpn_enabled.lower() != 'y':
            print(f"{Fore.RED}Warning: Please enable VPN before proceeding with Tor network scanning.{Style.RESET_ALL}")
    else:
        use_tor = False

    # Input option for directory scanning
    switch_to_directory_mode = input("Do you want to switch to directory mode? (y/n): ")

    if switch_to_directory_mode.lower() == 'y':
        # Input the domain name
        dom_name = input("Enter the Domain Name: ")

        # Input the word list filename for directories
        directory_word_list_file = input("Enter the Directory Word List Filename: ")

        # Opening the directory word list file with the appropriate encoding
        with open(directory_word_list_file, 'r', encoding='latin-1') as file:
            directory_word_list = file.read().splitlines()

        print(f"Scanning directories for {dom_name}...")

        if use_tor:
            directory_scanner(dom_name, directory_word_list, use_tor=True)
        else:
            directory_scanner(dom_name, directory_word_list, use_tor=False)
    else:
        # Input the domain name
        dom_name = input("Enter the Domain Name: ")

        # Input the word list filename for subdomains
        subdomain_word_list_file = input("Enter the Subdomain Word List Filename: ")

        # Opening the subdomain word list file with the appropriate encoding
        with open(subdomain_word_list_file, 'r', encoding='latin-1') as file:
            subdomain_word_list = file.read().splitlines()

        print(f"Scanning subdomains for {dom_name}...")

        if use_tor:
            subdomain_scanner(dom_name, subdomain_word_list, use_tor=True)
        else:
            subdomain_scanner(dom_name, subdomain_word_list, use_tor=False)
