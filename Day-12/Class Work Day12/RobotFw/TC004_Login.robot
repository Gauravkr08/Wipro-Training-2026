*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    chrome
${USERNAME}   Admin
${PASSWORD}   admin123

*** Test Cases ***
TC004 Login Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${USERNAME}
    Input Text    name=password    ${PASSWORD}

    Capture Page Screenshot    beforelogin.png

    Click Element    xpath=//button[@type='submit']

    Wait Until Page Contains    Dashboard    10s
    Capture Page Screenshot    afterlogin.png

    Close Browser
