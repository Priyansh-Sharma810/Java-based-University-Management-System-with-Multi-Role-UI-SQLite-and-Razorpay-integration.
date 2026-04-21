@echo off
echo Starting University Management System...
set JAVA_HOME=%~dp0jdk-17.0.8.1+1
set PATH=%JAVA_HOME%\bin;%PATH%

java -cp "lib/sqlite-jdbc-3.42.0.0.jar;." university_management_system.Main
pause
