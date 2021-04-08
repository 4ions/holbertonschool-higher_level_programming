#!/bin/bash
# Send request to url and display the status code.
curl -o /dev/null -s -w "%{http_code}\n" "$1"
