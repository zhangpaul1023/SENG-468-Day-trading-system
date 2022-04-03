#!/usr/bin/env bash
awk '{split($2,arr,","); print(arr[2]);}' final_workload_2019 | uniq > /tmp/usernames.txt
awk -f make_fixtures.awk /tmp/usernames.txt > users.yaml
rm /tmp/usernames.txt
