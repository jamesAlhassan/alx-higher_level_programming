#!/bin/bash

ADD=$(git add .)
MSG=$(git commit -m "$1")
PUSH=$(git push)

