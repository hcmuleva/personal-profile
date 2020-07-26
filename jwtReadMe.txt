****JWT*****


assuming there are 2 role

	UserName	Password	Role
1//	Arpita		hkak		Admin
2// 	Aaditya		adi		developer


in general 1st
->client enters login details
->info goes to server matches the details from db
-> shows if AUTHENTICATED or not
-> next sm operations can be done only admin(assuming delete operation)
->now that client wants to perform delete operation the server