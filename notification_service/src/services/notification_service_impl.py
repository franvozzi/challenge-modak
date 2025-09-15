from src.interfaces.notification_service import NotificationService
from src.utils.rate_limiter import RateLimiter, RateLimitExceededError
from src.gateway.gateway import Gateway

class NotificationServiceImpl(NotificationService):
    def __init__(self, gateway: Gateway):
        self.gateway = gateway
        self.rate_limiter = RateLimiter()

    def send(self, notification_type: str, user_id: str, message: str) -> None:
        if not self.rate_limiter.is_allowed(notification_type, user_id):
            raise RateLimitExceededError(f"Rate limit exceeded for user {user_id} and type {notification_type}")
        self.gateway.send(user_id, message)
