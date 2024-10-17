# Copyright 2022 Huawei Technologies Co., Ltd
# CREATED:  2022-10-04 13:12:13
# MODIFIED: 2022-12-23 12:48:45
#!/bin/bash

# yolov5 model type (s,m,x) 
wget https://github.com/ultralytics/yolov5/releases/download/v6.1/yolov5s.pt --no-check-certificate

# create python virtual environment
echo "[ENV] Virtual Environment Preparation Starting!"
python3 -m venv convertPt2Onnx
source convertPt2Onnx/bin/activate

# copy necessary file to repo
cp yolov5s.pt export/

# open repo
cd export/

# install necessary python libs
pip3 install --upgrade pip 
pip3 install -r requirements.txt 

echo "[ENV] Virtual Environment Preparation Done!"

python -m pip install --upgrade pip
pip3 install -r requirements.txt

# convert pt model to onnx model
echo "[MODEL] Conversion Starting!"
python3 onnx_export.py --weights yolov5s.pt

# mv onnx model
mv yolov5s.onnx  ../

# deactivate venv
deactivate
cd ../
# delete virtual environment
rm -r convertPt2Onnx

echo "[MODEL] Conversion Done!"
