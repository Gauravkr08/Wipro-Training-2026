*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}  Chrome

*** Test Cases ***
Form Interaction Using SeleniumLibrary

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id=name    Abhi nay

    Click Element    xpath=//input[@value='radio1']

    Click Element    xpath=//input[@id='checkBoxOption1']

    Select From List By Label    id=dropdown-class-example    Option1

    ${text}=    Get Value    id=name
    Run Keyword If    '${text}' != ''    Log    Text box value entered successfully

    Sleep    2s

    ${title}=    Get Title
    Should Be Equal    ${title}    Practice Page

    Close Browser