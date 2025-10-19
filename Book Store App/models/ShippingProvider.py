# Shipping Provider

class ShippingProvider:
    def __init__(self, provider_id: str, name: str, tracking_url: str):
        self.__provider_id = provider_id
        self.__name = name
        self.__tracking_url = tracking_url

    def get_status(self, order_id: str) -> str:
        # Simulate checking status
        print(f"Checking shipping status for Order {order_id} via {self.__name}")
        return f"Order {order_id} is in transit."

    def update_info(self, new_url: str = None, new_name: str = None):
        if new_url:
            self.__tracking_url = new_url
        if new_name:
            self.__name = new_name
        print(f"Provider info updated: {self.__name} - {self.__tracking_url}")

    @property
    def provider_id(self) -> str:
        return self.__provider_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tracking_url(self) -> str:
        return self.__tracking_url
