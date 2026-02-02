*** Settings ***
Documentation     Robot Framework Suite with Setup and Teardown
Suite Setup       Launch Application
Suite Teardown    Close Application
Test Setup        Prepare Test
Test Teardown     Cleanup Test

Library           BuiltIn

*** Variables ***
${APP_NAME}       SampleApp

*** Test Cases ***
Login Test Case
    [Tags]    smoke
    Log    Logging into ${APP_NAME}
    ${result}=    Evaluate    5 + 5
    Should Be Equal As Integers    ${result}    10

Search Test Case
    [Tags]    regression
    Log    Performing search operation
    Should Be True    ${True}

*** Keywords ***
Launch Application
    Log    Suite Setup: Application launched

Close Application
    Log    Suite Teardown: Application closed

Prepare Test
    Log    Test Setup: Preparing test data

Cleanup Test
    Log    Test Teardown: Cleaning test data