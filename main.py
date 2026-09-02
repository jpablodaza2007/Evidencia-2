import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
  return pymysql.connect(
      host=os.environ.get("DB_HOST", "db"),
      user=os.environ.get("DB_USER", "appuser"),
      password=os.environ.get("DB_PASSWORD", "apppassword"),
      database=os.environ.get("DB_NAME", "appdb"),
      port=3306,
  )


@app.route("/")
def health():
  return jsonify({"status": "healthy"}), 200


@app.route("/db-check")
def db_check():
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT 1;")
  conn.close()
  return jsonify({"db_status": "connected"}), 200


if __name__ == '__main__':
  app.run(
      host=os.environ.get('FLASK_HOST', '127.0.0.1'),
      port=int(os.environ.get('FLASK_PORT', 5000)),
  )
