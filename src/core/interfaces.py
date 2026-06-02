"""Interfaces comunes del motor multimodal.

Todo el sistema sigue el mismo paradigma, sin importar la modalidad:

    split  ->  extracción de features  ->  codebook  ->  índice invertido

Cada modalidad (texto, audio, imagen) implementa estas interfaces. El backend y la
evaluación trabajan contra estas abstracciones, no contra implementaciones
concretas. Esta es la pieza que desbloquea el trabajo en paralelo del equipo:
mantener estas firmas estables.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Sequence


@dataclass
class Chunk:
    """Unidad atómica de contenido tras el split.

    - doc_id:  documento/track al que pertenece el chunk.
    - payload: el contenido en sí (un documento de metadata, un segmento de audio,
               una portada, ...).
    - meta:    información auxiliar (posición, modalidad, etc.).
    """
    doc_id: int
    payload: Any
    meta: dict = field(default_factory=dict)


@dataclass
class Resultado:
    """Un resultado de búsqueda: documento recuperado y su score de similitud."""
    doc_id: int
    score: float


class Splitter(ABC):
    """Divide un documento en chunks (unidades atómicas indexables)."""

    @abstractmethod
    def split(self, documento: Any) -> list[Chunk]:
        ...


class FeatureExtractor(ABC):
    """Extrae el descriptor/feature de un chunk.

    Texto  -> términos / TF-IDF.
    Audio  -> MFCC por ventana.
    Imagen -> descriptores SIFT.
    """

    @abstractmethod
    def extract(self, chunk: Chunk) -> Any:
        ...


class Codebook(ABC):
    """Diccionario compartido: cuantiza features a codewords y arma histogramas."""

    @property
    @abstractmethod
    def size(self) -> int:
        """Tamaño del vocabulario (k)."""
        ...

    @abstractmethod
    def quantize(self, feature: Any) -> int:
        """Asigna un feature a su codeword más cercano (id)."""
        ...

    @abstractmethod
    def histogram(self, features: Iterable[Any]) -> Sequence[float]:
        """Construye el histograma de codewords de un documento."""
        ...


class CodebookBuilder(ABC):
    """Construye el codebook a partir de TODOS los features de la colección.

    Texto  -> top-k palabras más frecuentes.
    Audio  -> MiniBatchKMeans sobre los MFCC (palabras acústicas).
    Imagen -> K-Means / MiniBatchKMeans sobre los descriptores SIFT (palabras visuales).
    """

    @abstractmethod
    def build(self, features: Iterable[Any], k: int) -> Codebook:
        ...


class InvertedIndex(ABC):
    """Índice invertido (codeword -> documentos). Soporta búsqueda top-k."""

    @abstractmethod
    def add(self, doc_id: int, histograma: Sequence[float]) -> None:
        ...

    @abstractmethod
    def search(self, consulta: Sequence[float], top_k: int = 10) -> list[Resultado]:
        ...
