cat wall.html | egrep -o '<div class="comment"><span class="profile">([^<]+)' | sed -rn 's-<[^>]+>--gp' | uniq -c | sed -rn 's-      --gp' | sort -nr
