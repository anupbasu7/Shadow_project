*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
#Test Teardown   Close Application
#Test Setup      Launch Messaging App
Test Setup      Airplane mode check

*** Test Cases ***

TC:Check Airplane Mode
    Open Notifications
    Sleep    1s
    Scroll Down    locator
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

