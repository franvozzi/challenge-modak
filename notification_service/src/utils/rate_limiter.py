from collections import defaultdict, deque
from datetime import datetime, timedelta
from typing import Dict, Deque

class RateLimiter:
    """Rate limiter for controlling notification frequency."""
    
    def __init__(self, max_requests: int = 2, window_minutes: int = 1):
        self.max_requests = max_requests
        self.window_minutes = window_minutes
        self._requests: Dict[str, Deque[datetime]] = defaultdict(deque)
    
    def is_allowed(self, key: str) -> bool:
        """Check if request is allowed based on rate limiting."""
        now = datetime.now()
        window_start = now - timedelta(minutes=self.window_minutes)
        
        # Clean old requests
        requests = self._requests[key]
        while requests and requests[0] < window_start:
            requests.popleft()
        
        # Check if under limit
        if len(requests) < self.max_requests:
            requests.append(now)
            return True
        
        return False
    
    def get_key(self, notification_type: str, user_id: str) -> str:
        """Generate key for rate limiting."""
        return f"{notification_type}:{user_id}"
