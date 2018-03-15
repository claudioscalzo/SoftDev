#!/bin/bash

file=$(cat)
IFS=" "
numbers=$(echo $file | egrep -o '<div class="num-votes" id="num-votes-[0-9]+">((\-)?[0-9]+)' | sed -rn 's-<[^>]*>((\-)?[0-9]+)-\1-gp')
i=1
echo $file | egrep -o '<div class="command">([^<]+)' | sed -rn 's-<[^>]*>([^<]+).*-\1-gp' \
| \
while read -r line; do
    corresp=$(echo $numbers | sed -n "$i p")
    echo $corresp $line
    i=$(($i+1))
done \
| \
egrep -v "^(\-)" | egrep -v "^[01234] " | sed -rn 's-([0-9]+) (.*)-\2-gp'
