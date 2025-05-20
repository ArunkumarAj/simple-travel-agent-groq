@echo off
echo Stopping all running Docker containers...
FOR /F %%i IN ('docker ps -q') DO docker stop %%i

echo Removing all Docker containers...
FOR /F %%i IN ('docker ps -aq') DO docker rm %%i

echo Removing all Docker images...
FOR /F %%i IN ('docker images -q') DO docker rmi -f %%i

echo Done.
