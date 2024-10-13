#!/bin/bash

# Prompt for project name
echo "Enter the Lab Project:"
read project_name


# Author / Creator
author_name="GibzB"

# Create project structure
mkdir "$project_name"
mkdir "$project_name/images"

# Create README.md files
echo $project_name > "$project_name/README.md"


# Descriptive output
echo "Project structure created successfully!"
echo "Project name: $project_name"
echo "Author name: $author_name"
echo "Directories created: $project_name, $project_name/images"
echo "README.md files created in each directory with initial content."