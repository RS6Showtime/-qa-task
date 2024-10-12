from scripts.signup import signup_user
import random

# Case Tests

def test_case_1():
    """
    Test case 1 signup (Already exists)
    """
   
    result = signup_user("testing", "testing123").json()
    assert int(result['error']) == 1  # Should return error 1, because user already exists
    print(f"Case 1: {result['message']}")

def test_case_2():
    """
    Test case 2 signup (New user)
    """
    result = signup_user("testing" + str(random.randrange(10000000, 99999999)), "testing123").json()
    assert int(result['error']) == 0  # Should return error 0, because user was created
    print(f"Case 2: {result['message']}")

def test_case_3():
    """
    Test case 3 signup (Empty data)
    """
    result = signup_user("", "").json()
    assert int(result['error']) == 1  # Should return error 1, because no data was provided
    print(f"Case 3: {result['message']}")

def test_case_4():
    """
    Test case 4 signup (Less data)
    """
    result = signup_user("a", "a").json()
    assert int(result['error']) == 1  # Should return error 1, because not enough data was provided
    print(f"Case 4: {result['message']}")

def test_case_5():
    """
    Test case 5 signup (Longer|Overflow data)
    """
    result = signup_user("a" * 65, "a" * 65).json()
    assert int(result['error']) == 1  # Should return error 1, because too much data was provided
    print(f"Case 5: {result['message']}")
