from pydantic_settings import BaseSettings
from functools import lru_cache


# BaseSetting is a subclass of BaseModel specifically designed for configuration management. It adds features like:
# 1. Automatically loading environment variables.
# 2. Supporting .env files for environment variable loading.
# 3. Providing default values for configuration fields.

# When you run the app, Pydantic will automatically:
# 1. Look for the .env file (in the current working directory where you run the application from. Not relative to the config.py file).
# 2. Automatically looks / reads for environment variables that match the field names in the Settings class.
# 3. Assign that value to the Settings instance (the variable name in your .env file must match the field name in the Settings class + case sensitive).

# .env value assignment and validation
# If it finds a match, it assigns the value to the corresponding field. If no match is found, it uses the default value (if one is provided).
# If a field has no default value (like CLAUDE_API_KEY in your example), Pydantic considers it required.
# If the required environment variable is missing, Pydantic will raise a ValidationError when you try to create a Settings instance.

# class Config:
# Both BaseModel and BaseSettings in Pydantic can have a nested Config class.
# The Config class is used to define metadata or configuration options for the pydantic parent class extend to
# the specific options available depend on whether you're using BaseModel or BaseSettings (very important)

# CORS:
# When a browser makes a cross-origin request (e.g., from https://frontend.com to https://backend.com), the browser sends an Origin header with the request.
# CORS checks the Origin header in the request from client side, which contains the domain (e.g., https://frontend.com), and compares it to the ALLOWED_ORIGINS list configured on the backend.
# in dev stage, we can allow all origins by setting ALLOWED_ORIGINS = ["*"] in the settings. But in production, we should set this to the actual prod frontend domain.
# CORS is designed to enforce security at the domain level
# why CORS happens:
# Modern web applications are often built with a decoupled architecture. where the frontend (UI) and backend (API) are developed and deployed independently.
# When a user navigates to the frontend (e.g., https://frontend.com), when it sends requests to the backend’s domain (e.g., https://backend.com/api/data).
# Since the backend domain is different from the frontend domain, this is a cross-origin request, and CORS is triggered.


class Settings(BaseSettings):
    PROJECT_NAME: str = "Resume Tailor Assistant API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    CLAUDE_API_KEY: str
    ANTHROPIC_API_KEY: str
    OPENAI_API_KEY: str
    ALLOWED_ORIGINS: list = ["*"]  # For development, allow all origins

    # MongoDB settings
    MONGO_URI: str
    MONGO_DB_NAME: str

    # Stripe settings
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    FIRECRAWL_API_KEY: str

    # we use this Config class here as a nested class to further configure the "Settings" class (This is the pydantic feature)
    class Config:
        env_file = ".env"
        case_sensitive = True


# this will cache the settings object so that it is only created once and then reused
# the cache is cleared when the process is restarted under fastapi process
# cache is take place in memory directly
@lru_cache()
def get_settings() -> Settings:
    return Settings()
