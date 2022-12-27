#!/bin/bash

if [ -z "${PGPASSWORD}" ]; then
    echo "PGPASSWORD must be set for db user \`postgres\`"
    exit 1
fi

PGPASSWORD=${PGPASSWORD} psql -h devenv-postgres -U postgres -c "CREATE USER comic_collector_dev WITH CREATEDB PASSWORD 'password';"
PGPASSWORD=${PGPASSWORD} psql -h devenv-postgres -U postgres -c "CREATE DATABASE comic_collector_dev WITH OWNER comic_collector_dev;"