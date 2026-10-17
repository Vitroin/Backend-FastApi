def test_trip_analysis_flags_harsh_braking(client, auth_headers):
    payload = {
        "trip_id": "trip-1",
        "sensor_readings": [
            {"timestamp": 1.0, "acceleration_x": -1.2},
            {"timestamp": 2.0, "acceleration_x": -4.0},
            {"timestamp": 3.0, "acceleration_x": -6.5},
        ],
    }

    response = client.post("/analysis/trip", json=payload, headers=auth_headers)

    assert response.status_code == 200
    body = response.json()
    assert body["trip_id"] == "trip-1"
    assert body["status"] == "completed"
    assert [incident["timestamp"] for incident in body["incidents"]] == [2.0, 3.0]
    assert all(incident["type"] == "harsh_braking" for incident in body["incidents"])


def test_trip_analysis_with_no_incidents(client, auth_headers):
    payload = {
        "trip_id": "trip-2",
        "sensor_readings": [{"timestamp": 1.0, "acceleration_x": 0.5}],
    }

    response = client.post("/analysis/trip", json=payload, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["incidents"] == []


def test_trip_analysis_rejects_invalid_payload(client, auth_headers):
    payload = {"trip_id": "trip-3", "sensor_readings": [{"timestamp": 1.0}]}

    response = client.post("/analysis/trip", json=payload, headers=auth_headers)

    assert response.status_code == 422
