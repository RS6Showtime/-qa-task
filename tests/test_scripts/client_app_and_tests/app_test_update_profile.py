from scripts.update_profile import update_user_profile

# Case Tests

def test_case_1():
    """
    Test case 1 view profile (Valid token)
    """
   
    result = update_user_profile("kfn7g2e4t2797kou9clch8m09hbjg95s3zd", "Cool", "Tester").json()
    assert int(result['error']) == 0  # Should return error 0, because user provided valid data and token
    print(f"Case 1: {result['message']}")

def test_case_2():
    """
    Test case 2 view profile (invalid token)
    """
    result = update_user_profile("bananabananabananabanana")
    assert result.status_code == 401  # Should return error 1, because user could provided invalid token
    print(f"Case 2: {result.json()['detail']}")

def test_case_3():
    """
    Test case 3 view profile (Empty token)
    """
    result = update_user_profile("")
    assert result.status_code == 401  # Should return error code 401, because user provided empty token
    print(f"Case 3: {result.json()['detail']}")

def test_case_4():
    """
    Test case 4 view profile (Less data)
    """
    result = update_user_profile("a")
    assert result.status_code == 401  # Should return error code 401, because user provided small token
    print(f"Case 4: {result.json()['detail']}")

def test_case_5():
    """
    Test case 5 view profile (Longer|Overflow data)
    """
    result = update_user_profile("a"*65)
    assert result.status_code == 401  # Should return error code 401, because user provided longer token
    print(f"Case 5: {result.json()['detail']}")

def test_case_6():
    """
    Test case 6 view profile (Valid token, empty data)
    """
   
    result = update_user_profile("kfn7g2e4t2797kou9clch8m09hbjg95s3zd", "", "").json()
    assert int(result['error']) == 1  # Should return error 1, because user provided valid token, but invalid data
    print(f"Case 6: {result['message']}")

def test_case_7():
    """
    Test case 7 view profile (Valid token, less data)
    """
   
    result = update_user_profile("kfn7g2e4t2797kou9clch8m09hbjg95s3zd", "a", "a").json()
    assert int(result['error']) == 0  # Should return error 1, because user provided valid token, but less data (it require 1 char to be valid data)
    print(f"Case 7: {result['message']}")

def test_case_8():
    """
    Test case 8 view profile (Valid token, longer data)
    """
   
    result = update_user_profile("kfn7g2e4t2797kou9clch8m09hbjg95s3zd", "a"*65, "a"*65).json()
    assert int(result['error']) == 1  # Should return error 1, because user provided valid token, but longer data
    print(f"Case 8: {result['message']}")