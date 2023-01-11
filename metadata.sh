# Can be done using gcloud command as well from Cloud Shell
# Or Install Cloud-SDK to run it locally

INSTANCE_ID = "instance-id"
gcloud compute instances describe $INSTANCE_ID --format='value[](metadata.items.startup-script)'
