*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
Library    AutoItLibrary

*** Test Cases ***

TC_1_1:Download_link_check_LTE
    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    # Keycode 3 will take you to the homepage
    Press Keycode    3
    Direct Test File Download Link

TC_1_2:Download_link_check_3G
    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    # Keycode 3 will take you to the homepage
    Press Keycode    3
    Direct Test File Download Link

TC_1_3:Download_link_check_2G
    Set Preferred network As 2G
    Validate if the Preferred network is set to 2G
    # Keycode 3 will take you to the homepage
    Press Keycode    3
    Direct Test File Download Link