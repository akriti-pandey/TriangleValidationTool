# Triangle Validation Tool Documentation
This documentation provides an overview of a traingle script verifies GET/Version and POST endpoint for the triangle applications using a utility library. The script is designed to load test data, manipulate payload information, determine triangle types, and make API requests.

# Prerequisites
1)Python 3.x installed on your machine.  
2)set_python_path.bat need to be run in order to configure the python path.  
3)The os module, json module, requests module, and the custom utility library utility must be available.  

# Getting Started
Clone or download the project repository.  
git clone https://github.com/akriti-pandey/TraingleValidationTool.git  
Make sure the required prerequisites are installed.  
Navigate to the project directory.  

# Usage
The main script file is named triangle_validation_tool.py. It contains the code to execute the triangle operations. To use the script, follow these steps:  

Open a terminal or command prompt.   
Navigate to the project directory.   
Run the script using the following command:  
python triangle_validation_tool.py.  

# Configuration
Before running the script, you may need to configure the following variables in the triangle_validation_tool.py file:

base_url: The base URL of the service to which API requests will be made.  
payload_file_path: The file path of the payload JSON file.  
testData: The file path of the test data JSON file.  
Make sure to update these variables according to your specific setup.  

# Functionality
The script performs the following operations:  

•	Loads test data from a JSON file.  
•	Performs a GET request to verify the version of the service using the verify_get_version() function from the utility library.  
•	Iterates over each triangle in the test data and performs the following steps:  
    a.	Extracts the side lengths of the triangle.  
    b.	Replaces the values in the payload JSON file with the triangle side lengths using the replacePayload() function from the utility library.  
    c.	Determines the type of the triangle using the verify_triangle_type() function from the utility library.  
    d.	Makes a POST request to the specified URL with the modified payload and triangle type using the verify_postForTriangleApp() function from the utility library.  
Note:  
Custom Utility Library  
    The script utilizes a custom utility library named utility. The library contains functions to interact with the API service, manipulate payload information, and determine triangle types
