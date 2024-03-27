#!/bin/bash
# Request to a URL passed as an argument, and displays the status code of the response only
curl -so /dev/null -w "%{http_code}" "$1"
