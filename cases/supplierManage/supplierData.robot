*** Settings ***

Library  supplierData.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     供应商   信息管理页  

Library  supplierData.c1201   WITH NAME  c1201

Library  supplierData.c1202   WITH NAME  c1202

Library  supplierData.c1203   WITH NAME  c1203

Library  supplierData.c1204   WITH NAME  c1204

Library  supplierData.c1205   WITH NAME  c1205



*** Test Cases ***

信息管理页 - UI-1201

  c1201.teststeps


信息管理页 - UI-1202

  c1202.teststeps


信息管理页 - UI-1203

  c1203.teststeps


信息管理页 - UI-1204

  c1204.teststeps


信息管理页 - UI-1205

  c1205.teststeps
