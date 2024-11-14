data = [{"productType": "Edibles", "name": "dogfood", "supplier": "mewmew", "price": 20, "amount": 10, "sales": 0, "expiry": 1004, "petType": "dog"}, {"productType": "Accessories", "name": "dogtoy", "supplier": "mewmew", "price": 30, "amount": 5, "sales": 0, "isChewable": False, "color": "yellow"}, {"productType": "Accessories", "name": "cattoy", "supplier": "woofwoof", "price": 40, "amount": 50, "sales": 0, "isChewable": True, "color": "red"}]
test = [2, 4, 65, 1, 3]

def sort(data):
	n = len(data)
	for i in range(1, n):
		key = data[i]
		j=i-1
		while j>=0 and key>data[j]:
			data[j+1]=data[j]
			j-=1
		data[j+1] = key
	return data

def sortdict(data):
	n = len(data)
	for i in range(1, n):
		key = data[i]['price']
		pos = data[i]
		j=i-1
		while j>=0 and key>data[j]['price']:
			data[j+1]=data[j]
			j-=1
		data[j+1] = pos
	return data

print(sortdict(data))