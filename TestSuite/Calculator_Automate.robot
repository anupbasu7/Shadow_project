*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
Test Teardown   Close Application
Test Setup      Launch Calculator App

*** Test Cases ***

TC:Calculator_Automation

    AppiumLibrary.Click Element    id=digit_7
    AppiumLibrary.Click Element    id=digit_7
    AppiumLibrary.Click Element    id=op_add
    AppiumLibrary.Click Element    id=digit_6
    AppiumLibrary.Click Element    id=digit_6
    Sleep    1s
    AppiumLibrary.Click Element    id=eq
    Sleep    0.5s
    AppiumLibrary.Page Should Contain Text    143
    Sleep    1s
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots