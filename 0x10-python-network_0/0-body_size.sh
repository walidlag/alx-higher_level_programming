#!/bin/bash
# Send a request to URL, displays the size of the body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
