import pytest
import os
print(os.getcwd())

import metadata

@pytest.fixture
def sample_metadata():
    return metadata.metadata({'path':'sample_path'})

def test_metadata_set(sample_metadata):
    assert 'path' in sample_metadata.data
    assert 'style_structure' in sample_metadata.data
    assert 'style_colorway' in sample_metadata.data
    assert 'style_code' in sample_metadata.data
    assert 'hidden' in sample_metadata.data
    assert 'url_ext' in sample_metadata.data
    assert 'nav_group' in sample_metadata.data
    assert 'nav_order' in sample_metadata.data