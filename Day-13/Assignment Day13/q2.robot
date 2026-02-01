*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=day13testdata.csv
Test Template     Login With Multiple Users
Suite Setup       Open Browser To Site
Suite Teardown    Close Browser


*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    chrome


*** Keywords ***
Open Browser To Site
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login With Multiple Users
    [Arguments]    ${username}    ${password}
    Input Text     id=user-name    ${username}
    Input Text     id=password     ${password}
    Click Button   id=login-button
    Sleep          2s
    Capture Page Screenshot
    Go To          ${URL}


*** Test Cases ***
Login With Multiple Users
    # Data comes from CSV automatically