#!/bin/bash
# script to display size of the body of a response
curl -s -o file -i "$1" | cat file | grep Content-Length | cut -d ' ' -f 2
