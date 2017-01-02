from __future__ import print_function
from Registry import Registry as reg
import sys

__author__ = "Chapin Bryce"
__version__ = 20170101
__description__ = "Example usage of the python-registry module"

# The path to our exported registry hive file
# We will be using an NTUser.dat hive for an example.
# Pass this file as the first argument on the command line
# ie. $ python python_registry.py NTUser.dat
path_to_registy_hive = sys.argv[1]

# Let's open this registry hive.
# We will create a file object to pass into our registry library.
# We could also pass in the string path for this library to read.
open_file = open(path_to_registy_hive, 'rb')
open_hive = reg.Registry(filelikeobject=open_file)

# Gather the root of the registry
reg_root = open_hive.root()

# Access a subkey by name
software_key = reg_root.subkey("Software")

# Count number of subkeys and values for a particular subkey
print("The software subkey of NTUser.dat "
      "has {} subkeys and {} values"
      .format(software_key.subkeys_number(), software_key.values_number()))

# Lets take a look at the Explorer subkey within our NTUser.dat
## We can stack the `.subkey()` calls to move through the hive
subkey_explorer = software_key.find_key(r"Microsoft\Windows\CurrentVersion\Explorer")

# Explore metadata about the subkey 'Explorer'
print("\n\nSubkey Metadata")
print("===============")
print("{:20} {}".format("Name: ", subkey_explorer.name()))
print("{:20} {}".format("Path: ", subkey_explorer.path()))
print("{:20} {}".format("Parent: ", subkey_explorer.parent().name()))
print("{:20} {}".format("Last Written Time: ",
       subkey_explorer.timestamp().isoformat(' ')))

# Explore metadata about the values for this subkey
print("\n\nValues\n======")
print("{:20}\t{:<10}\t{}".format("Name", "Type", "Value"))
print("{:20}\t{:<10}\t{}".format("----", "----", "-----"))
for v in subkey_explorer.values():
    # Print our the name, value type, and value
    print("{:20}\t{:10}\t{}".format(v.name(), v.value_type_str(), v.value()))

# Explore all subkeys
print("\n\nSubkeys\n=======")
print("{:20}\t{}".format("Name", "Timestamp"))
print("{:20}\t{}".format("----", "---------"))
for s in subkey_explorer.subkeys():
    # Print our the name and last written time for each subkey discovered
    print("{:20}\t{}".format(s.name(), s.timestamp().isoformat(' ')))
