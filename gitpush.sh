#!/bin/sh
cd /works/bot/mocho/programs
git config --local user.name "Kazuki F."
git config --local user.email "doradora.prog@gmail.com"
git add .
git commit -m "Commit from auto-commit"
git push origin master
