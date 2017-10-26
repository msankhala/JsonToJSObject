# Json To Js Object

My custom SublimeText 3 plugins to convert JSON object to valid js object. This plugins do not work in all cases. Currently it convert all the json strings in a file into js object.

## @TODO
Imrove plugin to consider more cases and only convert selected json string into js object.

Sometimes you may want to convert a valid json response to a valid javascript object. For example you are getting json data from an api. You want to use that json response as javascript object inside your application.

### Use case 
Using dummy json object as valid js object in writing test cases.

Currently following standard
- Valid js object should use single quote around values as per eslint rule.
- Valid js object should use single quote in keys name if key has special characters.

### Command
 `cmd+shift+p` then run `Json to js object` command
