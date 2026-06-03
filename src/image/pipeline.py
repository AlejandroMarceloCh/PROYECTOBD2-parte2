"""Pipeline de IMAGEN — stubs para el Integrante 3.

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


class SplitterImagen(Splitter):
    def split(self, documento: Any) -> list[Chunk]:
        raise NotImplementedError("una portada de álbum = un Chunk")


class ExtractorSIFT(FeatureExtractor):
    def extract(self, chunk: Chunk) -> Any:
        raise NotImplementedError("SIFT: keypoints + descriptores de 128 dimensiones")


class CodebookVisual(Codebook):
    @property
    def size(self) -> int:
        raise NotImplementedError("tamaño del vocabulario visual (k)")

    def quantize(self, feature: Any) -> int:
        raise NotImplementedError("centroide más cercano a un descriptor SIFT (palabra visual)")

    def histogram(self, features: Iterable[Any]) -> Sequence[float]:
        raise NotImplementedError("conteo de palabras visuales de la portada -> vector tamaño k")


class ConstructorCodebookVisual(CodebookBuilder):
    def build(self, features: Iterable[Any], k: int) -> Codebook:
        raise NotImplementedError("K-Means sobre los descriptores SIFT de todas las portadas")
