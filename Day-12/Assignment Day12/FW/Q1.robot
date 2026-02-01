*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Gaurav
${COURSE}      Robot Framework
@{NUMBERS}     10    20    30    40

*** Test Cases ***
Test Case 1 - Logging Messages
    Log    Starting Test Case 1
    Log To Console    Hello ${NAME}, welcome to ${COURSE}!
    Log    This message goes to the log file
    Log To Console    Test Case 1 Completed

Test Case 2 - Using Variables
    Log To Console    Demonstrating scalar and list variables
    Log    Name is: ${NAME}
    Log    Course is: ${COURSE}
    Log To Console    Numbers list: @{NUMBERS}
    ${sum}=    Evaluate    sum(int(x) for x in ${NUMBERS})
    Log To Console    Sum of numbers is ${sum}
    Log    Test Case 2 Completed Successfully