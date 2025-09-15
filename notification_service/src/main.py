from src.services.notification_service_impl import NotificationServiceImpl
from src.gateway.gateway import Gateway
from src.utils.rate_limiter import RateLimitExceededError
import time

def main():
    service = NotificationServiceImpl(Gateway())
    print("=== Notification Service Demo ===")
    print("Testing rate limiting with multiple rules")

    try:
        service.send("status", "user1", "Status message 1")
        print("✓ Status 1 sent to user1")
        service.send("status", "user1", "Status message 2")
        print("✓ Status 2 sent to user1")
        service.send("status", "user1", "Status message 3")
        print("✓ Status 3 sent to user1")
    except RateLimitExceededError as e:
        print(f"✗ {e}")

    try:
        service.send("news", "user1", "News message 1")
        print("✓ News 1 sent to user1")
        service.send("news", "user1", "News message 2")
        print("✓ News 2 sent to user1")
    except RateLimitExceededError as e:
        print(f"✗ {e}")

    try:
        service.send("marketing", "user1", "Marketing message 1")
        print("✓ Marketing 1 sent to user1")
        service.send("marketing", "user1", "Marketing message 2")
        print("✓ Marketing 2 sent to user1")
        service.send("marketing", "user1", "Marketing message 3")
        print("✓ Marketing 3 sent to user1")
        service.send("marketing", "user1", "Marketing message 4")
        print("✓ Marketing 4 sent to user1")
    except RateLimitExceededError as e:
        print(f"✗ {e}")

    try:
        service.send("status", "user2", "Status message 1")
        print("✓ Status 1 sent to user2")
    except RateLimitExceededError as e:
        print(f"✗ {e}")

    print("=== Demo Complete ===")

if __name__ == "__main__":
    main()
