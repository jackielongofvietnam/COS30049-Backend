## API - Login
1. Request

    - POST: /login

    ```
    Body: 

    {
        userName: "JohnSmith",
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
        data: null
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
        fileName: "smart-contract.sol"
        fileContent: "This is the content of sol file"
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
            fileName: "smart-contract.sol",
            dateUploaded: "2023-10-16",
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
            auditHistory: [
                {
                    fileName: "smart-contract1.sol",
                    dateUploaded: "2023-10-16",
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
                    fileName: "smart-contract2.sol",
                    dateUploaded: "2023-10-18",
                    status: "safe",
                    vulnerabilities: []
                }
            ]
        }
    }
    ```
