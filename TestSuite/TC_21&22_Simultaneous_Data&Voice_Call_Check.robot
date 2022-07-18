*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${Phone_no}     8011843630

*** Test Cases ***

TC_21: Simultaneous_Data&Voice_Call_Check_on_LTE_connection

    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    Call Phone      ${Phone_no}
    Run Speed Test in Browser
    AppiumLibrary.Close All Applications


TC_22: Simultaneous_Data&Voice_Call_Check_on_WCDMA_connection

    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    Call Phone      ${Phone_no}
    Run Speed Test in Browser
    AppiumLibrary.Close All Applications