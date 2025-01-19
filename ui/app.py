from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API service URL (change port to 5002)
API_URL = "http://api_service:5002"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_name = request.form["user_name"]
        response = requests.post(f"{API_URL}/api/add-user", json={"name": user_name})
        if response.status_code == 200:
            return f"User '{user_name}' User is added!!"
        return f"Failed to add user. Reason: {response.json().get('error')}"

    response = requests.get(f"{API_URL}/api/get-users")
    users = response.json() if response.status_code == 200 else []
    return f"""
        <h1>Registration</h1>
        <form method="POST">
            Enter your name: <input type="text" name="user_name" required>
            <button type="submit">Submit</button>
        </form>
        <h2>Users That are registerd</h2>
        <ul>
            {''.join([f'<li>{user["id"]}: {user["name"]}</li>' for user in users])}
        </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
