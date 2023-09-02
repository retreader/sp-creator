import requests
from typing import Dict, Optional, Callable

def make_request(endpoint: str, headers: Dict[str, str], method: str = "GET", params: Optional[Dict] = None, json: Optional[Dict] = None, retries: int = 1) -> Dict:
    pass