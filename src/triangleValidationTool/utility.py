import json
import requests

def replacePayload(payloadFilePath: str, first_side: str, second_side: str, third_side: str):
    """
        This function replace the payload with triagle side data
        Args:
            payloadFilePath as string: payload File Path path as string
            first_side as string: First side of triangle as string
            second_side as string: Second side of triangle as string
            third_side as string:  Third side of triangle as string
        Return:
            payload as string: final payload with user defined side values 
    """
    with open(payloadFilePath) as file:
        readPayload = json.load(file)

        payload = json.dumps(readPayload)
        payload = payload.replace("#firstSide#", str(first_side))
        payload = payload.replace("#secondSide#", str(second_side))
        payload = payload.replace("#thirdSide#", str(third_side))

        return payload


def verify_get_version(url) -> None:
    """
    This function verify GET version endpoint of application using rest service
    Args:
        url as string: base rest url as string
    
    Return -> n/a
    Raises:
        ValueError: If the provided URL is empty or None.
    """
    if not url:
        raise ValueError("URL cannot be empty or None.")

    final_url = f"{url}/version"
    print(f'Final URL to get version : {final_url}')
    
    try:
        #trigger GET method
        response = requests.get(final_url)
        responseContent = response.text

        if response.status_code == 200:
            print(f"Pass: API Version: {responseContent}")
        else:
            print("Fail: Failed to get API version")
            print(responseContent)
            
    except requests.exceptions.RequestException as e:
        print("Fail: Failed to connect to the server")
        print(str(e))

def verify_postForTriangleApp(url, payload, requirement: str) -> None:
    """
    This function verify post version endpoint of application using rest service and checks the correct response is generated
    Args:
        url as string: The URL of the post version endpoint.
        payload as string: The payload to be sent in the request body.
        requirement as string: The requirement string to check in the response content.

    Returns:N/A
    
    Raises:
        ValueError: If the provided URL, payload, or requirement is empty.
        requests.RequestException: If there is an error in the request.
    """
    headers = {
        "Content-Type": "application/json"
    }

    if not url:
        raise ValueError("URL cannot be empty.")

    if not payload:
        raise ValueError("Payload cannot be empty.")

    if not requirement:
        raise ValueError("Requirement cannot be empty.")
    
    try:
        #Trigger POST to create triangle
        response = requests.post(url, headers=headers, data=payload)
        responseContent = response.text
        print(response.status_code)
        
        #Verify response code from reponse
        if response.status_code == 200 or response.status_code == 201:
            
            # Verify that the page content matches the content requirements
            responseContent = response.text
            if requirement.lower() in responseContent.lower():
                message = f'{url} is up and running. Response is correctly displayed. Triange is {requirement}'
                print(message)
            else:
                message = f'{url} is up, but the content does not match the requirement.'
                print(message)

        else:
            print("Fail: Failed to create triangle")
            print("Error Message is"+responseContent)
            print(f'Input is {payload} ')
            
    except requests.RequestException as e:
        print(f"Error occurred while making the request: {str(e)}")


def verify_triangle_type(first_side: int, second_side: int, third_side: int):
    """
    This function determines the type of triangle based on the lengths of its sides.
    Args:
        first_side as int: The length of the first side of the triangle.
        second_side as int : The length of the second side of the triangle.
        third_side as int: The length of the third side of the triangle.

    Returns:
        str: The type of triangle identified as either "equilateral", "isosceles", or "versatile".

    Raises:
        ValueError: If any of the side lengths are not positive numbers.
    """
    if int(first_side) <= 0 or int(second_side) <= 0 or int(third_side) <= 0:
        raise ValueError("Fail : Side lengths must be positive numbers.")
    if first_side == second_side == third_side:
        return "equilateral"
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        return "isosceles"
    else:
        return "versatile"