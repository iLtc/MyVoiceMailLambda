#!/usr/bin/env bash

rm -rf ../MyVoiceMailLambdaBuild ../MyVoiceMailLambdaBuild.zip

cp -r . ../MyVoiceMailLambdaBuild

cd ../MyVoiceMailLambdaBuild

pip install -r requirements.txt -t .

rm -rf .env venv __pycache__

zip -r ../MyVoiceMailLambdaBuild.zip *