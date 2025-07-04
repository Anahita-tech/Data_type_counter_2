# Data Type Counter2

This is a simple Python script that analyzes a list of mixed data types and count
 how many elements belongs to each one and the result will be shown as an dictionary

** The different between this program with previous one(type_counter1) is that this script is written by 'for'.

*** Note: In Python, 'bool' is subclass of 'int'.
    So 'isinstance(True,int)' returns 'True'.
    That's why we must check for 'bool' before 'int' to avoid miscounting
