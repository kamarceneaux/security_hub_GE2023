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

def find_name(target_name: str) -> dict:
    a = None
    for item in TEEN_TITANS:
        if target_name == item["name"]:
            a = item

    return a

def validate_password(character_data: dict) -> bool:
    attempts1 = 0
    while attempts1 < 3:
        password = input(f"Enter the password for {character_data['name']}: ")
        if password == character_data['password']:
            print(password)
        else:
            attempts1 += 1
            print(f"Password was wrong. You have {3 - attempts1} attempt(s) left")


