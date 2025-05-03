import time
import sys
import signal
from faker import Faker
from colorama import Fore, Style, init

# Colorama'yı başlat
init()

fake = Faker()

# Ctrl+C ile çıkış mesajı
def exit_handler(sig, frame):
    print(Fore.RED + "\nÇıkış yapılıyor... Güle güle!" + Style.RESET_ALL)
    sys.exit(0)

# Ctrl+C sinyalini yakala
signal.signal(signal.SIGINT, exit_handler)

while True:
    print(Fore.BLUE + "-" * 32 + Style.RESET_ALL)
    print(Fore.RED + "Kart Bulundu!" + Style.RESET_ALL)
    print(Fore.CYAN + "Kart Sahibi:" + Style.RESET_ALL, fake.name())
    print(Fore.GREEN + "Kart Numarası:" + Style.RESET_ALL, fake.credit_card_number(card_type="visa"))
    print(Fore.YELLOW + "Son Kullanma Tarihi:" + Style.RESET_ALL, fake.credit_card_expire())
    print(Fore.MAGENTA + "CVV:" + Style.RESET_ALL, fake.credit_card_security_code())
    print(Fore.BLUE + "-" * 32 + Style.RESET_ALL)
    
    time.sleep(3)  # 3 saniye bekle
