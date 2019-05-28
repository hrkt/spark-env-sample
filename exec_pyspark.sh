#!/bin/sh
sudo docker-compose exec master /spark/bin/pyspark --master spark://localhost:7077
