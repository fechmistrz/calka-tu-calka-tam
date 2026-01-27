git ls-files | grep 'tex$' | xargs dirname | sort -u | while read -r line; do
    (
        cd "$line";
        find . -maxdepth 1 -type f -name '*.tex' | sort -u | while read -r subline; do
            echo "$(git log -n 1 --format=format:%aI -- "$subline") $line/$subline";
        done | sort -V | grep -v 'src/00_intro' | head -n 3
    );
done | sort -V
