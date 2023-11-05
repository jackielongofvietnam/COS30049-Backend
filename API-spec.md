## API - Login
1. Request

    - POST: api/login

    ```json
    Body: 

    {
        "user_name": "JohnSmith",
        "password": "123456789Abc"
    }
    ```
2. Response
    - 201 Created
    ```json
    Body:

    {
        "status": 201,
        "message": "Successful login",
        "data": {
            "user_name": "long"
        }
    }
    ```

    - 401 Unauthorized
    ```json
    Body:

    {
        "status": 401,
        "message": "Login failed! Wrong username or password",
        "data": null
    }
    ```


## API - Audit logic

1. Request
    - POST: api/audit

    ```json
    Body:

    {
        "file_name": "smart-contract.sol",
        "file_content": "This is the content of sol file"
    }
    ```

2. Response
    - 200 OK

    ```json
    Body:

    {
        "status": 201,
        "message": "",
        "data": {
            "file_name": "smart-contract.sol",
            "date_uploaded": "2023-10-16",
            "status": "risky",
            "vulnerabilities": [
                {
                    "issue": "Smart contract is risky",
                    "suggestion": "Fix it"
                },
                {
                    "issue": "Smart contract is dangerous",
                    "suggestion": "Remove it"
                }
            ]
        }  
    }
    ```

    - 404 Not Found
     ```json
    Body:

    {
        "status": 404,
        "message": "File not found!",
        "data": null
    }
    ```

## API - Audit history
1. Request
    - GET: api/audit-history

    ```json
    Query-params:

    {
        "search": "smart contract"
    }
    ```
2. Response
    - 200 OK

    ```json
    Body:

    {
        "status": 200,
        "message": "",
        "data": [
            {
                "file_name": "smart-contract1.sol",
                "date_uploaded": "2023-10-16",
                "status": "risky",
                "vulnerabilities": [
                    {
                        "issue": "Smart contract is risky",
                        "suggestion": "Fix it"
                    },
                    {
                        "issue": "Smart contract is dangerous",
                        "suggestion": "Remove it"
                    }
                ]
            },
            {
                "file_name": "smart-contract2.sol",
                "date_uploaded": "2023-10-18",
                "status": "safe",
                "vulnerabilities": []
            }
        ]
    }
    ```
