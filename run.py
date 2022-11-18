import os
from datetime import datetime
from pyrogram import Client, filters
from colorama import init, Fore, Style

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


init(autoreset=True)

api_id = "11111" # change me
api_hash = "2222222222" # change me
app = Client("my_account", api_id=api_id, api_hash=api_hash)

prefix = "."
own_chat = -100000000000 # change me

def get_chat_id(client, message, channel_name):
    try:

        messages_id = []
        titles = []
        for dialog in app.get_dialogs():
            if dialog.chat.title:
                titles.append(dialog.chat.title)
            elif dialog.chat.first_name:
                titles.append(dialog.chat.first_name)
            
            messages_id.append(dialog.chat.id)

        c = 0
        for i in titles:
            if channel_name == i:
                return f"{messages_id[c]}"
            else:
                pass
            c += 1
    except Exception as e:
        pass        


@app.on_message(filters.command("get", prefixes=prefix))
def videos(client, message):
    T1 = datetime.now()
    count = 0
    splited_message = message.text.split(" ")
    limit = False
    try:
        longer = float(splited_message[1])
        less = float(splited_message[2])
        channel_name = " ".join(splited_message[4:])
        chat_id = get_chat_id(client, message, channel_name=channel_name)
        if splited_message[3]:
            limit = int(splited_message[3])
        
    except Exception as e:
        message.edit_text(f"Error: {e}")
        # print(f"{e}")


    try:
        print(Style.BRIGHT + Fore.WHITE + f"[&] Looking for videos longer than " + Fore.YELLOW + str(longer) + Fore.WHITE + " and less than " + Fore.YELLOW + str(less) + Fore.WHITE + "...")

        for message in app.get_chat_history(chat_id):
            if message.video:
                duration = (((message.video.duration / 60) * 100) // 1) / 100
                if duration >= longer and duration <= less:
                    count += 1
                    if count == limit + 1:
                        break
                    
                    client.copy_message(
                        chat_id=own_chat,
                        from_chat_id=chat_id,
                        message_id=message.id
                    )
                    print(Fore.GREEN + f"[*] Video duration: {duration}")
                else:
                    pass 
            else:
                continue


        T2 = datetime.now()
        finall_tile = T2 - T1
        print(Style.BRIGHT + "[*] Found " + Fore.CYAN + str(count - 1) + Fore.WHITE + " videos in " + Fore.YELLOW + str(finall_tile) + Fore.WHITE + " seconds. Copy to your channel.")
        
        print(Fore.GREEN + "[*] Done.")
    except Exception as e:
        pass



if __name__ == "__main__":
    print(Style.BRIGHT + Fore.GREEN + "[*] Scritp is running.")
    app.run()
