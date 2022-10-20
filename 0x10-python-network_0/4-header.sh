#!/bin/bash
# script to send a GET request with a header variable
curl -XH GET "X-School-User-Id:98" "$1"
