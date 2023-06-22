import pyfiglet
from colorama import init, Fore, Style
import requests

# Initialize colorama
init()

# Function to print ASCII art
def print_ascii_art(text):
    result = pyfiglet.figlet_format(text)
    print(result)

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
    # Print ASCII art for the program name
    print_ascii_art("Seer")
    print("Made By R4GN4R0K")

    # Input option for Tor scanning
    tor_scan_option = input("Do you want to scan using Tor network? (y/n): ")

    if tor_scan_option.lower() == 'y':
        use_tor = True

        print("Attention: Enabling Tor network scanning requires VPN to be enabled.")
        vpn_enabled = input("Is your VPN enabled? (y/n): ")
        if vpn_enabled.lower() != 'y':
            print("Please enable your VPN before proceeding with Tor network scanning.")
            exit()

        print("Tor scanning enabled.")
        tor_site = input("Enter the Tor site (e.g., example.onion): ")

        # Input the word list filename for directories
        directory_word_list_file = input("Enter the Directory Word List Filename: ")

        # Opening the directory word list file with the appropriate encoding
        with open(directory_word_list_file, 'r', encoding='latin-1') as file:
            directory_word_list = file.read().splitlines()

        print("Scanning Tor network...")
        directory_scanner(tor_site, directory_word_list, use_tor=True)
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

            # Calling the function for scanning the directories
            directory_scanner(dom_name, directory_word_list, use_tor=False)
        else:
            # Input the domain name
            dom_name = input("Enter the Domain Name: ")

            # Input the word list filename for subdomains
            subdomain_word_list_file = input("Enter the Subdomain Word List Filename: ")

            # Opening the subdomain word list file with the appropriate encoding
            with open(subdomain_word_list_file, 'r', encoding='latin-1') as file:
                subdomain_word_list = file.read().splitlines()

            # Calling the function for scanning the subdomains
            directory_scanner(dom_name, subdomain_word_list, use_tor=False)
