def setPorts(visionAddress = "224.0.0.1", visionPort = 10002, refereeAddress = "224.5.23.2", refereePort = 10003, firaAddress = "127.0.0.1", firaPort = 20011):
    ports["visionAddress"] = visionAddress
    ports["visionPort"] = visionPort

    ports["refereeAddress"] = refereeAddress
    ports["refereePort"] = refereePort

    ports["firaAddress"] = firaAddress
    ports["firaPort"] = firaPort


ports = {
    "visionAddress": "224.0.0.1",
    "visionPort": 10002,

    "refereeAddress": "224.5.23.2",
    "refereePort": 10003,

    "firaAddress": "127.0.0.1",
    "firaPort": 20011
}