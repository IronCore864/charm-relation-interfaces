# `my_fancy_database`

## Overview
This relation interface describes the expected behavior between of any charm claiming to be able to interface with a Fancy Database and the Fancy Database itself.
Other Fancy Database-compatible providers can be used interchangeably as well.

## Usage

Typically, you can use the implementation of this interface from [this charm library](https://github.com/your_org/my_fancy_database_operator/blob/main/lib/charms/my_fancy_database/v0/fancy.py), although charm developers are free to provide alternative libraries as long as they comply with this interface specification.

## Direction
The `my_fancy_database` interface implements a provider/requirer pattern.
The requirer is a charm that wishes to act as a Fancy Database Service consumer, and the provider is a charm exposing a Fancy Database (-compatible API).

/```mermaid
flowchart TD
    Requirer -- tables --> Provider
    Provider -- endpoint, access_keys --> Requirer
/```

## Behavior

The requirer and the provider must adhere to a certain set of criteria to be considered compatible with the interface.

### Requirer

- Is expected to publish a list of tables in the application databag


### Provide

- Is expected to publish an endpoint URL in the application databag
- Is expected to create and grant a Juju Secret containing the access key for each shard and publish its secret ID in the unit databags.

## Relation Data

See the [\[Pydantic Schema\]](./schema.py)


### Requirer

The requirer publishes a list of tables to be created, as a json-encoded list of strings.

#### Example
\```yaml
application_data: {
   "tables": "['users', 'passwords']"
}
\```

### Provider

The provider publishes an endpoint url and access keys for each shard.

#### Example

```
application_data: {
   "api_endpoint": "https://foo.com/query"
},
units_data : {
  "my_fancy_unit/0": {
     "secret_id": "secret:12312321321312312332312323"
  },
  "my_fancy_unit/1": {
     "secret_id": "secret:45646545645645645646545456"
  }
}
```
