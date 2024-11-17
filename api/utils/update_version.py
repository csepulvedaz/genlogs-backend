import os

import tomlkit


toml_path = os.path.abspath("pyproject.toml")
init_path = os.path.abspath("api/__init__.py")

# Read the configuration file
with open(toml_path, "r") as f:
    config = tomlkit.parse(f.read())

# Get the current version
current_version = config["tool"]["poetry"]["version"]

# Split the version into its components
major, minor, patch = map(int, current_version.split("."))

# Increment the desired version type
# For example, to increment the patch
patch += 1

# Check if the third number reached 99
if patch > 99:
    patch = 0
    minor += 1

    # Check if the second number reached 99
    if minor > 99:
        minor = 0
        major += 1

# Update the version in the configuration file
new_version = f"{major}.{minor}.{patch}"
config["tool"]["poetry"]["version"] = new_version

# Write the configuration file preserving the order
with open(toml_path, "w") as f:
    f.write(tomlkit.dumps(config))

# Save the version number in the __init__.py file
with open(init_path, "w") as f:
    f.write(f"__version__ = '{new_version}'")
