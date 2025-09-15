# Notification Service Challenge from Modak

Rate-limited notification service implementation in Python.

## Problem Description

Implementation of a notification service that:

* Sends messages to users through a Gateway
* Implements rate limiting per notification type and user
* Prevents spam by enforcing configurable limits per type (e.g., status: 2 per minute, news: 1 per day, marketing: 3 per hour)
* Rejects requests that exceed the defined limits for each type/user combination

## Architecture

### Components

* **NotificationService**: Interface defining the send contract
* **NotificationServiceImpl**: Main business logic with rate limiting
* **Gateway**: Message delivery mechanism
* **RateLimiter**: Traffic control using sliding window algorithm with configurable rules per type

### Rate Limiting Strategy

* **Key Format**: `{notification_type}:{user_id}`
* **Configurable Limits**: Defined per type with custom limits and time windows (e.g., minutes, hours, days)
* **Algorithm**: Sliding window with automatic cleanup for fair and precise rate control

## Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate environment (Linux/Mac)
source venv/bin/activate

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python3 -m src.main
```

### Expected Output

```
=== Notification Service Demo ===
Testing rate limiting with multiple rules
✓ Status 1 sent to user1
✓ Status 2 sent to user1
✗ Rate limit exceeded for user user1 and type status
✓ News 1 sent to user1
✗ Rate limit exceeded for user user1 and type news
✓ Marketing 1 sent to user1
✓ Marketing 2 sent to user1
✓ Marketing 3 sent to user1
✗ Rate limit exceeded for user user1 and type marketing
✓ Status 1 sent to user2
=== Demo Complete ===
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

1. **Rate Limiting**: Chose sliding window over fixed window for fair distribution and precise control across varying time windows.
2. **Modularity**: Separated concerns (interface, implementation, utils) for easy testing and maintenance.
3. **Type Safety**: Used type hints throughout for better code clarity.
4. **Error Handling**: Comprehensive validation, logging, and explicit rejection via custom exceptions for over-limit requests.
5. **Extensibility**: Configurable rules allow easy addition of new notification types without code changes.

## Performance Considerations

* Memory usage grows with the number of unique user/type combinations.
* Automatic cleanup prevents memory leaks.
* O(1) access time for rate limit checks after cleanup.

## Execution Commands

```bash
# Create and activate virtual environment
python3 -m venv venv

# Windows
venv\Scripts\activate

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
Testing rate limiting with multiple rules
✓ Status 1 sent to user1
✓ Status 2 sent to user1
✗ Rate limit exceeded for user user1 and type status
✓ News 1 sent to user1
✗ Rate limit exceeded for user user1 and type news
✓ Marketing 1 sent to user1
✓ Marketing 2 sent to user1
✓ Marketing 3 sent to user1
✗ Rate limit exceeded for user user1 and type marketing
✓ Status 1 sent to user2
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
