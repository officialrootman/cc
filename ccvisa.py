import time
from faker import Faker

fake = Faker()

while True:
    print("-" * 32)
    print("Kart Bulundu!")
    print("Kart Sahibi:", fake.name())
    print("Kart Numarası:", fake.credit_card_number(card_type="visa"))
    print("Son Kullanma Tarihi:", fake.credit_card_expire())
    print("CVV:", fake.credit_card_security_code())
    print("-" * 32)  # Ayracı ekleyelim
    
    time.sleep(3)  # 3 saniye bekle
