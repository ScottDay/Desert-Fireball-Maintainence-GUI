from . import Dev


class Local(Dev):
	# Logging.
	SHOULD_USE_FILE = False

	# Paths.
	DFN_CONFIG_PATH = 'sample/dfnstation.cfg'
	DFN_DISK_USAGE_PATH = 'sample/dfn_disk_usage'

	# Console (terminal / ssh) and Command Type (prod / dev).
	USE_DEV_COMMAND = True
