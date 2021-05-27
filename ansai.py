from random import choice as rch

user = ""


def respond(string):
    print(f"\033[36m{string}\033[0m")


print(
    "Hello! I am AHI, I will try to understand what you type,\nbut I am still a work in progress.\n"
)

greetings = ["hi", "hello", "hai", "hoi", f"how are {["you", "u", "u?"]}", f"{["hello", "hi", "hai", "hoi"]} there"]
greet = [
    "And hello to you.", "Hai!", "How are you?", "Hello.", "Hi",
    "Nice to meet you."
]

while True:
    user = input("... ").casefold()
    txt = user.split(' ')

    # print(txt)

    if any(word in user for word in greetings):
        respond(rch(greet))

    elif user.strip(' ') == '':
        pass

    else:

        idk = [
            "I am sorry, but I don't seem to understand that...",
            f"I don't understand \033[31m{user}\033[0m"
        ]

        respond(rch(idk))
