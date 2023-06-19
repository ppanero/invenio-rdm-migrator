# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-RDM-Migrator is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio RDM migration OAuth load module."""

from ...load.postgresql import (
    ExistingDataTableGenerator,
    PostgreSQLCopyLoad,
    TableGenerator,
)

from .models import RemoteAccount, ServerClient, UserIdentity


class ExitingOAuthClientDataLoad(PostgreSQLCopyLoad):
    """OAuthClient loading of existing data.

    It does not load the two tables with tokens, since they need rehashing.
    """

    def __init__(self, db_uri, data_dir, **kwargs):
        """Constructor."""
        super().__init__(
            db_uri=db_uri,
            table_generators=[
                ExistingDataTableGenerator(tables=[RemoteAccount, UserIdentity], pks=[])
            ],
            data_dir=data_dir,
            existing_data=True,
        )


class ExitingOAuthServerDataLoad(PostgreSQLCopyLoad):
    """OAuth2Server loading of existing data.

    It does not load the two tables with tokens, since they need rehashing.
    """

    def __init__(self, db_uri, data_dir, **kwargs):
        """Constructor."""
        super().__init__(
            db_uri=db_uri,
            table_generators=[
                ExistingDataTableGenerator(tables=[ServerClient], pks=[])
            ],
            data_dir=data_dir,
            existing_data=True,
        )
