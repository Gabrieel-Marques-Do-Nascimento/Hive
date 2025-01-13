from .token_crietor import TokenCreator, TokenUpdate
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

jwt_config: dict = {
    "TOKEN_KEY": str(os.getenv("TOKEN_KEY") or "2202116123"),
    "EXP_TIME_MIN": int(os.getenv("EXP_TIME_MIN") or 30),
    "REFRESH_TIME_MIN": int(os.getenv("REFRESH_TIME_MIN") or 15),
    "EXP_TIME_DAY": int(os.getenv("EXP_TIME_DAY") or 15),
    "REFRESH_TIME_DAY": int(os.getenv("REFRESH_TIME_DAY") or 5),
    "BACKUP_URL": str(os.getenv("BACKUP_URL") or 'http://127.0.0.1:5001')
}


token_crietor = TokenCreator(token_key=jwt_config['TOKEN_KEY'],
                             exp_time_min=jwt_config['EXP_TIME_MIN'],
                             refresh_time_min=jwt_config['REFRESH_TIME_MIN'])


token_update = TokenUpdate(token_key=jwt_config['TOKEN_KEY'],
                           exp_time_day=jwt_config['EXP_TIME_DAY'],
                           refresh_time_day=jwt_config['REFRESH_TIME_DAY'])

if __name__ == '__main__':
    pass
