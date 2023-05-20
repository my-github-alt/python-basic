#!/usr/bin/env python
# coding: utf-8

import pytest
import requests


@pytest.mark.tags('api_free_001')
def test_iseven_is_true_bij_een_even_nummer():
    # given
    number = 2
    # when
    response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{number}/")
    data: dict = response.json()
    # then
    assert response.ok, f"{response.status_code} {response.reason} body: {data}"
    # and
    iseven: bool = data.get('iseven')
    assert iseven and isinstance(iseven, bool), f"iseven should be True, received {iseven}"


@pytest.mark.tags('api_free_002')
def test_iseven_is_false_bij_een_oneven_nummer():
    # given
    number = 1
    # when
    response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{number}/")
    data: dict = response.json()
    # then
    assert response.ok, f"{response.status_code} {response.reason} body: {data}"
    # and
    iseven: bool = data.get('iseven')
    assert not iseven and isinstance(iseven, bool), f"iseven should be False, received {iseven}"


@pytest.mark.tags('api_free_003')
def test_iseven_is_geeft_een_error_bij_een_negatief_nummer():
    # given
    number = -2
    expected_message = "Number out of range. Upgrade to isEven API Premium or Enterprise."
    # when
    response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{number}/")
    data: dict = response.json()
    # then
    assert not response.ok, f"{response.status_code} {response.reason} body: {data}"
    # and
    error_message: str = data.get('error')
    assert error_message == expected_message, f"error message was not the same, received: {error_message}"
    # and
    iseven: None = data.get('iseven')
    assert iseven is None, f"iseven should not be available in error response, received: {iseven}"


@pytest.mark.tags('api_free_004')
def test_iseven_is_geeft_een_error_bij_een_te_groot_nummer():
    # given
    number = 1_000_000
    expected_message = ...
    # when

    # then

    # and
    pytest.fail('Todo!')


if __name__ == '__main__':
    pytest.main(['--verbosity=1'])
