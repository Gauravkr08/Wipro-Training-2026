*** Settings ***
Library           RequestsLibrary
Library           Collections
Suite Setup       Create Session    foodie    http://localhost:5000/api/v1

*** Variables ***
&{RESTAURANT_DATA}    name=Spice Garden    category=Indian    location=North    images=@{EMPTY}    contact=98765
&{USER_DATA}          name=John Doe    email=john@example.com    password=secret123
&{DISH_DATA}          name=Paneer Tikka    type=Veg    price=15.0    available_time=All Day    image=paneer.jpg

*** Test Cases ***

### --- RESTAURANT MODULE --- ###

Register New Restaurant Successfully
    [Documentation]    Verify admin can register a restaurant
    ${response}=    POST On Session    foodie    /restaurants    json=${RESTAURANT_DATA}
    Status Should Be    201    ${response}
    ${json}=    Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${json}    id
    Set Suite Variable    ${NEW_RES_ID}    ${json['id']}

Update Restaurant Details
    [Documentation]    Verify updating restaurant info
    ${update_data}=    Create Dictionary    location=South
    ${response}=    PUT On Session    foodie    /restaurants/${NEW_RES_ID}    json=${update_data}
    Status Should Be    200    ${response}
    Should Be Equal As Strings    ${response.json()['location']}    South

Approve Restaurant Via Admin
    [Documentation]    Verify admin can approve a registered restaurant
    ${response}=    PUT On Session    foodie    /admin/restaurants/${NEW_RES_ID}/approve
    Status Should Be    200    ${response}
    Should Be Equal As Strings    ${response.json()['message']}    Restaurant approved

### --- DISH MODULE --- ###

Add Dish To Restaurant
    [Documentation]    Verify adding a dish to an existing restaurant
    ${response}=    POST On Session    foodie    /restaurants/${NEW_RES_ID}/dishes    json=${DISH_DATA}
    Status Should Be    201    ${response}
    Set Suite Variable    ${NEW_DISH_ID}    ${response.json()['id']}

Update Dish Status
    [Documentation]    Verify toggling dish availability
    ${status}=    Create Dictionary    enabled=${FALSE}
    ${response}=    PUT On Session    foodie    /dishes/${NEW_DISH_ID}/status    json=${status}
    Status Should Be    200    ${response}

### --- USER & SEARCH MODULE --- ###

Register New User
    [Documentation]    Verify user registration
    ${response}=    POST On Session    foodie    /users/register    json=${USER_DATA}
    Status Should Be    201    ${response}
    Set Suite Variable    ${USER_ID}    ${response.json()['id']}

Search For Restaurant By Name
    [Documentation]    Verify search functionality
    ${params}=    Create Dictionary    name=Spice
    ${response}=    GET On Session    foodie    /restaurants/search    params=${params}
    Status Should Be    200    ${response}
    Should Not Be Empty    ${response.json()}

### --- ORDER & RATING MODULE --- ###

Place An Order
    [Documentation]    Verify user can place an order for dishes
    ${dishes_list}=    Create List    ${NEW_DISH_ID}
    ${order_payload}=    Create Dictionary    user_id=${USER_ID}    restaurant_id=${NEW_RES_ID}    dishes=${dishes_list}
    ${response}=    POST On Session    foodie    /orders    json=${order_payload}
    Status Should Be    201    ${response}
    Set Suite Variable    ${ORDER_ID}    ${response.json()['id']}

Submit Rating And Feedback
    [Documentation]    Verify user can rate an order
    ${rating_payload}=    Create Dictionary    order_id=${ORDER_ID}    rating=5    comment=Excellent food!
    ${response}=    POST On Session    foodie    /ratings    json=${rating_payload}
    Status Should Be    201    ${response}

View Admin Feedback
    [Documentation]    Verify admin can view submitted feedback
    ${response}=    GET On Session    foodie    /admin/feedback
    Status Should Be    200    ${response}
    Should Not Be Empty    ${response.json()}

### --- CLEANUP --- ###

Delete Dish
    [Documentation]    Remove dish from system
    ${response}=    DELETE On Session    foodie    /dishes/${NEW_DISH_ID}
    Status Should Be    200    ${response}

Delete Restaurant
    [Documentation]    Cleanup restaurant test data
    ${response}=    DELETE On Session    foodie    /restaurants/${NEW_RES_ID}
    Status Should Be    200    ${response}