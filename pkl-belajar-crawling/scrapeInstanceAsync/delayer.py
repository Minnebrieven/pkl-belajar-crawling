import time

def hold(seco):
    time.sleep(seco)

def AsyncioTimeout(sec):
    print('AsyncioTimeout! will try again in ',sec,' sec')
    hold(sec)

def ClientError(sec):
    print('ClientError! will try again in ',sec,' sec')
    hold(sec)

def ClientPayloadError(sec):
    print('ClientPayloadError! Will try again in ',sec,'sec')
    hold(sec)

def InvalidURL(sec):
    print('InvalidURL! will try again in ',sec,' sec')
    hold(sec)

def ContentDisposition(sec):
    print('ContentDisposition! will try again in ',sec,' sec')
    hold(sec)

def ClientResponseError(sec):
    print('ClientResponseError! will try again in ',sec,' sec')
    hold(sec)

def WSServerHandshakeError(sec):
    print('WSServerHandshakeError! will try again in ',sec,' sec')
    hold(sec)

def ContentTypeError(sec):
    print('ContentTypeError! will try again in ',sec,' sec')
    hold(sec)

def TooManyRedirects(sec):
    print('TooManyRedirects! will try again in ',sec,' sec')
    hold(sec)

def ClientConnectionError(sec):
    print('ClientConnectionError! will try again in ',sec,' sec')
    hold(sec)

def ClientOSError(sec):
    print('ClientOSError! will try again in ',sec,' sec')
    hold(sec)

def ClientConnectorError(sec):
    print('ClientConnectorError! will try again in ',sec,' sec')
    hold(sec)
        
def ClientProxyConnectionError(sec):
    print('ClientProxyConnectionError! will try again in ',sec,' sec')
    hold(sec)
        
def ServerConnectionError(sec):
    print('ServerConnectionError! will try again in ',sec,' sec')
    hold(sec)

def ClientSSLError(sec):
    print('ClientSSLError! will try again in ',sec,' sec')
    hold(sec)

def ClientConnectorSSLError(sec):
    print('ClientConnectorSSLError! will try again in ',sec,' sec')
    hold(sec)
                
def ClientConnectorCertificateError(sec):
    print('ClientConnectorCertificateError! will try again in ',sec,' sec')
    hold(sec)
                
def ServerDisconnectedError(sec):
    print('ServerDisconnectedError! will try again in ',sec,' sec')
    hold(sec)
                
def ServerTimeoutError(sec):
    print('ServerTimeoutError! will try again in ',sec,' sec')
    hold(sec)

def ServerFingerprintMismatch(sec):
    print('ServerFingerprintMismatch! will try again in ',sec,' sec')
    hold(sec)