TEEN_TITANS = [
    {
        "name": "Beast Boy",
        "password": "bbrocks69420",
        "security_question": "What color am I?",
        "security_answer": "Green"
    },
    {
        "name": "Raven",
        "password": "azarath_metrion_zinthos",
        "security_question": "What is my house name?",
        "security_answer": "Azarath"
    },
    {
        "name": "Starfire",
        "password": "password",
        "security_question": "What is my pet name?",
        "security_answer": "Silkie"
    },
    {
        "name": "Cyborg",
        "password": "ERRBDK",
        "security_question": "What is my car name?",
        "security_answer": "T-Car"
    },
    {
        "name": "Robin",
        "password": "bruce_wayn3",
        "security_question": "",
        "security_answer": ""
    },
]

def find_name(target_name: str) -> dict:
    """
    This function will take a string containing a users input for what Titan they want to log in as.
    If the Titan Name they type is valid, the function should return a dictionary with that information.
    Else if not found,

    :param target_name: String containing the users input for what teen titans.
    :return: Dict OR None. If none is returned the character doesn't exist.
    """
    a = None
    for item in TEEN_TITANS:
        if target_name == item["name"]:
            a = item
    return a

def validate_password(character_data: dict) -> bool:
    attempts1 = 0
    passFound = False

    # Make sure a user doesn't use more than three attempts to enter his/her password.
    while attempts1 < 3:
        password = input(f"Enter the password for {character_data['name']}: ")
        if password == character_data['password']:
            passFound = True
            break
        else:
            attempts1 += 1
            print(f"Password was wrong. You have {3 - attempts1} attempt(s) left")

    return passFound

def validate_security_question(character_data: dict) -> bool:
    print(f"Answer the security question for: {character_data['name']}")
    attempts1 = 0
    access = False

    # Make sure a user doesn't use more than three attempts to enter his/her password.
    while attempts1 < 3:
        response: str = input(f"{character_data['security_question']}: ")
        if response == character_data['security_answer']:
            access = True
            break
        elif response.lower() == character_data['security_answer']:
            attempts1 += 1
            print(f"Security question answer was wrong. Watch your capitalization. You have {3 - attempts1} attempt(s) left")
        else:
            attempts1 += 1
            print(f"Security question answer was wrong. You have {3 - attempts1} attempt(s) left")

    return access


# Actual Application

titans_name = input("What is your teen titan's name: ").title()

character_info = find_name(titans_name)

#If the character name is found
if character_info:
    # Validate the characters password
    passInformation = validate_password(character_info)

    if passInformation:
        # VALIDATE SECURITY QUESTIONS
        securityCheck = validate_security_question(character_info)

        if securityCheck:
            print("ACCESS APPROVED")
        else:
            print("ACCESS DENIED.")

    else:
        print("Out of attempts. ACCESS DENIED.")

else:
    print("Character not found.")


