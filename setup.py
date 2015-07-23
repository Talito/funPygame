import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
	name="FunGame"
	options={"build_exe":{"packages":["pygame"], "include_files":["apple.png", "snakehead.png", "icon.png"]}},
	
	description = "FunGame is a basic dynamic Snake game",
	executables = executables.
	)
	
# command to run: python setup.py build