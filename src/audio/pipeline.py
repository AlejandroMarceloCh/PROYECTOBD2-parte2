"""Pipeline de AUDIO — stubs para el Integrante 2.

Implementá los métodos marcados con NotImplementedError. El histograma que devuelvas
(lista de floats de tamaño k) entra tal cual a IndiceEnMemoria.add(doc_id, histograma).
Ver src/core/index.py y src/core/README.md.
"""
from __future__ import annotations

from typing import Any, Iterable, Sequence

from src.core.interfaces import (
    Chunk,
    Codebook,
    CodebookBuilder,
    FeatureExtractor,
    Splitter,
)


class SplitterAudio(Splitter):
    def split(self, documento: Any) -> list[Chunk]:
        raise NotImplementedError("partir el track en segmentos de ~7.5 s (un Chunk por segmento)")


class ExtractorMFCC(FeatureExtractor):
    def extract(self, chunk: Chunk) -> Any:
        raise NotImplementedError("MFCC por ventana dentro del segmento -> matriz de frames")


class CodebookAcustico(Codebook):
    @property
    def size(self) -> int:
        raise NotImplementedError("tamaño del codebook acústico (k)")

    def quantize(self, feature: Any) -> int:
        raise NotImplementedError("centroide más cercano a un frame MFCC (palabra acústica)")

    def histogram(self, features: Iterable[Any]) -> Sequence[float]:
        raise NotImplementedError("conteo de palabras acústicas del segmento -> vector tamaño k")


class ConstructorCodebookAcustico(CodebookBuilder):
    def build(self, features: Iterable[Any], k: int) -> Codebook:
        raise NotImplementedError("MiniBatchKMeans sobre los MFCC de todos los segmentos")
