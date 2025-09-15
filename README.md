# Notification Service Challenge from Modak

Rate-limited notification service implementation in Python.

## Problem Description

Implementation of a notification service that:

* Sends messages to users through a Gateway
* Implements rate limiting per notification type and user
* Prevents spam by limiting to n messages per minute per user/type combination

## Architecture

### Components

* **NotificationService**: Interface defining the send contract
* **NotificationServiceImpl**: Main business logic with rate limiting
* **Gateway**: Message delivery mechanism
* **RateLimiter**: Traffic control using sliding window algorithm

### Rate Limiting Strategy

* **Key Format**: `{notification_type}:{user_id}`
* **Default Limit**: 2 requests per minute per key
* **Algorithm**: Sliding window with automatic cleanup

## Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate environment (Linux/Mac)
source venv/bin/activate

# Activate environment (Windows)
venv\ScriptsActivate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python3 -m src.main
```

### Expected Output

```
sending message to user user
sending message to user user
Rate limit exceeded for user user and type news
sending message to user another user
sending message to user user
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_notification_service.py -v
```

## Design Decisions

1. **Rate Limiting**: Chose sliding window over fixed window for fair distribution.
2. **Modularity**: Separated concerns for easy testing and maintenance.
3. **Type Safety**: Used type hints throughout for better code clarity.
4. **Error Handling**: Comprehensive validation and logging.

## Performance Considerations

* Memory usage grows with the number of unique user/type combinations.
* Automatic cleanup prevents memory leaks.
* O(1) access time for rate limit checks after cleanup.

## Execution Commands

```bash
# Create and activate virtual environment
python3 -m venv venv

# Windows
env\ScriptsActivate

# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=src --cov-report=term-missing

# Run demo application
python3 -m src.main

# (Optional) Verify project structure
tree notification_service/
```

## Expected Results

### Running `python3 -m src.main`

```
=== Notification Service Demo ===
Testing rate limiting (max 2 per minute per user/type)

Sending news to user...
✓ Message sent to 'user': news 1

Sending news to user...
✓ Message sent to 'user': news 2

Sending news to user (should be rate limited)...
✗ Rate limit exceeded for user 'user' and type 'news'

Sending news to another user...
✓ Message sent to 'another user': news 1

Sending update to user (different type)...
✓ Message sent to 'user': update 1

=== Demo Complete ===
```
### Running tests

```
======================== test session starts ========================
collected 7 items

tests/test_integration.py::TestIntegration::test_complete_workflow PASSED
tests/test_notification_service.py::TestNotificationServiceImpl::test_send_valid_notification PASSED
tests/test_notification_service.py::TestNotificationServiceImpl::test_send_rate_limited_notification PASSED
tests/test_notification_service.py::TestNotificationServiceImpl::test_send_invalid_parameters PASSED
tests/test_rate_limiter.py::TestRateLimiter::test_allows_requests_under_limit PASSED
tests/test_rate_limiter.py::TestRateLimiter::test_blocks_requests_over_limit PASSED
tests/test_rate_limiter.py::TestRateLimiter::test_different_keys_independent_limits PASSED

======================== 7 passed in 0.XX s ========================
```
