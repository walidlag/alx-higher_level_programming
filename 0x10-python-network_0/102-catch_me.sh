#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me and request to causes an specific response
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
