This error is indicating that the protocol file you are trying to run does not have an API version specified in the metadata. To fix this error, you need to add the API version number to the metadata by adding a line like this at the beginning of your Python script:

```
metadata = {
    'protocolName': 'My Protocol',
    'author': 'John Doe',
    'description': 'A cool experiment',
    'apiLevel': '2.10'
}
```

In this case, the API level specified is `2.10`, but you should replace this with the appropriate version of the Opentrons API that you are using.


:*************************


