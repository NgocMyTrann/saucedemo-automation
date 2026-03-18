login_test_data = [

("standard_user","secret_sauce","success"),
("standard_user","wrongpass","fail"),
("wronguser","secret_sauce","fail"),
("wronguser","wrongpass","fail"),
("","secret_sauce","fail"),
("standard_user","","fail"),
("","", "fail")

]