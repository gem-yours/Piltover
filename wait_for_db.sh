#!/bin/bash

until ./manage.py inspectdb; do
  echo "Database is unavailable"
  sleep 1
done