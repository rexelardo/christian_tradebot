from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class MyWrapper(EWrapper):
    def __init__(self):
        super().__init__()
        self.next_order_id = None

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        print(f"Received next valid order ID: {orderId}")
        self.next_order_id = orderId

app = EClient(MyWrapper())

# Connect to TWS/Gateway API
app.connect("127.0.0.1", 4002, clientId=0)

if app.isConnected():
    print("Connected to TWS/Gateway API!")
else:
    print("Not connected to TWS/Gateway API")

# Disconnect from TWS/Gateway API
app.disconnect()