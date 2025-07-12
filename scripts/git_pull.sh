#!/bin/bash
cd /home/stree/assistente_universal || exit
git stash
git pull origin main --rebase
git stash pop
