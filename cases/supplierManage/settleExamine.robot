*** Settings ***

Library  settleExamine.py   WITH NAME  F

Suite Setup    F.suite_setup

Library  settleExamine.c1101   WITH NAME  c1101



*** Test Cases ***

入驻审核页 - UI-1101

  c1101.teststeps
