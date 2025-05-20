# Design and Archtitecture Dossier

## Class diagrams
```mermaid
classDiagram

class Cfg {
      config
      cfg_fn
    + get_api_key()
      
    + __init__()
}
class APIList {
    api_list: dict
    foo
    get_dict()
    get_headers()
        __init__()
}
class Foo {
        ~ last
    __init__()
}

class ApiReader {
    get()
    post()
    put()
        lst_response
    dta
    __init__()
}

class RESTList {
    foo()
        bar
}   

APIList <|-- RESTList

```


## Sequence diagram

```mermaid

sequenceDiagram
    autonumber
    API->>Python: api/v1/users/
    loop iterate user list
        Python->>Python: parse item from JSON to native data structure
    end
    Note right of Python: Rational thoughts!
    Python-->>PreSQLPersistor: Transform
    PreSQLPersistor-->> FileSystem: Transform
    PreSQLPersistor->>RDBMS: Persisting
    
```

## Securitiy implications

```mermaid
zenuml
    title Participants
    @Actor Alice
    @Database Bob
    Alice->Bob: ACK
    Bob->Alice: SYN/ACK
    Bob->Claire: ACK/SYN
    Bob->Didier: ACK/SYN
    Claire->Cryp: Key gen.
    Cryp.SyncMessage
    Cryp.SyncMessage(with, parameters) {
      B.nestedSyncMessage()
      return result
    }
```

## RFCstuff

```mermaid
---
title: "TCP Packet"
---
packet-beta
0-15: "Source Port"
16-31: "Destination Port"
32-63: "Sequence Number"
64-95: "Acknowledgment Number"
96-99: "Data Offset"
100-105: "Reserved"
106: "URG"
107: "ACK"
108: "PSH"
109: "RST"
110: "SYN"
111: "FIN"
112-127: "Window"
128-143: "Checksum"
144-159: "Urgent Pointer"
160-191: "(Options and Padding)"
192-255: "Data (variable length)"
```