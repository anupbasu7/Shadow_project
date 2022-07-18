*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${file_name}    "Test.zip.pdf"

*** Test Cases ***

TC_4_1:FTP_Upload_link_check_LTE

        Set Preferred network As LTE
        Validate if the Preferred network is set to LTE
        FTP_Upload      ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_4_2:FTP_Upload_link_check_3G

        Set Preferred network As 3G
        Validate if the Preferred network is set to 3G
        FTP_Upload      ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_4_3:FTP_Upload_link_check_2G

        Set Preferred network As 2G
        Validate if the Preferred network is set to 2G
        FTP_Upload      ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3