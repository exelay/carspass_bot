from typing import List, AnyStr

from environs import Env

env = Env()
env.read_env()

# Environment variables
TOKEN: AnyStr = env.str("TOKEN")
ADMINS: List = env.list("ADMINS")
