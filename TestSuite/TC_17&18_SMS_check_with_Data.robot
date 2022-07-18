*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${Phone_no}     7002539096

*** Test Cases ***

TC_17: SMS_check_on_LTE_connection
    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    Send Message    ${Phone_no}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_18: SMS_check_on_3G_connection

    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    Send Message     ${Phone_no}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots