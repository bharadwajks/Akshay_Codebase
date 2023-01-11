const gcpMetadata = require('gcp-metadata');

async function metadata () {
    const isAvailable = await gcpMetadata.isAvailable();
    if (isAvailable) {
        // All metadata of the instance
        const instanceMetadata = await gcpMetadata.instance(); 
        console.log('Instance metadata:');
        console.log(instanceMetadata);
        
        // Query specific data key
        const property = await gcpMetadata.instance('startup-script');
        console.log(property);
    }
}
metadata ();
