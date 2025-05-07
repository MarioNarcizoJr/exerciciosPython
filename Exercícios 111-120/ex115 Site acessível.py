import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print('\033[0;31mUops, o site ou a conexão com a internet está fora do ar, por favor tente novamente mais tarde.\033[m')
else:
    print('\033[0;32mEURECA, o site está online, boa navegação.\033[m')
