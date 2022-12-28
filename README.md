#### The Google Cloud metadata server is available at metadata.google.internal. It is necessary to provide the header Metadata-Flavor: Google in order to get the response. For example, the request below retrieves the instance ID:

 ``` curl -H "Metadata-Flavor: Google" \
  "http://metadata.google.internal/computeMetadata/v1/instance/id"
```

Get into script.py where following Python script, which can be used with the xm_python module, collects the instance ID from the GCP metadata server and adds a field to the event record.
