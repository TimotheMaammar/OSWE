# Client minimaliste permettant de gérer les websockets
#
# Utilisation : 
#   python3 wsclient.py --url wss://[URL] -k [KEY] -v
# Exemple : 
#   python3 wsclient.py --url wss://openitcockpit/sudo_server -k 1fea123e07f730f76e661bced33a94152378611e -v

import websocket
import ssl 
import json
import argparse
import _thread as thread

uniqid = ""
key = ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', '-u',
                        required=True,
                        dest='url',
                        help='Websocket URL')
    parser.add_argument('--key', '-k',
                        required=True,
                        dest='key',
                        help='openITCOCKPIT Key')
    parser.add_argument('--verbose', '-v',
                        help='Print more data',
                        action='store_true')
    args = parser.parse_args()

    key = args.key
    websocket.enableTrace(args.verbose)
    ws = websocket.WebSocketApp(args.url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              on_open = on_open)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

def on_open(ws):
    def run():
        while True:
            cmd = input()
            ws.send(toJson("execute_nagios_command", cmd))
    thread.start_new_thread(run, ())

def toJson(task,data):
    req = {
        "task": task,
        "data": data,
        "uniqid": uniqid,
        "key" : key
    }
    return json.dumps(req)

def on_message(ws, message):
    mes = json.loads(message)

    if "uniqid" in mes.keys():
        uniqid = mes["uniqid"]
      
    print(mes)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("[+] Connection Closed")
