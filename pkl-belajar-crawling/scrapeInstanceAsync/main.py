import aiohttp, asyncio, conf, platgen, bsparse, delayer, mongotor
counterStoredDict = len(conf.storedData)

class scrape:
    def __init__(self):
        self.counterStoredDict = counterStoredDict 
    async def flow1(self,session,plat):
        while True:
            f = open('counter.txt', 'r')
            counterF = f.readline()
            if counterF == None or counterF == '':
                counterF = 1
            f.close()
            try:
                async with session.get(conf.base_link,headers=conf.headers_get,ssl=False):
                    payload = {'POLA':counterF,'POLH':plat,'tombol':'Proses','flag':2,'PESAN':'+'}
                    async with session.post(conf.base_link,headers=conf.headers_post,data=payload,ssl=False) as response:
                        r = bsparse.bsparsing(await response.text(),payload.get('POLA')+payload.get('POLH'))  
                        if r != None:
                            conf.storedData.append(r)
                        print("data stored ="+self.counterStoredDict)
                if self.counterStoredDict == 100:
                    async with session.get('http://157.230.242.8:1711',json=r) as resp:
                        await resp.text()
                    conf.storedData.clear()

            except aiohttp.ClientPayloadError:
                delayer.ClientPayloadError(0.1)
            except aiohttp.InvalidURL:
                delayer.InvalidURL(0.1)
            except aiohttp.ClientProxyConnectionError:
                delayer.ClientProxyConnectionError(0.1)
            except aiohttp.ClientSSLError:
                delayer.ClientSSLError(0.1)
            except aiohttp.ClientConnectorSSLError:
                delayer.ClientConnectorSSLError(0.1)
            except aiohttp.ClientConnectorCertificateError:
                delayer.ClientConnectorCertificateError(0.1)
            except aiohttp.ClientConnectorError:
                delayer.ClientConnectorError(0.1)
            except aiohttp.ClientOSError:
                delayer.ClientOSError(0.1)
            except asyncio.TimeoutError:
                delayer.AsyncioTimeout(0.1)
            except aiohttp.ClientResponseError:
                delayer.ClientResponseError(0.1)
            except aiohttp.ServerTimeoutError:
                delayer.ServerTimeoutError(0.1)
            except aiohttp.ServerConnectionError:
                delayer.ServerConnectionError(0.1)
            except aiohttp.ClientConnectionError:
                delayer.ClientConnectionError(0.1)
            except aiohttp.ClientError:
                delayer.ClientError(0.1)
            else:
                if counterF == '1001':
                    break
                addingNewNum = int(counterF) + 1
                c = open('counter.txt','w')
                c.write(str(addingNewNum))
                c.close()
        
    async def main(self):
        async with aiohttp.ClientSession(loop=loop) as session:
            tasks = [scrape().flow1(session,plat) for plat in platgen.generatePlat()]
            await asyncio.gather(*tasks)
    
a = scrape()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a.main())
    loop.close()