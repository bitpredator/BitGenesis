from bitgenesis.kernel.bootstrap import bootstrap

bus, kernel = bootstrap()

bus.emit("perception.event", {
    "type": "system.boot",
    "data": "BitGenesis initialized"
})