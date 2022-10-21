#!/bin/bash
# script to send a json POST request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
