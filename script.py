import nxlog, requests

def request_metadata(item):
    """Gets value of metadata attribute 'item', returns text string"""
    # Set metadata URL
    metaurl = 'http://metadata.google.internal/computeMetadata/v1/instance/{0}'.format(item)
    # Set header require to retrieve metadata
    metaheader = {'Metadata-Flavor':'Google'}

    # Send HTTP GET request
    r = requests.get(metaurl, headers=metaheader)

    # If present, get text payload from the response
    if r.status_code != 404:
        value = r.text
    else:
        value = None

    # Return text value
    return value

def get_attribute(event):
    """Reads metadata and stores as an event field"""
    # Get nxlog module object
    module = event.module

    # Set an attribute to retrieve; in this case: GCE instance id
    attribute = 'id'

    # Request for metadata only if not already present in the module
    if 'metadata' not in module:
        module['metadata'] = request_metadata('id')

    # Save metadata as an event field
    event.set_field(attribute, module['metadata'])
