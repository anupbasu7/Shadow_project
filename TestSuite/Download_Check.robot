*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource
Test Teardown   Close Application
Test Setup      Launch Chrome Browser

*** Test Cases ***

TC:Download_link_check_LTE

    AppiumLibrary.Input Text    id=search_box_text    https://drive.google.com/uc?export=download&id=1TVofGzjHWIPzyB-mYOiAn3e5qn77_Kvl
    ${time1}    Get Current Date
    AppiumLibrary.press keycode           66
    Open Notifications
    AppiumLibrary.Wait Until Page Contains    Download complete     timeout=500s
    ${time2}   Get Current Date
    ${final_time}     Subtract Date From Date     ${time2}        ${time1}
    Log To Console    ${final_time}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC:Download_link_check_4G

    #Please check settings first
    AppiumLibrary.Input Text    id=search_box_text    https://drive.google.com/uc?export=download&id=1TVofGzjHWIPzyB-mYOiAn3e5qn77_Kvl
    ${time1}    Get Current Date
    AppiumLibrary.press keycode           66
    Open Notifications
    AppiumLibrary.Wait Until Page Contains    Download complete     timeout=500s
    ${time2}   Get Current Date
    ${final_time}     Subtract Date From Date     ${time2}        ${time1}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots
    Log To Console    ${final_time}

TC:Download_link_check_3G

    #Please check settings first
    AppiumLibrary.Input Text    id=search_box_text    https://drive.google.com/uc?export=download&id=1TVofGzjHWIPzyB-mYOiAn3e5qn77_Kvl
    ${time1}    Get Current Date
    AppiumLibrary.press keycode           66
    Open Notifications
    AppiumLibrary.Wait Until Page Contains    Download complete     timeout=500s
    ${time2}   Get Current Date
    ${final_time}     Subtract Date From Date     ${time2}        ${time1}
    Log To Console    ${final_time}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots

TC:Download_link_check_2G

    #Please check settings first
    AppiumLibrary.Input Text    id=search_box_text    https://drive.google.com/uc?export=download&id=1TVofGzjHWIPzyB-mYOiAn3e5qn77_Kvl
    ${time1}    Get Current Date
    AppiumLibrary.press keycode           66
    Open Notifications
    AppiumLibrary.Wait Until Page Contains    Download complete     timeout=500s
    ${time2}   Get Current Date
    ${final_time}     Subtract Date From Date     ${time2}        ${time1}
    Log To Console    ${final_time}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots