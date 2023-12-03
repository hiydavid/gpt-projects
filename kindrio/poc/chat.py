# import libs
import os
import time
from datetime import datetime
import json
from dotenv import load_dotenv
import openai
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    messages_from_dict,
    messages_to_dict,
)

# get key from .env
_ = load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
    
# chat
class ChatSession():

    def __init__(self, user, chat_history=None):

        # load user
        self.user = user

        # load chat history if there is one
        if chat_history is not None:
            self.chat_history = messages_from_dict(chat_history)
        
        # if no chat history, start a new one
        else:
            self.chat_history = [
                SystemMessage(content=self.user.system_prompt),
                AIMessage(
                    content="Hi, what can I help you with today?", 
                    additional_kwargs={"timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}"}
                )
            ]
        
        # initialize chat
        self.chat = ChatOpenAI(
            model='gpt-4',
            temperature=0.1,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

    def send_chat_message(self, user_prompt, get_results=True):

        # append user message
        self.chat_history.append(
            HumanMessage(
                content=user_prompt,
                additional_kwargs={"timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}"}
            )
        )
        
        # send message to chat
        start_time = time.time()
        with get_openai_callback() as cb:
            response = self.chat([SystemMessage(content=self.user.system_prompt)] + self.chat_history[-10:])
            response.additional_kwargs = {"timestamp": f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')}"}
            self.chat_history.append(response)
            self.response_content = response.content
        end_time = time.time()
        self.response_time = end_time - start_time
        self.response_total_tokens = cb.total_tokens
        self.response_prompt_tokens = cb.prompt_tokens
        self.response_completion_tokens = cb.completion_tokens
        self.response_total_cost = round(cb.total_cost, 4)
        self.response_successful_requests = cb.successful_requests
        print(self.response_content)

        # save chat history by overriding
        chat_history_dict = messages_to_dict(self.chat_history)
        with open(f"./history/chat_{self.user.name}.json", "w") as f:
            json.dump(chat_history_dict, f)

        # print chat metadata
        if get_results:
            print("")
            print("Total tokens used:      ", cb.total_tokens)
            print("Prompt tokens used:     ", cb.prompt_tokens)
            print("Completion tokens used: ", cb.completion_tokens)
            print("Total prompt cost:      ", round(cb.total_cost, 4))
            print("Successful requests:    ", cb.successful_requests)
        else:
            pass

