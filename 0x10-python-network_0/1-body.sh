#!/bin/bash
# script to display body of a url
curl -L so file.txt "$1"; cat file.txt
