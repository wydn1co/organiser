import json
import os

DATA_FILE = "accounts.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def add_account(user_id, platform, username, password):
    data = load_data()
    user_id = str(user_id)
    platform = platform.lower()
    
    if user_id not in data:
        data[user_id] = {}
    
    if platform not in data[user_id]:
        data[user_id][platform] = []
    
    # Check if account already exists
    for account in data[user_id][platform]:
        if account['username'] == username:
            account['password'] = password
            save_data(data)
            return True
            
    data[user_id][platform].append({
        "username": username,
        "password": password
    })
    save_data(data)
    return True

def get_accounts(user_id, platform):
    data = load_data()
    user_id = str(user_id)
    platform = platform.lower()
    
    if user_id in data and platform in data[user_id]:
        return data[user_id][platform]
    return []

def get_platforms(user_id):
    data = load_data()
    user_id = str(user_id)
    
    if user_id in data:
        return list(data[user_id].keys())
    return []
