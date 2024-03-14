# StringManipulation
# Description : It's a python script to mimic the cd operations on the command prompt

# 1. Environment set up
# Make sure to use Python installed and version >= 3.8.0
# Create a virtual environment with name of StringManipulation using below command
# Command --> python -m venv StringManipulation
# Activate the virtual environment and install requirements.txt
# Command --> cd StringManipulation\Scripts\activate
# Go to the main folder 
# Command --> cd ../..
# Install the required libraries
# Command --> pip install -r requirements.txt
# Command to check libraries installed r not
# Command --> pip freeze

# Now the environment is ready to run the python script
# 2. Run the main.py
# To run main.py, need to provide two arguments
# python main.py <current_directory> <new_directory>
# Example : python main.py "/" "abc"
# Output : Generated result path : /abc

# 3. Run test cases
# Automated test cases to ran it use below command
# Command : pytest
# if it shows any issues use below command
# Command : pytest test_main.py