# ANSI escape codes for color
RED = '\033[91m'
WHITE_ON_MAGENTA = '\033[97;45m'
RESET = '\033[0m'

# Create a decorative banner
print(RED + "=" * 40 + RESET)
print(WHITE_ON_MAGENTA + "       Welcome to GitLab       " + RESET)
print(RED + "=" * 40 + RESET)
