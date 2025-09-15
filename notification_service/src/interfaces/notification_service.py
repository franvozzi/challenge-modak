from abc import ABC, abstractmethod

class NotificationService(ABC):
    """Interface for notification service"""

    @abstractmethod
    def send(self, notification_type: str, user_id: str, message: str) -> None:
        """Send notification to user"""
        pass
