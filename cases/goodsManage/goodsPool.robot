*** Settings ***

Library  goodsPool.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     供应商   商家商品池  

Library  goodsPool.c2101   WITH NAME  c2101



*** Test Cases ***

商家商品池 - UI-2101

  c2101.teststeps
