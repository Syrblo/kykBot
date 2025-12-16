import os
import json
import requests
from datetime import datetime
import pytz # Saat dilimi ayarı için

# 1. Ortam değişkenlerinden şifreleri al (GitHub'a koyacağız)
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. Mesajları dosyadan oku
def mesajlari_yukle():
    with open('liste.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 3. Telegram'a mesaj gönderme fonksiyonu
def telegrama_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mesaj}
    requests.post(url, data=data)

# 4. Ana işlem
def main():
    # Türkiye saatini al
    turkey_tz = pytz.timezone('Europe/Istanbul')
    bugun = datetime.now(turkey_tz).strftime("%m-%d") # Format: Ay-Gün (Örn: 12-16)
    
    mesajlar = mesajlari_yukle()
    
    if bugun in mesajlar:
        gonderilecek_mesaj = mesajlar[bugun]
        telegrama_gonder(f"Günün Yemeği:\n{gonderilecek_mesaj}")
        print(f"Mesaj gönderildi: {bugun}")
    else:
        print(f"Bugün ({bugun}) için planlanmış bir mesaj bulunamadı.")

if __name__ == "__main__":
    main()
