*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${file_name}    "manual_en.pdf"

*** Test Cases ***

TC_3_1:FTP_Download_link_check_LTE

        Set Preferred network As LTE
        Validate if the Preferred network is set to LTE
        FTP_Download        ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_3_2:FTP_Download_link_check_3G

        Set Preferred network As 3G
        Validate if the Preferred network is set to 3G
        FTP_Download        ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3

TC_3_3:FTP_Download_link_check_2G

        Set Preferred network As 2G
        Validate if the Preferred network is set to 2G
        FTP_Download        ${file_name}
        # Keycode 3 will take you to the homepage
        Press Keycode    3