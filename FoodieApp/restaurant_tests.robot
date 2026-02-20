*** Settings ***
Library           RequestsLibrary
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections

Suite Setup       Setup Suite
Suite Teardown    Teardown Suite

*** Variables ***
${BASE_URL}       http://127.0.0.1:5000/api/v1
${LOG_FILE}       ${CURDIR}/robot_results.txt
${rid}            0
${uid}            0
${oid}            0
${did}            0

*** Keywords ***
Setup Suite
    Create Session    foodie    ${BASE_URL}
    # Create or overwrite the log file at the start
    Create File       ${LOG_FILE}    ROBOT TEST EXECUTION LOG${\n}==========================${\n}

Log Status
    [Arguments]    ${test_name}
    Append To File    ${LOG_FILE}    ${test_name} : PASS${\n}

Teardown Suite
    Close All Browsers

*** Test Cases ***
1-Reg Res
    ${body}=    Create Dictionary    name=Robot Hub    category=Veg    location=Delhi    contact=1
    ${r}=       POST On Session    foodie    /restaurants    json=${body}
    Status Should Be    201    ${r}
    Set Suite Variable    ${rid}    ${r.json()['id']}
    Log Status    1-Reg Res

2-Dup Res
    ${body}=    Create Dictionary    name=Robot Hub    category=Veg    location=Delhi    contact=1
    POST On Session    foodie    /restaurants    json=${body}    expected_status=409
    Log Status    2-Dup Res

3-View Res
    GET On Session    foodie    /restaurants/${rid}
    Log Status    3-View Res

4-Upd Res
    ${body}=    Create Dictionary    location=Mumbai
    PUT On Session    foodie    /restaurants/${rid}    json=${body}
    Log Status    4-Upd Res

5-Dis Res
    PUT On Session    foodie    /restaurants/${rid}/disable
    Log Status    5-Dis Res

6-Add Dish
    ${body}=    Create Dictionary    name=Pizza    type=Veg    price=10
    ${r}=       POST On Session    foodie    /restaurants/${rid}/dishes    json=${body}
    Set Suite Variable    ${did}    ${r.json()['id']}
    Log Status    6-Add Dish

7-Upd Dish
    ${body}=    Create Dictionary    price=20
    PUT On Session    foodie    /dishes/${did}    json=${body}
    Log Status    7-Upd Dish

8-Tog Dish
    ${body}=    Create Dictionary    enabled=${False}
    PUT On Session    foodie    /dishes/${did}/status    json=${body}
    Log Status    8-Tog Dish

9-Del Dish
    DELETE On Session    foodie    /dishes/${did}
    Log Status    9-Del Dish

10-Reg User
    ${body}=    Create Dictionary    name=Harsh    email=h@t.com
    ${r}=       POST On Session    foodie    /users/register    json=${body}
    Set Suite Variable    ${uid}    ${r.json()['id']}
    Log Status    10-Reg User

11-Dup User
    ${body}=    Create Dictionary    name=Harsh    email=h@t.com
    POST On Session    foodie    /users/register    json=${body}    expected_status=409
    Log Status    11-Dup User

12-Order
    ${body}=    Create Dictionary    user_id=${uid}    restaurant_id=${rid}    dishes=@{EMPTY}
    ${r}=       POST On Session    foodie    /orders    json=${body}
    Set Suite Variable    ${oid}    ${r.json()['id']}
    Log Status    12-Order

13-User Orders
    GET On Session    foodie    /users/${uid}/orders
    Log Status    13-User Orders

14-Res Orders
    GET On Session    foodie    /restaurants/${rid}/orders
    Log Status    14-Res Orders

15-Rate
    ${body}=    Create Dictionary    order_id=${oid}    rating=5
    POST On Session    foodie    /ratings    json=${body}
    Log Status    15-Rate

16-Adm App
    PUT On Session    foodie    /admin/restaurants/${rid}/approve
    Log Status    16-Adm App

17-Adm Dis
    PUT On Session    foodie    /admin/restaurants/${rid}/disable
    Log Status    17-Adm Dis

18-Adm Ord
    # Open browser first, then navigate, then capture
    Open Browser      ${BASE_URL}/admin/orders    chrome
    Set Window Size    1280    800
    Capture Page Screenshot    ${CURDIR}/robot_final_state.png
    GET On Session    foodie    /admin/orders
    Log Status    18-Adm Ord