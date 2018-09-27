#!/bin/bash

cat repos.list | while read line
do
    # line is <org> <repo> <url>
    parts=($line)
    org=${parts[0]}
    repo=${parts[1]}
    url=${parts[2]}

    outdir="out/$org/$repo"
    echo "$outdir"

    if [ ! -d "$outdir/.git" ]; then
        git clone --depth 1 $url $outdir
	echo $?
    fi
done

