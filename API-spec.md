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
        fileUrl: "https://file.scas.com/diles/smart-contract.sol"
    }
    ```

2. Response
    - 200 OK

    ```
    Body:

    {
        fileName: "smart-contract.sol",
        dateUploaded: "2023-10-16"
        status: "risky"
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
    ```
