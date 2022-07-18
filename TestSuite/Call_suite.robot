*** Settings ***
Resource        ../Resources/CommonFunctionality.resource

Test Setup      Call

*** Test Cases ***
Call Test
    Click Element    id=dialpad_fab
    Click Element    id=eight
    Click Element    id=zero
    Click Element    id=one
    Click Element    id=one
    Click Element    id=eight
    Click Element    id=four
    Click Element    id=three
    Click Element    id=six
    Click Element    id=three
    Click Element    id=zero
    Click Element    id=dialpad_voice_call_button
    Sleep    2s
    Click Element    id=text
    Close Application
