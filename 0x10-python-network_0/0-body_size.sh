#!/bin/bash
# Taks a url and get the size in bytes 
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2