*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${Phone_no}    8011843630

*** Test Cases ***

TC:Text_Msg_Automation
    Send Message        ${Phone_no}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots