#!/bin/bash

API_KEY=`jq -r .apikey ~/.bluemix/visual_recognition_credentials.json`
curl -u "apikey:${API_KEY}" "https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?url=https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/640px-IBM_VGA_90X8941_on_PS55.jpg&version=2018-03-19"

