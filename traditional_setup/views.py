# returns dynamic response
def view(path):
    if path == "/":
        return f"You are at Homepage: ({path})"
    else:
        return f"You are at some other page: ({path})"
