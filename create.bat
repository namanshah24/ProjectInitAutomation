@echo off
set fn=%1
@REM set flag=%2
set viz=%3
cd /d %~dp0
if "%3"=="" (
    python initproject.py %fn% %visibility%
) 



@REM cd "%mp%\%fn%"