import pytest
from unittest.mock import Mock, patch

from src.services.notification_service_impl import NotificationServiceImpl
from src.gateway.gateway import Gateway
from src.utils.rate_limiter import RateLimiter

class TestNotificationServiceImpl:
    def setup_method(self):
        self.gateway = Mock(spec=Gateway)
        self.rate_limiter = Mock(spec=RateLimiter)
        self.service = NotificationServiceImpl(self.gateway, self.rate_limiter)
    
    def test_send_valid_notification(self):
        self.rate_limiter.get_key.return_value = "news:user1"
        self.rate_limiter.is_allowed.return_value = True
        
        self.service.send("news", "user1", "test message")
        
        self.gateway.send.assert_called_once_with("user1", "test message")
        self.rate_limiter.is_allowed.assert_called_once_with("news:user1")
    
    def test_send_rate_limited_notification(self):
        self.rate_limiter.get_key.return_value = "news:user1"
        self.rate_limiter.is_allowed.return_value = False
        
        with patch('builtins.print') as mock_print:
            self.service.send("news", "user1", "test message")
        
        self.gateway.send.assert_not_called()
        mock_print.assert_called_once()
    
    def test_send_invalid_parameters(self):
        with pytest.raises(ValueError):
            self.service.send("", "user1", "message")
        
        with pytest.raises(ValueError):
            self.service.send("news", "", "message")
        
        with pytest.raises(ValueError):
            self.service.send("news", "user1", "")
