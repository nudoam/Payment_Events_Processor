def test_create_and_get_event(client):
    payload = {
        "event_type": "payment_authorized",
        "payment_id": "pay_123",
        "amount": 10.5,
        "currency": "usd",
        "metadata": {"source": "web"},
    }

    r = client.post("/events", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert "id" in data
    assert data["currency"] == "USD"

    event_id = data["id"]
    r2 = client.get(f"/events/{event_id}")
    assert r2.status_code == 200
    assert r2.json()["payment_id"] == "pay_123"
