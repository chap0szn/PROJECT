from colorama import init, Fore, Style
import logging

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.GREEN}
    ____  ____  ____  __  __  ____  _  _ 
   (  _ \\( ___)( ___)(  \\/  )(  _ \\( \\/ )
    )___/ )__)  )__)  )    (  )___/ \\  / 
   (__)  (____)(____)(_/\\/\\_)(__)   (__)
{Style.RESET_ALL}
"""
    print(banner)

def setup_logger():
    logging.basicConfig(
        filename='shell_activity.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',)

def log_activity(msg):
    logging.info(msg)