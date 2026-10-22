#!/bin/bash
set -e
cd /home/ec2-user/ec2-auto-deploy
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart flaskapp
