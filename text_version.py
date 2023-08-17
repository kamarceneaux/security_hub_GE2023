# TEEN_TITANS = ["Beast Boy", "Raven", "Starfire", "Cyborg", "Robin"]

TEEN_TITANS = [
    {
        "name": "Beast Boy",
        "password": "bbrocks69420",
        "security_question": "",
        "security_answer": ""
    },
    {
        "name": "Raven",
        "password": "azarath_metrion_zinthos",
        "security_question": "",
        "security_answer": ""
    },
    {
        "name": "Starfire",
        "password": "password",
        "security_question": "",
        "security_answer": ""
    },
    {
        "name": "Cyborg",
        "password": "ERRBDK",
        "security_question": "",
        "security_answer": ""
    },
    {
        "name": "Robin",
        "password": "bruce_wayn3",
        "security_question": "",
        "security_answer": ""
    },
]

def errorMessage():
    return "ACCCESS DENIED"

# Ask for input
titans_name = input("What is your teen titan's name: ").title()

a = None
active = True

# Find Name
for item in TEEN_TITANS:
    if titans_name == item["name"]:
        a = item

while active:
    if a != None:
        # PROMPT PASSWORD
        attempts1 = 0
        while attempts1 < 3 and a == 1:
            password = input(f"Enter the password for {a['name']}: ")
            if password == a['password']:
                print(password)
            else:
                attempts1 += 1
                print(f"Password was wrong. You have {3 - attempts1} attempt(s) left.")
        else:
            active = False
    else:
        active = False
else:
    print(errorMessage())

