run_tests:
	@echo "before tests"
	@cmd /c "conda activate PythonProject && pytest && conda deactivate"
	@echo "after tests"

show_cases:
	@cmd /c "conda activate PythonProject && pytest --collect-only && conda deactivate"