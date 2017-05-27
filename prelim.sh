#!/bin/bash

# Preliminary script, will we do this all in shell?

cd /Users/simonzhou/Google\ Drive/Projects/react_tutorial/src
touch iseegreen.txt
echo "I love commits!" >> iseegreen.txt
cd ..
git init
git add .
git commit -m "iseegreen commit"
git push
cd src
rm iseegreen.txt
