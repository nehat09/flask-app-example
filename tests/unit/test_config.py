from server import config


def test_development_configuration():
    configuration = config.DevelopmentConfig()
    assert configuration.TESTING == False
    assert configuration.DEBUG == True


def test_testing_configuration():
    configuration = config.TestConfig()
    assert configuration.TESTING == True
    assert configuration.DEBUG == True
