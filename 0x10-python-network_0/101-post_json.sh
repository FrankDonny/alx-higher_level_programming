#!/bin/bash/
# script to send a json POST request
curl -X POST -d "$2" -H 'Content-Type: application/json' "$1"
