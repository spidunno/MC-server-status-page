for i in range(len(status.description.extra)):
	arr2.append(str(status.description.extra[i].text))
motd = ''.join(arr2)