@echo off
set fn=%1
set flag=%2
set viz=%3
cd /d %~dp0
if "%2"=="g" (
    python initproject.py %fn% %viz%
)
if "%2" == "" (
    python initproject.py %fn% %viz%
)
if "%2" == "l" (
    python initlocalproject.py %fn%
)


@REM cd "%mp%\%fn%"