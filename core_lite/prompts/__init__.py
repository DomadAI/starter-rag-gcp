import os
from dotenv import load_dotenv
from .domad_rag_prompt import STRICT_PROMPT, VERBOSE_PROMPT, DEFAULT_PROMPT

load_dotenv()
style = os.getenv("PROMPT_STYLE", "strict").lower()

if style == "strict":
    SELECTED_PROMPT = STRICT_PROMPT
elif style == "verbose":
    SELECTED_PROMPT = VERBOSE_PROMPT
else:
    SELECTED_PROMPT = DEFAULT_PROMPT
