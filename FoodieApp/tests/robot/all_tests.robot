*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://localhost:5000
Suite Teardown    Delete All Sessions

*** Test Cases ***

# ---------------- Restaurant Module ----------------
Add Restaurant
    ${body}=    Create Dictionary    name=Food Hub    category=Fast Food    location=City Center    images=[]    contact=1234567890
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    201    ${response}
    ${restaurant_id}=    Set Variable    ${response.json()["id"]}

Update Restaurant
    ${body}=    Create Dictionary    name=Food Hub Updated
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${restaurant_id}    json=${body}
    Status Should Be    200    ${response}

Disable Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${restaurant_id}/dis
    Status Should Be    200    ${response}

Get Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/${restaurant_id}
    Status Should Be    200    ${response}

# ---------------- Dish Module ----------------
Add Dish
    ${body}=    Create Dictionary    name=Pizza    type=Main    price=120    available_time=10:00-22:00    image=""
    ${response}=    POST On Session    foodie    /api/v1/restaurants/${restaurant_id}/dishes    json=${body}
    Status Should Be    201    ${response}
    ${dish_id}=    Set Variable    ${response.json()["id"]}

Update Dish
    ${body}=    Create Dictionary    price=150
    ${response}=    PUT On Session    foodie    /api/v1/dishes/${dish_id}    json=${body}
    Status Should Be    200    ${response}

Toggle Dish
    ${body}=    Create Dictionary    enabled=True
    ${response}=    PUT On Session    foodie    /api/v1/dishes/${dish_id}/status    json=${body}
    Status Should Be    200    ${response}

Delete Dish
    ${response}=    DELETE On Session    foodie    /api/v1/dishes/${dish_id}
    Status Should Be    200    ${response}

# ---------------- User Module ----------------
Register User
    ${body}=    Create Dictionary    name=Alice    email=alice@example.com    password=123
    ${response}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Status Should Be    201    ${response}
    ${user_id}=    Set Variable    ${response.json()["id"]}

Search Restaurant
    ${params}=    Create Dictionary    name=Food Hub    location=City Center    dish=Pizza    rating=
    ${response}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Status Should Be    200    ${response}

# ---------------- Order Module ----------------
Place Order
    ${body}=    Create Dictionary    user_id=${user_id}    restaurant_id=${restaurant_id}    dishes=[]
    ${response}=    POST On Session    foodie    /api/v1/orders    json=${body}
    Status Should Be    201    ${response}
    ${order_id}=    Set Variable    ${response.json()["id"]}

Give Rating
    ${body}=    Create Dictionary    order_id=${order_id}    rating=5    comment=Excellent
    ${response}=    POST On Session    foodie    /api/v1/ratings    json=${body}
    Status Should Be    201    ${response}

View Orders User
    ${response}=    GET On Session    foodie    /api/v1/users/${user_id}/orders
    Status Should Be    200    ${response}

View Orders Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/${restaurant_id}/orders
    Status Should Be    200    ${response}

# ---------------- Admin Module ----------------
Approve Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${response}

Disable Restaurant Admin
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${restaurant_id}/disable
    Status Should Be    200    ${response}

View Feedback
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${response}

View Orders Admin
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}
