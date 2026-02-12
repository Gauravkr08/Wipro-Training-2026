*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    file:///C:/Users/KIIT/OneDrive/Desktop/wipro class question/Case study 4(03.02.2026)/index.html    chrome
Suite Teardown    Close Browser
Test Teardown    Capture Page Screenshot

*** Variables ***
${NAME1}      John
${AGE1}       30
${GENDER1}    Male
${CONTACT1}   9999999999
${DISEASE1}   Fever
${DOCTOR1}    Dr. Smith

${NAME2}      Alice
${AGE2}       28
${GENDER2}    Female
${CONTACT2}   8888888888
${DISEASE2}   Cold
${DOCTOR2}    Dr. Brown

*** Test Cases ***
Register Single Patient
    Wait Until Element Is Visible    id=name    10s
    Input Text    id=name      ${NAME1}
    Input Text    id=age       ${AGE1}
    Select From List By Value    id=gender    ${GENDER1}
    Input Text    id=contact   ${CONTACT1}
    Input Text    id=disease   ${DISEASE1}
    Select From List By Value    id=doctor    ${DOCTOR1}
    Click Button    id=submitBtn
    Sleep    1s

Register Multiple Patients
    Wait Until Element Is Visible    id=name    10s
    Clear Element Text    id=name
    Input Text    id=name      ${NAME2}
    Clear Element Text    id=age
    Input Text    id=age       ${AGE2}
    Select From List By Value    id=gender    ${GENDER2}
    Clear Element Text    id=contact
    Input Text    id=contact   ${CONTACT2}
    Clear Element Text    id=disease
    Input Text    id=disease   ${DISEASE2}
    Select From List By Value    id=doctor    ${DOCTOR2}
    Click Button    id=submitBtn
    Sleep    1s

