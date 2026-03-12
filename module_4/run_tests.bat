@echo off
echo before tests
call conda activate PythonProject
pytest
call conda deactivate
echo after tests
pause