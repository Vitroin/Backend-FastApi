def predict_incidents(sensor_readings: list[dict]) -> list[dict]:
    """Simulate AI predictions from sensor readings."""

    incidents = []

    for reading in sensor_readings:
        # Dummy rule: acceleration_x <= -4.0 means harsh braking.
        if reading["acceleration_x"] <= -4.0:
            incidents.append({
                "type": "harsh_braking",
                "timestamp": reading["timestamp"],
                "severity": "high",
                "confidence": 0.96,
            })

    return incidents