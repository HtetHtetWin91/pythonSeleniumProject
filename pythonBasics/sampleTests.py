import requests


def test_get_users():
    url = "https://example.com/api/users"

    try:
        response = requests.get(url, timeout=10)
        assert response.status_code == 200, f"❌ Expected 200, got {response.status_code}"

        try:
            data = response.json()
        except ValueError:
            raise AssertionError("❌ Response is not valid JSON")

        assert len(data) > 0, "❌ User list is empty"
        assert "id" in data[0] and "name" in data[0], "❌ User data missing required fields"

        print("✅ API Test Passed!")

    except Exception as e:
        print(f"❌ Test failed: {e}")


# Run the test
test_get_users()
