from setuptools import setup  
setup(     
	name="ConsoleTask",
	version="1.0",
	packages=["src","src/start_todo"],
	install_requires=[         
		"todo_manager",
		"todo",
	],
	entry_points={         
		"console_scripts": [         
			"ConsoleTask=src.main.:main",      
		],
	}, 
)