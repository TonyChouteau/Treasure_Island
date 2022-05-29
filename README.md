# Treasure_Island
Treasure_Island


## Coding guidelines
- Follow the [PEP8 conventions](https://peps.python.org/pep-0008/)

- Try to avoid multiple inheritance entirely.

- Comment not obvious code sections.

## Installation
___

### NodeJS

```npm install```

### Python >=3.6

```pip install websockets opencv-python numpy```

## Development
___

### Map processing

//

### Make jquery d.ts files for typescript (Don't do this again)

```npm install typings``` \
```.\node_modules\.bin\typings install dt~jquery --global --save```

### Compile front-end app from typescript

One last thing is to add a file "websocket_url.ts" in the "src" folder with the content : \
```export default "ws://localhost:8001/"```

```npm run dev```

## Run
___

### Websocket

```python3 ./run.py```
