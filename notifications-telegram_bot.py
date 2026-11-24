import os
import json
import urllib.request


def send_message(message):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = json.dumps({
        "chat_id": chat_id,
        "text": message
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
            if not result.get("ok"):
                raise RuntimeError("Telegram rejected message")
    except Exception:
        raise RuntimeError("Telegram delivery failed") from None

    print("Notification sent successfully.")


if __name__ == "__main__":
    send_message(
        "🟢 QUANT TRADING V2\n\n"
        "Telegram connection established.\n"
        "Mode: Paper Testing\n"
        "Automatic trading: Disabled\n"
        "System status: Online"
    )
