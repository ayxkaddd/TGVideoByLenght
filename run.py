import os
from datetime import datetime
from pyrogram import Client, filters
from colorama import init, Fore, Style


if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

init(autoreset=True)

# you can find it at my.telegram.org -> API development tools
api_id = "api_id"
api_hash = "api_hash"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
own_chat = "your_chat_id"
prefix = "."


@app.on_message(filters.command("get_id", prefixes=prefix))
def get_channel_id(client, message):
    query = " ".join(message.text.split(" ")[1:])

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
        if query == i:
            message.edit(f"ID for {query}: `{messages_id[c]}`")
            return f"Id for {query}: {messages_id[c]}"
        else:
            pass
        c += 1
    

@app.on_message(filters.command("get", prefixes=prefix))
def videos(client, message):
    T1 = datetime.now()
    count = 0
    splited_message = message.text.split(" ")
    limit = False
    try:
        longer = float(splited_message[2])
        less = float(splited_message[3])
        chat_id = splited_message[1]
        if splited_message[4]:
            limit = int(splited_message[4])
    except Exception as e:
        print(f"{e}")


    print(Style.BRIGHT + Fore.WHITE + f"[&] Looking for videos longer than " + Fore.YELLOW + str(longer) + Fore.WHITE + " and less than " + Fore.YELLOW + str(less) + Fore.WHITE + "...")

    for message in app.get_chat_history(chat_id):
        if message.video:
            duration = (((message.video.duration / 60) * 100) // 1) / 100
            if duration >= longer and duration <= less:
                count += 1
                if limit:
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


print(Style.BRIGHT + Fore.GREEN + "[*] Scritp is running.")

app.run()
