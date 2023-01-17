from pathlib import Path

import numpy as np

from myproject import StandardScaler


def test_save_load(tmp_path: Path) -> None:
    processor = StandardScaler()
    data = np.random.default_rng(0).random(5)
    processor.fit(data)
    processor.save(tmp_path / "processor.pkl")
    processor = StandardScaler.load(tmp_path / "processor.pkl")
    assert processor._mean == data.mean()
    assert processor._std == data.std()


def test_transform() -> None:
    data = np.random.default_rng(0).random(5)
    data_transformed = StandardScaler().fit_transform(data)
    assert np.array_equal((data - data.mean()) / data.std(), data_transformed)
