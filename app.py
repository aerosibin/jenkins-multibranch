def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    return f"Hello, {name.strip()}!"

def login(username: str, password: str) -> bool:
    """A simple mock login function."""
    if not username or not password:
        return False
    # Hardcoded credentials for demonstration purposes
    if username == "admin" and password == "secret123":
        return True
    return False
    
if __name__ == "__main__":
    print(greet("Jenkins"))