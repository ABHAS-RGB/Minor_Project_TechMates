from flask import Flask, jsonify, request
import math
import time
import random
import os

app = Flask(__name__)



# Home Endpoint

@app.route("/")
def home():
    return jsonify({
        "message": "Cloud Auto-Scaling Test Application",
        "status": "running",
        "server_pid": os.getpid()
    })



# CPU Load Simulation

@app.route("/cpu-load")
def cpu_load():

    start_time = time.time()

    total = 0

    # Heavy CPU workload
    for i in range(1, 8000000):
        total += math.sqrt(i) * math.sin(i)

        if i % 1000000 == 0:
            time.sleep(0.05)

    duration = time.time() - start_time

    return jsonify({
        "task": "CPU Load Simulation",
        "result": round(total, 2),
        "processing_time_seconds": round(duration, 4)
    })



# Memory Load Simulation

@app.route("/memory-load")
def memory_load():

    data = [random.random() for _ in range(1000000)]

    return jsonify({
        "task": "Memory Load Simulation",
        "items_created": len(data)
    })



# Request Processing Simulation

@app.route("/process")
def process_request():

    user = request.args.get("user", "anonymous")

    time.sleep(random.uniform(0.2, 0.5))

    return jsonify({
        "message": "Request processed",
        "user": user,
        "timestamp": time.time()
    })



# Health Checkkk
 

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "server_pid": os.getpid()
    })


 
# Run Flask App

if __name__ == "__main__":
    print("Starting Cloud Auto-Scaling Test Server...")
    app.run(host="0.0.0.0", port=5000)
