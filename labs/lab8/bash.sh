#!/bin/bash

jq -r '.[].receiptTime | strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%d %H:%M:%S")' aviation.json | head -n 6

