#!/bin/bash
# script to display size of the body of a response
curl -so file.txt -i "$1" | cat file.txt | grep Content-Length | cut -d ' ' -f 2
