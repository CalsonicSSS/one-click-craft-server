from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
from app.config import get_settings

main_config_settings = get_settings()

# Initialize the model
def initialize_llm(model_name: Literal["openai", "anthropic"], model: str, temperature: float, max_tokens: int):
    if model_name == "openai":
        return ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens, api_key=main_config_settings.OPENAI_API_KEY)
    elif model_name == "anthropic":
        return ChatAnthropic(model=model, temperature=temperature, max_tokens=max_tokens, api_key=main_config_settings.ANTHROPIC_API_KEY)
    else:
        raise ValueError(f"Invalid model name: {model_name}")