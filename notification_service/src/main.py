from .gateway.gateway import Gateway
from .services.notification_service_impl import NotificationServiceImpl

def main():
    """Main function to demonstrate the notification service."""
    service = NotificationServiceImpl(Gateway())
    
    print("=== Notification Service Demo ===")
    print("Testing rate limiting (max 2 per minute per user/type)\n")
    
    print("[1] Sending news to user...")
    service.send("news", "user", "news 1")
    
    print("[2] Sending news to user...")
    service.send("news", "user", "news 2")
    
    print("[3] Sending news to user (should be rate limited)...")
    service.send("news", "user", "news 3")
    
    print("[4] Sending news to another user...")
    service.send("news", "another user", "news 1")
    
    print("[5] Sending update to user (different type)...")
    service.send("update", "user", "update 1")
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
