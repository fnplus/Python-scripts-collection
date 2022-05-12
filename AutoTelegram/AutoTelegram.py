from telethon.sync import TelegramClient
from telethon.errors import TimedOutError, TimeoutError, UserPrivacyRestrictedError, FloodWaitError

import config

client = TelegramClient("session", config.api_id, config.api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(config.phone)
    client.sign_in(config.phone, input('Enter the code: '))

user = client.get_entity(input("User phone, or username: "))
times = int(input("How many times to send: "))
message = input("Message: ")

print("!WARNING! You may get ban or restrictions for your account! Use at your own risk!")
if input("Are you sure? (y/n) ").lower() != "y":
    print("Aborting...")
    exit(0)

for i in range(times):
    try:
        client.send_message(user, message)
    except TimeoutError | TimedOutError | FloodWaitError:
        print("Telegram blocked you for flodding")
    except UserPrivacyRestrictedError:
        print("User cant accept messages")
    except Exception as e:
        print("Unknown error:", e)
