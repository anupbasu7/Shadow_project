*** Settings ***

Library  AppiumLibrary
Library     DateTime
Library     BuiltIn

*** Test Cases ***

TC1
    Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=WWCIXWGEAAX8VWY9     appPackage=com.android.chrome   appActivity=com.google.android.apps.chrome.Main     noReset=${True}
#    https://speed.hetzner.de/
    Input Text    id=search_box_text        https://drive.google.com/uc?export=download&id=1uojXwBVzfCk9g_Eswlg89xywpa2Hs0L-
    Sleep    1s
    ${time1}    Get Current Date
    press keycode           66
    Sleep    2s
    Open Notifications
    Sleep   2s
    Wait Until Page Contains    Download complete     timeout=700s
    ${time2}   Get Current Date
    ${final_time}     Subtract Date From Date     ${time2}        ${time1}
    Log To Console    ${final_time}
    Close Application
