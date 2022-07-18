*** Settings ***

Library  AppiumLibrary
Library     DateTime

*** Keywords ***
Open Browser
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=WWCIXWGEAAX8VWY9     appPackage=com.android.chrome   appActivity=com.google.android.apps.chrome.Main     noReset=${True}

Send Message
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=WWCIXWGEAAX8VWY9     appPackage=com.google.android.apps.messaging   appActivity=com.google.android.apps.messaging.home.HomeActivity     noReset=${True}

Call
        Open Application    http://localhost:4723/wd/hub    platformName=Android    deviceName=WWCIXWGEAAX8VWY9     appPackage=com.google.android.dialer   appActivity=com.android.dialer.DialtactsActivity     noReset=${True}
