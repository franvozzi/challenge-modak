import logging
from typing import Optional

from ..interfaces.notification_service import NotificationService
from ..gateway.gateway import Gateway
from ..utils.rate_limiter import RateLimiter

logger = logging.getLogger(__name__)

class NotificationServiceImpl(NotificationService):
    """Implementation of notification service with rate limiting."""
    
    def __init__(self, gateway: Gateway, rate_limiter: Optional[RateLimiter] = None):
        self.gateway = gateway
        self.rate_limiter = rate_limiter or RateLimiter(max_requests=2, window_minutes=1)
    
    def send(self, notification_type: str, user_id: str, message: str) -> None:
        """Send notification with rate limiting."""
        if not notification_type or not user_id or not message:
            raise ValueError("All parameters must be non-empty")
        
        rate_key = self.rate_limiter.get_key(notification_type, user_id)
        
        if self.rate_limiter.is_allowed(rate_key):
            self.gateway.send(user_id, message)
        else:
            print(f"✗ Rate limit exceeded for user '{user_id}' and type '{notification_type}'")
