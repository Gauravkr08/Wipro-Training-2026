*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    Starting environment verification...

    Log To Console    Python is available in the system

    ${rf_version}=    Get Variable Value    ${ROBOT_VERSION}
    Log    Robot Framework Version: ${rf_version}
    Log To Console    Robot Framework Version: ${rf_version}

    Log    SeleniumLibrary imported successfully
    Log To Console    SeleniumLibrary is available

    Log To Console    Environment verification completed successfully