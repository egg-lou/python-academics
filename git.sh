#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: ./git.sh commit_message branch_name"
    exit 1
fi

# Assign the arguments to variables
commit_message=$1
branch_name=$2

# Execute the git commands
git add .
git commit -m "$commit_message"
git push -u origin $branch_name