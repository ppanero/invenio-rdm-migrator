# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-RDM-Migrator is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio RDM migration record transform interfaces."""

from abc import abstractmethod

from ...transform import Transform


class OAuthServerTokenTransform(Transform):
    """OAuth server token data transformation."""

    @abstractmethod
    def _id(self, entry):
        """Server token id."""
        pass

    @abstractmethod
    def _client_id(self, entry):
        """Client id."""
        pass

    @abstractmethod
    def _user_id(self, entry):
        """User id."""
        pass

    @abstractmethod
    def _token_type(self, entry):
        """Server token type."""
        pass

    @abstractmethod
    def _access_token(self, entry):
        """Server access token."""
        pass

    @abstractmethod
    def _refresh_token(self, entry):
        """Server refresh token."""
        pass

    @abstractmethod
    def _expires(self, entry):
        """Token expiration date."""
        pass

    @abstractmethod
    def _scopes(self, entry):
        """Token scopes."""
        pass

    @abstractmethod
    def _is_personal(self, entry):
        """If the token is personal."""
        pass

    @abstractmethod
    def _is_internal(self, entry):
        """If the token is internal."""
        pass

    def _transform(self, entry):
        """Transform a single entry."""
        return {
            "id": self._id(entry),
            "client_id": self._client_id(entry),
            "user_id": self._user_id(entry),
            "token_type": self._token_type(entry),
            "access_token": self._access_token(entry),
            "refresh_token": self._refresh_token(entry),
            "expires": self._expires(entry),
            "_scopes": self._scopes(entry),
            "is_personal": self._is_personal(entry),
            "is_internal": self._is_internal(entry),
        }


class OAuthRemoteTokenTransform(Transform):
    """OAuth client remote token data transformation."""

    @abstractmethod
    def _id_remote_account(self, entry):
        """Remote account id."""
        pass

    @abstractmethod
    def _token_type(self, entry):
        """Remove token type."""
        pass

    @abstractmethod
    def _access_token(self, entry):
        """Remote access token."""
        pass

    @abstractmethod
    def _secret(self, entry):
        """Secret for access token hashing."""
        pass

    @abstractmethod
    def _created(self, entry):
        """Returns the creation date of the record."""
        pass

    @abstractmethod
    def _updated(self, entry):
        """Returns the update date of the record."""
        pass

    def _transform(self, entry):
        """Transform a single entry."""
        return {
            "id_remote_account": self._id_remote_account(entry),
            "token_type": self._token_type(entry),
            "access_token": self._access_token(entry),
            "secret": self._secret(entry),
            "created": self._created(entry),
            "updated": self._updated(entry),
        }
