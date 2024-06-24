import json

# Sample employee data
employee_data ={
        "employeeId": "1",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "position": "Software Engineer",
        "salary": 75000,
        "hireDate": "2020-01-15"
    },{
        "employeeId": "2",
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "position": "Project Manager",
        "salary": 85000,
        "hireDate": "2018-05-22"
    },
print("Test")

    # Add all other employee data here


def lambda_handler(event, context):
    # Get employeeId from query parameters
    employee_id = event.get('queryStringParameters', {}).get('employeeId')
    
    if not employee_id:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing employeeId query parameter')
        }
    
    # Find the employee with the given employeeId
    for employee in employee_data:
        if employee['employeeId'] == employee_id:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'firstName': employee['firstName'],
                    'lastName': employee['lastName']
                })
            }
    
    return {
        'statusCode': 404,
        'body': json.dumps('Employee not found')
    }
