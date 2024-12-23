#!/bin/bash

docker compose up -d --build && docker compose exec -it bot sh
