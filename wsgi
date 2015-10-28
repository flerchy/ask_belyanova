CONFIG = {
	'mode': 'wsgi',
	'working_dir': '/home/flerchy/ask_belyanova/',
	'user': 'www-data',
	'group': 'www-data',
	'python': '/usr/bin/python',
	'args': (
	    '--bind=127.0.0.1:8081',
            '--workers=8',
            '--timeout=60',
    	    'myapp:application',
	),
}
