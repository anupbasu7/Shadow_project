*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
Test Teardown       Close All Applications

*** Variables ***

${Phone_no}     8011843630

*** Test Cases ***

TC_19: Call_check_on_LTE_connection

    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    Call Phone      ${Phone_no}
    AppiumLibrary.Click Element    id=incall_end_call

TC_20: Call_check_on_WCDMA_connection

    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    Call Phone      ${Phone_no}
    AppiumLibrary.Click Element    id=incall_end_call