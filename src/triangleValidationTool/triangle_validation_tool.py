"""
This script that verifies GET/Version and POST endpoint for the triangle applications using a utility library. 
The script is designed to load test data, manipulate payload information, determine triangle types, and make API requests.
Author: Akriti Pandey
"""
import os
import utility as utilLibrary
import json

base_url = "http://ew1eppqaassignment-env.eba-rqr3rd8p.eu-west-1.elasticbeanstalk.com"

payload_file_path = os.path.join("src", "resource", "payload.json")

testData = os.path.join("src", "resource", "testdata.json")


if __name__ == '__main__':
    with open(testData) as testData_file:
        test_data = json.load(testData_file)
   
    # Verify GET service
    utilLibrary.verify_get_version(base_url)

    for triangle in test_data['triangles']:
        side1 = triangle['side1']
        side2 = triangle['side2']
        side3 = triangle['side3']

        # Replace payload with user provided value
        payload = utilLibrary.replacePayload(payload_file_path, str(side1), str(side2), str(side3))

        # Verify triangle type for POST end validation step
        triangle_type = utilLibrary.verify_triangle_type(str(side1), str(side2), str(side3))

        # Validate POST end point for triangle app 
        utilLibrary.verify_postForTriangleApp(base_url, payload, triangle_type)
