@echo off
echo Compiling University Management System...
set JAVA_HOME=%~dp0jdk-17.0.8.1+1
set PATH=%JAVA_HOME%\bin;%PATH%

javac -cp "lib/sqlite-jdbc-3.42.0.0.jar" -d . src/university_management_system/*.java
if %ERRORLEVEL% EQU 0 (
    echo Compilation Successful!
) else (
    echo Compilation Failed!
)
pause
