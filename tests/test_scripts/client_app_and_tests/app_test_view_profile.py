from scripts.view_profile import view_user_profile

# Case Tests

def test_case_1():
    """
    Test case 1 view profile (Valid token)
    """
   
    result = view_user_profile("kfn7g2e4t2797kou9clch8m09hbjg95s3zd").json()
    assert int(result['error']) == 0  # Should return error 0, because user provided valid token
    print(f"Case 1: Valid token")
    print(f"Username: {result['username']}")
    print(f"First Name: {result['name']}")
    print(f"Last Name: {result['last_name']}")

def test_case_2():
    """
    Test case 2 view profile (invalid token)
    """
    result = view_user_profile("bananabananabananabanana")
    assert result.status_code == 401  # Should return error code 401, because user provided invalid token
    print(f"Case 2: {result.json()['detail']}")

def test_case_3():
    """
    Test case 3 view profile (Empty token)
    """
    result = view_user_profile("")
    assert result.status_code == 401  # Should return error code 401, because user provided empty token
    print(f"Case 3: {result.json()['detail']}")

def test_case_4():
    """
    Test case 4 view profile (Less data)
    """
    result = view_user_profile("a")
    assert result.status_code == 401  # Should return error code 401, because user provided small token
    print(f"Case 4: {result.json()['detail']}")

def test_case_5():
    """
    Test case 5 view profile (Longer|Overflow data)
    """
    result = view_user_profile("a"*65)
    assert result.status_code == 401  # Should return error code 401, because user provided longer token
    print(f"Case 5: {result.json()['detail']}")
