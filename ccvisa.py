import time
from faker import Faker

fake = Faker("tr_TR")  # Türkçe desteği

def generate_credit_card():
    time.sleep(3)  # İlk bekleme
    return {
        "Kart Sahibi": fake.name()
        "Kart Sağlayıcı": fake.credit_card_provider(),
        "Kart Numarası": fake.credit_card_number(card_type="visa"),  # Visa formatında üretme
        "Son Kullanma Tarihi": fake.credit_card_expire(),
        "CVV": fake.random_int(min=100, max=999),  # Rastgele 3 haneli CVV
    }

credit_card = generate_credit_card()
for key, value in credit_card.items():
    time.sleep(3)  # Her adımda bekleme ekleyerek daha kontrollü bir çıktı sağlıyoruz
    print(f"{key}: {value}")
