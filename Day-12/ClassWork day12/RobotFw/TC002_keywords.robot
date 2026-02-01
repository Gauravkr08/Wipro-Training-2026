*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    firefox
    Maximize Browser Window

*** Test Cases ***
TC001.robot
    Open Application
    Title Should Be    Google
    Close Browser
