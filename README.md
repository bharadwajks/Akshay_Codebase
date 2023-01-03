#### The Google Cloud metadata server is available at metadata.google.internal. It is necessary to provide the header Metadata-Flavor: Google in order to get the response. For example, the request below retrieves the instance ID:

 ``` curl -H "Metadata-Flavor: Google" \
  "http://metadata.google.internal/computeMetadata/v1/instance/id"
```

Get into script.py where following Python script, which can be used with the xm_python module, collects the instance ID from the GCP metadata server and adds a field to the event record.

Point  to notice here that :
Metadata-Flavor: Google

This header indicates that the request was sent with the intention of retrieving metadata values, rather than unintentionally from an insecure source, and lets the metadata server return the data you requested. If you don't provide this header, the metadata server denies your request.
