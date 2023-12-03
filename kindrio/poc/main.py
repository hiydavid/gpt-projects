# import
import pickle
import json
from chat import ChatSession
from user import User

# run
if __name__ == "__main__":

    # request input
    print("\nWELCOME!\n")

    print("Please enter your information below...")
    input_login = input("> Type 'new user' or 'resume chat': ")
    if input_login == "new user":

        # get info
        input_name = input("> Name: ")
        input_email = input("> Email: ")
        input_dob = input("> Date of birth (YYYY-MM-DD): ")
        input_identity = input("> Do you identify as 'dad', 'mom', or 'parent'?: ")
        input_child_name = input("> Child's name: ")
        input_child_dob = input("> Child's date of birth (YYYY-MM-DD): ")
        input_goals = input("> What's your parenting goals?: ")

        # instantiate user
        user = User(
            name=input_name, 
            email=input_email, 
            dob=input_dob, 
            identity=input_identity, 
            child_name=input_child_name, 
            child_dob=input_child_dob, 
            goals=input_goals
        )
        print(user)

        # pickle user object
        with open(f"./users/user_{user.name}.pkl", "wb") as f:
            pickle.dump(user, f)
        
        # init session
        session = ChatSession(user=user, chat_history=None)

    elif input_login == "resume chat":
        
        # ask for name
        input_name = input("> Name: ")

        # load user object
        with open(f"./users/user_{input_name}.pkl", "rb") as f:
            user = pickle.load(f)
            print(user)
        
        # load chat history
        with open(f"./history/chat_{input_name}.json", "r") as f:
            chat_history = json.load(f)
        
        # init session
        session = ChatSession(user=user, chat_history=chat_history)

    else:
        print("\nSomething's wrong. Exiting program.\n")

    # begin chat
    print("\nHi, what can I help you with today? ")
    
    while True:
        conversation_text = input("\nPlease enter your message or 'quit' to exit: ")
        if conversation_text.lower() == 'quit':
            print("\nGOOD BYE!\n")
            break
        print("\n-----RESPONSE START-----\n")
        session.send_chat_message(user_prompt=conversation_text)
        print("\n-----RESPONSE END-----\n")
        print("")