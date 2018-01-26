def cheeseshop(kind, *arguments, ** keywords):
	print('Do you have any', kind, "?")
	print("I am sorry, we're all out of", kind)
	
	for arg in arguments:
		print(arg)
	print("-" * 40)
	
	for kw in keywords:
		print(kw, ':', keywords[kw])
		

cheeseshop("Limburer", "It is very runny, sir.", "Fuck you !", shopkeeper="Michael Plain", client="John Cleese",
			sketch="Cheese Shop sketch")