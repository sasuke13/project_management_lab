#!/bin/bash

cd src && celery -A core worker -l INFO