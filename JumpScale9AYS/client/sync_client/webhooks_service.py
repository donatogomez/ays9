class WebhooksService:
    def __init__(self, client):
        self.client = client



    def webhooks_events_post(self, data, headers=None, query_params=None):
        """
        Endpoint that receives generic events
        It is method for POST /webhooks/events
        """
        uri = self.client.base_url + "/webhooks/events"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def webhooks_github_post(self, data, headers=None, query_params=None):
        """
        Endpoint that receives the events from github
        It is method for POST /webhooks/github
        """
        uri = self.client.base_url + "/webhooks/github"
        return self.client.post(uri, data, headers=headers, params=query_params)
