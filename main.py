from security_hub_information.utilities import find_name, validate_password, validate_security_question

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


