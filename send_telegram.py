import requests
import os

# Obtener variables desde las GitHub Secrets o definirlas aquí
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MESSAGE = "¡Hola! Este es un mensaje automático desde GitHub Actions."

def send_telegram_message():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": MESSAGE}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Mensaje enviado correctamente.")
    else:
        print(f"Error al enviar mensaje: {response.text}")

if __name__ == "__main__":
    send_telegram_message()
