#!/bin/zsh

echo "\n--- Test 1: Quoted commit message ---"
echo "edit1" >> gitquick_dummy.txt
gitq 'Commit with quoted message'
sleep 2

echo "\n--- Test 2: Bareword unquoted message ---"
echo "edit2" >> gitquick_dummy.txt
gitq Hello123
sleep 2

echo "\n--- Test 3: No message (fallback to datetime) ---"
echo "edit3" >> gitquick_dummy.txt
gitq
sleep 2

echo "\n--- Test 4: Too many arguments ---"
gitq one two
sleep 2

echo "\n--- Test 5: Push fails (no upstream) ---"
git checkout -b testbranch-no-upstream
echo "edit4" >> gitquick_dummy.txt
gitq 'Trying push with no upstream'
sleep 2

echo "\n--- Cleaning up test branch ---"
git checkout main
git branch -D testbranch-no-upstream
