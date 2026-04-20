import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy

# Store the original activities data
original_activities = copy.deepcopy(activities)

@pytest.fixture
def client():
    # Reset the activities data before each test
    activities.clear()
    activities.update(copy.deepcopy(original_activities))
    yield TestClient(app)