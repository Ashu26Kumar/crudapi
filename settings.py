
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROSTGRES_URL :str 
    POSTGRES_PORT :int
    POSTGRES_DB  :str
    POSTGRES_USER :str
    POSTGRES_PASSWORD :str

    model_config = SettingsConfigDict(
        env_file= "./.env",
        env_ignore_empty=True
    )



setting = Settings()

print(setting.PROSTGRES_URL)