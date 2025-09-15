class Gateway:
    """Gateway for sending messages to users."""
    
    def send(self, user_id: str, message: str) -> None:
        """Send message to user."""
        print(f"✓ Message sent to '{user_id}': {message}")
