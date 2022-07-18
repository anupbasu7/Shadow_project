*** Settings ***
Resource        ../Resources/CommonFunctionality.resource
#Library  AppiumLibrary
#Library     DateTime

Test Setup      Send Message

*** Test Cases ***
Message Automation
#    Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=WWCIXWGEAAX8VWY9     appPackage=com.android.chrome   appActivity=com.google.android.apps.chrome.Main     noReset=${True}
    Sleep       1s
    Click Element    id=start_chat_fab
    Sleep       1s
    Input Value    id=recipient_text_view    8011843630
    Sleep    1s
    press keycode           66
    Sleep    1s
    Input Text    id=compose_message_text    Hello_Anand
    Sleep    1s
    Click Element    id=send_message_button_icon
    Sleep    1s