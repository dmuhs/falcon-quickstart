from falcon_limiter import Limiter
from falcon_limiter.utils import get_remote_addr

rate = Limiter(key_func=get_remote_addr, default_limits="1000 per day")
