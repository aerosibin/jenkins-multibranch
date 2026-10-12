def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    return f"Hello, {name.strip()}!"


if __name__ == "__main__":
    print(greet("Jenkins"))