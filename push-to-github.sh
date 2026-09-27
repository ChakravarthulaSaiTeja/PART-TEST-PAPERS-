#!/bin/bash
# Run this in Terminal on your Mac:
#     bash ~/Desktop/"QUESTIONS 1ST DRAFT"/PART-TEST-PAPERS/push-to-github.sh
#
# It builds the git repo in this folder and pushes it to GitHub. The first time,
# git will ask for your GitHub username and a personal access token (not your
# account password) unless you already have the gh CLI or a credential helper.
set -e
cd "$(dirname "$0")"

REMOTE="https://github.com/ChakravarthulaSaiTeja/PART-TEST-PAPERS-.git"

# the four source question sets live one level up
mkdir -p source-pdfs
for f in "Surds - All Questions.pdf" \
         "Logarithms - All Questions.pdf" \
         "Quadratic Equations - All Questions.pdf" \
         "Sequences and Series - All Questions.pdf"; do
  [ -f "source-pdfs/$f" ] || cp "../$f" "source-pdfs/$f"
done

# start the history clean -- an earlier attempt may have left a partial .git here
rm -rf .git
git init -q -b main
git add -A
git -c user.email="saitejachakravarthula@gmail.com" \
    -c user.name="Sai Teja Chakravarthula" \
    commit -q -m "Part test papers: Surds, Logarithms and Quadratic Equations (L1-L4), sources, page images and full context"
git remote add origin "$REMOTE"
git push -u origin main

echo
echo "Pushed  ->  https://github.com/ChakravarthulaSaiTeja/PART-TEST-PAPERS-"
