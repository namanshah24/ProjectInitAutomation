@echo off
set fn=%1
cd /d %~dp0
python delgitrepo.py %fn%