#!/bin/bash
#Whenever you clone a repo, you do not clone all of its branches by default.
#If you wish to do so, use the following script:


cd /mnt/c/devel/GitTesting/newtest/thistest/


rm tester2.txt;
touch  tester2.txt;

cd <folder location>
for branch in `git branch -a`; do echo -b $branch | awk -F/ '{print $NF}' >> ../tester2.txt;
done

cd ..
grep -E "^[^-b]" tester2.txt | grep -E "[^(^HEAD)]" | grep -E --invert-match "^LOWER" | grep -E -v "^<disregard branch name>" > tester3.txt


rm tester4.txt;
touch  tester4.txt;
while read line; do echo "git checkout "$line >> tester4.txt; done < tester3.txt

cd <folder location>

git config --global credential.helper 'cache --timeout 3600'

# Make sure the list in tester3.txt is correct, you are about to push to the new place, also change the repo url
while read line; do git checkout -b $line; done < ../tester3.txt
while read line; do git push -f <repo URL> $line:$line; done < ../tester3.txt
