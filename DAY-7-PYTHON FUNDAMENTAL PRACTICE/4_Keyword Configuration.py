def create_device_config(device_id, **kwargs):
    accepted_fields = ["baud_rate", "parity", "timeout_ms", "debug"]

    for key in kwargs:
        if key not in accepted_fields:
            raise ValueError("Unsupported key: " + key)

    config = {"device_id": device_id}
    config.update(kwargs)

    return config


result = create_device_config(
    "D01",
    baud_rate=115200,
    parity="N",
    timeout_ms=500
)

print(result)