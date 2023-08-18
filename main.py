from utilities import find_name, validate_password, validate_security_question

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


