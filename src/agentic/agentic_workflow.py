import os
import json
#from openai import ChatOpenAI
from typing import List, Literal, TypedDict, Dict
import logging

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class GPTHandler:

    def __init__(self, 
                 model :str = 'o4-mini', 
                 reasoning_effort : Literal['low', 'medium', 'high'] = 'medium' ):
        
        self.model = model
        self.reasoning_effort = reasoning_effort
        self.client = OpenAI(api_key = openai_api_key)

        logger.info("OPENAI Client Loaded")

    def build_messages( self, system : str,  user: str ) -> List[Dict[str,str]]:
        
        return [
            {"role":"system", "content":system},
            {"role":"user", "content": user}
        ]
    
    def generate(self, system_prompt: str, user_prompt : str, max_tokens : int ):

        response = self.client.chat.completions.create(
            model=self.model,
            messages = self.build_messages(system_prompt, user_prompt)
            max_completion_tokens=max_tokens,
        )

        return response.choices[0].message.content
        

handler = GPTHandler(model = 'gpt-4o')

