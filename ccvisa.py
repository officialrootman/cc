import sys
import signal
import time
import qrcode
from faker import Faker
from colorama import Fore, init
from PIL import Image, ImageDraw, ImageFont

# Colorama başlatılıyor
init(autoreset=True)

class CardGenerator:
    """
    Sahte kredi kartı bilgileri oluşturur ve resimli olarak kaydeder.
    """
    def __init__(self, locale: str = "tr_TR", card_type: str = "visa") -> None:
        self.fake = Faker(locale)
        self.card_type = card_type
        self.font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

    def generate_card_data(self) -> dict:
        """
        Sahte kart bilgilerini üretir.
        """
        return {
            "owner": self.fake.name(),
            "card_number": self.fake.credit_card_number(card_type=self.card_type),
            "expire": self.fake.credit_card_expire(),
            "cvv": self.fake.credit_card_security_code()
        }

    def create_qr_code(self, card_number: str) -> Image.Image:
        """
        Kart numarasını içeren bir QR kod oluşturur.
        """
        qr = qrcode.make(card_number)
        return qr.resize((80, 80))

    def create_card_image(self, card_data: dict, filename: str = "card.png") -> None:
        """
        Kart görseli oluşturur ve kaydeder.
        """
        img = Image.new("RGB", (450, 280), "navy")
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(self.font_path, 20)
        except IOError:
            font = ImageFont.load_default()

        draw.text((20, 30), f"Kart Sahibi: {card_data['owner']}", fill="white", font=font)
        draw.text((20, 80), f"Kart No: {card_data['card_number']}", fill="white", font=font)
        draw.text((20, 130), f"Son Kullanma: {card_data['expire']}", fill="white", font=font)
        draw.text((20, 180), f"CVV: {card_data['cvv']}", fill="white", font=font)

        # QR kod ekleme
        qr_image = self.create_qr_code(card_data["card_number"])
        img.paste(qr_image, (330, 180))

        img.save(filename)
        print(Fore.GREEN + f"Kart görseli kaydedildi: {filename}")

def exit_handler(sig, frame):
    """
    CTRL+C sinyalini yakalar ve çıkışı yönetir.
    """
    print(Fore.RED + "\nÇıkış yapılıyor... Güle güle!")
    sys.exit(0)

def run(interval=5.0):
    """
    Ana çalışma döngüsü.
    """
    generator = CardGenerator()

    signal.signal(signal.SIGINT, exit_handler)

    try:
        while True:
            card_data = generator.generate_card_data()
            generator.create_card_image(card_data, f"card_{int(time.time())}.png")
            time.sleep(interval)
    except Exception as e:
        print(Fore.RED + f"\nBir hata oluştu: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
