class WebhooksService:
    def __init__(self, client):
        self.client = client



    def webhooks_events_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Endpoint that receives generic events
        It is method for POST /webhooks/events
        """
        uri = self.client.base_url + "/webhooks/events"
        return self.client.post(uri, data, headers, query_params, content_type)


    def webhooks_github_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Endpoint that receives the events from github
        It is method for POST /webhooks/github
        """
        uri = self.client.base_url + "/webhooks/github"
        return self.client.post(uri, data, headers, query_params, content_type)
