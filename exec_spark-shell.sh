#!/bin/sh
sudo docker-compose exec master /spark/bin/spark-shell --master spark://localhost:7077
