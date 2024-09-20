# SPDX-License-Identifier: Apache-2.0

import uuid

from EmbeddingUtils import (
    EMBEDDING_MODEL,
    HUGGING_FACE,
    HUGGING_FACE_MODEL,
    OPENAI,
    OPENAI_MODEL,
)
from nifiapi.properties import (
    ExpressionLanguageScope,
    PropertyDependency,
    PropertyDescriptor,
    StandardValidators,
)

DEFAULT_COLLECTION_NAME = "apache-nifi"


COLLECTION_NAME = PropertyDescriptor(
    name="Collection Name",
    description="The name of the Qdrant collection to use.",
    sensitive=False,
    required=True,
    default_value=DEFAULT_COLLECTION_NAME,
    validators=[StandardValidators.NON_EMPTY_VALIDATOR],
    expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES,
)
QDRANT_URL = PropertyDescriptor(
    name="Qdrant URL",
    description="The fully qualified URL to the Qdrant instance.",
    sensitive=False,
    required=True,
    default_value="http://localhost:6333",
    validators=[StandardValidators.URL_VALIDATOR],
)
QDRANT_API_KEY = PropertyDescriptor(
    name="Qdrant API Key",
    description="The API Key to use in order to authentication with Qdrant. Can be empty.",
    sensitive=True,
    required=True,
)

PREFER_GRPC = PropertyDescriptor(
    name="Prefer gRPC",
    description="Specifies whether to use gRPC for interfacing with Qdrant.",
    required=True,
    default_value=False,
    allowable_values=["True", "False"],
    validators=[StandardValidators.BOOLEAN_VALIDATOR],
)
HTTPS = PropertyDescriptor(
    name="Use HTTPS",
    description="Specifies whether to TLS(HTTPS) while interfacing with Qdrant.",
    required=True,
    default_value=False,
    allowable_values=["True", "False"],
    validators=[StandardValidators.BOOLEAN_VALIDATOR],
)

QDRANT_PROPERTIES = [COLLECTION_NAME, QDRANT_URL, QDRANT_API_KEY, PREFER_GRPC, HTTPS]

HUGGING_FACE_API_KEY = PropertyDescriptor(
    name="HuggingFace API Key",
    description="The API Key for interacting with HuggingFace",
    validators=[StandardValidators.NON_EMPTY_VALIDATOR],
    required=True,
    sensitive=True,
    dependencies=[PropertyDependency(EMBEDDING_MODEL, HUGGING_FACE)],
)
OPENAI_API_KEY = PropertyDescriptor(
    name="OpenAI API Key",
    description="The API Key for OpenAI in order to create embeddings.",
    sensitive=True,
    required=True,
    validators=[StandardValidators.NON_EMPTY_VALIDATOR],
    dependencies=[PropertyDependency(EMBEDDING_MODEL, OPENAI)],
)

EMBEDDING_MODEL_PROPERTIES = [
    EMBEDDING_MODEL,
    HUGGING_FACE_API_KEY,
    HUGGING_FACE_MODEL,
    OPENAI_API_KEY,
    OPENAI_MODEL,
]


def convert_id(_id: str) -> str:
    """
    Converts any string into a UUID string deterministically.

    Qdrant accepts UUID strings and unsigned integers as point ID.
    This allows us to overwrite the same point with the original ID.
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, _id))
