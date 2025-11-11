from src.data_feed import load_mock_data

def test_mock_data_structure():
    """
    Ensure mock data loads correctly and contains required fields for simulation.
    """
    data = load_mock_data()
    
    # Check it's a list
    assert isinstance(data, list), "Mock data should be a list"
    
    # Check it's not empty
    assert len(data) > 0, "Mock data should not be empty"

    # Check required keys in first frame
    first_frame = data[0]
    assert isinstance(first_frame, dict), "Each frame should be a dictionary"
    assert "time" in first_frame, "Frame should contain 'time'"
    assert "sector_flags" in first_frame, "Frame should contain 'sector_flags'"
    assert isinstance(first_frame["sector_flags"], dict), "'sector_flags' should be a dictionary"
