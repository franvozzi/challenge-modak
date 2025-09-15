import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

from src.utils.rate_limiter import RateLimiter

class TestRateLimiter:
    def setup_method(self):
        self.rate_limiter = RateLimiter(max_requests=2, window_minutes=1)
    
    def test_allows_requests_under_limit(self):
        key = "test:user1"
        
        assert self.rate_limiter.is_allowed(key) is True
        assert self.rate_limiter.is_allowed(key) is True
    
    def test_blocks_requests_over_limit(self):
        key = "test:user1"
        
        # Use up the limit
        self.rate_limiter.is_allowed(key)
        self.rate_limiter.is_allowed(key)
        
        # Should be blocked
        assert self.rate_limiter.is_allowed(key) is False
    
    def test_different_keys_independent_limits(self):
        key1 = "news:user1"
        key2 = "update:user1"
        
        # Different keys should have independent limits
        assert self.rate_limiter.is_allowed(key1) is True
        assert self.rate_limiter.is_allowed(key1) is True
        assert self.rate_limiter.is_allowed(key2) is True
        assert self.rate_limiter.is_allowed(key2) is True
