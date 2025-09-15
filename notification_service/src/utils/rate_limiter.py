from time import time
from collections import defaultdict, deque
from datetime import timedelta

# Rate limit rules for each notification type
RATE_LIMIT_RULES = {
    "status": {"limit": 2, "window": timedelta(minutes=1).total_seconds()},
    "news": {"limit": 1, "window": timedelta(days=1).total_seconds()},
    "marketing": {"limit": 3, "window": timedelta(hours=1).total_seconds()},
}

class RateLimitExceededError(Exception):
    pass

class RateLimiter:
    def __init__(self, rules=RATE_LIMIT_RULES):
        self.rules = rules
        self.requests = defaultdict(lambda: defaultdict(deque))

    def is_allowed(self, notification_type: str, user_id: str) -> bool:
        if notification_type not in self.rules:
            raise ValueError(f"No rate limit rule defined for type: {notification_type}")
        rule = self.rules[notification_type]
        limit = rule["limit"]
        window = rule["window"]
        queue = self.requests[notification_type][user_id]
        now = time()
        while queue and queue[0] < now - window:
            queue.popleft()
        if len(queue) >= limit:
            return False
        queue.append(now)
        return True
