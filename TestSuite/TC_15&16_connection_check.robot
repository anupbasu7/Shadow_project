*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Test Cases ***

TC_15_1: 4G_LTE_connection_IPv4
    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    Test IPv4 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_15_2: 3G_connection_IPv4
    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    Test IPv4 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_15_3: 2G_connection_IPv4
    Set Preferred network As 2G
    Validate if the Preferred network is set to 2G
    Test IPv4 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_16_1: 4G_LTE_connection_IPv6
    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    Test IPv6 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_16_2: 3G_LTE_connection_IPv6
    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    Test IPv6 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC_16_3: 2G_LTE_connection_IPv6
    Set Preferred network As 2G
    Validate if the Preferred network is set to 2G
    Test IPv6 In Browser
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots