#!/bin/bash
# script to send a GET request with a header variable
curl -sH GET -H "X-School-User-Id:98" "$1"
