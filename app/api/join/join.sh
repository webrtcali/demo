#!/bin/bash

API_KEY="Rogachat_default_secret"
Rogachat_URL="https://.Rogachat.com/api/v1/join"
# Rogachat_URL="http://localhost:3010/api/v1/join"

curl $Rogachat_URL \
    --header "authorization: $API_KEY" \
    --header "Content-Type: application/json" \
    --data '{"room":"test","password":"0","name":"Rogachat","audio":"1","video":"1","screen":"1","notify":"1"}' \
    --request POST