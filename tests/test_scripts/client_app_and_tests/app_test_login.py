from scripts.login import login_user

# Case Tests

def test_case_1():
    """
    Test case 1 login (Valid credentials)
    """
   
    result = login_user("testing", "testing123").json()
    assert int(result['error']) == 0  # Should return error 0, because user provided valid data
    print(f"Case 1: {result['message']}")

def test_case_2():
    """
    Test case 2 login (invalid credentials)
    """
    result = login_user("username123", "passowrd123").json()
    assert int(result['error']) == 1  # Should return error 1, because user provided invalid data
    print(f"Case 2: {result['message']}")

def test_case_3():
    """
    Test case 3 login (Empty data)
    """
    result = login_user("", "").json()
    assert int(result['error']) == 1  # Should return error 1, because no data was provided
    print(f"Case 3: {result['message']}")

def test_case_4():
    """
    Test case 4 login (Less data)
    """
    result = login_user("a", "a").json()
    assert int(result['error']) == 1  # Should return error 1, because not enough data was provided
    print(f"Case 4: {result['message']}")

def test_case_5():
    """
    Test case 5 login (Longer|Overflow data)
    """
    result = login_user("a" * 65, "a" * 65).json()
    assert int(result['error']) == 1  # Should return error 1, because too much data was provided
    print(f"Case 5: {result['message']}")
