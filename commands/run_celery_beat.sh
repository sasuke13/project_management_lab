#!/bin/bash

cd src && celery -A config beat -l info