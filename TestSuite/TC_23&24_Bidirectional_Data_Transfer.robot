*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${Phone_no}     8011843630
${file_name}    "Test.zip.pdf"

*** Test Cases ***

TC23: Bidirectional Data Transfer on LTE connection

    Set Preferred network As LTE
    Validate if the Preferred network is set to LTE
    # Keycode 3 will take you to the homepage
    Press Keycode    3
    Direct Test File Download Link
    HTTP Upload     ${file_name}
    # Keycode 3 will take you to the homepage
    Press Keycode    3

TC24: Bidirectional Data Transfer on 3G connection

    Set Preferred network As 3G
    Validate if the Preferred network is set to 3G
    # Keycode 3 will take you to the homepage
    Press Keycode    3
    Direct Test File Download Link
    HTTP Upload     ${file_name}
    # Keycode 3 will take you to the homepage
    Press Keycode    3
