# Day 3 Notes

Goal was to create a serverless app that processed a webhook if there was a PNG in the committed files.

## Process Overview

- Webhook in Github forwards message into Azure API Management.
- API Management Endpoint proxies to an Azure Function (See functions/d3-github-webook)
- Function iterates over the message and checks for any new items that are PNGs. Each item is added to an array as a custom class to hold the URL and file name, parsed using RegEx. 
- Each of those items are saved into a container in Azure Storage Account. 
- A direct link to each blob saved in the SA is then stored in a CosmoDB collection using the MongoDB API.

## Resources

### Python

- https://www.w3schools.com/python/python_mongodb_insert.asp
- https://www.tutorialspoint.com/python/string_endswith.htm
- https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
- https://www.guru99.com/python-regular-expressions-complete-tutorial.html
- https://pythex.org/
- https://docs.python.org/3/howto/urllib2.html
- https://www.programiz.com/python-programming/regex
- https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
- https://docs.python.org/3/tutorial/errors.html
- https://docs.python.org/3/howto/logging.html
- https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
- https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules

### Azure

- https://stackoverflow.com/questions/57816849/upload-image-to-azure-blob-storage-using-python
- https://www.programcreek.com/python/example/102053/azure.storage.blob.BlockBlobService
- https://stackoverflow.com/questions/53178116/upload-file-from-url-to-microsoft-azure-blob-storage
- https://azure-storage.readthedocs.io/ref/azure.storage.blob.blockblobservice.html
- https://docs.microsoft.com/en-us/azure/storage/blobs/storage-manage-access-to-resources
- https://docs.microsoft.com/en-us/azure/azure-functions/functions-monitoring
- https://docs.microsoft.com/en-us/azure/api-management/import-function-app-as-api