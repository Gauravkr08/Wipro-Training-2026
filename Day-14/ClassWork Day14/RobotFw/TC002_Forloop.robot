*** Test Cases ***
Print Names using for loop
    FOR    ${name}    IN    Ram    Ravi    Raj
        Log To Console    ${name}
    END

WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log To Console    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END
If-Else Exampe
     ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END

IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log To Console    Grade A
    ELSE IF    ${marks} >= 75
        Log To Console    Grade B
    ELSE
        Log To Console    Grade C
    END


Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log To Console    Test Passed


FOR Loop Example
    FOR    ${name}    IN    Ram    Ravi    Raj
        Log To Console    ${name}
    END


BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log To Console    ${i}
    END


CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log To Console    ${i}
    END


WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END


Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log To Console    Error handled
    FINALLY
        Log To Console    Always executed
    END


Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log To Console    Test Passed


Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log To Console    Test Failed