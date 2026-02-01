*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    temp1

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}  chrome

*** Keywords ***
open orangehrm
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

orangehrmlogin with Excel
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//*[@type="submit"]
    Sleep    3s
    Close Browser

temp1
    [Arguments]    ${username}    ${password}
    open orangehrm
    orangehrmlogin with Excel    ${username}    ${password}

*** Test Cases ***
Login using Excel