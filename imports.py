import base64
from io import BytesIO
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from urllib.request import urlretrieve
import boto3, botocore
import cv2
# from keras.layers import *
import numpy as np
# from tensorflow.keras.models import Sequential
from collections import deque
from keras.models import model_from_json
