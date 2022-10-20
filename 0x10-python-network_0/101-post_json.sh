#!/bin/bash/
# script to send a json POST request
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
