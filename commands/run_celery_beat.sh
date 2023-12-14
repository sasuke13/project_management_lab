#!/bin/bash

cd src && celery -A core beat -l info