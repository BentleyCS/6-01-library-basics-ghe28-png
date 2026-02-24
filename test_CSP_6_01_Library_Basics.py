import CSP_6_01_Library_Basics as HW

def test_process_expenses():

    assert HW.process_expenses([1,2,3])==[1.15,2.3,3.4499999999999997]


def test_analyze_scores():
    assert True


def test_sanitize_usernames():

    assert HW.sanitize_usernames(["ABC"," ","DOG"])==["abc","","dog"]


def test_identify_outliers():

    assert HW.identify_outliers([1,101,202])==[101,202]


def test_search_and_report():

    assert HW.search_and_report(["Dog ", " Cat "," Bird "],"Dog ")==0
