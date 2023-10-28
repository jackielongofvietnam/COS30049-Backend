## API - Login
1. Request

    - POST: /login

    ```
    Body: 

    {
        username: "JohnSmith",
        password: "123456789Abc"
    }
    ```
2. Response
    - 201 Created
    ```
    Body:

    {
        status: 201,
        message: "Successful login",
        data: {
            "username": "long"
        }
    }
    ```

    - 401 Unauthorized
    ```
    Body:

    {
        status: 401,
        message: "Login failed! Wrong username or password",
        data: null
    }
    ```


## API - Audit logic

1. Request
    - GET: /audit

    ```
    Body:

    {
        file_name: "smart-contract.sol"
        file_content: "This is the content of sol file"
    }
    ```

2. Response
    - 200 OK

    ```
    Body:

    {
        status: 201,
        message: "",
        data: {
            file_name: "smart-contract.sol",
            date_uploaded: "2023-10-16",
            status: "risky",
            vulnerabilities: [
                {
                    issue: "Smart contract is risky",
                    suggestion: "Fix it"
                },
                {
                    issue: "Smart contract is dangerous",
                    suggestion: "Remove it"
                }
            ]
        }  
    }
    ```

    - 404 Not Found
     ```
    Body:

    {
        status: 404,
        message: "File not found!",
        data: null
    }
    ```

## API - Audit history
1. Request
    - GET: /audit-history

    ```
    Body:

    {
        search: "smart contract"
    }
    ```
2. Response
    - 200 OK

    ```
    Body:

    {
        status: 200,
        message: "",
        data: {
            audit_history: [
                {
                    file_name: "smart-contract1.sol",
                    date_uploaded: "2023-10-16",
                    status: "risky",
                    vulnerabilities: [
                        {
                            issue: "Smart contract is risky",
                            suggestion: "Fix it"
                        },
                        {
                            issue: "Smart contract is dangerous",
                            suggestion: "Remove it"
                        }
                    ]
                },
                {
                    file_name: "smart-contract2.sol",
                    date_uploaded: "2023-10-18",
                    status: "safe",
                    vulnerabilities: []
                }
            ]
        }
    }
    ```
