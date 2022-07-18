*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
Library    AutoItLibrary

*** Variables ***

#${ARN}     IPv4
${ARN}     IPv6
#${ARN}     IPv4/IPv6

*** Test Cases ***

TC7: LTE_Test_HTTP_APN_IPv4_Or_IPv6_Or_Both
        Set Preferred network As LTE
        Validate if the Preferred network is set to LTE
        Set ARN to IPv4 or IPv6 or Both     ${ARN}  #Change ARN value in the Variables Section according to requirements
        Press Keycode    3
        Run Speed Test in Browser

TC8: 3G_Test_HTTP_APN_IPv4_Or_IPv6_Or_Both
        Set Preferred network As 3G
        Validate if the Preferred network is set to 3G
        Set ARN to IPv4 or IPv6 or Both     ${ARN}  #Change ARN value in the Variables Section according to requirements
        Press Keycode    3
        Run Speed Test in Browser

TC9: 2G_Test_HTTP_APN_IPv4_Or_IPv6_Or_Both
        Set Preferred network As 2G
        Validate if the Preferred network is set to 2G
        Set ARN to IPv4 or IPv6 or Both     ${ARN}  #Change ARN value in the Variables Section according to requirements
        Press Keycode    3
        Run Speed Test in Browser