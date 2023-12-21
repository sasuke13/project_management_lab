#!/bin/bash

cd backend/src && celery -A core beat -l info