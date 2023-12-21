#!/bin/bash

cd backend/src && celery -A core worker -l INFO