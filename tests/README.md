# Automation QA Interview Tasks

## Introduction
This repository contains a backend application that connects to PostgreSQL, supports authentication (JWT-based), and allows users to sign up, log in, and update their profile. Your task as a QA engineer is to write automation tests, identify issues, and ensure that the API functions as expected.

### Setup

1. **Fork the Repository**:  
   Navigate to the repository on GitHub and click the "Fork" button in the top right to create your own copy of the repository.

2. **Clone the Forked Repository**:  
Clone your fork to your local machine:
```bash
   git clone <your-forked-repo-url>
   cd <repo-name>
```

2. Start the services using Docker Compose:
```bash
    docker compose up -d
```

3. Access the API at `http://localhost:8000`.


### After Completion

Once you have completed your tasks, follow these steps:

1. **Commit and Push Your Changes**:  
After making your changes and adding test scripts:
    ```bash
    git add .
    git commit -m "Completed QA tasks"
    git push origin main
    ```

2. **Create a Merge Request**:  
   Navigate to your forked repository on GitHub and click "Compare & pull request" to create a merge request back to the original repository.

3. **Review & Submit**:  
   Add any additional comments or documentation if needed and submit the merge request.

---
<br><br>


# Tasks

### **Task 1: Write API Automation Tests**

Write automated tests for the following scenarios:

1. **Sign Up**: Verify that users can sign up with a username and password.
2. **Login**: Verify that users can log in and receive a valid JWT token.
3. **Get Profile (Protected)**: Verify that a logged-in user can access their profile using the JWT token.
4. **Update Profile (Protected)**: Verify that the user can update only their name and last name.

**Deliverables**: Write test scripts using any framework (Postman, RestAssured, pytest, etc.) and place them in the `/tests/test_scripts/` directory.

### **Task 2: Performance Testing**

Create performance/load tests for the following endpoints:

- `/signup/`
- `/login/`
- `/profile/`

Measure response times under load (e.g., 1000 concurrent requests).

**Deliverables**: Add the performance test results or scripts to `/tests/test_scripts/`.

### **Task 3: Continuous Integration (CI)**

Set up a CI pipeline that automatically runs your tests whenever changes are pushed to the repository. You may use GitHub Actions, Jenkins, or any tool you're comfortable with.

**Deliverables**: Add the CI configuration file (e.g., `.github/workflows/ci.yml` for GitHub Actions).

### **Task 4: Identify and Report Issues**

Identify any issues in the application. One issue has been intentionally left in the code.

**Deliverables**: Report the issue(s) you find by creating a new Issue in this repository with:
- Clear steps to reproduce the problem
- Expected vs actual behavior
- Any logs or screenshots
