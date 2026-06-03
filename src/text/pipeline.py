"""Pipeline de TEXTO — stubs para el Integrante 1.

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


class SplitterTexto(Splitter):
    def split(self, documento: Any) -> list[Chunk]:
        raise NotImplementedError("un Chunk por documento de metadata del track")


class ExtractorTFIDF(FeatureExtractor):
    def extract(self, chunk: Chunk) -> Any:
        raise NotImplementedError("tokenizar, normalizar, stopwords, stemming -> términos")


class CodebookTexto(Codebook):
    @property
    def size(self) -> int:
        raise NotImplementedError("tamaño del vocabulario (k)")

    def quantize(self, feature: Any) -> int:
        raise NotImplementedError("id del término en el vocabulario")

    def histogram(self, features: Iterable[Any]) -> Sequence[float]:
        raise NotImplementedError("vector TF-IDF de tamaño k")


class ConstructorVocabulario(CodebookBuilder):
    def build(self, features: Iterable[Any], k: int) -> Codebook:
        raise NotImplementedError("vocabulario top-k del corpus (post preproceso)")
