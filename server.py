import os
import mysql.connector
from flask import Flask, request, jsonify
import numpy as np
import cv2
import boto3
import os
import io
from PIL import Image
import time
from datetime import datetime
import uuid


app = Flask(__name__)


def save_label_to_db(label, confidence):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO detections (label) VALUES (%s, %s, %d)", (label, datetime.now(), confidence))
    conn.commit()
    cursor.close()
    conn.close()

# Function to save the image to S3
def save_image_to_s3(image, filename):
    s3_client = boto3.client('s3')
    image_buffer = io.BytesIO()
    image.save(image_buffer, 'JPEG')
    image_buffer.seek(0)
    s3_client.upload_fileobj(image_buffer, os.environ.get("bucket"), filename)


@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    label = data.get("label")
    confidence = data.get("confidence")
    image_data = data.get("image")
    save_image_to_s3(image_data, uuid.uuid4())
    save_label_to_db(label, confidence)


def get_db_conn():
     return mysql.connector.connect(
        user='admin', 
        password=os.environ.get["pass"],
        host=os.environ.get["host"],
        database='sys'
    )

if __name__ == '__main__':
    app.run(debug=True)