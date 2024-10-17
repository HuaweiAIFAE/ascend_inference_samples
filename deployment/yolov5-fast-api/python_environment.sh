#!/bin/bash

# create python virtual environment
echo "[ENV] Virtual Environment Preparation Starting!"
python3 -m venv yolov5_npu_inference
source yolov5_npu_inference/bin/activate
echo "[ENV] Virtual Environment yolov5_npu_inference activated!"

# install necessary python libs
echo "[ENV] Installing dependecies!"
pip3 install -qq --upgrade pip 
pip3 install -qqr requirements.txt 
echo "[ENV] The errors shown in red text are not a problem!"
echo "[ENV] Virtual Environment yolov5_npu_inference is ready for inference!"