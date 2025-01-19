from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "database_service",
    "user": "db_user",
    "password": "db_password",
    "database": "app_db"
}

@app.route("/", methods=["GET"])
def status_check():
    return render_template("status_check.html", service="API", status="Operational")

@app.route("/api/add-user", methods=["POST"])
def add_user():
    data = request.json
    user_name = data.get("name")
    if not user_name:
        return jsonify({"error": "Name is required"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (user_name,))
        conn.commit()
        return jsonify({"message": f"User '{user_name}' User is added to the database successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route("/api/get-users", methods=["GET"])
def get_users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
