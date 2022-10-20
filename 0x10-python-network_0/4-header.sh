#!/bin/bash
# script to send a GET request with a header variable
curl -Xi GET -H "X-School-User-Id:98" "$1"
