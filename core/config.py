from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    db_url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000
    
    
class ApiPrefixConfig(BaseModel):
    prefix: str = '/api'
    

class Settings(BaseSettings):
    runner: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()