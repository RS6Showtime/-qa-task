# Current username & password for testing only its:

- Username: 
```
testing
```
- Password: 
```
testing123
```

auth_token will be:

```
kfn7g2e4t2797kou9clch8m09hbjg95s3zd
```

# the scripts perfomance directory

This directory will be use to check the response from client-server and check for valid response in all kind of scenarios.

The tests could be executed on windows & linux:

- windows_tests
- linux_tests

- SignUp: 
```
1. SignUp with User already exists.
2. SignUp and Create new random user.
3. SignUp with Empty data.
4. SignUp with less data.
5. SignUp with Longer data.
```

- Login:
```
1. Login with valid credentials.
2. Login with invalid credentials.
3. Login with empty data.
3. Login with less data.
4. Login with longer data.
```

- View Profile:
```
1. Send valid token.
2. Send invalid token.
3. Send empty token.
4. Send small token.
5. Send longer token.
```

- Update Profile:
```
1. Send valid token with required profile update data.
2. Send invalid token.
3. Send empty token.
4. Send small token.
5. Send longer token.
6. Send valid token with empty data required profile update data.
7. Send valid token with less data required profile update data.
8. Send valid token with longer data required profile update data.
```

# To Do
```
Add test case for Update Profile:

- Try adding new scenario where it's only specified the First Name or Last Name, Or Both are used.

Check if the linux version of test work.

Create performance tests for (1000 requests):

signup (Already exists user or creating accounts)
login (Invalid/Valid account)
profile (View/Update profile)

Creating configuration file for CI

```

