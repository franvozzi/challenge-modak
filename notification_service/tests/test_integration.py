import pytest
from unittest.mock import patch

from src.services.notification_service_impl import NotificationServiceImpl
from src.gateway.gateway import Gateway
from src.utils.rate_limiter import RateLimiter

class TestIntegration:
    def setup_method(self):
        self.gateway = Gateway()
        self.rate_limiter = RateLimiter(max_requests=2, window_minutes=1)
        self.service = NotificationServiceImpl(self.gateway, self.rate_limiter)
    
    def test_complete_workflow(self):
        """Test the complete workflow matching Java example."""
        with patch('builtins.print') as mock_print:
            # First two should go through
            self.service.send("news", "user", "news 1")
            self.service.send("news", "user", "news 2")
            
            # Third should be rate limited
            self.service.send("news", "user", "news 3")
            
            # Different user should work
            self.service.send("news", "another user", "news 1")
            
            # Different type should work for same user
            self.service.send("update", "user", "update 1")
        
        # Verify outputs
        print_calls = [call.args[0] for call in mock_print.call_args_list]
        
        assert "sending message to user user" in print_calls
        assert "sending message to user another user" in print_calls
        assert "Rate limit exceeded for user user and type news" in print_calls
