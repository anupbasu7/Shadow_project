*** Settings ***

Resource        ../Resources_and_Keywords/Common_Functionality.resource

*** Variables ***

${first_name}    Test
${last_name}     Number
${Phone_number}     8011843631

*** Test Cases ***

TC_5:Add_Contact_Automation
    Add Contact     ${first_name}       ${last_name}        ${Phone_number}
    Validate Contact        ${first_name}       ${last_name}        ${Phone_number}
    Set Screenshot Directory    ${EXECDIR}${/}Screenshots


