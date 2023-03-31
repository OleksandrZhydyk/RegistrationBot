from pydantic import BaseSettings, Field


class BotConfig(BaseSettings):
    BOT_ACCESS_TOKEN: str = Field(..., env='BOT_ACCESS_TOKEN')
    BACKEND_HOST: str = Field(..., env='BACKEND_HOST')
    HOST: str = Field(..., env='HOST')

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


conf_bot = BotConfig()
