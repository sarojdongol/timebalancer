from config.settings import Setting

def test_get_config():
    width = 900
    height = 600
    config = Setting(width=width,height=height)
    actual_value = config.get_config()
    expected_value = (900,600)
    assert expected_value == actual_value
