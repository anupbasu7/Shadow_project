*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${file_name}    "Test.zip.pdf"

*** Test Cases ***

TC_2_1:HTTP_Upload_link_check_LTE

        Set Preferred network As LTE
        Validate if the Preferred network is set to LTE
        HTTP Upload     ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_2_2:HTTP_Upload_link_check_3G

        Set Preferred network As 3G
        Validate if the Preferred network is set to 3G
        HTTP Upload     ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_2_3:HTTP_Upload_link_check_2G

        Set Preferred network As 2G
        Validate if the Preferred network is set to 2G
        HTTP Upload     ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3
