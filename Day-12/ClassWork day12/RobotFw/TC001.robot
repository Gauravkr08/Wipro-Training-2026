*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***

Open Google
    Open Browser    https://www.google.com    firefox
    Title Should Be    Google
    Close Browser