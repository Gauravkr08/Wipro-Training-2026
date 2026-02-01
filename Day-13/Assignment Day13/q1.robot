*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome
${TITLE}    Your Store

*** Test Cases ***
Verify Page Title And Capture Screenshot
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    ${TITLE}
    Capture Page Screenshot
    Close Browser