#!/bin/sh

# Check if the migrations directory exists and is not empty
if [ -d "migrations" ] && [ "$(ls -A migrations)" ]; then
    echo "Migrations directory exists. Running aerich migrate..."
    if ! poetry run aerich migrate; then
        echo "Error running aerich migrate"
        exit 1
    fi
else
    echo "Migrations directory does not exist or is empty. Running aerich init-db..."
    if ! poetry run aerich init-db; then
        echo "Error running aerich init-db"
        exit 1
    fi
fi

# Check for changes in the models directory and run aerich upgrade if needed
if [ "$(find src/api/models -type f -newer migrations)" ]; then
    echo "Models have changed. Running aerich upgrade..."
    if ! poetry run aerich upgrade; then
        echo "Error running aerich upgrade"
        exit 1
    fi
fi

# Execute the main command
exec "$@"