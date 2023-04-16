Yes, it seems like your protocol code is not specifying the API level. You can fix this error by adding the following lines of code at the beginning of your protocol:

```
metadata = {
    'protocolName': 'Your protocol name',
    'author': 'Your name',
    'description': 'Your protocol description',
    'apiLevel': '2.0' # change to the appropriate API level
}

# Initialize the protocol
protocol = Protocol()
``` 

Make sure to replace `Your protocol name` and `Your name` with appropriate strings. Also, change the value of `apiLevel` to the appropriate API level (e.g. 1, 2, 2.1).


:*************************


