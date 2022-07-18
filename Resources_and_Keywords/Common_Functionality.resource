*** Settings ***
Documentation       This file handles app configuration, reuseable scripts,etc.
Library     DateTime
Library     SeleniumLibrary
Library     AppiumLibrary

*** Variables ***
${HOST_NAME}     http://localhost:4723/wd/hub
${device_Name}    WWCIXWGEAAX8VWY9
${app_Package}    com.android.chrome
${app_Activity}   com.google.android.apps.chrome.Main


*** Keywords ***

Launch Chrome Browser
        [Documentation]     This Keyword will Launch the Browser and navigate to a new Tab
        Open Application    ${HOST_NAME}    platformName=Android     deviceName=${device_Name}     appPackage=${app_Package}     appActivity=${app_Activity}     noReset=${True}
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Element    id=menu_button
        AppiumLibrary.Click Element     id=new_tab_menu_id

Launch Messaging App
        [Documentation]     This Keyword will Launch the Messaging application in your Android Devices
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}    appPackage=com.google.android.apps.messaging   appActivity=com.google.android.apps.messaging.home.HomeActivity      noReset=${True}
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s

Airplane mode Switch
        [Documentation]     This Keyword will switch the android device to Airplane mode
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}     noReset=${True}
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s

Launch Calculator App
        [Documentation]     This Keyword will Launch the Calculator App in your Android Devices
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}     appPackage=com.coloros.calculator       appActivity=com.android.calculator2.Calculator     noReset=${True}
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s

Launch Contact App
        [Documentation]     This Keyword will Launch the Contact Application in your Android Device
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}     appPackage=com.google.android.contacts       appActivity=com.google.android.apps.contacts.activities.PeopleActivity     noReset=${True}
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s

Launch Settings App
        [Documentation]     This Keyword will Launch the Settings Application
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}     appPackage=com.android.settings       appActivity=com.oppo.settings.SettingsActivity     noReset=${True}      fullReset=${False}
        SeleniumLibrary.Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s


Launch Call Management App
        [Documentation]     This Keyword will Launch the Phone/Dialer in Android Devices
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${device_Name}     appPackage=com.google.android.dialer       appActivity=com.android.dialer.main.impl.MainActivity   noReset=${True}      appWaitForLaunch=${False}
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        set selenium implicit wait      30s

Set Preferred network As LTE
        [Documentation]     This Keyword will set the Preffered Network to LTE in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Click Text    Preferred network type
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.CheckedTextView[@text="4G/3G/2G (Auto)"]
        Sleep    1s

Validate if the Preferred network is set to LTE
        [Documentation]     This Keyword will validate if the Preffered Network is set to LTE in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Wait Until Page Contains    4G/3G/2G (Auto)

Set Preferred network As 3G
        [Documentation]     This Keyword will set the Preffered Network to 3G in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Click Text    Preferred network type
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.CheckedTextView[@text="3G/2G (Auto)"]
        Sleep    1s

Validate if the Preferred network is set to 3G
        [Documentation]     This Keyword will validate if the Preffered Network is set to 3G in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Wait Until Page Contains    3G/2G (Auto)

Set Preferred network As 2G
        [Documentation]     This Keyword will set the Preffered Network to 2G only in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Click Text    Preferred network type
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.CheckedTextView[@text="2G Only"]
        Sleep    1s

Validate if the Preferred network is set to 2G
        [Documentation]     This Keyword will validate if the Preffered Network is set to 2G in Android Devices
        Launch Settings App
        set selenium implicit wait      30s
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        AppiumLibrary.Click Text    SIM card & mobile data
        Sleep    1s
        AppiumLibrary.Click Text    SIM2
        Sleep    1s
        AppiumLibrary.Wait Until Page Contains    2G Only


Call Phone
        [Documentation]     This Keyword will open dialer and call the given phone_no in Android Devices
        [Arguments]     ${Phone_no}
        Launch Call Management App
        set selenium implicit wait      30s
        Sleep    1s
        AppiumLibrary.Click Element     id=dialpad_fab
        Sleep    1s
        AppiumLibrary.Input Value    id=digits    ${Phone_no}
        AppiumLibrary.Click Element    id=dialpad_voice_call_button
        Sleep    1s
        AppiumLibrary.Click Text    SIM1
        Sleep    1s

Send Message
        [Documentation]     This Keyword will Send Message to a phone from the android device
        [Arguments]     ${Phone_no}
        Launch Messaging App
        set selenium implicit wait      30s
        AppiumLibrary.Click Element    id=start_chat_fab
        Sleep    1s
        AppiumLibrary.Input Value    id=recipient_text_view    ${Phone_no}
        AppiumLibrary.press keycode           66
        AppiumLibrary.Click Element    id=send_message_button_icon
        AppiumLibrary.Click Text    SIM2
        AppiumLibrary.Input Text    id=compose_message_text    Hello_Ananda_Test_Case_Check
        AppiumLibrary.Click Element    id=send_message_button_icon
        Sleep    2s

Test IPv6 In Browser
        [Documentation]     This Keyword will Launch Browser and Chect if the Android device has IPv6 Compatibility
        Launch Chrome Browser
        set selenium implicit wait      30s
        AppiumLibrary.Input Text    id=search_box_text    https://test-ipv6.com/
        AppiumLibrary.press keycode           66
        AppiumLibrary.Wait Until Page Contains    Your IPv6 address on the public Internet appears to be     timeout=5s

Test IPv4 In Browser
        [Documentation]     This Keyword will Launch Browser and Chect if the Android device has IPv4 Compatibility
        Launch Chrome Browser
        set selenium implicit wait      30s
        AppiumLibrary.Input Text    id=search_box_text    https://test-ipv6.com/
        AppiumLibrary.press keycode           66
        AppiumLibrary.Wait Until Page Contains    Your IPv4 address on the public Internet appears to be     timeout=5s

Run Speed Test in Browser
        [Documentation]     This Keyword will Launch Browser and check the internet connection in the Android device
        Launch Chrome Browser
        Sleep    1s
        set selenium implicit wait      30s
        AppiumLibrary.Input Text    id=search_box_text    speed test
        AppiumLibrary.press keycode           66
        Sleep    1s
        AppiumLibrary.Wait Until Page Contains    RUN SPEED TEST
        Sleep    1s
        Close All Applications

Direct Test File Download Link
        [Documentation]     This Keyword will Launch Browser download a demo file in the Android device
        set selenium implicit wait      30s
        Launch Chrome Browser
        Sleep    1s
        AppiumLibrary.Input Text    id=search_box_text    https://drive.google.com/uc?export=download&id=16LykHzZOb1kAxr4t_NPKHIrbYnUR9iCg
        ${time1}    Get Current Date
        AppiumLibrary.press keycode           66
        Open Notifications
        AppiumLibrary.Wait Until Page Contains    Download complete     timeout=500s
        Press Keycode    4
        ${time2}   Get Current Date
        ${final_time}     Subtract Date From Date     ${time2}        ${time1}
        Press Keycode    3
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots
        Log To Console    ${final_time}


Set ARN to IPv4 or IPv6 or Both
        [Documentation]     This Keyword will Set ARN to IPv4/IPv6 or both based on input on the android device
        [Arguments]     ${ARN}
        Launch Settings App
        set selenium implicit wait      10s
        AppiumLibrary.Click Text    SIM card & mobile data
        AppiumLibrary.Click Text    SIM2
        AppiumLibrary.Click Text    Access point names
        Sleep    1s
        AppiumLibrary.Click Text    Airtel MMS
        Scroll        //android.widget.TextView[@text="MCC"]       //android.widget.TextView[@text="Server"]
        Scroll        //android.widget.TextView[@text="APN Protocol"]       //android.widget.TextView[@text="MMS Port"]
        AppiumLibrary.Click Text    APN Protocol
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="${ARN}"]
        AppiumLibrary.Click Element    //android.widget.TextView[@content-desc="save"]
        AppiumLibrary.Click Element    //android.widget.Button[@text="Save"]
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots


FTP_Download
        [Documentation]     This Keyword will download a FTP file in the android device
        [Arguments]     ${file_name}
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${deviceName}       appPackage=com.wftpserver.ftprush   appActivity=crc64479b29261e5a40c6.SplashActivity      noReset=${True}
        Sleep    10s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="Demo"]
        Sleep    10s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="download"]
        Sleep    10s
        AppiumLibrary.Click Element         //android.widget.TextView[@text=${file_name}]
        AppiumLibrary.Wait Until Page Contains    Open     timeout=300s
        Log To Console    "FTP File Downloaded"
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots

FTP_Upload
        [Documentation]     This Keyword will upload a FTP file in the android device
        [Arguments]     ${file_name}
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${deviceName}       appPackage=com.wftpserver.ftprush   appActivity=crc64479b29261e5a40c6.SplashActivity      noReset=${True}
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="Demo"]
        Sleep    10s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="upload"]
        Sleep    10s
        AppiumLibrary.Click Element    //android.widget.Button[@bounds="[651,68][703,154]"]
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="Upload file"]
        Sleep    2s
        AppiumLibrary.Click Element    //android.widget.CompoundButton[@text="Documents"]
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text=${file_name}]
        #Validation here
        AppiumLibrary.Wait Until Page Contains    /upload/     timeout=10s
        Log To Console    FTP File Uploaded
        Set Screenshot Directory    ${EXECDIR}${/}Screenshots

HTTP Upload
        [Documentation]     This Keyword will upload a FTP file in the android device
        [Arguments]     ${file_name}
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=${deviceName}       appPackage=com.google.android.apps.docs   appActivity=com.google.android.apps.docs.drive.startup.StartupActivity      noReset=${True}
        Sleep    1s
        AppiumLibrary.Click Element    id=navigation_bar_item_active_indicator_view
        Sleep    1s
        AppiumLibrary.Click Element    id=extended_fab
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text="Upload"]
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.CompoundButton[@text="Documents"]
        Sleep    1s
        AppiumLibrary.Click Element    //android.widget.TextView[@text=${file_name}]
        #Validation here
        AppiumLibrary.Wait Until Page Contains    Test.zip.pdf     timeout=10s
        Log To Console    HTTP File Uploaded


Add Contact
        [Documentation]     This Keyword will create a new contact in the android device
        [Arguments]     ${first_name}       ${last_name}        ${Phone_number}
        Set Selenium Implicit Wait    10s
        Launch Contact App
        AppiumLibrary.Click Element    id=floating_action_button
        AppiumLibrary.Input Text    xpath=//android.widget.EditText[@text="First name"]    ${first_name}
        AppiumLibrary.Input Text    xpath=//android.widget.EditText[@text="Last name"]    ${last_name}
        AppiumLibrary.Input Value    xpath=//android.widget.EditText[@text="Phone"]    ${Phone_number}
        AppiumLibrary.Click Element    xpath=//android.widget.Button[@text="Save"]

Validate Contact
        [Documentation]     This Keyword will validate a newly created contact in the android device
        [Arguments]     ${first_name}       ${last_name}        ${Phone_number}
        Set Selenium Implicit Wait    10s
        Launch Contact App
        Sleep    2s
        AppiumLibrary.Click Element    xpath=//android.widget.TextView[@text="Search contacts"]
        AppiumLibrary.Input Text    id=open_search_view_edit_text    ${first_name}
        AppiumLibrary.Wait Until Page Contains    ${last_name}
