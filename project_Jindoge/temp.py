url = 'http://203.253.128.177:7579/Mobius/walwal/training'

headers =	{
        'Accept':'application/json',
        'X-M2M-RI':'12345',
        'X-M2M-Origin':'walwal', # change to your aei
        'Content-Type':'application/vnd.onem2m-res+json; ty=4'
    }

data =	{
    "m2m:cin": {
        "con": a_1
    }
}

r = requests.post(url, headers=headers, json=data)
time.sleep(1)