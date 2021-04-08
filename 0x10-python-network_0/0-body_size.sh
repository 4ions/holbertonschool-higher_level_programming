#!/bin/bash
# Taks a url and get the size in bytes 
curl -sI "$1" | grep -i Content-Length | cut -d' ' -f2